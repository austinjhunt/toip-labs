# The Alice/Faber Demo

There are several demos available for ACA-Py mostly (but not only) aimed at developers learning how to deploy an instance of the agent and an ACA-Py controller to implement an application.

This folder contains the terminal output for the von-network, Faber, and Alice terminals mentioned in the [Alice/Faber Demo documentation](https://aca-py.org/latest/demo/#the-alicefaber-python-demo). The terminal output was saved for each terminal for the purpose of analyzing the execution flow.

# Startup

To begin, I started each of the following in their own terminal windows:

- the VON Network with `./manage start --logs` in the [von-network folder](../von-network/README.md)
- the Faber agent with `AGENT_PORT_OVERRIDE=8010 ./run_demo faber` in the [aries-cloudagent-python/demo folder](../aries-cloudagent-python/demo/), and
- the Alice agent with `./run_demo alice` in the [aries-cloudagent-python/demo folder](../aries-cloudagent-python/demo/)

# Alice accepts Invitation from Faber

With both the Alice and Faber agents started, Alice was prompting for an invitation to be pasted, so I went to the Faber agent window which had created and was displaying an invitation. That invitation was presented in two forms: a QR code (for connecting from a mobile agent) and a JSON object that looked like this:

```json
{
  "@type": "https://didcomm.org/out-of-band/1.1/invitation",
  "@id": "9be04831-aac4-4739-a85e-0d5ee109f407",
  "label": "faber.agent",
  "handshake*protocols": ["https://didcomm.org/didexchange/1.1"],
  "services": [
    {
      "id": "#inline",
      "type": "did-communication",
      "recipientKeys": [
        "did:key:z6Mkf3YkNHBYb8UgeWxuqGAPkdgjsu3YGkFDhdLbmpm3BW1p#z6Mkf3YkNHBYb8UgeWxuqGAPkdgjsu3YGkFDhdLbmpm3BW1p"
      ],
      "serviceEndpoint": "http://host.docker.internal:8010"
    }
  ]
}
```

## Invitation Analysis

The invitation created by Faber is a digital handshake, allowing Alice and Faber to establish a secure communication channel via **DIDComm**, a protocol for decentralized identity communication. It’s presented in the form of a JSON object, which contains all the necessary details to initiate a secure connection between Alice (the user) and Faber (the institution or entity issuing credentials).

In simpler terms, think of it as an invitation to an encrypted chat, with both parties agreeing to certain rules and security measures to ensure their conversation is private and trustworthy.

### Invitation Attributes

- `@type`: This field (https://didcomm.org/out-of-band/1.1/invitation) defines the type of message. In this case, it’s an "out-of-band invitation." Out-of-band refers to setting up a connection without needing an existing channel, which is perfect for new connections like Alice and Faber.
- `@id`: The unique identifier for the invitation, in this case, 9be04831-aac4-4739-a85e-0d5ee109f407. This ensures the invitation is specific to this interaction.

- `label`: The label (faber.agent) is a friendly name that Faber’s agent gives itself. It helps Alice’s agent identify who is making the request.

- `handshake_protocols`: This specifies the protocols the agents will use to establish their connection. The value here is https://didcomm.org/didexchange/1.1, which is the **DIDComm DID Exchange protocol version 1.1**, responsible for exchanging decentralized identifiers (DIDs) and establishing a secure channel.

- `services`: The services block contains all the technical details of how Alice's agent can reach Faber’s agent. In this case:
  - `id`: The identifier #inline represents this service's unique ID.
  - `type`: The type did-communication tells Alice’s agent that the service is using DID communication to manage this interaction.
  - `recipientKeys`: This is the public key of Faber’s agent (did:key:z6Mkf...) that Alice’s agent will use to securely communicate.
  - `serviceEndpoint`: This specifies where Alice’s agent can reach Faber’s agent (via http://host.docker.internal:8010), which is where Faber is running in this demo.

### What Happens When Alice Accepts the Invitation?

When I paste this invitation into Alice’s agent terminal, as seen below, Alice’s agent interprets the invitation and initiates a connection to Faber’s agent. This is where the DIDComm protocol takes over, allowing Alice’s agent to establish a secure channel with Faber.

```bash

#9 Input faber.py invitation details
Invite details: {"@type": "https://didcomm.org/out-of-band/1.1/invitat
ion", "@id": "9be04831-aac4-4739-a85e-0d5ee109f407", "label": "faber.a
gent", "handshake_protocols": ["https://didcomm.org/didexchange/1.1"],
 "services": [{"id": "#inline", "type": "did-communication", "recipien
tKeys": ["did:key:z6Mkf3YkNHBYb8UgeWxuqGAPkdgjsu3YGkFDhdLbmpm3BW1p#z6M
kf3YkNHBYb8UgeWxuqGAPkdgjsu3YGkFDhdLbmpm3BW1p"], "serviceEndpoint": "h
ttp://host.docker.internal:8010"}]}
Invitation response:
  {
    "state": "deleted",
    "created_at": "2024-09-11T17:22:58.537033Z",
    "updated_at": "2024-09-11T17:22:58.537033Z",
    "trace": false,
    "oob_id": "13383976-0cd3-4727-8b16-8df29bd94fa0",
    "invi_msg_id": "9be04831-aac4-4739-a85e-0d5ee109f407",
    "invitation": {
      "@type": "https://didcomm.org/out-of-band/1.1/invitation",
      "@id": "9be04831-aac4-4739-a85e-0d5ee109f407",
      "label": "faber.agent",
      "handshake_protocols": [
        "https://didcomm.org/didexchange/1.1"
      ],
      "services": [
        {
          "id": "#inline",
          "type": "did-communication",
          "recipientKeys": [
            "did:key:z6Mkf3YkNHBYb8UgeWxuqGAPkdgjsu3YGkFDhdLbmpm3BW1p#z6Mkf3YkNHBYb8UgeWxuqGAPkdgjsu3YGkFDhdLbmpm3BW1p"
          ],
          "serviceEndpoint": "http://host.docker.internal:8010"
        }
      ]
    },
    "connection_id": "e9baec09-780e-448a-9c77-c49bdbef8d78",
    "role": "receiver",
    "multi_use": false
  }

Connect duration: 0.08s
Waiting for connection...
Alice      | Connected
Alice      | Check for endorser role ...
Connect duration: 0.23s
```

The code that handles this:

```python
# alice.py:73

async def input_invitation(agent_container):
    agent_container.agent._connection_ready = asyncio.Future()
    async for details in prompt_loop("Invite details: "):
        b64_invite = None
        try:
            url = urlparse(details)
            query = url.query
            if query and "c_i=" in query:
                pos = query.index("c_i=") + 4
                b64_invite = query[pos:]
            elif query and "oob=" in query:
                pos = query.index("oob=") + 4
                b64_invite = query[pos:]
            else:
                b64_invite = details
        except ValueError:
            b64_invite = details

        if b64_invite:
            try:
                padlen = 4 - len(b64_invite) % 4
                if padlen <= 2:
                    b64_invite += "=" * padlen
                invite_json = base64.urlsafe_b64decode(b64_invite)
                details = invite_json.decode("utf-8")
            except binascii.Error:
                pass
            except UnicodeDecodeError:
                pass

        if details:
            try:
                details = json.loads(details)
                break
            except json.JSONDecodeError as e:
                log_msg("Invalid invitation:", str(e))

    with log_timer("Connect duration:"):
        connection = await agent_container.input_invitation(details, wait=True)

# Once invitation details are provided at the prompt, connection gets its value from the following method execution:

agent_container.py:660
async def input_invitation(self, invite_details: dict, wait: bool = False):
    self._connection_ready = asyncio.Future()
    with log_timer("Connect duration:"):
        connection = await self.receive_invite(invite_details)
        log_json(connection, label="Invitation response:")

    if wait:
        log_msg("Waiting for connection...")
        await self.detect_connection()

### which calls receive_invite defined here
agent.py:1517
async def receive_invite(self, invite, auto_accept: bool = True):
    if self.endorser_role and self.endorser_role == "author":
        params = {"alias": "endorser"}
    else:
        params = {}
    if self.mediation:
        params["mediation_id"] = self.mediator_request_id

    # This runs because our invitation type is out-of-band
    if "/out-of-band/" in invite.get("@type", ""):
        # reuse connections if requested and possible
        params["use_existing_connection"] = json.dumps(self.reuse_connections)
        connection = await self.admin_POST(
            "/out-of-band/receive-invitation",
            invite,
            params=params,
        )
    else:
        connection = await self.admin_POST(
            "/connections/receive-invitation",
            invite,
            params=params,
        )

    self.connection_id = connection["connection_id"]
    return connection
```

We see that ultimately Alice is waiting for the invitation data, and once received, it posts that invitation data to the `/out-of-band/receive-invitation` admin URL (specific to the Alice agent, shown in the Alice terminal to be `http://host.docker.internal:8031`); this API call returns the connection.

Once the connection is returned and established, Alice and Faber can exchange encrypted messages, credentials, or proofs through their agents. Essentially, it’s like having a trusted, private conversation channel between the two agents.

### Why is This Important?

This invitation is the starting point for all trustful, encrypted communication between Alice and Faber in this demo. Without it, they wouldn’t be able to connect, and thus, Alice wouldn’t be able to receive credentials or send proofs. The invitation allows Alice’s agent to know:

- Who it’s talking to (Faber’s agent),
- How to communicate securely (via the provided public key), and
- Where to send messages (Faber’s service endpoint).

## Connection Established: What are the options?

As instructed, I copied this invitation and pasted it at the Alice prompt. The agents will connect and then show a menu of options:

### Faber Options

    (1) Issue Credential - Send a credential to Alice after the connection is established (e.g., a university diploma).
    (1a) Set Credential Type (indy) - Choose the type of credential to issue, typically "indy" for the Indy-based ledger system.
    (2) Send Proof Request - Ask Alice to provide proof of a credential (e.g., to verify her diploma).
    (3) Send Message - Send an encrypted message to Alice through the established connection.
    (4) Create New Invitation - Generate a new connection invitation for another agent (like Alice) to connect with Faber.
    (T) Toggle tracing on credential/proof exchange - Enable or disable detailed logging of credential issuance and proof exchanges for debugging.
    (X) Exit? - Quit the Faber agent terminal

### Alice Options Explained

    (3) Send Message - Send an encrypted message to Faber through the established connection
    (4) Input New Invitation - Provide a new invitation to connect to another agent (like Faber)
    (X) Exit?

## Exchanging Messages

First let's explore the execution flow for encrypted message exchange (option 3).

In the Faber terminal, I enter 3 to send a message to Alice, and I provide a message to send at the prompt:

```bash
Enter message: Message1
```

### What happens? Execution flow of message exchange.

1. In `faber.py`, we see the first step:

```python
faber.py:881
...
    elif option == "3":
        msg = await prompt("Enter message: ")
        await faber_agent.agent.admin_POST(
            f"/connections/{faber_agent.agent.connection_id}/send-message",
            {"content": msg},
        )
...
```

Upon receiving the message to send from the prompt, it POSTs the message with key "content" to the Faber agent Admin API (shown in the faber terminal to be `http://host.docker.internal:8011`) at the `/connections/` path followed by the ID of the connection between Faber and Alice, followed by the `send-message` action. Simple enough.

2. What happens at that route?

```python

# Registration of send-message route
routes.py:66
async def register(app: web.Application):
    """Register routes."""

    app.add_routes(
        [web.post("/connections/{conn_id}/send-message", connections_send_message)]
    )
...

# definitiion of connections_send_message function:

routes.py:36
@docs(tags=["basicmessage"], summary="Send a basic message to a connection")
@match_info_schema(BasicConnIdMatchInfoSchema())
@request_schema(SendMessageSchema())
@response_schema(BasicMessageModuleResponseSchema(), 200, description="")
@tenant_authentication
async def connections_send_message(request: web.BaseRequest):
    """Request handler for sending a basic message to a connection.

    Args:
        request: aiohttp request object

    """
    context: AdminRequestContext = request["context"]
    connection_id = request.match_info["conn_id"]
    outbound_handler = request["outbound_message_router"]
    params = await request.json()

    try:
        async with context.profile.session() as session:
            connection = await ConnRecord.retrieve_by_id(session, connection_id)
    except StorageNotFoundError as err:
        raise web.HTTPNotFound(reason=err.roll_up) from err

    if connection.is_ready:
        msg = BasicMessage(content=params["content"])
        await outbound_handler(msg, connection_id=connection_id)

    return web.json_response({})
```

This method retrieves connection between Faber and Alice by ID (`conn_id`), ensures that the connection is ready for use, and then sends the message content from the API POST request through that connection to Alice using the `outbound_handler` and awaits the response from the handler (note: this does not mean it waits for a response from Alice).

## Issuing and Proving Credentials

This one feels a little more complicated than simply sending a message through a secure channel.
Let's break it into the two key phases:

### Issuing a Credential

1. I press 1 to Issue a Credential from the Faber agent

When ready to test the credentials exchange protocols, go to the Faber prompt, enter "1" to send a credential, and then "2" to request a proof.

You don't need to do anything with Alice's agent - her agent is implemented to automatically receive credentials and respond to proof requests.

Note there is an option "2a" to initiate a connectionless proof - you can execute this option but it will only work end-to-end when connecting to Faber from a mobile agent.

```bash
    (1) Issue Credential
    (1a) Set Credential Type (indy)
    (2) Send Proof Request
    (2a) Send *Connectionless* Proof Request (requires a Mobile client)
    (3) Send Message
    (4) Create New Invitation
    (T) Toggle tracing on credential/proof exchange
    (X) Exit?
[1/2/3/4/T/X] 1

#13 Issue credential offer to X
Faber      | Credential: state = offer-sent, cred_ex_id = 4514a6bc-d346-4f11-9f3f-f12d5255c3ec
Faber      | Credential: state = request-received, cred_ex_id = 4514a6bc-d346-4f11-9f3f-f12d5255c3ec

#17 Issue credential to X
Faber      | Credential: state = credential-issued, cred_ex_id = 4514a6bc-d346-4f11-9f3f-f12d5255c3ec
Faber      | Credential: state = done, cred_ex_id = 4514a6bc-d346-4f11-9f3f-f12d5255c3ec
```

#### Execution Flow As Seen from Terminal Output

1. Faber sends a _credential offer_ to Alice, indicating that Faber is ready to issue a credential (e.g., a diploma or certificate).
2. The state of the credential exchange becomes `offer-sent` with a unique identifier cred_ex_id = 4514a6bc-d346-4f11-9f3f-f12d5255c3ec.

```bash
#13 Issue credential offer to X
Faber      | Credential: state = offer-sent, cred_ex_id = 4514a6bc-d346-4f11-9f3f-f12d5255c3ec
```

3. Alice’s agent acknowledges the offer. Credential exchange state changes to `offer-received`.
4. Alice sends a request to receive the credential. Credential exchange state changes to `request-sent`.

```bash
Alice      | Credential: state = offer-received, cred_ex_id = a983e241-e389-450d-ab0c-839dcc4e04cd

#15 After receiving credential offer, send credential request
Alice      | Credential: state = request-sent, cred_ex_id = a983e241-e389-450d-ab0c-839dcc4e04cd
```

5. Faber receives the credential request from Alice. Credential exchange state transitions to `request-received`.
6. Faber issues a credential to Alice. The credential exchange state changes to `credential-issued`.

```bash
Faber      | Credential: state = request-received, cred_ex_id = 4514a6bc-d346-4f11-9f3f-f12d5255c3ec
#17 Issue credential to X
Faber      | Credential: state = credential-issued, cred_ex_id = 4514a6bc-d346-4f11-9f3f-f12d5255c3ec
```

7. Alice receives the issued credential from Faber. Credential exchange state changes to `credential-received`
8. Alice stores that credential in her digital wallet for future access. We see the details of the credential. Credential exchange state changes to `done`.

```bash
Alice      | Credential: state = credential-received, cred_ex_id = a983e241-e389-450d-ab0c-839dcc4e04cd

#18.1 Stored credential 882d02e7-f7a6-4232-8ca4-be99dbcc3d56 in wallet
Alice      | Credential: state = done, cred_ex_id = a983e241-e389-450d-ab0c-839dcc4e04cd
Credential details:
{
    "referent": "882d02e7-f7a6-4232-8ca4-be99dbcc3d56",
    "schema_id": "BFrwRn2CRVXLBMDDaPnpE8:2:degree schema:83.50.79",
    "cred_def_id": "BFrwRn2CRVXLBMDDaPnpE8:3:CL:12:faber.agent.degree_schema",
    "rev_reg_id": null,
    "cred_rev_id": null,
    "attrs": {
        "date": "2018-05-28",
        "degree": "Maths",
        "timestamp": "1726085749",
        "birthdate_dateint": "20000911",
        "name": "Alice Smith"
    }
}

Alice      | credential_id 882d02e7-f7a6-4232-8ca4-be99dbcc3d56
Alice      | cred_def_id BFrwRn2CRVXLBMDDaPnpE8:3:CL:12:faber.agent.degree_schema
Alice      | schema_id BFrwRn2CRVXLBMDDaPnpE8:2:degree schema:83.50.79
```

9. We see that credential exchange state change to `done` on the Faber agent as well.

```bash
Faber      | Credential: state = done, cred_ex_id = 4514a6bc-d346-4f11-9f3f-f12d5255c3ec
```

#### The credential details explained:

These fields in the credential JSON object define the credential's identity, structure, revocation status, and the actual information contained within it.

- `referent`: Unique identifier for this credential instance.
- `schema_id`: Identifier for the schema used to define the structure of the - - credential (who issued it, version, and name).
- `red_def_id`: Credential definition ID specifying the format and cryptographic setup for the credential issuance.
- `rev_reg_id`: ID for the revocation registry (null if the credential is non-revocable).
- `cred_rev_id`: ID representing the credential's revocation status (null if not revocable).
- `attrs`: Actual data in the credential, including:
  - `date`: The date of issuance (2018-05-28).
  - `degree`: Type of degree awarded (Maths).
  - `timestamp`: Unix timestamp of the credential issuance (1726085749).
  - `birthdate_dateint`: The recipient’s birthdate in YYYYMMDD format (20000911).
  - `name`: The recipient’s full name (Alice Smith).

#### Execution Flow in Python

The following code in `faber.py` executes when you enter `1` for Issuing a credential to Alice.

```python
faber.py:680

elif option == "1":
    log_status("#13 Issue credential offer to X")

    if faber_agent.aip == 10:
        offer_request = faber_agent.agent.generate_credential_offer(
            faber_agent.aip, None, faber_agent.cred_def_id, exchange_tracing
        )
        await faber_agent.agent.admin_POST(
            "/issue-credential/send-offer", offer_request
        )

    elif faber_agent.aip == 20:
        if faber_agent.cred_type == CRED_FORMAT_INDY:
            offer_request = faber_agent.agent.generate_credential_offer(
                faber_agent.aip,
                faber_agent.cred_type,
                faber_agent.cred_def_id,
                exchange_tracing,
            )

        elif faber_agent.cred_type == CRED_FORMAT_JSON_LD:
            offer_request = faber_agent.agent.generate_credential_offer(
                faber_agent.aip,
                faber_agent.cred_type,
                None,
                exchange_tracing,
            )

        elif faber_agent.cred_type == CRED_FORMAT_VC_DI:
            offer_request = faber_agent.agent.generate_credential_offer(
                faber_agent.aip,
                faber_agent.cred_type,
                faber_agent.cred_def_id,
                exchange_tracing,
            )

        else:
            raise Exception(
                f"Error invalid credential type: {faber_agent.cred_type}"
            )

        await faber_agent.agent.admin_POST(
            "/issue-credential-2.0/send-offer", offer_request
        )

    else:
        raise Exception(f"Error invalid AIP level: {faber_agent.aip}")

```

This code is handling the control flow for issuing the credential offer to Alice; it executes differently depending on the AIP (Aries Interop Profile) level and the credential type, where the AIP defines the rules interoperability between Aries agents. It specifies how agents communicate, exchange credentials, and handle proofs, ensuring compatibility across different implementations. Different AIP levels (e.g., AIP 1.0, AIP 2.0) represent different versions of these standards, with newer levels supporting additional features and formats.

Here's a concise breakdown of the control flow:

1. Log `#13 Issue credential offer to X` to standard output
2. Check Aries Interop Profile (AIP) Level to determine how to generate and send the credential offer. Note that the default AIP level is 20 as seen here:

```python
agent_container:719

class AgentContainer:
    def __init__(
        self,
        ident: str,
        start_port: int,
        prefix: str = None,
        no_auto: bool = False,
        revocation: bool = False,
        genesis_txns: str = None,
        genesis_txn_list: str = None,
        tails_server_base_url: str = None,
        cred_type: str = CRED_FORMAT_INDY,
        show_timing: bool = False,
        multitenant: bool = False,
        mediation: bool = False,
        use_did_exchange: bool = False,
        wallet_type: str = None,
        public_did: bool = True,
        seed: str = "random",
        aip: int = 20, # HERE
        arg_file: str = None,
        endorser_role: str = None,
        reuse_connections: bool = False,
        multi_use_invitations: bool = False,
        public_did_connections: bool = False,
        emit_did_peer_2: bool = False,
        emit_did_peer_4: bool = False,
        taa_accept: bool = False,
        anoncreds_legacy_revocation: str = None,
        log_file: str = None,
        log_config: str = None,
        log_level: str = None,
        extra_args: List[str] = None,
    ):
```

3. If AIP is 20: - Check the credential format (cred_type). We know from the terminal output that the cred format is indy, so we know the flow here. - Generate a credential offer with the Indy credential format, and send the offer to the `/issue-credential-2.0/send-offer` endpoint of the Admin API.

4. The Admin API route is defined here:

```python

routes.py:1745

web.post(
    "/issue-credential-2.0/send-offer", credential_exchange_send_free_offer
),

```

5. The function `credential_exchange_send_free_offer` executes, defined here:

```python
routes.py:1031
@docs(
    tags=["issue-credential v2.0"],
    summary="Send holder a credential offer, independent of any proposal",
)
@request_schema(V20CredOfferRequestSchema())
@response_schema(V20CredExRecordSchema(), 200, description="")
@tenant_authentication
async def credential_exchange_send_free_offer(request: web.BaseRequest):
    """Request handler for sending free credential offer.

    An issuer initiates a such a credential offer, free from any
    holder-initiated corresponding credential proposal with preview.

    Args:
        request: aiohttp request object

    Returns:
        The credential exchange record

    """
    r_time = get_timer()

    context: AdminRequestContext = request["context"]
    profile = context.profile
    outbound_handler = request["outbound_message_router"]

    body = await request.json()

    connection_id = body.get("connection_id")
    filt_spec = body.get("filter")
    if not filt_spec:
        raise web.HTTPBadRequest(reason="Missing filter")
    auto_issue = body.get(
        "auto_issue", context.settings.get("debug.auto_respond_credential_request")
    )
    auto_remove = body.get(
        "auto_remove", not profile.settings.get("preserve_exchange_records")
    )
    replacement_id = body.get("replacement_id")
    comment = body.get("comment")
    preview_spec = body.get("credential_preview")
    trace_msg = body.get("trace")

    cred_ex_record = None
    conn_record = None
    try:
        async with profile.session() as session:
            conn_record = await ConnRecord.retrieve_by_id(session, connection_id)
        if not conn_record.is_ready:
            raise web.HTTPForbidden(reason=f"Connection {connection_id} not ready")

        cred_ex_record, cred_offer_message = await _create_free_offer(
            profile=profile,
            filt_spec=filt_spec,
            connection_id=connection_id,
            auto_issue=auto_issue,
            auto_remove=auto_remove,
            preview_spec=preview_spec,
            comment=comment,
            trace_msg=trace_msg,
            replacement_id=replacement_id,
        )
        result = cred_ex_record.serialize()

    except (
        BaseModelError,
        AnonCredsIssuerError,
        IndyIssuerError,
        LedgerError,
        StorageNotFoundError,
        V20CredFormatError,
        V20CredManagerError,
    ) as err:
        LOGGER.exception("Error preparing free credential offer")
        if cred_ex_record:
            async with profile.session() as session:
                await cred_ex_record.save_error_state(session, reason=err.roll_up)
        # other party cannot yet receive a problem report about our failed protocol start
        raise web.HTTPBadRequest(reason=err.roll_up)

    await outbound_handler(cred_offer_message, connection_id=connection_id)

    trace_event(
        context.settings,
        cred_offer_message,
        outcome="credential_exchange_send_free_offer.END",
        perf_counter=r_time,
    )

    return web.json_response(result)

```

This function handles the process of sending a credential offer to Alice without requiring any prior proposal from Alice. In other words, it allows an issuer (Faber) to initiate a credential offer to a holder (Alice) without waiting for the holder to request it.

Key Steps:

- Request Parsing: The function extracts required fields from the request, including connection_id, filter, credential_preview, and other options like auto_issue.
- Validate Connection: It verifies the connection with the holder (using connection_id) to ensure it's ready.
- Create Credential Offer: A credential offer is generated using the specified filter and preview attributes.
- Error Handling: If any errors occur during this process (like invalid connection or credential format issues), appropriate exceptions are raised and logged.
- Send Credential Offer: Once the offer is created, it’s sent to the holder via the outbound_message_router, similar to how a basic encrypted message is sent as described previously.
- Response: The credential exchange record is serialized and returned in the HTTP response.

In summary, this function allows an issuer to send a credential offer directly to a holder, managing the process end-to-end, including validation, creation, error handling, and sending the offer.

### Requesting Proof of Credentials

Now that Faber successfully issued a credential, Faber can now request proof of said credential from Alice via that same encrypted communication channel.

We press 2 to do this.

#### Execution Flow in the Terminal

Note that we use the term **presentation** here. A presentation in the context of decentralized identity systems (like those built with Aries or DIDComm) refers to the proof of claims or credentials that a holder (e.g., Alice) provides to a verifier (e.g., Faber) to prove certain information about themselves.

Note these definitions:

- Holder: The individual or entity that owns a credential (e.g., Alice with her degree credential).
- Verifier: The entity requesting proof (e.g., Faber requesting proof of Alice's degree).
- Presentation: The process by which the holder presents verifiable information (e.g., degree, name) to the verifier in response to a request.

A presentation typically includes:

- Requested Data: The specific attributes the verifier asked for (e.g., degree name, issue date).
- Proof: Cryptographic evidence that the data comes from a trusted source and hasn’t been tampered with.
- Selective Disclosure: The holder can choose which pieces of data to share without revealing the entire credential.

The flow in the terminal is below:

1. Faber sends a proof request to Alice, asking her to provide verifiable information about her degree.
2. The state of the presentation becomes `request-sent`, with a unique ID (`pres_ex_id = 37e8f60b-a56f-4103-b717-bce421446b18`).

```bash
[1/2/3/4/T/X] 2  # (enter 2 at the prompt to Send a Proof Request to Alice)

#20 Request proof of degree from alice
Faber      | Presentation: state = request-sent, pres_ex_id = 37e8f60b-a56f-4103-b717-bce421446b18
Presentation: state = request-sent, pres_ex_id = 37e8f60b-a56f-4103-b717-bce421446b18
```

3. Alice receives the proof request. Presentation state changes to `request-received`.
4. Alice searches her digital wallet to find the credential that satisfies the specific request from Faber.
5. Alice, upon finding the satisfying credentials, generates the indy proof from the credentials. An Indy proof is a cryptographic proof generated from credentials issued on the Hyperledger Indy blockchain. It allows the holder to prove certain information (e.g., identity, qualifications) to a verifier without revealing unnecessary data, ensuring privacy. The proof is based on zero-knowledge proofs, meaning it confirms the truth of the claims without exposing sensitive details.
6. Alice sends the proof back to the verifier, Faber. Presentation state changes to `presentation-sent`.
7. Alice changes the presentation state to `done`.

```bash
Alice      | Presentation: state = request-received, pres_ex_id = fc1ed5b1-98bf-48d2-a8c3-1cf6a0eac76d

#24 Query for credentials in the wallet that satisfy the proof request

Presentation: state = request-received, pres_ex_id = fc1ed5b1-98bf-48d2-a8c3-1cf6a0eac76d

#25 Generate the indy proof

#26 Send the proof to X: {"indy": {"requested_predicates": {"0_birthdate_dateint_GE_uuid": {"cred_id": "c5d4f3fb-97f9-4cea-ba3c-39751322e2d1"}}, "requested_attributes": {"0_name_uuid": {"cred_id": "c5d4f3fb-97f9-4cea-ba3c-39751322e2d1", "revealed": false}, "0_date_uuid": {"cred_id": "c5d4f3fb-97f9-4cea-ba3c-39751322e2d1", "revealed": true}, "0_degree_uuid": {"cred_id": "c5d4f3fb-97f9-4cea-ba3c-39751322e2d1", "revealed": true}}, "self_attested_attributes": {}}}

Alice      | Presentation: state = presentation-sent, pres_ex_id = fc1ed5b1-98bf-48d2-a8c3-1cf6a0eac76d
Presentation: state = presentation-sent, pres_ex_id = fc1ed5b1-98bf-48d2-a8c3-1cf6a0eac76d
Alice      | Presentation: state = done, pres_ex_id = fc1ed5b1-98bf-48d2-a8c3-1cf6a0eac76d
Presentation: state = done, pres_ex_id = fc1ed5b1-98bf-48d2-a8c3-1cf6a0eac76d
```

8. Faber receives the proof from Alice. Presentation state changes to
   `presentation-received`.
9. Faber processes the proof to verify it.
10. Once verified, Faber changes presentation state to `done`.
11. The proof is flagged as either true or false. In this case, true.

```bash
Faber      | Presentation: state = presentation-received, pres_ex_id = 37e8f60b-a56f-4103-b717-bce421446b18

#27 Process the proof provided by X

#28 Check if proof is valid
Presentation: state = presentation-received, pres_ex_id = 37e8f60b-a56f-4103-b717-bce421446b18
Faber      | Presentation: state = done, pres_ex_id = 37e8f60b-a56f-4103-b717-bce421446b18
Presentation: state = done, pres_ex_id = 37e8f60b-a56f-4103-b717-bce421446b18
Faber      | Proof = true
```
