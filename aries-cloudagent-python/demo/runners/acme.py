import asyncio
import logging
import os
import sys

### PROOF REQUEST IMPLEMENTATION ###
import random
from datetime import date
from uuid import uuid4

TAILS_FILE_COUNT = int(os.getenv("TAILS_FILE_COUNT", 100))
CRED_PREVIEW_TYPE = "https://didcomm.org/issue-credential/2.0/credential-preview"
### PROOF REQUEST IMPLEMENTATION ###

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))  # noqa

from runners.agent_container import (  # noqa:E402
    AriesAgent,
    arg_parser,
    create_agent_with_args,
)
from runners.support.utils import (  # noqa:E402
    check_requires,
    log_msg,
    log_status,
    prompt,
    prompt_loop,
    log_timer,
)

CRED_PREVIEW_TYPE = "https://didcomm.org/issue-credential/2.0/credential-preview"
SELF_ATTESTED = os.getenv("SELF_ATTESTED")
TAILS_FILE_COUNT = int(os.getenv("TAILS_FILE_COUNT", 100))

logging.basicConfig(level=logging.WARNING)
LOGGER = logging.getLogger(__name__)


class AcmeAgent(AriesAgent):
    def __init__(
        self,
        ident: str,
        http_port: int,
        admin_port: int,
        no_auto: bool = False,
        **kwargs,
    ):
        super().__init__(
            ident,
            http_port,
            admin_port,
            prefix="Acme",
            no_auto=no_auto,
            **kwargs,
        )
        self.connection_id = None
        self._connection_ready = None
        self.cred_state = {}
        self.cred_attrs = {}

    async def detect_connection(self):
        await self._connection_ready
        self._connection_ready = None

    @property
    def connection_ready(self):
        return self._connection_ready.done() and self._connection_ready.result()

    async def handle_oob_invitation(self, message):
        pass

    async def handle_connections(self, message):
        print(self.ident, "handle_connections", message["state"], message["rfc23_state"])
        conn_id = message["connection_id"]
        if (not self.connection_id) and message["rfc23_state"] == "invitation-sent":
            print(self.ident, "set connection id", conn_id)
            self.connection_id = conn_id
        if (
            message["connection_id"] == self.connection_id
            and message["rfc23_state"] == "completed"
            and (self._connection_ready and not self._connection_ready.done())
        ):
            self.log("Connected")
            self._connection_ready.set_result(True)

    async def handle_issue_credential_v2_0(self, message):
        state = message["state"]
        cred_ex_id = message["cred_ex_id"]
        prev_state = self.cred_state.get(cred_ex_id)
        if prev_state == state:
            return  # ignore
        self.cred_state[cred_ex_id] = state

        self.log(f"Credential: state = {state}, cred_ex_id = {cred_ex_id}")

        if state == "request-received":
            ### ISSUE CREDENTIALS IMPLEMENTATION ###
            # issue credentials based on offer preview in cred ex record
            if not message.get("auto_issue"):
                await self.admin_POST(
                    f"/issue-credential-2.0/records/{cred_ex_id}/issue",
                    {"comment": f"Issuing credential, exchange {cred_ex_id}"},
                )
            ### ISSUE CREDENTIALS IMPLEMENTATION ###

    async def handle_issue_credential_v2_0_indy(self, message):
        pass  # employee id schema does not support revocation

    async def handle_present_proof_v2_0(self, message):
        state = message["state"]
        pres_ex_id = message["pres_ex_id"]
        self.log(f"Presentation: state = {state}, pres_ex_id = {pres_ex_id}")

        if state == "presentation-received":
            log_status("#27 Process the proof provided by X")

            ### PROOF REQUEST IMPLEMENTATION ###
            log_status("#28 Check if proof is valid")
            proof = await self.admin_POST(
                f"/present-proof-2.0/records/{pres_ex_id}/verify-presentation"
            )
            self.log("Proof = ", proof["verified"])

            if not proof["verified"] or proof["verified"] == "false":
                # immediately return if proof is not valid
                self.log("#28.1 Proof is not valid. Not processing further.")
                return

            # if presentation is a degree schema (proof of education),
            # check values received
            pres_req = message["by_format"]["pres_request"]["indy"]
            pres = message["by_format"]["pres"]["indy"]
            is_proof_of_education = pres_req["name"] == "Proof of Education"
            if is_proof_of_education:
                log_status("#28.1 Received proof of education, check claims")
                for referent, attr_spec in pres_req["requested_attributes"].items():
                    if referent in pres["requested_proof"]["revealed_attrs"]:
                        self.log(
                            f"{attr_spec['name']}: "
                            f"{pres['requested_proof']['revealed_attrs'][referent]['raw']}"
                        )
                    else:
                        self.log(f"{attr_spec['name']}: " "(attribute not revealed)")

                for id_spec in pres["identifiers"]:
                    # just print out the schema/cred def id's of presented claims
                    self.log(f"schema_id: {id_spec['schema_id']}")
                    self.log(f"cred_def_id {id_spec['cred_def_id']}")

                ### ISSUE CREDENTIALS IMPLEMENTATION ###
                with log_timer("Publish schema and cred def duration:"):
                    # define schema
                    version = format(
                        "%d.%d.%d"
                        % (
                            random.randint(1, 101),
                            random.randint(1, 101),
                            random.randint(1, 101),
                        )
                    )
                    # register schema and cred def
                    schema_name = "employee id schema"
                    schema_attrs = ["employee_id", "name", "date", "position"]
                    (schema_id, cred_def_id) = await self.register_schema_and_creddef(
                        schema_name,
                        version,
                        schema_attrs,
                        support_revocation=False,
                        revocation_registry_size=TAILS_FILE_COUNT,
                    )
                # issue credentials based on proof received automatically without waiting for 1 input at Acme prompt from user
                self.log("#28.2 Issue credential offer to X automatically based on proof received")
                await issue_credential_offer(
                    agent=self,
                    schema_attrs=schema_attrs,
                    schema_name=schema_name,
                    cred_def_id=cred_def_id,
                )
                self.log("#28.3 Issue credential offer sent")
                ### ISSUE CREDENTIALS IMPLEMENTATION ###
            else:
                # in case there are any other kinds of proofs received
                self.log("#28.1 Received ", pres_req["name"])
            ### PROOF REQUEST IMPLEMENTATION ###

    async def handle_basicmessages(self, message):
        self.log("Received message:", message["content"])


