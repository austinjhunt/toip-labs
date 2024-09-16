# Lab 2: Help Alice Get a Job

## Overview

This lab involves creating a new controller for ACME Corp. We use the Alice and Faber samples from lab 1 to finish a controller that generates an invitation to connect to Alice and then requests proof that she has a degree.
Once everything is done, we are able to go through the Alice, Faber, and ACME demo from end-to-end.

The task is to add functionality to a **third** participant in the Alice/Faber drama - namely, Acme Inc. After completing her education at Faber College, Alice is going to apply for a job at **Acme Inc**. To do this she must provide proof of education (once she has completed the interview and other non-Indy tasks), and then Acme will issue her an employment credential.

Note that an updated Acme controller is available here: https://github.com/ianco/aries-cloudagent-python/tree/acme_workshop/demo if you just want to skip ahead ... There is also an alternate solution with some additional functionality available here: https://github.com/ianco/aries-cloudagent-python/tree/agent_workshop/demo

## Instructions

The instructions for getting started with the coding for this lab were found here: [https://aca-py.org/latest/demo/AcmeDemoWorkshop/](https://aca-py.org/latest/demo/AcmeDemoWorkshop/)

## Running

For simplicity, we're using Docker to run this lab locally.

Similar to lab 1, we'll create a von-network terminal session with `./manage start --logs` in the `von-network` folder.
Then, we'll need **3 terminal sessions**: one for Alice, one for Faber, one for Acme, Inc. The Acme one can join after Faber is gone.

We can pretty much follow the same steps we followed for lab 1. We need to run one terminal instance with Faber, then another terminal instance with Alice. Then we need to copy Faber's invitation to Alice so they can connect, and then we tell Faber to issue a credential to Alice. We know the proof works so we don't need to do that from the Faber terminal. If we think of this like Alice attending a school and then graduating, the next step is just to exit the Faber controller by entering X at the Faber prompt. That represents the end of Alice's academic relationship with Faber College, but she still does have the credential she was issued because she's still running.

Here's the output from the terminal sessions:

```bash

## FABER OUTPUT

Waiting for connection...
Faber      | Connected
Faber      | Check for endorser role ...
    (1) Issue Credential
    (1a) Set Credential Type (indy)
    (2) Send Proof Request
    (2a) Send *Connectionless* Proof Request (requires a Mobile client)
    (3) Send Message
    (4) Create New Invitation
    (T) Toggle tracing on credential/proof exchange
    (X) Exit?
[1/2/3/4/T/X] 3
Enter message: hello
Faber      | Received message: alice.agent received your message
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
Faber      | Credential: state = offer-sent, cred_ex_id = 8859dfdd-528d-4058-a1ab-634f6f83c29c
Faber      | Credential: state = request-received, cred_ex_id = 8859dfdd-528d-4058-a1ab-634f6f83c29c

#17 Issue credential to X
Faber      | Credential: state = credential-issued, cred_ex_id = 8859dfdd-528d-4058-a1ab-634f6f83c29c
Faber      | Credential: state = done, cred_ex_id = 8859dfdd-528d-4058-a1ab-634f6f83c29c
    (1) Issue Credential
    (1a) Set Credential Type (indy)
    (2) Send Proof Request
    (2a) Send *Connectionless* Proof Request (requires a Mobile client)
    (3) Send Message
    (4) Create New Invitation
    (T) Toggle tracing on credential/proof exchange
    (X) Exit?
[1/2/3/4/T/X]

...

## ALICE RESPONSE

Connect duration: 0.08s
Waiting for connection...
Alice      | Connected
Alice      | Check for endorser role ...
Connect duration: 0.23s
Alice      | Received message: hello
Alice      | Credential: state = offer-received, cred_ex_id = 8bb0fcae-fd66-4a54-922b-93b961c15e61

#15 After receiving credential offer, send credential request
Alice      | Credential: state = request-sent, cred_ex_id = 8bb0fcae-fd66-4a54-922b-93b961c15e61
Alice      | Credential: state = credential-received, cred_ex_id = 8bb0fcae-fd66-4a54-922b-93b961c15e61

#18.1 Stored credential d6f24513-60bb-4975-bad6-bd20e8e71aba in wallet
Alice      | Credential: state = done, cred_ex_id = 8bb0fcae-fd66-4a54-922b-93b961c15e61
Credential details:
  {
    "referent": "d6f24513-60bb-4975-bad6-bd20e8e71aba",
    "schema_id": "FrWdCvYJHr528X6DjiAYXG:2:degree schema:95.16.78",
    "cred_def_id": "FrWdCvYJHr528X6DjiAYXG:3:CL:1981088:faber.agent.degree_schema",
    "rev_reg_id": null,
    "cred_rev_id": null,
    "attrs": {
      "birthdate_dateint": "20000912",
      "degree": "Maths",
      "name": "Alice Smith",
      "timestamp": "1726110475",
      "date": "2018-05-28"
    }
  }

Alice      | credential_id d6f24513-60bb-4975-bad6-bd20e8e71aba
Alice      | cred_def_id FrWdCvYJHr528X6DjiAYXG:3:CL:1981088:faber.agent.degree_schema
Alice      | schema_id FrWdCvYJHr528X6DjiAYXG:2:degree schema:95.16.78
    (3) Send Message
    (4) Input New Invitation
    (X) Exit?


### NOW WE CLOSE FABER
    (1) Issue Credential
    (1a) Set Credential Type (indy)
    (2) Send Proof Request
    (2a) Send *Connectionless* Proof Request (requires a Mobile client)
    (3) Send Message
    (4) Create New Invitation
    (T) Toggle tracing on credential/proof exchange
    (X) Exit?
[1/2/3/4/T/X] x
Shutting down agent ...
Faber      |
Faber      | Shutting down
Faber      | Exited with return code 0
austinhunt@Austins-MBP-2 demo %
```

Now that the Faber agent is closed (Alice left Faber College), we run the Acme agent in the same terminal.

```bash

# ACME agent
austinhunt@Austins-MBP-2 demo % LEDGER_URL=http://test.bcovrin.vonx.io AGENT_PORT_OVERRIDE=8010 ./run_demo acme
Resolution not specified or invalid.
You can utilize the 'build' option to build the agent or the 'run' option to run the agent.
Preparing agent image...
...
...
...
Starting [acme] agent with args [--port 8010]
/home/aries/demo/runners/acme.py:225: DeprecationWarning: There is no current event loop
  asyncio.get_event_loop().run_until_complete(main(args))
Initializing demo agent acme with AIP 20 and credential type indy
#1 Provision an agent and wallet, get back configuration details
Started webhook listener on port: 8012
Acme       | Registering acme.agent ...
using ledger: http://test.bcovrin.vonx.io/register
Acme       | nym_info: {'did': '6ZRiAwACT86h1PbzxMYJYp', 'seed': '8588f83f6cf7582fa8906d9e98325632', 'verkey': '42jXJfv6p47R66FfBBcRbDoPxQDTSH4Fczkvzmqu5zDC'}
Acme       | Registered DID: 6ZRiAwACT86h1PbzxMYJYp
Created public DID
...
...
...
Acme       | Created new profile
Acme       | Profile backend: askar
Acme       | Profile name: acme.agentf5f2900f
Acme       | Created new public DID: 6ZRiAwACT86h1PbzxMYJYp
Acme       | Verkey: 42jXJfv6p47R66FfBBcRbDoPxQDTSH4Fczkvzmqu5zDC
...
...
...
Acme       | ::                                          ::
Acme       | ::                                          ::
Acme       | :: Inbound Transports:                      ::
Acme       | ::                                          ::
Acme       | ::   - http://0.0.0.0:8010                  ::
Acme       | ::                                          ::
Acme       | :: Outbound Transports:                     ::
Acme       | ::                                          ::
Acme       | ::   - http                                 ::
Acme       | ::   - https                                ::
Acme       | ::                                          ::
Acme       | :: Public DID Information:                  ::
Acme       | ::                                          ::
Acme       | ::   - DID: 6ZRiAwACT86h1PbzxMYJYp          ::
Acme       | ::                                          ::
Acme       | :: Administration API:                      ::
Acme       | ::                                          ::
Acme       | ::   - http://0.0.0.0:8011                  ::
Acme       | ::                                          ::
Acme       | ::                               ver: 1.0.0 ::
Acme       | ::::::::::::::::::::::::::::::::::::::::::::::
Acme       |
Acme       | Listening...
Acme       |
Acme       |
Startup duration: 3.55s
Admin URL is at: http://host.docker.internal:8011
Endpoint URL is at: http://host.docker.internal:8010

#7 Create a connection to alice and print out the invite details
Generate invitation duration: 0.03s
Use the following JSON to accept the invite from another demo agent. Or use the QR code to connect from a mobile agent.
Invitation Data:
{"@type": "https://didcomm.org/out-of-band/1.1/invitation", "@id": "70ac49b5-a9cb-46e0-ab3e-ce8acbd4586f", "label": "acme.agent", "handshake_protocols": ["https://didcomm.org/didexchange/1.1"], "services": [{"id": "#inline", "type": "did-communication", "recipientKeys": ["did:key:z6MkjgzQnZUAPMJJ9B5nbF7hvGw4VjyRzzRNpyzvPTtTzhEG#z6MkjgzQnZUAPMJJ9B5nbF7hvGw4VjyRzzRNpyzvPTtTzhEG"], "serviceEndpoint": "http://host.docker.internal:8010"}]}
```

Since we now have an invitation for Acme, we can go to Alice, enter 4 to enter a new invitation, and copy the Acme invitation over:

```bash
Alice      | schema_id FrWdCvYJHr528X6DjiAYXG:2:degree schema:95.16.78
    (3) Send Message
    (4) Input New Invitation
    (X) Exit?
[3/4/X] 4

Input new invitation details
Invite details: {"@type": "https://didcomm.org/out-of-band/1.1/invitat
ion", "@id": "70ac49b5-a9cb-46e0-ab3e-ce8acbd4586f", "label": "acme.ag
ent", "handshake_protocols": ["https://didcomm.org/didexchange/1.1"],
"services": [{"id": "#inline", "type": "did-communication", "recipient
Keys": ["did:key:z6MkjgzQnZUAPMJJ9B5nbF7hvGw4VjyRzzRNpyzvPTtTzhEG#z6Mk
jgzQnZUAPMJJ9B5nbF7hvGw4VjyRzzRNpyzvPTtTzhEG"], "serviceEndpoint": "ht
tp://host.docker.internal:8010"}]}
Invitation response:
  {
    "state": "deleted",
    "created_at": "2024-09-12T03:15:55.838878Z",
    "updated_at": "2024-09-12T03:15:55.838878Z",
    "trace": false,
    "oob_id": "ad0f8970-c766-474d-bcd4-101328b5f69b",
    "invi_msg_id": "70ac49b5-a9cb-46e0-ab3e-ce8acbd4586f",
    "invitation": {
      "@type": "https://didcomm.org/out-of-band/1.1/invitation",
      "@id": "70ac49b5-a9cb-46e0-ab3e-ce8acbd4586f",
      "label": "acme.agent",
      "handshake_protocols": [
        "https://didcomm.org/didexchange/1.1"
      ],
      "services": [
        {
          "id": "#inline",
          "type": "did-communication",
          "recipientKeys": [
            "did:key:z6MkjgzQnZUAPMJJ9B5nbF7hvGw4VjyRzzRNpyzvPTtTzhEG#z6MkjgzQnZUAPMJJ9B5nbF7hvGw4VjyRzzRNpyzvPTtTzhEG"
          ],
          "serviceEndpoint": "http://host.docker.internal:8010"
        }
      ]
    },
    "connection_id": "4a881b93-28f3-43d1-82e8-3c35520f4840",
    "role": "receiver",
    "multi_use": false
  }

Connect duration: 0.08s
Waiting for connection...
Alice      | Connected
Alice      | Check for endorser role ...
Connect duration: 0.26s
```

Because we haven't implemented the controller yet, entering 2 or 1 in the Acme agent does nothing yet (no output in Alice's agent either).