### ISSUE CREDENTIALS IMPLEMENTATION ###
async def issue_credential_offer(agent, schema_attrs, schema_name, cred_def_id):
    """Reusable function to issue credential offer based on schema attributes
    and cred def id provided as input arguments
    Args:

    agent: AriesAgent object
    schema_attrs: list of schema attributes
    schema_name: name of the schema
    cred_def_id: credential definition id

    """
    agent.cred_attrs[cred_def_id] = {
        "employee_id": "ACME0009",
        "name": "Alice Smith",
        "date": date.isoformat(date.today()),
        "position": "CEO",
    }
    cred_preview = {
        "@type": CRED_PREVIEW_TYPE,
        "attributes": [{"name": n, "value": v} for (n, v) in agent.cred_attrs[cred_def_id].items()],
    }
    offer_request = {
        "connection_id": agent.connection_id,
        "comment": f"Offer on cred def id {cred_def_id}",
        "credential_preview": cred_preview,
        "filter": {"indy": {"cred_def_id": cred_def_id}},
    }
    await agent.admin_POST("/issue-credential-2.0/send-offer", offer_request)


### ISSUE CREDENTIALS IMPLEMENTATION ###



### PROOF REQUEST IMPLEMENTATION ###
async def request_proof_of_education(agent, test_failure=False):
    """
    Function to send proof request to Alice for proof of education
    Args:
    agent: AriesAgent object

    """
    print(f'request_proof_of_education: test_failure: {test_failure}')

    req_attrs = [
        {"name": "name", "restrictions": [{"schema_name": "degree schema"}]},
        {"name": "date", "restrictions": [{"schema_name": "degree schema"}]},
        {"name": "degree", "restrictions": [{"schema_name": "degree schema"}]},
    ]
    req_preds = []
    indy_proof_request = {
        "name": "Proof of Education",
        "version": "1.0",
        "nonce": str(uuid4().int),
        "requested_attributes": {
            f"0_{req_attr['name']}_uuid": req_attr for req_attr in req_attrs
        },
        "requested_predicates": {},
    }
    proof_request_web_request = {
        "connection_id": agent.connection_id,
        "presentation_request": {"indy": indy_proof_request},
    }
    if test_failure:
        proof_request_web_request.update({"comment": "test_failure"}) # tell Alice to fail so we can test handling the failed proof request

    # this sends the request to our agent, which forwards it to Alice
    # (based on the connection_id)
    await agent.admin_POST("/present-proof-2.0/send-request", proof_request_web_request)
### PROOF REQUEST IMPLEMENTATION ###

async def main(args):
    acme_agent = await create_agent_with_args(args, ident="acme")

    try:
        log_status(
            "#1 Provision an agent and wallet, get back configuration details"
            + (f" (Wallet type: {acme_agent.wallet_type})" if acme_agent.wallet_type else "")
        )
        agent = AcmeAgent(
            "acme.agent",
            acme_agent.start_port,
            acme_agent.start_port + 1,
            genesis_data=acme_agent.genesis_txns,
            genesis_txn_list=acme_agent.genesis_txn_list,
            no_auto=acme_agent.no_auto,
            tails_server_base_url=acme_agent.tails_server_base_url,
            timing=acme_agent.show_timing,
            multitenant=acme_agent.multitenant,
            mediation=acme_agent.mediation,
            wallet_type=acme_agent.wallet_type,
            seed=acme_agent.seed,
        )

        acme_agent.public_did = True

        ### ISSUE CREDENTIALS IMPLEMENTATION ###

        acme_schema_name = "employee id schema"
        acme_schema_attrs = ["employee_id", "name", "date", "position"]
        await acme_agent.initialize(
            the_agent=agent,
            schema_name=acme_schema_name,
            schema_attrs=acme_schema_attrs,
        )
        with log_timer("Publish schema and cred def duration:"):
            # define schema
            version = format(
                "%d.%d.%d"
                % (
                    random.randint(1, 101),
                    random.randint(1, 101),
                    random.randint(1, 101),
                )
            )
            # register schema and cred def
            (schema_id, cred_def_id) = await agent.register_schema_and_creddef(
                "employee id schema",
                version,
                ["employee_id", "name", "date", "position"],
                support_revocation=False,
                revocation_registry_size=TAILS_FILE_COUNT,
            )
        ### ISSUE CREDENTIALS IMPLEMENTATION ###

        # generate an invitation for Alice
        await acme_agent.generate_invitation(display_qr=True, wait=True)

        options = (
            "    (1) Issue Credential\n"
            "    (2) Send Proof Request\n"
            "    (2a) Send Proof Request (with failure handling)\n"
            "    (3) Send Message\n"
            "    (X) Exit?\n"
            "[1/2/3/X]"
        )
        async for option in prompt_loop(options):
            if option is not None:
                option = option.strip()

            if option is None or option in "xX":
                break

            elif option == "1":
                log_status("#13 Issue credential offer to X")
                ### ISSUE CREDENTIALS IMPLEMENTATION ###
                await issue_credential_offer(
                    agent,
                    acme_schema_attrs,
                    acme_schema_name,
                    cred_def_id,
                )
                ### ISSUE CREDENTIALS IMPLEMENTATION ###

            elif option == "2":
                log_status("#20 Request proof of degree from alice")
                ### PROOF REQUEST IMPLEMENTATION ###
                await request_proof_of_education(agent)
                ### PROOF REQUEST IMPLEMENTATION ###

            elif option == "2a":
                log_status("#20 Request proof of degree from alice AND test failure handling")
                ### PROOF REQUEST IMPLEMENTATION ###
                await request_proof_of_education(agent, test_failure=True)
                ### PROOF REQUEST IMPLEMENTATION ###

            elif option == "3":
                msg = await prompt("Enter message: ")
                await agent.admin_POST(
                    f"/connections/{agent.connection_id}/send-message", {"content": msg}
                )

        if acme_agent.show_timing:
            timing = await acme_agent.agent.fetch_timing()
            if timing:
                for line in acme_agent.agent.format_timing(timing):
                    log_msg(line)

    finally:
        terminated = await acme_agent.terminate()

    await asyncio.sleep(0.1)

    if not terminated:
        os._exit(1)


if __name__ == "__main__":
    parser = arg_parser(ident="acme", port=8040)
    args = parser.parse_args()

    ENABLE_PYDEVD_PYCHARM = os.getenv("ENABLE_PYDEVD_PYCHARM", "").lower()
    ENABLE_PYDEVD_PYCHARM = ENABLE_PYDEVD_PYCHARM and ENABLE_PYDEVD_PYCHARM not in (
        "false",
        "0",
    )
    PYDEVD_PYCHARM_HOST = os.getenv("PYDEVD_PYCHARM_HOST", "localhost")
    PYDEVD_PYCHARM_CONTROLLER_PORT = int(os.getenv("PYDEVD_PYCHARM_CONTROLLER_PORT", 5001))

    if ENABLE_PYDEVD_PYCHARM:
        try:
            import pydevd_pycharm

            print(
                "Acme remote debugging to "
                f"{PYDEVD_PYCHARM_HOST}:{PYDEVD_PYCHARM_CONTROLLER_PORT}"
            )
            pydevd_pycharm.settrace(
                host=PYDEVD_PYCHARM_HOST,
                port=PYDEVD_PYCHARM_CONTROLLER_PORT,
                stdoutToServer=True,
                stderrToServer=True,
                suspend=False,
            )
        except ImportError:
            print("pydevd_pycharm library was not found")

    check_requires(args)

    try:
        asyncio.get_event_loop().run_until_complete(main(args))
    except KeyboardInterrupt:
        os._exit(1)