```bash
Acme       | Connected
    (1) Issue Credential
    (2) Send Proof Request
    (3) Send Message
    (X) Exit?
[1/2/3/X]2

#20 Request proof of degree from alice
    (1) Issue Credential
    (2) Send Proof Request
    (3) Send Message
    (X) Exit?
[1/2/3/X]1

#13 Issue credential offer to X
    (1) Issue Credential
    (2) Send Proof Request
    (3) Send Message
    (X) Exit?
[1/2/3/X]

```

So, we need to implement:

- Option 2, Proof Request, so Acme can send a proof request to Alice (i.e., request proof of education at Faber College)
- Option 1, Issue Credential, so Acme can issue a work credential (i.e., so Alice can prove to future employers that she works/worked at Acme).

Please note that the [Lab 1 README](../lab-1/README.md) explains in detail how each of these processes work and walks through the control flow for each, so review that if necessary. These changes applied to `acme.py` are pretty much the exact same thing.

## Implementing the Proof Request

We need to update [acme.py](../aries-cloudagent-python/demo/runners/acme.py) with this implementation. Refer to the file itself for the implementation details. I've wrapped all changes related to the proof request implementation in the following comments that you can search for:

```python
### PROOF REQUEST IMPLEMENTATION ###
changes here
### PROOF REQUEST IMPLEMENTATION ###
```

### Testing

To test these changes, I closed the Acme agent, and restarted it. I then re-invited Alice with the new invitation from Acme. Then, I entered 2 at the Acme prompt to send a proof request to Alice. The results indicate a successful, functional implementation. We see that Acme receives the proof back from Alice with claims that reveal some information about the education. Note that the name claim is not revealed, so we can see that she's got a verified education credential but we don't know from which college.

```bash
Acme       | Connected
    (1) Issue Credential
    (2) Send Proof Request
    (3) Send Message
    (X) Exit?
[1/2/3/X]2

#20 Request proof of degree from alice
Acme       | Presentation: state = request-sent, pres_ex_id = ab1678ac-730f-45bd-8689-9d8669083ce9
Acme       | Presentation: state = presentation-received, pres_ex_id = ab1678ac-730f-45bd-8689-9d8669083ce9

#27 Process the proof provided by X

#28 Check if proof is valid
Acme       | Presentation: state = done, pres_ex_id = ab1678ac-730f-45bd-8689-9d8669083ce9
Acme       | Proof =  true

#28.1 Received proof of education, check claims
Acme       | name: (attribute not revealed)
Acme       | date: 2018-05-28
Acme       | degree: Maths
Acme       | schema_id: FrWdCvYJHr528X6DjiAYXG:2:degree schema:95.16.78
Acme       | cred_def_id FrWdCvYJHr528X6DjiAYXG:3:CL:1981088:faber.agent.degree_schema
```

## Implementing the Issuing of Credentials

This implementation is also isolated to the [acme.py](../aries-cloudagent-python/demo/runners/acme.py) file. Refer to the file itself for the implementation details.

I've wrapped all changes related to the issuing of credentials in the following comments that you can search for:

```python
### ISSUE CREDENTIALS IMPLEMENTATION ###
changes here
### ISSUE CREDENTIALS IMPLEMENTATION ###
```

### Testing

To test these changes, I again closed the Acme agent, and restarted it. I then re-invited Alice with the new invitation from Acme. Then, I entered 1 at the Acme prompt to issue a work credential to Alice. The terminal output shows a successful implementation below; we see the successful issuing of a work credential by Acme to Alice, and the successful storage of that credential by Alice.

```bash
## ACME

Acme       | Connected
    (1) Issue Credential
    (2) Send Proof Request
    (3) Send Message
    (X) Exit?
[1/2/3/X]1

#13 Issue credential offer to X
Acme       | Credential: state = offer-sent, cred_ex_id = 26410273-530b-4bba-82e9-9a8440ac7d8e
Acme       | Credential: state = request-received, cred_ex_id = 26410273-530b-4bba-82e9-9a8440ac7d8e
Acme       | Credential: state = credential-issued, cred_ex_id = 26410273-530b-4bba-82e9-9a8440ac7d8e
Acme       | Credential: state = done, cred_ex_id = 26410273-530b-4bba-82e9-9a8440ac7d8e

...
...
...

### ALICE

Alice      | Credential: state = offer-received, cred_ex_id = b233806f-4205-4709-a468-b9279a777aa6

#15 After receiving credential offer, send credential request
Alice      | Credential: state = request-sent, cred_ex_id = b233806f-4205-4709-a468-b9279a777aa6
Alice      | Credential: state = credential-received, cred_ex_id = b233806f-4205-4709-a468-b9279a777aa6

#18.1 Stored credential 4bb80721-1191-49a1-a4cc-7eefbe0443a2 in wallet
Alice      | Credential: state = done, cred_ex_id = b233806f-4205-4709-a468-b9279a777aa6
Credential details:
  {
    "referent": "4bb80721-1191-49a1-a4cc-7eefbe0443a2",
    "schema_id": "Pxx41UDWRUNHeASFzRhDFG:2:employee id schema:30.21.23",
    "cred_def_id": "Pxx41UDWRUNHeASFzRhDFG:3:CL:1981114:acme.agent.employee_id_schema",
    "rev_reg_id": null,
    "cred_rev_id": null,
    "attrs": {
      "date": "2024-09-12",
      "employee_id": "ACME0009",
      "position": "CEO",
      "name": "Alice Smith"
    }
  }

Alice      | credential_id 4bb80721-1191-49a1-a4cc-7eefbe0443a2
Alice      | cred_def_id Pxx41UDWRUNHeASFzRhDFG:3:CL:1981114:acme.agent.employee_id_schema
Alice      | schema_id Pxx41UDWRUNHeASFzRhDFG:2:employee id schema:30.21.23
```

## Implementing Supplemental Issuing of Credentials (Extra Feature)

Lab 2 offers a choice of also implementing the issuing of a work credential offer from Acme to Alice upon receipt of the Faber proof from Alice. In other words, when she proves she went to Faber, immediately issue a work credential offer, rather than waiting on "1" to be input at the Acme prompt.

Since this would entail the same logic as what we put under the condition for option 1, I wrapped the logic in a modular, reusable async method `issue_credential_offer`, seen below:

```python
async def issue_credential_offer(agent, schema_attrs, schema_name, cred_def_id, ):
    """ Reusable function to issue credentials based on schema attributes """
    agent.cred_attrs[cred_def_id] = {
        "employee_id": "ACME0009",
        "name": "Alice Smith",
        "date": date.isoformat(date.today()),
        "position": "CEO"
    }
    cred_preview = {
        "@type": CRED_PREVIEW_TYPE,
        "attributes": [
            {"name": n, "value": v}
            for (n, v) in agent.cred_attrs[cred_def_id].items()
        ],
    }
    offer_request = {
        "connection_id": agent.connection_id,
        "comment": f"Offer on cred def id {cred_def_id}",
        "credential_preview": cred_preview,
        "filter": {"indy": {"cred_def_id": cred_def_id}},
    }
    await agent.admin_POST(
        "/issue-credential-2.0/send-offer", offer_request
    )
```

So the condition for option 1 looks a little different from the instructions (it's cleaner):

```python
elif option == "1":
    log_status("#13 Issue credential offer to X")
    ### ISSUE CREDENTIALS IMPLEMENTATION ###
    await issue_credentials(
        agent,
        acme_schema_attrs,
        acme_schema_name,
        cred_def_id,
    )
    ### ISSUE CREDENTIALS IMPLEMENTATION ###
```

And the logic after receiving the proof of education now looks a bit different as well:

```python
 if is_proof_of_education:
                log_status("#28.1 Received proof of education, check claims")
                for (referent, attr_spec) in pres_req["requested_attributes"].items():
                    if referent in pres['requested_proof']['revealed_attrs']:
                        self.log(
                            f"{attr_spec['name']}: "
                            f"{pres['requested_proof']['revealed_attrs'][referent]['raw']}"
                        )
                    else:
                        self.log(
                            f"{attr_spec['name']}: "
                            "(attribute not revealed)"
                        )

                ### ISSUE CREDENTIALS IMPLEMENTATION ###
                cred_def_id = None # initialize
                ### ISSUE CREDENTIALS IMPLEMENTATION ###

                for id_spec in pres["identifiers"]:
                    # just print out the schema/cred def id's of presented claims
                    self.log(f"schema_id: {id_spec['schema_id']}")
                    self.log(f"cred_def_id {id_spec['cred_def_id']}")

                    ### ISSUE CREDENTIALS IMPLEMENTATION ###
                    # Set cred def id to the one received in proof
                    cred_def_id = id_spec["cred_def_id"]
                    ### ISSUE CREDENTIALS IMPLEMENTATION ###

                ### ISSUE CREDENTIALS IMPLEMENTATION ###
                # issue credentials based on proof received automatically without waiting for 1 input at Acme prompt from user
                self.log("#28.2 Issue credential offer to X automatically based on proof received")
                await issue_credential_offer(
                    agent=self,
                    schema_attrs=["employee_id", "name", "date", "position"],
                    schema_name="employee id schema",
                    cred_def_id=cred_def_id
                )
                self.log("#28.3 Issue credential offer sent")
                ### ISSUE CREDENTIALS IMPLEMENTATION ###
            else:
                # in case there are any other kinds of proofs received
                self.log("#28.1 Received ", pres_req["name"])
            ### PROOF REQUEST IMPLEMENTATION ###
```

### Testing

To test these changes, I again closed the Acme agent, and restarted it. I then re-invited Alice with the new invitation from Acme.

Now, instead of pressing 1 to issue a work credential explicitly/manually from Acme to Alice, I press 2 to just send a proof request. The output of this should include log statements that I added indicating automatic issuing of a credential offer back to Alice upon receipt of the proof. Successful results are shown in the Acme terminal output below:

```bash

Acme       | Connected
    (1) Issue Credential
    (2) Send Proof Request
    (3) Send Message
    (X) Exit?
[1/2/3/X]2

#20 Request proof of degree from alice
Acme       | Presentation: state = request-sent, pres_ex_id = b9b70174-27cc-4679-a4f6-34e42b77cb41
Acme       | Presentation: state = presentation-received, pres_ex_id = b9b70174-27cc-4679-a4f6-34e42b77cb41

#27 Process the proof provided by X

#28 Check if proof is valid
Acme       | Presentation: state = done, pres_ex_id = b9b70174-27cc-4679-a4f6-34e42b77cb41
Acme       | Proof =  true

#28.1 Received proof of education, check claims
Acme       | name: (attribute not revealed)
Acme       | date: 2018-05-28
Acme       | degree: Maths
Acme       | schema_id: FrWdCvYJHr528X6DjiAYXG:2:degree schema:95.16.78
Acme       | cred_def_id FrWdCvYJHr528X6DjiAYXG:3:CL:1981088:faber.agent.degree_schema
Schema:
  {
    "sent": {
      "schema_id": "PDxcKNtrhEZ2j5YMy9Hhnq:2:employee id schema:46.12.57",
      "schema": {
        "ver": "1.0",
        "id": "PDxcKNtrhEZ2j5YMy9Hhnq:2:employee id schema:46.12.57",
        "name": "employee id schema",
        "version": "46.12.57",
        "attrNames": [
          "employee_id",
          "name",
          "date",
          "position"
        ],
        "seqNo": 1981128
      }
    },
    "schema_id": "PDxcKNtrhEZ2j5YMy9Hhnq:2:employee id schema:46.12.57",
    "schema": {
      "ver": "1.0",
      "id": "PDxcKNtrhEZ2j5YMy9Hhnq:2:employee id schema:46.12.57",
      "name": "employee id schema",
      "version": "46.12.57",
      "attrNames": [
        "employee_id",
        "name",
        "date",
        "position"
      ],
      "seqNo": 1981128
    }
  }

Schema ID: PDxcKNtrhEZ2j5YMy9Hhnq:2:employee id schema:46.12.57
Cred def ID: PDxcKNtrhEZ2j5YMy9Hhnq:3:CL:1981128:acme.agent.employee_id_schema
Publish schema and cred def duration: 9.92s
Acme       | #28.2 Issue credential offer to X automatically based on proof received
Acme       | Credential: state = offer-sent, cred_ex_id = 6848f83d-329e-418b-98ed-e429590f585d
Acme       | #28.3 Issue credential offer sent
Acme       | Credential: state = request-received, cred_ex_id = 6848f83d-329e-418b-98ed-e429590f585d
Acme       | Credential: state = credential-issued, cred_ex_id = 6848f83d-329e-418b-98ed-e429590f585d
Acme       | Credential: state = done, cred_ex_id = 6848f83d-329e-418b-98ed-e429590f585d
```

And the corresponding Alice output, following entering 2 at the Acme agent prompt:

```bash

Alice      | Presentation: state = request-received, pres_ex_id = df37a2ef-1dd8-4612-b0f7-399917eb9d59

#24 Query for credentials in the wallet that satisfy the proof request
Presentation: state = request-received, pres_ex_id = df37a2ef-1dd8-4612-b0f7-399917eb9d59

#25 Generate the indy proof

#26 Send the proof to X: {"indy": {"requested_predicates": {}, "requested_attributes": {"0_name_uuid": {"cred_id": "d6f24513-60bb-4975-bad6-bd20e8e71aba", "revealed": false}, "0_date_uuid": {"cred_id": "d6f24513-60bb-4975-bad6-bd20e8e71aba", "revealed": true}, "0_degree_uuid": {"cred_id": "d6f24513-60bb-4975-bad6-bd20e8e71aba", "revealed": true}}, "self_attested_attributes": {}}}
Alice      | Presentation: state = presentation-sent, pres_ex_id = df37a2ef-1dd8-4612-b0f7-399917eb9d59
Presentation: state = presentation-sent, pres_ex_id = df37a2ef-1dd8-4612-b0f7-399917eb9d59
Alice      | Presentation: state = done, pres_ex_id = df37a2ef-1dd8-4612-b0f7-399917eb9d59
Presentation: state = done, pres_ex_id = df37a2ef-1dd8-4612-b0f7-399917eb9d59

Alice      | Credential: state = offer-received, cred_ex_id = 528f1ab7-f714-474f-a8af-5d6a4ed42dd1

#15 After receiving credential offer, send credential request
Alice      | Credential: state = request-sent, cred_ex_id = 528f1ab7-f714-474f-a8af-5d6a4ed42dd1
Alice      | Credential: state = credential-received, cred_ex_id = 528f1ab7-f714-474f-a8af-5d6a4ed42dd1

#18.1 Stored credential d1aedb57-992c-40f9-babe-4f2af00999b9 in wallet
Alice      | Credential: state = done, cred_ex_id = 528f1ab7-f714-474f-a8af-5d6a4ed42dd1
Credential details:
  {
    "referent": "d1aedb57-992c-40f9-babe-4f2af00999b9",
    "schema_id": "PDxcKNtrhEZ2j5YMy9Hhnq:2:employee id schema:46.12.57",
    "cred_def_id": "PDxcKNtrhEZ2j5YMy9Hhnq:3:CL:1981128:acme.agent.employee_id_schema",
    "rev_reg_id": null,
    "cred_rev_id": null,
    "attrs": {
      "date": "2024-09-12",
      "name": "Alice Smith",
      "employee_id": "ACME0009",
      "position": "CEO"
    }
  }

Alice      | credential_id d1aedb57-992c-40f9-babe-4f2af00999b9
Alice      | cred_def_id PDxcKNtrhEZ2j5YMy9Hhnq:3:CL:1981128:acme.agent.employee_id_schema
Alice      | schema_id PDxcKNtrhEZ2j5YMy9Hhnq:2:employee id schema:46.12.57

```

So, Acme requests proof of Alice's education, receives it, verifies it, then offers a work credential offer back to Alice, who sees that then requests a work credential and receives it from Acme. Beautiful.

## Implementing Option 2a on ACME Agent

The default code does not allow us to test what happens when a proof fails. The task: to test the handling of negative scenarios in which the proof of credential generated by Alice actually **cannot be verified** by ACME, Inc.

To do this, I had to:

1. Of course, add the new 2a option for [acme.py](../aries-cloudagent-python/demo/runners/acme.py) as well as a handler. That handler definition is shown below.

```python
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
```

I defined it to wrap the same logic previously under option 2, such that the logic for crafting and sending a proof request is only defined once, and we can simply call this handler without the `test_failure` argument for the regular option 2:

```python
elif option == "2":
    log_status("#20 Request proof of degree from alice")
    ### PROOF REQUEST IMPLEMENTATION ###
    await request_proof_of_education(agent)
```

and we call it with `test_failure` for option 2a:

```python
elif option == "2a":
    log_status("#20 Request proof of degree from alice AND test failure handling")
    ### PROOF REQUEST IMPLEMENTATION ###
    await request_proof_of_education(agent, test_failure=True)
```

**The handler:** I needed to somehow add a boolean flag on the acme side that says to test a failure, so that Alice can see that same flag upon receiving the proof request. Since `comment` was already a field sent in the proof request from ACME to Alice and it wasn't being used for anything by default, I used this `comment` field. When option 2a is selected, we set the comment value to `test_failure`.

3. On the Alice side, when receiving a presentation request (proof request) from Acme, we check for the string `test_failure` in the comment property of the request. If present, we set the presentation exchange record state to a **new state**, `V20PresExRecord.STATE_REQUEST_RECEIVED_TEST_FAILURE (the string "request-received-test-failure")`. The default (when the comment does not contain this string) was originally just `request-received`.

4. Then, in the same place where we were checking if the state was the original `request-received`, we modify that to say `if state in ["request-received", "request-received-test-failure"]:`. Why? Because we still want to run the base proof generation logic used for a successful proof generation. After that original foundation logic runs, though, before Alice posts to her admin URL to send the presentation back to Acme, we do this:

```python
      # BEGIN NEW CODE
      if state == "request-received-test-failure":
          request.update({"test_failure": True})
      # END NEW CODE


      # This was original code
      log_status("#26 Send the proof to X: " + json.dumps(request))
      await self.admin_POST(
          f"/present-proof-2.0/records/{pres_ex_id}/send-presentation",
          request,
      )

```

The function that handles the /send-presentation route (called `present_proof_send_presentation(request: web.BaseRequest)`) now can see in the request payload that we need to test a failure. Where it previously would just generate the succesful presentation message for the proof request response and send it back to Acme via the encrypted connection, NOW we check if `test_failure` is true, and if so, we corrupt the degree claim in the data before responding:

```python
if test_failure:
    # Corrupt the presentation message data
    print(f'TESTING FAILURE: Corrupting presentation message data')
    # decode current data - FIX THIS - corrupted string just fails
    b64_string = pres_message.presentations_attach[0].data.base64

    # this a stringified JSON object in base64 format, can't directly call decode() on it yet
    # structure of decoded is stored in lab2/expected-data.json for reference
    decoded = base64.b64decode(b64_string).decode('utf-8')
    # now we can decode the JSON
    decoded = json.loads(decoded)

    # increment the degree attribute to corrupt it
    current_degree = decoded["proof"]["proofs"][0]["primary_proof"]["eq_proof"]["revealed_attrs"]["degree"]
    # all claims in the creds are numeric strings
    # they have to remain numeric strings
    # to corrupt "successfully", cast degree numeric string to int, increment, then cast back to str
    decoded["proof"]["proofs"][0]["primary_proof"]["eq_proof"]["revealed_attrs"]["degree"] = str(int(current_degree) + 1)
    encoded_new_degree = base64.b64encode(json.dumps(decoded).encode('utf-8'))
    pres_message.presentations_attach[0].data = AttachDecoratorData(
        base64_=encoded_new_degree
    )

  # Back to original code
  await outbound_handler(pres_message, connection_id=pres_ex_record.connection_id)
```

Now, when `acme.py` gets that proof back and tries to verify it, it fails as expected, and Acme immediately stops processing the credential because it is not verified.

```python
if not proof["verified"] or proof["verified"] == "false":
  # immediately return if proof is not valid
  self.log("#28.1 Proof is not valid. Not processing further.")
  return
```

As seen in the Acme terminal:

```bash
acme.agent handle_connections active completed
Acme       | Connected
    (1) Issue Credential
    (1) Issue Credential
    (2) Send Proof Request
    (2a) Send Proof Request (with failure handling)
    (3) Send Message
    (X) Exit?
[1/2/3/X]2a

#20 Request proof of degree from alice AND test failure handling
request_proof_of_education: test_failure: True
Acme       | Presentation: state = request-sent, pres_ex_id = 30764134-de36-4210-835f-86e523319f65
Acme       | Presentation: state = presentation-received, pres_ex_id = 30764134-de36-4210-835f-86e523319f65

#27 Process the proof provided by X

#28 Check if proof is valid
Acme       | Presentation: state = done, pres_ex_id = 30764134-de36-4210-835f-86e523319f65
Acme       | Proof =  false
Acme       | #28.1 Proof is not valid. Not processing further.
Acme       | 2024-09-13 15:40:59,713 aries_cloudagent.indy.credx.verifier ERROR Presentation on nonce=326468928587849843118056166676006383834 cannot be validated (presentation will be marked as Invalid): Encoded representation mismatch for 'degree'
```

And as seen in the Alice terminal (parallel to the Acme one):

```bash
Alice      | handle_present_proof_v2_0: state = request-received-test-failure, pres_ex_id = 86d0ade0-0661-4b26-b136-9e50be94861f

#24 Query for credentials in the wallet that satisfy the proof request

#25 Generate the indy proof

#26 Send the proof to X: {"indy": {"requested_predicates": {}, "requested_attributes": {"0_name_uuid": {"cred_id": "02463029-ef11-47dc-981b-17682221f966", "revealed": false}, "0_date_uuid": {"cred_id": "02463029-ef11-47dc-981b-17682221f966", "revealed": true}, "0_degree_uuid": {"cred_id": "02463029-ef11-47dc-981b-17682221f966", "revealed": true}}, "self_attested_attributes": {}}, "test_failure": true}
Alice      | TEST FAILURE
Alice      | handle_present_proof_v2_0: state = presentation-sent, pres_ex_id = 86d0ade0-0661-4b26-b136-9e50be94861f
Alice      | handle_present_proof_v2_0: state = done, pres_ex_id = 86d0ade0-0661-4b26-b136-9e50be94861f
Alice      | present_proof_send_presentation: TESTING FAILURE
Alice      | TESTING FAILURE: Corrupting presentation message data
```

So, we can see that if Alice "lies" about her degree, e.g., "I have a master's in something I didn't study", ACME is able to check that against the ledger and see that it is not verified, and thus not process her credential further, which could mean not hiring her or opening further communication to resolve the problem with Alice, etc.
