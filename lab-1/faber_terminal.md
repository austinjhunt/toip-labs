```bash
austinhunt@Austins-MBP-2 demo % AGENT_PORT_OVERRIDE=8010 ./run_demo faber

Resolution not specified or invalid.
You can utilize the 'build' option to build the agent or the 'run' option to run the agent.
Preparing agent image...
[+] Building 0.3s (21/21) FINISHED docker:desktop-linux
=> [internal] load build definition from Dockerfile 0.0s
=> => transferring dockerfile: 3.38kB 0.0s
=> [internal] load metadata for docker.io/library/python:3.12-slim-bullseye 0.2s
=> [internal] load .dockerignore 0.0s
=> => transferring context: 220B 0.0s
=> [build 1/5] FROM docker.io/library/python:3.12-slim-bullseye@sha256:6532d3187193a1ac4ee1 0.0s
=> [internal] load build context 0.1s
=> => transferring context: 1.73MB 0.0s
=> CACHED [main 2/12] RUN useradd -U -ms /bin/bash -u 1001 aries 0.0s
=> CACHED [main 3/12] RUN apt-get update -y && apt-get install -y --no-install-recomme 0.0s
=> CACHED [main 4/12] WORKDIR /home/aries 0.0s
=> CACHED [main 5/12] RUN usermod -a -G 0 aries 0.0s
=> CACHED [main 6/12] RUN mkdir -p /home/aries/.aries*cloudagent /home/aries/.cach 0.0s
=> CACHED [main 7/12] RUN chown -R aries:root /home/aries/.indy_client /home/aries/.aries* 0.0s
=> CACHED [main 8/12] RUN mkdir -p /home/indy 0.0s
=> CACHED [main 9/12] RUN ln -s /home/aries/.indy_client /home/indy/.indy_client 0.0s
=> CACHED [build 2/5] WORKDIR /src 0.0s
=> CACHED [build 3/5] ADD . . 0.0s
=> CACHED [build 4/5] RUN pip install --no-cache-dir poetry 0.0s
=> CACHED [build 5/5] RUN poetry build 0.0s
=> CACHED [main 10/12] COPY --from=build /src/dist/aries_cloudagent*.whl . 0.0s
=> CACHED [main 11/12] RUN aries_cloudagent_package=$(find ./ -name "aries_cloudagent*.whl" 0.0s
=> CACHED [main 12/12] RUN apt-get purge -y --auto-remove build-essential 0.0s
=> exporting to image 0.0s
=> => exporting layers 0.0s
=> => writing image sha256:9cf89a67fc62a5a093aaad352f3bc09d86ba406a8804d2030e77c356c74c3f24 0.0s
=> => naming to docker.io/library/acapy-base 0.0s

What's Next?
View a summary of image vulnerabilities and recommendations → docker scout quickview
[+] Building 0.1s (17/17) FINISHED docker:desktop-linux
=> [internal] load build definition from Dockerfile.demo 0.0s
=> => transferring dockerfile: 1.04kB 0.0s
=> [internal] load metadata for docker.io/library/acapy-base:latest 0.0s
=> [internal] load .dockerignore 0.0s
=> => transferring context: 220B 0.0s
=> [ 1/12] FROM docker.io/library/acapy-base:latest 0.0s
=> [internal] load build context 0.0s
=> => transferring context: 150.49kB 0.0s
=> CACHED [ 2/12] RUN mkdir -p bin && curl -L -o bin/jq https://github.com/stedolan/jq/rel 0.0s
=> CACHED [ 3/12] RUN pip install --no-cache-dir poetry 0.0s
=> CACHED [ 4/12] ADD README.md pyproject.toml poetry.lock ./ 0.0s
=> CACHED [ 5/12] RUN if ! [ -z 0 ]; then poetry install --no-root --no-directory --all-ext 0.0s
=> CACHED [ 6/12] ADD aries_cloudagent ./aries_cloudagent 0.0s
=> CACHED [ 7/12] ADD scripts ./scripts 0.0s
=> CACHED [ 8/12] RUN pip3 install --no-cache-dir -e . 0.0s
=> CACHED [ 9/12] RUN mkdir demo && chown -R aries:aries demo && chmod -R ug+rw demo 0.0s
=> CACHED [10/12] ADD demo/requirements.txt ./demo/requirements.txt 0.0s
=> CACHED [11/12] RUN pip3 install --no-cache-dir -r demo/requirements.txt 0.0s
=> CACHED [12/12] ADD demo ./demo 0.0s
=> exporting to image 0.0s
=> => exporting layers 0.0s
=> => writing image sha256:308caad3f815b0c3ab732ada3a1cc0f5d33931a4eb2f33ff355e60c975ef5df8 0.0s
=> => naming to docker.io/library/faber-alice-demo 0.0s

What's Next?
View a summary of image vulnerabilities and recommendations → docker scout quickview
You can utilize the 'build' option to build the agent or the 'run' option to run the agent.
Trying to detect ngrok service endpoint
ngrok not detected for agent endpoint
DOCKERHOST=host.docker.internal
DOCKER_ENV=-e LOG_LEVEL= -e RUNMODE=docker -e DOCKERHOST=host.docker.internal -e AGENT_PORT=8010 -e TRACE_TARGET=log -e TRACE_TAG=acapy.events -e TRACE_ENABLED=
Starting [faber] agent with args [--port 8010]
/home/aries/demo/runners/faber.py:1066: DeprecationWarning: There is no current event loop
asyncio.get_event_loop().run_until_complete(main(args))
Initializing demo agent faber with AIP 20 and credential type indy

#1 Provision an agent and wallet, get back configuration details
Started webhook listener on port: 8012
Faber | Registering faber.agent ...
using ledger: http://host.docker.internal:9000/register
Faber | nym_info: {'did': 'VX3a3ZJ5tqrp33QKRGv8N4', 'seed': '9bf125de139126ed130afeabd8ea53c4', 'verkey': 'GYWbseGp7EFBqVMoboB65U5g7AEsU9J7qSNLXaLJvdPY'}
Faber | Registered DID: VX3a3ZJ5tqrp33QKRGv8N4
Created public DID
Faber | ['/usr/local/bin/python', '-m', 'aries_cloudagent', 'start', '--endpoint', 'http://host.docker.internal:8010', '--label', 'faber.agent', '--auto-ping-connection', '--auto-respond-messages', '--inbound-transport', 'http', '0.0.0.0', '8010', '--outbound-transport', 'http', '--admin', '0.0.0.0', '8011', '--admin-insecure-mode', '--wallet-type', 'askar', '--wallet-name', 'faber.agent137e27ff', '--wallet-key', 'faber.agent137e27ff', '--preserve-exchange-records', '--auto-provision', '--public-invites', '--emit-new-didcomm-prefix', '--genesis-transactions', '{"reqSignature":{},"txn":{"data":{"data":{"alias":"Node1","blskey":"4N8aUNHSgjQVgkpm8nhNEfDf6txHznoYREg9kirmJrkivgL4oSEimFF6nsQ6M41QvhM2Z33nves5vfSn9n1UwNFJBYtWVnHYMATn76vLuL3zU88KyeAYcHfsih3He6UHcXDxcaecHVz6jhCYz1P2UZn2bDVruL5wXpehgBfBaLKm3Ba","blskey_pop":"RahHYiCvoNCtPTrVtP7nMC5eTYrsUA8WjXbdhNc8debh1agE9bGiJxWBXYNFbnJXoXhWFMvyqhqhRoq737YQemH5ik9oL7R4NTTCz2LEZhkgLJzB3QRQqJyBNyv7acbdHrAT8nQ9UkLbaVL9NBpnWXBTw4LEMePaSHEw66RzPNdAX1","client_ip":"host.docker.internal","client_port":9702,"node_ip":"host.docker.internal","node_port":9701,"services":["VALIDATOR"]},"dest":"Gw6pDLhcBcoQesN72qfotTgFa7cbuqZpkX3Xo6pLhPhv"},"metadata":{"from":"Th7MpTaRZVRYnPiabds81Y"},"type":"0"},"txnMetadata":{"seqNo":1,"txnId":"fea82e10e894419fe2bea7d96296a6d46f50f93f9eeda954ec461b2ed2950b62"},"ver":"1"}\n{"reqSignature":{},"txn":{"data":{"data":{"alias":"Node2","blskey":"37rAPpXVoxzKhz7d9gkUe52XuXryuLXoM6P6LbWDB7LSbG62Lsb33sfG7zqS8TK1MXwuCHj1FKNzVpsnafmqLG1vXN88rt38mNFs9TENzm4QHdBzsvCuoBnPH7rpYYDo9DZNJePaDvRvqJKByCabubJz3XXKbEeshzpz4Ma5QYpJqjk","blskey_pop":"Qr658mWZ2YC8JXGXwMDQTzuZCWF7NK9EwxphGmcBvCh6ybUuLxbG65nsX4JvD4SPNtkJ2w9ug1yLTj6fgmuDg41TgECXjLCij3RMsV8CwewBVgVN67wsA45DFWvqvLtu4rjNnE9JbdFTc1Z4WCPA3Xan44K1HoHAq9EVeaRYs8zoF5","client_ip":"host.docker.internal","client_port":9704,"node_ip":"host.docker.internal","node_port":9703,"services":["VALIDATOR"]},"dest":"8ECVSk179mjsjKRLWiQtssMLgp6EPhWXtaYyStWPSGAb"},"metadata":{"from":"EbP4aYNeTHL6q385GuVpRV"},"type":"0"},"txnMetadata":{"seqNo":2,"txnId":"1ac8aece2a18ced660fef8694b61aac3af08ba875ce3026a160acbc3a3af35fc"},"ver":"1"}\n{"reqSignature":{},"txn":{"data":{"data":{"alias":"Node3","blskey":"3WFpdbg7C5cnLYZwFZevJqhubkFALBfCBBok15GdrKMUhUjGsk3jV6QKj6MZgEubF7oqCafxNdkm7eswgA4sdKTRc82tLGzZBd6vNqU8dupzup6uYUf32KTHTPQbuUM8Yk4QFXjEf2Usu2TJcNkdgpyeUSX42u5LqdDDpNSWUK5deC5","blskey_pop":"QwDeb2CkNSx6r8QC8vGQK3GRv7Yndn84TGNijX8YXHPiagXajyfTjoR87rXUu4G4QLk2cF8NNyqWiYMus1623dELWwx57rLCFqGh7N4ZRbGDRP4fnVcaKg1BcUxQ866Ven4gw8y4N56S5HzxXNBZtLYmhGHvDtk6PFkFwCvxYrNYjh","client_ip":"host.docker.internal","client_port":9706,"node_ip":"host.docker.internal","node_port":9705,"services":["VALIDATOR"]},"dest":"DKVxG2fXXTU8yT5N7hGEbXB3dfdAnYv1JczDUHpmDxya"},"metadata":{"from":"4cU41vWW82ArfxJxHkzXPG"},"type":"0"},"txnMetadata":{"seqNo":3,"txnId":"7e9f355dffa78ed24668f0e0e369fd8c224076571c51e2ea8be5f26479edebe4"},"ver":"1"}\n{"reqSignature":{},"txn":{"data":{"data":{"alias":"Node4","blskey":"2zN3bHM1m4rLz54MJHYSwvqzPchYp8jkHswveCLAEJVcX6Mm1wHQD1SkPYMzUDTZvWvhuE6VNAkK3KxVeEmsanSmvjVkReDeBEMxeDaayjcZjFGPydyey1qxBHmTvAnBKoPydvuTAqx5f7YNNRAdeLmUi99gERUU7TD8KfAa6MpQ9bw","blskey_pop":"RPLagxaR5xdimFzwmzYnz4ZhWtYQEj8iR5ZU53T2gitPCyCHQneUn2Huc4oeLd2B2HzkGnjAff4hWTJT6C7qHYB1Mv2wU5iHHGFWkhnTX9WsEAbunJCV2qcaXScKj4tTfvdDKfLiVuU2av6hbsMztirRze7LvYBkRHV3tGwyCptsrP","client_ip":"host.docker.internal","client_port":9708,"node_ip":"host.docker.internal","node_port":9707,"services":["VALIDATOR"]},"dest":"4PS3EDQ3dW1tci1Bp6543CfuuebjFrg36kLAUcskGfaA"},"metadata":{"from":"TWwCRQRZ2ZHMJFn9TzLp7W"},"type":"0"},"txnMetadata":{"seqNo":4,"txnId":"aa5e817d7cc626170eca175822029339a444eb0ee8f0bd20d3b0b76e566fb008"},"ver":"1"}', '--seed', '9bf125de139126ed130afeabd8ea53c4', '--webhook-url', 'http://host.docker.internal:8012/webhooks', '--monitor-revocation-notification', '--trace-target', 'log', '--trace-tag', 'acapy.events', '--trace-label', 'faber.agent.trace', '--auto-accept-invites', '--auto-accept-requests', '--auto-store-credential']
Faber | Created new profile
Faber | Profile backend: askar
Faber | Profile name: faber.agent137e27ff
Faber | Created new public DID: VX3a3ZJ5tqrp33QKRGv8N4
Faber | Verkey: GYWbseGp7EFBqVMoboB65U5g7AEsU9J7qSNLXaLJvdPY
Faber |
Faber | ::::::::::::::::::::::::::::::::::::::::::::::
Faber | :: faber.agent ::
Faber | :: ::
Faber |Faber | ::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
Faber | :: ⚠ DEPRECATION NOTICE: ⚠ ::
Faber | :: -------------------------------------------------------------------------------- ::
Faber | :: Receiving a core DIDComm protocol with the `did:sov:BzCbsNYhMrjHiqZDTUASHg;spec` ::
Faber | :: prefix is deprecated. All parties sending this prefix should be notified that ::
Faber | :: support for receiving such messages will be removed in a future release. Use ::
Faber | :: https://didcomm.org/ instead. ::
Faber | :: -------------------------------------------------------------------------------- ::
Faber | :: Aries RFC 0160: Connection Protocol is deprecated and support will be removed in ::
Faber | :: a future release; use RFC 0023: DID Exchange instead. ::
Faber | :: -------------------------------------------------------------------------------- ::
Faber | :: Aries RFC 0036: Issue Credential 1.0 is deprecated and support will be removed ::
Faber | :: in a future release; use RFC 0453: Issue Credential 2.0 instead. ::
Faber | :: -------------------------------------------------------------------------------- ::
Faber | :: Aries RFC 0037: Present Proof 1.0 is deprecated and support will be removed in a ::
:: ::
Faber | :: future release; use RFC 0454: Present Proof 2.0 instead. ::
Faber | ::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
Faber | :: Inbound Transports: ::
Faber | :: ::
Faber | :: - http://0.0.0.0:8010 ::
Faber | :: ::
Faber | :: Outbound Transports: ::
Faber | :: ::
Faber | :: - http ::
Faber | :: - https ::
Faber | :: ::
Faber | :: Public DID Information: ::
Faber | :: ::
Faber | :: - DID: VX3a3ZJ5tqrp33QKRGv8N4 ::
Faber | :: ::
Faber | :: Administration API: ::
Faber | :: ::
Faber | :: - http://0.0.0.0:8011 ::
Faber | :: ::
Faber | :: ver: 1.0.0 ::
Faber | ::::::::::::::::::::::::::::::::::::::::::::::
Faber |
Faber | Listening...
Faber |
Faber |
Startup duration: 3.55s
Admin URL is at: http://host.docker.internal:8011
Endpoint URL is at: http://host.docker.internal:8010

#3/4 Create a new schema/cred def on the ledger
Schema:
{
"sent": {
"schema_id": "VX3a3ZJ5tqrp33QKRGv8N4:2:degree schema:41.56.92",
"schema": {
"ver": "1.0",
"id": "VX3a3ZJ5tqrp33QKRGv8N4:2:degree schema:41.56.92",
"name": "degree schema",
"version": "41.56.92",
"attrNames": [
"degree",
"birthdate_dateint",
"name",
"date",
"timestamp"
],
"seqNo": 8
}
},
"schema_id": "VX3a3ZJ5tqrp33QKRGv8N4:2:degree schema:41.56.92",
"schema": {
"ver": "1.0",
"id": "VX3a3ZJ5tqrp33QKRGv8N4:2:degree schema:41.56.92",
"name": "degree schema",
"version": "41.56.92",
"attrNames": [
"degree",
"birthdate_dateint",
"name",
"date",
"timestamp"
],
"seqNo": 8
}
}

Schema ID: VX3a3ZJ5tqrp33QKRGv8N4:2:degree schema:41.56.92
Cred def ID: VX3a3ZJ5tqrp33QKRGv8N4:3:CL:8:faber.agent.degree_schema
Publish schema/cred def duration: 9.96s

#7 Create a connection to alice and print out the invite details
Generate invitation duration: 0.03s
Use the following JSON to accept the invite from another demo agent. Or use the QR code to connect from a mobile agent.
Invitation Data:
{"@type": "https://didcomm.org/out-of-band/1.1/invitation", "@id": "9be04831-aac4-4739-a85e-0d5ee109f407", "label": "faber.agent", "handshake*protocols": ["https://didcomm.org/didexchange/1.1"], "services": [{"id": "#inline", "type": "did-communication", "recipientKeys": ["did:key:z6Mkf3YkNHBYb8UgeWxuqGAPkdgjsu3YGkFDhdLbmpm3BW1p#z6Mkf3YkNHBYb8UgeWxuqGAPkdgjsu3YGkFDhdLbmpm3BW1p"], "serviceEndpoint": "http://host.docker.internal:8010"}]}
█▀▀▀▀▀▀▀█▀█▀▀▀█▀▀▀▀▀█▀█▀▀█▀███████▀▀███▀▀██▀▀▀▀▀█▀▀▀███▀█▀█▀▀█▀██▀▀▀██▀█▀▀▀▀▀█▀▀▀█▀█▀▀▀█▀▀█▀▀▀▀▀▀▀█
█ █▀▀▀█ █ █ ▀▀ ▄█▀▀▄▄▀███ █▄ ▀▄ ▀ ██▀▄▀▄ ▀██    ██▀█ ▀▄█▄▄▀▄▀█  ▄  ▀ ▀   ▀▄█▄▄▄▀   █ ▄██▀ █ █▀▀▀█ █
█ █   █ █▀▄██▀██ ▄▄█▀▀▄▀▀▄▀██  ▀   ▀▀▀ ▀ ▄█ ▄▄█▄▄ ▀ ▄▄▄   ▄▄▄ ▀  ▀▀ █▀ ▀█▀▄▀█▀▀█▀█▀ ▀▀▀██ █ █   █ █
█ ▀▀▀▀▀ █▀█ █ ▄▀▄▀█▀█ ▄▀█▀█▀█ █ █ █▀█ ▄ ▄▀▄▀█▀▄▀▄ ▄▀█▀▄▀█▀█ █ █▀█ █ ▄▀▄▀▄▀▄ █ ▄▀█▀█▀█▀█▀▄▀█ ▀▀▀▀▀ █
█▀██▀▀▀▀▀▀█▀ ▀█ █▀▄▄ █▄▀▄   ▀▄▄▄▄ ▀▀▀ ▀██ ▀ █▄█▀    █▀▄▄▄█▀ █ ▀▀▀ ▄▀▀█▀▄██▄▄▀ ▀█▀▀ ▀██▄ ▀█▀██▀█▀▀▀█
█▄▄▄  ▄▀█ ██▀▀▄ █▀███▄▄  █ ▄▄ ▀█ ▄ ██▀ ▄▄▄  ▀█   ▄  ▄█▄ █▀▄▄█▀▄▀█████▄▀ █▀▀ ▄▄▀██▀█▀█▄█▄█▀▀▀█▄▀ █▀█
█▄▀▀█▄▄▀▄▀██ █ ▄▀▀  ▀█▄▄▄▄█▄▄█ ██▀████▄ ▄▀█▄▄ ▀▀▀▀▀██▀█▀  ▄▄▀█ ▀██▀▀ ▄█ ▀█▄ ▀▀▀█▀▄  ▀▄█▀▀▄██ ██▄ ▀█
██▄▄█▄▄▀██▀▀▄ ▄▀▄▄ ▀▄▄▄█ ▄█▀ ▀█▀  ▄ █▀▄  █▄ ▄█ ▀▄▄█▄  ▀▄▀ ▄█  ▄▀█▀▀███▀█▄▀▄ ▀ ▀▄▀ █▄▀ ▄▀█ ▀█▄▀  ▀▀█
██▄▀█▀█▀ ▀█▄▀  ▀█▀ ▀▄▀▄█ ▄▄▀██ ▄ ▀▀▀██▄██▄▀█  █ ▄  ▄█▄▀▀▀▀▄  ▀▄ ███ ▄▀█▀ █▄▀ █  ▄█▄▄ █▀▀█ █ █▄  █▀█
█ ▀▄█▀▀▀█▀▄█▄▀▀█▀██▀▄██▄▄ ▀ ▄▀▄███ ▄ █  ▀▀█ ▄▀   █ ▀▄▄▀▄ ▀▄ ▄  ▄█ ▄▄▄▄▀██ █▄▀█ ▄ ▀█ ██▀▄█ ▄  ▀ ▀▄ █
█▄▀▀▀ █▀███▄▄██  ▄█▀▀▄█▀ ▀ ▀▀▄█▄▀  ▄ ▀▀▀▄ █▀▀█▀ ▄▀█ ▄▀▀▀██▄█▄▄ ▄█ ██  ▀█▀▀▄ ▀█▀▄▄█  █▄█  ▄▄█▀ ▄████
█▀▄▀█  ▀ ▄▀▄█▄▀  ▀ ▀ ██▄ ▀▀▄  ▄▀ ▄█▄▀█ ▄▀   ▄▀█ ▄▀▄ █▄ ▄ ▄█ ▄ █▀█▀▀██▄█▀▄█▀▄▀▄██ ███▀▄█▄█▀█ ▀████▀█
██▄▄▀▄ ▀███ ▀█▀ █▄▄ █ ▄▄▄▀▄█   ▄█ ▀ ▄█ ██ ▀ █ █▀█▀ ▀▄▀███ ▀▀▄  ▄ ▄▄█▀ ██▀█   ▀ ▄ █▀█ █▄▀█▀ ▀█▀ ▄▀ █
█▀▄▄▄▀▄▀▀█ █▄█▄▀ ██▀█▄▀▀████▀▄▀█▄▄ ▄▀ ▄  ▀▄▄▀  █▄▄▀▄ █▀▄ ▄ █▀ █▀▀▄█▄█▀▀███▄▀█ ██▄ ▀█▀▀  ▀▀    ▀▄▀ █
█  █▀▄▀▀▄▀▀█ █▄▄▄█ █▀▀▀▄▄██▀█▀▄█▀   ▄▀ ▀███ ▀  ▀ ▀▀  █ █ ▀█▄█ █▄█  ▀██▄█▀▀ ▄ ▀█▄▄▀ ▄ █▀█▀ ▄▀ ▄ ▄▀██
█▄▄██ █▀▀▄█▀▄ █▀ ██▄ ▄██▀█▀▀▄█▄▀█  ▄▀▄  █ ▄ █▄ ▀ ▀█▀▄▀▀▀█▄█ █ ▄ ▀█▄▀▀ ▀▄█▄▀███▄█  ██▄ ▀▄▄▄▄▀▄▀█ █▀█
███ █  ▀▀▀▀▀▄ ▀▄▄ ▀██ ▄██▀▄ █▄▀█▀  ▀▀▀ ▄█▀ ▀▀█▄▄▀▀▄▄  ██▀█ ▄█    ▀ █ █▄▀▄▀█▄▀▄▀▄ ▀▀█▄█ █▄ ▀ ▀ ███▀█
█▄▀   █▀█ ▄▀ █▀▀█▀ ▀▀█▀ ▄▄█ ▄█▀█▄ █▀█ ▀▀▀▀ ▄█▀  ▄█▀▄▀▄█▄▀▄  ▀ █▀█ ▀▄█▀█ ▀▄▀ ▄▄████▀ ▀█▀█▀ █▀█  ▄▀ █
███ █ ▀▀▀ ▀▄  █ ▀ ▄██▀█ ██▀ ▄█▀▄▄ ▀▀▀ █   ▀▀███▄▀ ▀▀█▄▀▄ ▀▀██ ▀▀▀ █▀▀▄▀▄▀▀ ▄▀▀▀▀ ▄█  ██▀█ ▀▀▀  ▄█▄█
█▄▄▄ ██▀█▀▀█▄ ▄   █▀▀▄▄▄█▀  ██▄ ▄██▀▀▀▀▀ ▀▀▄▄▀ ▀▄ █ █▄▄▄▀▄ ▀▀ ▄█▀ █▄▀▀▀▄▄█▄ ▀▄▀█ ▄█ ▀█ ▀  ▄  ▀██▄▀█
███▄█ ▀▀██▀█▀▀██▀ █▀▄██ ▀▄█▀▄▀███▀▄█▀▀▄  ███▀▀▄ █   █▄█ ▀▀▄ ▀▄▀█▄▄█ █▀▀█▀▀▀ ▀██ ████ ██  ▄  ▀▀ ▄ ▄█
█▄██▄▀▄▀███▄█▀▀ ▄▀ ██ ▀▀▀▄    ▄▀  ▀  ██   ▀  ▀ ▄█▀ ▀▄▄█ █▀  █▄▀▄ █▄▄ ▀█▄▄ █▄▄▄▄▄ ██▄▀█▀█▄█▄▀▄▀█▀▄▀█
█▄▄ ▄▀▄▀ ▄▀▄  ▄█▄▄  ██▄ ▄██▀  ▀███ ▄▀▄  █▀█ ▄▄█▀▀▀▄██ ██▄▄█▀ ▄▄█▄▄ ▄▀█▀▀█▀█ ▀▄█▀▀█▄▄█▀ ▄▀▀▄ ▄▄ ██▄█
█  ▀▀█▀▀█▀▀█▀▄▄  ▀▄█▀▀▀ ██▄▀████ ▄▄██ ▄▄██▄▄▀ ▄▄▄▄  ▄▀ ▄█ █ ▀█▀▀ █ ▄▀█▀█▀▀▄▄ █▀▀▀█  █▀█▀▀█▀▀▄▀ ▀█▀█
█▀█▀  ▀▀▀▀  ████▄██▄ ▀▀ █▄ █ ▀▄▀█▄▄▀▄██▀█▀▄▀▄ ▀▀▄▀ ██ ▄▀█ ▄█ █  ▄▄▀ ▀▄▀█▀█▄█▀▀ █▀▄   █▄ ▄ ▀ █  ▀█▀█
██ ▀█▄▀▀▄ ▀█ ▀ ▀▄█▄▀██▄▄▄ ▄ ▀▄▀ ▄ █▀▄▀▄▀██   ▄ ▀▀ ▀ █▀  ██ ██▀ ▀  ▀█▄██▄ █▄▀█▄▀  ███▄ ▄▄██▀▀▀▄█▀▀▀█
█▀  ▄██▀▀▀▀██▀▀▄▀▄▄▀█  █▀▄▄█▄▀▀ ████ ▄▄▀▄▄█▄    █▀▀▄▄█▀▄▀ ▀ ▀▄▄   █▄█▀██ ▄▄ ▀█▄ ▄▀█ ▀█  ▄▄▄     ▀▄█
█ ▀█ ▀▀▀█▀▄█▄▄▄█▀▀▄▀ ▄▄▄██▄██▄▄▀  ▄█ ▄ ▄█ ▀▄▄   ▀█▄██▄▄▄▄█▄▄ ▄▀█▀▀ ▄▄███▄▄▀█▄▀▄▄▄▄▀▄▀█▀█▀█▄▄▀▄█ █ █
█ ▀█▄▀▄▀▄▄█ ▀ ▀█▀▀ ██▀ ▀ █ ██ ▀█▀  ▄██▀██ ██▀█▄█▀▀▀▀  ▄▀▄▄█▀██▄█▄█▀ ▀ █ ▄█ ▀     ▀ ▀▄▄▀█▄▀▄ ▀█ ████
██▀█ ▀▄▀▀█▄▀▄▄  █▀▀█▄▀▄█▀ ▄▄ █▀▄█▄▀▄█▀ █ ▄▄ ▀██ ██▄▄ ▄ ▄█ ▄▄▀▄█▄  █▄▀███▀▄▀█▄▄▀██▄▀▀█ ▀▀█▀▄▄▄▄ ▄█ █
█  ▀▄  ▀ ▀▀ ██▄▄▄▀  ▀█▄▀█▀ ▀█▀▀▄ ▀  ▀▀▄██▀▀▀▄▀█▀█▀▄▄▄▀█▄█▀█▄▄▀▀ ▀▀▄▄▀ ▀▀ █▄ ▀▀█▄   █▀█  ▄ ▀     █ █
█ ██▀ █▀█ █▄▀▄▀▀▄ █ ▀▄▀▀█▀▀▄▀█ ▀▀ █▀█ ▄▄█  ▄ ▀ ▀▀ ▀ ▀    █ █▄ █▀█ ██▄██▄▀   █▀█▄▀█▀▄▀▄▄█▀ █▀█ ██▀▀█
█▄▀ ▀ ▀▀▀ ▄▄███▀ █▀▀▄  ▀▄▄ █▀ ▀▀█ ▀▀▀ █▄ ██ ▄▀▀ ▄   ▄▄  ▄▀▀ █ ▀▀▀   ███▄ █▀ ▀▀█ ██▀█▀█ █▄ ▀▀▀  ▄▄▀█
█▄ ▄█▄▄▀  ▄▄   ▄▀█ ▀█▀ ▄▄▀▄▄█ █    █ ▀▄▄▄▀█ █     ▄██ ▀▄▀ █▄▀▄ ▀ █ █ ▄▀▄ ▄▀▄█ ▄██▄▀▄▀█▀▄▀▀  ██ ▀▄ █
█▀▄ ▀▄▀▀████ ▄▄ █ ▄  ▄▀▄▄██▄ ▀ ███▀ ▀▄▀ █ ▀█▀█▀█▀  ▀█  ▀▄█▀█ ▄▀▀██▀▀ █▀████     ▀▀████ ███▀▀ ▄▄▀█▄█
█▄▀ ▀ ▀▀▀██▀▄ ▄▀   ▀█▄█  █▀█ █  █▄▄▀█▀█▄▄▄█▄▄▄▄▄ ▄▄  ▄▄ ▄▄   █▄▀▄█▀█▀▄█ █▀██▀▀▀▄██▀▀▀▀▀█  ▄ ▄  ▀▄ █
█▀▄▀█▀▀▀ ▄ █▄▀ ▀▀█ ▄▄█ ▄█▄▄▄██▄ ██▀▄█  █ ▀█▀█  ██ ▀██ ▄ ▄▀▀▄█ ▄ ▀▄▀  ▄ ▄ ██  ▀▄  █▄ ▀█ ██▀█ ▄█▄  ▄█
█▄▀ ██ ▀▀ ▄█ ██  █ ▀ ▀███ ▄█  ██▀█▀▀▄█▀█  ▀▄█▄ ▀ █▀ ▄▀▄▄████▀▄ ▀▄▄██▄▄████▄▄█ ▀▄▀██▄█ ▄ ▀ █▀▀▄▀▀▀▀█
█▀  ▀██▀▀  ▄█ ██▀▄▄█▀▀█▀▀ █ ▄ █  ▀    █▄███▀▀ █ █ ▄ ▄██    ▄█▄▄▄█ ▄▀▄▀█  ▀█▀ ▀█ ██▄ ▀█▀██▀▄▀▀▀  █▄█
█▀▄▀▀▄▀▀▄▀█▄ █▀ ▀▄▄▀████ █▄▀▀█▄▄  ██▀ ▄▀ ▄▄▄ █▄ ▀▄ █ ▄▀▄█  ▄▀▄▀█ ▀▄▄▄▀█▄▀ ▀█▄▀▄███▀▄▀ █▄ █▄▀█▀▀██ █
██▄▀▀▄▀▀██▄██ █▀▄█▀▄█▀▀█▄  █  ▄█▀▀▄▀▄▄▀▀█ ▀ ██▄█   ▀█ ▀█▄▄▀█    ▀ █ ▀▄  ▄███  ▀ ▀▀▀▀▄▄▀▄▀ ▀    ▀▀ █
█▄   ▄ ▀█ ▄ ▀▄▀▄███▄▄ ▄▄█▄▀▄██▄▄ ▄▀▀ ▀▄ ▄█ ▄▄▄█  ▄ ▄▀▀▄ ▄▄ ▄█████ ▀▄▄ █▀ ▄▀▄▄██▄ ██ ▄▀██▀▀▀  ▄▄▄▄ █
█▀▀▀▀█▀▀▄▄▀▀ ██ ▀▀▀▀ ▀ █▀▄▀██▀▄  ██▀▀█▄ ▄ ▄ ▄▀▀ ▄▀█ ▄▀ ██▀▄  ▄ ▄▀▄▀▀█ ▀▄ ▄▀██▀  ▀██ ▄▀▄▀█▄█▀  ▄   █
█▄▄█▄▄█▀▀█▄█ █ ▀▄ ▄██ ▀█▄▄█ ▀▄ ▀ █ █▀█ ▀▄ ▀▄ ▀ █▀ ▀  ▄▄▄▀████▄▀▄ ██▄█████▄▄▀▄ ██  ██ ▀▄ ▀ █ █ █ ▄▀█
█ ▀ ▀▀▄▀█▀▀▄█▀█ █ █▀ ▀ ▀▄██▄▄█▀  ▀ ▀ ▀▀▀▄█ ▄▀  ▀█▀   █  ▄▀▀ ▄  ▀▀   ▄▀▄▄ ▄   █▄▀█▀▄  ▀▀▄ ▀  ▀ ▄  ▄█
█▀▀▀▀▀▀▀█ ▀▄▀▄██▀███ ▄▀▄ ▀█▄▀▀▀▄▄ █▀█  █▀▀█ ▄ █▄▀▄▄█▄▀▀ █   █ █▀█ ▄▄ ██ ▄▄██▀▀ ▄ ▄▀█▄▀▀▄▄ █▀█  █▄ █
█ █▀▀▀█ █ ▀▀ ▀▀▄█▄███▀▄ ▄ ▄▄▄▀ █▀ ▀▀▀ ▀█  ▄█▄██▀▀▀▀▀▄▀▀ ▄▄ ▄▀ ▀▀▀ ▀ ▀██▄█▀▄▄  ▀▀ █ ▄▄█▄█  ▀▀▀  █▄▄█
█ █   █ █▄▄▄ ▄ ▄▄▀▄█▀▀█  █ ▄█▄▄▀█▄ ▄█ ▀▄▀█ ▀███▄▄ ▄▀▀██  ▀ █▀▀█▀█ ██▄██ ▄▄██▀█▀▄▄▄██▀▄█▄█ █   ▀▄▀ █
█ ▀▀▀▀▀ █▀█▄█   █▀▄█ █▄▄ ▄▀▀ ▀ █ ▄█  ▀ ▀▄▀█ █ ▄█▀▀▀▀ ▀ ▀█ █ ▄▀██▀▀█ ▀ ▀█▀▀█  ▀ █▀ █▀ ██▀▄▀▀ ██▄ ▄ █
▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀
Waiting for connection...
Faber | Connected
Faber | Check for endorser role ...
(1) Issue Credential
(1a) Set Credential Type (indy)
(2) Send Proof Request
(2a) Send \_Connectionless* Proof Request (requires a Mobile client)
(3) Send Message
(4) Create New Invitation
(T) Toggle tracing on credential/proof exchange
(X) Exit?
[1/2/3/4/T/X] 3
Enter message: Hello
Faber | Received message: alice.agent received your message
(1) Issue Credential
(1a) Set Credential Type (indy)
(2) Send Proof Request
(2a) Send _Connectionless_ Proof Request (requires a Mobile client)
(3) Send Message
(4) Create New Invitation
(T) Toggle tracing on credential/proof exchange
(X) Exit?
[1/2/3/4/T/X] What's up
(1) Issue Credential
(1a) Set Credential Type (indy)
(2) Send Proof Request
(2a) Send _Connectionless_ Proof Request (requires a Mobile client)
(3) Send Message
(4) Create New Invitation
(T) Toggle tracing on credential/proof exchange
(X) Exit?
[1/2/3/4/T/X] 3
Enter message: What's up
Faber | Received message: alice.agent received your message
(1) Issue Credential
(1a) Set Credential Type (indy)
(2) Send Proof Request
(2a) Send _Connectionless_ Proof Request (requires a Mobile client)
(3) Send Message
(4) Create New Invitation
(T) Toggle tracing on credential/proof exchange
(X) Exit?
[1/2/3/4/T/X] T

> > > Credential/Proof Exchange Tracing is ON

    (1) Issue Credential
    (1a) Set Credential Type (indy)
    (2) Send Proof Request
    (2a) Send *Connectionless* Proof Request (requires a Mobile client)
    (3) Send Message
    (4) Create New Invitation
    (T) Toggle tracing on credential/proof exchange
    (X) Exit?

[1/2/3/4/T/X] 3
Enter message: Hello
Faber | Received message: alice.agent received your message
(1) Issue Credential
(1a) Set Credential Type (indy)
(2) Send Proof Request
(2a) Send _Connectionless_ Proof Request (requires a Mobile client)
(3) Send Message
(4) Create New Invitation
(T) Toggle tracing on credential/proof exchange
(X) Exit?
[1/2/3/4/T/X] 1

#13 Issue credential offer to X
Faber | 2024-09-11 17:24:04,498 aries_cloudagent.utils.tracing INFO acapy.events {"msg_id": "N/A", "thread_id": "ff0bbb34-5c17-4ac3-b830-b80fd21023e4", "traced_type": "dict:Exchange", "timestamp": 1726075444.4981415, "str_time": "2024-09-11 17:24:04.498142", "handler": "faber.agent.trace", "elapsed_milli": 0, "outcome": "OutboundTransportManager.DELIVER.START.http://host.docker.internal:8012/webhooks/topic/issue_credential_v2_0/"}
Faber | 2024-09-11 17:24:04,498 aries_cloudagent.utils.tracing INFO acapy.events {"msg_id": "N/A", "thread_id": "ff0bbb34-5c17-4ac3-b830-b80fd21023e4", "traced_type": "dict:Exchange", "timestamp": 1726075444.4985466, "str_time": "2024-09-11 17:24:04.498547", "handler": "faber.agent.trace", "elapsed_milli": 0, "outcome": "OutboundTransportManager.DELIVER.END.http://host.docker.internal:8012/webhooks/topic/issue_credential_v2_0/"}
Faber | 2024-09-11 17:24:04,501 aries_cloudagent.utils.tracing INFO acapy.events {"msg_id": "ff0bbb34-5c17-4ac3-b830-b80fd21023e4", "thread_id": "ff0bbb34-5c17-4ac3-b830-b80fd21023e4", "traced_type": "https://didcomm.org/issue-credential/2.0/offer-credential", "timestamp": 1726075444.5015025, "str_time": "2024-09-11 17:24:04.501503", "handler": "faber.agent.trace", "elapsed_milli": 58, "outcome": "credential_exchange_send_free_offer.END"}
Faber | 2024-09-11 17:24:04,501 aries_cloudagent.utils.tracing INFO acapy.events {"msg_id": "ff0bbb34-5c17-4ac3-b830-b80fd21023e4", "thread_id": "ff0bbb34-5c17-4ac3-b830-b80fd21023e4", "traced_type": "https://didcomm.org/issue-credential/2.0/offer-credential", "timestamp": 1726075444.501856, "str_time": "2024-09-11 17:24:04.501856", "handler": "faber.agent.trace", "elapsed_milli": 0, "outcome": "OutboundTransportManager.ENCODE.START"}
Faber | 2024-09-11 17:24:04,502 aries_cloudagent.utils.tracing INFO acapy.events {"msg_id": "ff0bbb34-5c17-4ac3-b830-b80fd21023e4", "thread_id": "ff0bbb34-5c17-4ac3-b830-b80fd21023e4", "traced_type": "https://didcomm.org/issue-credential/2.0/offer-credential", "timestamp": 1726075444.5019827, "str_time": "2024-09-11 17:24:04.501983", "handler": "faber.agent.trace", "elapsed_milli": 0, "outcome": "OutboundTransportManager.ENCODE.END"}
Faber | 2024-09-11 17:24:04,505 aries_cloudagent.utils.tracing INFO acapy.events {"msg_id": "ff0bbb34-5c17-4ac3-b830-b80fd21023e4", "thread_id": "ff0bbb34-5c17-4ac3-b830-b80fd21023e4", "traced_type": "https://didcomm.org/issue-credential/2.0/offer-credential", "timestamp": 1726075444.505106, "str_time": "2024-09-11 17:24:04.505106", "handler": "faber.agent.trace", "elapsed_milli": 0, "outcome": "OutboundTransportManager.DELIVER.START.http://host.docker.internal:8030"}
Faber | 2024-09-11 17:24:04,505 aries_cloudagent.utils.tracing INFO acapy.events {"msg_id": "ff0bbb34-5c17-4ac3-b830-b80fd21023e4", "thread_id": "ff0bbb34-5c17-4ac3-b830-b80fd21023e4", "traced_type": "https://didcomm.org/issue-credential/2.0/offer-credential", "timestamp": 1726075444.5052946, "str_time": "2024-09-11 17:24:04.505295", "handler": "faber.agent.trace", "elapsed_milli": 0, "outcome": "OutboundTransportManager.DELIVER.END.http://host.docker.internal:8030"}
Faber | Credential: state = offer-sent, cred_ex_id = cae2e77b-747b-4063-acdc-3b2687399bdf
Faber | 2024-09-11 17:24:04,893 aries_cloudagent.utils.tracing INFO acapy.events {"msg_id": "46b68771-aef7-4ccf-9e17-ecbaedf652d7", "thread_id": "ff0bbb34-5c17-4ac3-b830-b80fd21023e4", "traced_type": "https://didcomm.org/issue-credential/2.0/request-credential", "timestamp": 1726075444.8932433, "str_time": "2024-09-11 17:24:04.893243", "handler": "faber.agent.trace", "elapsed_milli": 0, "outcome": "Dispatcher.handle_message.START"}
Faber | Credential: state = request-received, cred_ex_id = cae2e77b-747b-4063-acdc-3b2687399bdf

#17 Issue credential to X
Faber | 2024-09-11 17:24:04,905 aries*cloudagent.utils.tracing INFO acapy.events {"msg_id": "N/A", "thread_id": "ff0bbb34-5c17-4ac3-b830-b80fd21023e4", "traced_type": "dict:Exchange", "timestamp": 1726075444.9051454, "str_time": "2024-09-11 17:24:04.905145", "handler": "faber.agent.trace", "elapsed_milli": 0, "outcome": "OutboundTransportManager.DELIVER.START.http://host.docker.internal:8012/webhooks/topic/issue_credential_v2_0/"}
Faber | Credential: state = credential-issued, cred_ex_id = cae2e77b-747b-4063-acdc-3b2687399bdf
Faber | 2024-09-11 17:24:04,905 aries_cloudagent.utils.tracing INFO acapy.events {"msg_id": "N/A", "thread_id": "ff0bbb34-5c17-4ac3-b830-b80fd21023e4", "traced_type": "dict:Exchange", "timestamp": 1726075444.9054132, "str_time": "2024-09-11 17:24:04.905413", "handler": "faber.agent.trace", "elapsed_milli": 0, "outcome": "OutboundTransportManager.DELIVER.END.http://host.docker.internal:8012/webhooks/topic/issue_credential_v2_0/"}
Faber | 2024-09-11 17:24:04,906 aries_cloudagent.utils.tracing INFO acapy.events {"msg_id": "46b68771-aef7-4ccf-9e17-ecbaedf652d7", "thread_id": "ff0bbb34-5c17-4ac3-b830-b80fd21023e4", "traced_type": "https://didcomm.org/issue-credential/2.0/request-credential", "timestamp": 1726075444.9062698, "str_time": "2024-09-11 17:24:04.906270", "handler": "faber.agent.trace", "elapsed_milli": 10, "outcome": "V20CredRequestHandler.handle.END"}
Faber | 2024-09-11 17:24:04,906 aries_cloudagent.utils.tracing INFO acapy.events {"msg_id": "46b68771-aef7-4ccf-9e17-ecbaedf652d7", "thread_id": "ff0bbb34-5c17-4ac3-b830-b80fd21023e4", "traced_type": "https://didcomm.org/issue-credential/2.0/request-credential", "timestamp": 1726075444.906415, "str_time": "2024-09-11 17:24:04.906415", "handler": "faber.agent.trace", "elapsed_milli": 14, "outcome": "Dispatcher.handle_message.END"}
Faber | Credential: state = done, cred_ex_id = cae2e77b-747b-4063-acdc-3b2687399bdf
Faber | 2024-09-11 17:24:04,977 aries_cloudagent.utils.tracing INFO acapy.events {"msg_id": "N/A", "thread_id": "ff0bbb34-5c17-4ac3-b830-b80fd21023e4", "traced_type": "dict:Exchange", "timestamp": 1726075444.977852, "str_time": "2024-09-11 17:24:04.977852", "handler": "faber.agent.trace", "elapsed_milli": 0, "outcome": "OutboundTransportManager.DELIVER.START.http://host.docker.internal:8012/webhooks/topic/issue_credential_v2_0/"}
Faber | 2024-09-11 17:24:04,978 aries_cloudagent.utils.tracing INFO acapy.events {"msg_id": "N/A", "thread_id": "ff0bbb34-5c17-4ac3-b830-b80fd21023e4", "traced_type": "dict:Exchange", "timestamp": 1726075444.97813, "str_time": "2024-09-11 17:24:04.978130", "handler": "faber.agent.trace", "elapsed_milli": 0, "outcome": "OutboundTransportManager.DELIVER.END.http://host.docker.internal:8012/webhooks/topic/issue_credential_v2_0/"}
Faber | 2024-09-11 17:24:04,994 aries_cloudagent.utils.tracing INFO acapy.events {"msg_id": "f06d25ec-e49b-429d-b3d8-628a4c4c52fe", "thread_id": "ff0bbb34-5c17-4ac3-b830-b80fd21023e4", "traced_type": "https://didcomm.org/issue-credential/2.0/issue-credential", "timestamp": 1726075444.9947536, "str_time": "2024-09-11 17:24:04.994754", "handler": "faber.agent.trace", "elapsed_milli": 85, "outcome": "credential_exchange_issue.END"}
Faber | 2024-09-11 17:24:04,995 aries_cloudagent.utils.tracing INFO acapy.events {"msg_id": "f06d25ec-e49b-429d-b3d8-628a4c4c52fe", "thread_id": "ff0bbb34-5c17-4ac3-b830-b80fd21023e4", "traced_type": "https://didcomm.org/issue-credential/2.0/issue-credential", "timestamp": 1726075444.995165, "str_time": "2024-09-11 17:24:04.995165", "handler": "faber.agent.trace", "elapsed_milli": 0, "outcome": "OutboundTransportManager.ENCODE.START"}
Faber | 2024-09-11 17:24:04,995 aries_cloudagent.utils.tracing INFO acapy.events {"msg_id": "f06d25ec-e49b-429d-b3d8-628a4c4c52fe", "thread_id": "ff0bbb34-5c17-4ac3-b830-b80fd21023e4", "traced_type": "https://didcomm.org/issue-credential/2.0/issue-credential", "timestamp": 1726075444.9952834, "str_time": "2024-09-11 17:24:04.995283", "handler": "faber.agent.trace", "elapsed_milli": 0, "outcome": "OutboundTransportManager.ENCODE.END"}
Faber | 2024-09-11 17:24:04,997 aries_cloudagent.utils.tracing INFO acapy.events {"msg_id": "f06d25ec-e49b-429d-b3d8-628a4c4c52fe", "thread_id": "ff0bbb34-5c17-4ac3-b830-b80fd21023e4", "traced_type": "https://didcomm.org/issue-credential/2.0/issue-credential", "timestamp": 1726075444.9972444, "str_time": "2024-09-11 17:24:04.997244", "handler": "faber.agent.trace", "elapsed_milli": 0, "outcome": "OutboundTransportManager.DELIVER.START.http://host.docker.internal:8030"}
Faber | 2024-09-11 17:24:04,997 aries_cloudagent.utils.tracing INFO acapy.events {"msg_id": "f06d25ec-e49b-429d-b3d8-628a4c4c52fe", "thread_id": "ff0bbb34-5c17-4ac3-b830-b80fd21023e4", "traced_type": "https://didcomm.org/issue-credential/2.0/issue-credential", "timestamp": 1726075444.9974601, "str_time": "2024-09-11 17:24:04.997460", "handler": "faber.agent.trace", "elapsed_milli": 0, "outcome": "OutboundTransportManager.DELIVER.END.http://host.docker.internal:8030"}
Faber | 2024-09-11 17:24:05,063 aries_cloudagent.utils.tracing INFO acapy.events {"msg_id": "40e7f196-c41c-4ac4-9736-2c234377f32f", "thread_id": "ff0bbb34-5c17-4ac3-b830-b80fd21023e4", "traced_type": "https://didcomm.org/issue-credential/2.0/ack", "timestamp": 1726075445.063404, "str_time": "2024-09-11 17:24:05.063404", "handler": "faber.agent.trace", "elapsed_milli": 0, "outcome": "Dispatcher.handle_message.START"}
Faber | 2024-09-11 17:24:05,075 aries_cloudagent.utils.tracing INFO acapy.events {"msg_id": "N/A", "thread_id": "ff0bbb34-5c17-4ac3-b830-b80fd21023e4", "traced_type": "dict:Exchange", "timestamp": 1726075445.0753343, "str_time": "2024-09-11 17:24:05.075334", "handler": "faber.agent.trace", "elapsed_milli": 0, "outcome": "OutboundTransportManager.DELIVER.START.http://host.docker.internal:8012/webhooks/topic/issue_credential_v2_0/"}
Faber | 2024-09-11 17:24:05,075 aries_cloudagent.utils.tracing INFO acapy.events {"msg_id": "N/A", "thread_id": "ff0bbb34-5c17-4ac3-b830-b80fd21023e4", "traced_type": "dict:Exchange", "timestamp": 1726075445.0756485, "str_time": "2024-09-11 17:24:05.075649", "handler": "faber.agent.trace", "elapsed_milli": 0, "outcome": "OutboundTransportManager.DELIVER.END.http://host.docker.internal:8012/webhooks/topic/issue_credential_v2_0/"}
Faber | 2024-09-11 17:24:05,076 aries_cloudagent.utils.tracing INFO acapy.events {"msg_id": "40e7f196-c41c-4ac4-9736-2c234377f32f", "thread_id": "ff0bbb34-5c17-4ac3-b830-b80fd21023e4", "traced_type": "https://didcomm.org/issue-credential/2.0/ack", "timestamp": 1726075445.0764956, "str_time": "2024-09-11 17:24:05.076496", "handler": "faber.agent.trace", "elapsed_milli": 11, "outcome": "V20CredAckHandler.handle.END"}
Faber | 2024-09-11 17:24:05,076 aries_cloudagent.utils.tracing INFO acapy.events {"msg_id": "40e7f196-c41c-4ac4-9736-2c234377f32f", "thread_id": "ff0bbb34-5c17-4ac3-b830-b80fd21023e4", "traced_type": "https://didcomm.org/issue-credential/2.0/ack", "timestamp": 1726075445.0766468, "str_time": "2024-09-11 17:24:05.076647", "handler": "faber.agent.trace", "elapsed_milli": 13, "outcome": "Dispatcher.handle_message.END"}
(1) Issue Credential
(1a) Set Credential Type (indy)
(2) Send Proof Request
(2a) Send \_Connectionless* Proof Request (requires a Mobile client)
(3) Send Message
(4) Create New Invitation
(T) Toggle tracing on credential/proof exchange
(X) Exit?
[1/2/3/4/T/X] 2

#20 Request proof of degree from alice
Faber | 2024-09-11 17:24:30,640 aries_cloudagent.utils.tracing INFO acapy.events {"msg_id": "N/A", "thread_id": "5e645af6-8b39-45a0-83cc-23dbcf334e1e", "traced_type": "dict:Exchange", "timestamp": 1726075470.640245, "str_time": "2024-09-11 17:24:30.640245", "handler": "faber.agent.trace", "elapsed_milli": 0, "outcome": "OutboundTransportManager.DELIVER.START.http://host.docker.internal:8012/webhooks/topic/present_proof_v2_0/"}
Faber | 2024-09-11 17:24:30,640 aries_cloudagent.utils.tracing INFO acapy.events {"msg_id": "N/A", "thread_id": "5e645af6-8b39-45a0-83cc-23dbcf334e1e", "traced_type": "dict:Exchange", "timestamp": 1726075470.6405625, "str_time": "2024-09-11 17:24:30.640563", "handler": "faber.agent.trace", "elapsed_milli": 0, "outcome": "OutboundTransportManager.DELIVER.END.http://host.docker.internal:8012/webhooks/topic/present_proof_v2_0/"}
Faber | 2024-09-11 17:24:30,643 aries_cloudagent.utils.tracing INFO acapy.events {"msg_id": "5e645af6-8b39-45a0-83cc-23dbcf334e1e", "thread_id": "5e645af6-8b39-45a0-83cc-23dbcf334e1e", "traced_type": "https://didcomm.org/present-proof/2.0/request-presentation", "timestamp": 1726075470.6431017, "str_time": "2024-09-11 17:24:30.643102", "handler": "faber.agent.trace", "elapsed_milli": 10, "outcome": "presentation_exchange_send_request.END"}
Faber | 2024-09-11 17:24:30,643 aries_cloudagent.utils.tracing INFO acapy.events {"msg_id": "5e645af6-8b39-45a0-83cc-23dbcf334e1e", "thread_id": "5e645af6-8b39-45a0-83cc-23dbcf334e1e", "traced_type": "https://didcomm.org/present-proof/2.0/request-presentation", "timestamp": 1726075470.6433656, "str_time": "2024-09-11 17:24:30.643366", "handler": "faber.agent.trace", "elapsed_milli": 0, "outcome": "OutboundTransportManager.ENCODE.START"}
Faber | 2024-09-11 17:24:30,643 aries_cloudagent.utils.tracing INFO acapy.events {"msg_id": "5e645af6-8b39-45a0-83cc-23dbcf334e1e", "thread_id": "5e645af6-8b39-45a0-83cc-23dbcf334e1e", "traced_type": "https://didcomm.org/present-proof/2.0/request-presentation", "timestamp": 1726075470.6435015, "str_time": "2024-09-11 17:24:30.643502", "handler": "faber.agent.trace", "elapsed_milli": 0, "outcome": "OutboundTransportManager.ENCODE.END"}
Faber | 2024-09-11 17:24:30,647 aries_cloudagent.utils.tracing INFO acapy.events {"msg_id": "5e645af6-8b39-45a0-83cc-23dbcf334e1e", "thread_id": "5e645af6-8b39-45a0-83cc-23dbcf334e1e", "traced_type": "https://didcomm.org/present-proof/2.0/request-presentation", "timestamp": 1726075470.6473835, "str_time": "2024-09-11 17:24:30.647383", "handler": "faber.agent.trace", "elapsed_milli": 0, "outcome": "OutboundTransportManager.DELIVER.START.http://host.docker.internal:8030"}
Faber | 2024-09-11 17:24:30,647 aries_cloudagent.utils.tracing INFO acapy.events {"msg_id": "5e645af6-8b39-45a0-83cc-23dbcf334e1e", "thread_id": "5e645af6-8b39-45a0-83cc-23dbcf334e1e", "traced_type": "https://didcomm.org/present-proof/2.0/request-presentation", "timestamp": 1726075470.6476445, "str_time": "2024-09-11 17:24:30.647645", "handler": "faber.agent.trace", "elapsed_milli": 0, "outcome": "OutboundTransportManager.DELIVER.END.http://host.docker.internal:8030"}
Faber | Presentation: state = request-sent, pres_ex_id = ee270c4c-58de-4c4f-83ab-a297694d47df
Presentation: state = request-sent, pres_ex_id = ee270c4c-58de-4c4f-83ab-a297694d47df
Faber | 2024-09-11 17:24:30,849 aries_cloudagent.utils.tracing INFO acapy.events {"msg_id": "0373e94e-6da3-44da-8c3b-591688213aa4", "thread_id": "5e645af6-8b39-45a0-83cc-23dbcf334e1e", "traced_type": "https://didcomm.org/present-proof/2.0/presentation", "timestamp": 1726075470.8490188, "str_time": "2024-09-11 17:24:30.849019", "handler": "faber.agent.trace", "elapsed_milli": 0, "outcome": "Dispatcher.handle_message.START"}
Faber | Presentation: state = presentation-received, pres_ex_id = ee270c4c-58de-4c4f-83ab-a297694d47df

#27 Process the proof provided by X

#28 Check if proof is valid
Presentation: state = presentation-received, pres*ex_id = ee270c4c-58de-4c4f-83ab-a297694d47df
Faber | 2024-09-11 17:24:30,860 aries_cloudagent.utils.tracing INFO acapy.events {"msg_id": "N/A", "thread_id": "5e645af6-8b39-45a0-83cc-23dbcf334e1e", "traced_type": "dict:Exchange", "timestamp": 1726075470.8600743, "str_time": "2024-09-11 17:24:30.860074", "handler": "faber.agent.trace", "elapsed_milli": 0, "outcome": "OutboundTransportManager.DELIVER.START.http://host.docker.internal:8012/webhooks/topic/present_proof_v2_0/"}
Faber | 2024-09-11 17:24:30,860 aries_cloudagent.utils.tracing INFO acapy.events {"msg_id": "N/A", "thread_id": "5e645af6-8b39-45a0-83cc-23dbcf334e1e", "traced_type": "dict:Exchange", "timestamp": 1726075470.860595, "str_time": "2024-09-11 17:24:30.860595", "handler": "faber.agent.trace", "elapsed_milli": 0, "outcome": "OutboundTransportManager.DELIVER.END.http://host.docker.internal:8012/webhooks/topic/present_proof_v2_0/"}
Faber | Presentation: state = done, pres_ex_id = ee270c4c-58de-4c4f-83ab-a297694d47df
Presentation: state = done, pres_ex_id = ee270c4c-58de-4c4f-83ab-a297694d47df
Faber | Proof = true
Faber | 2024-09-11 17:24:30,861 aries_cloudagent.utils.tracing INFO acapy.events {"msg_id": "0373e94e-6da3-44da-8c3b-591688213aa4", "thread_id": "5e645af6-8b39-45a0-83cc-23dbcf334e1e", "traced_type": "https://didcomm.org/present-proof/2.0/presentation", "timestamp": 1726075470.861221, "str_time": "2024-09-11 17:24:30.861221", "handler": "faber.agent.trace", "elapsed_milli": 9, "outcome": "V20PresHandler.handle.END"}
Faber | 2024-09-11 17:24:30,861 aries_cloudagent.utils.tracing INFO acapy.events {"msg_id": "0373e94e-6da3-44da-8c3b-591688213aa4", "thread_id": "5e645af6-8b39-45a0-83cc-23dbcf334e1e", "traced_type": "https://didcomm.org/present-proof/2.0/presentation", "timestamp": 1726075470.8613312, "str_time": "2024-09-11 17:24:30.861331", "handler": "faber.agent.trace", "elapsed_milli": 25, "outcome": "Dispatcher.handle_message.END"}
Faber | 2024-09-11 17:24:30,967 aries_cloudagent.utils.tracing INFO acapy.events {"msg_id": "N/A", "thread_id": "5e645af6-8b39-45a0-83cc-23dbcf334e1e", "traced_type": "dict:Exchange", "timestamp": 1726075470.9676383, "str_time": "2024-09-11 17:24:30.967638", "handler": "faber.agent.trace", "elapsed_milli": 0, "outcome": "OutboundTransportManager.DELIVER.START.http://host.docker.internal:8012/webhooks/topic/present_proof_v2_0/"}
Faber | 2024-09-11 17:24:30,968 aries_cloudagent.utils.tracing INFO acapy.events {"msg_id": "N/A", "thread_id": "5e645af6-8b39-45a0-83cc-23dbcf334e1e", "traced_type": "dict:Exchange", "timestamp": 1726075470.9682288, "str_time": "2024-09-11 17:24:30.968229", "handler": "faber.agent.trace", "elapsed_milli": 0, "outcome": "OutboundTransportManager.DELIVER.END.http://host.docker.internal:8012/webhooks/topic/present_proof_v2_0/"}
Faber | 2024-09-11 17:24:30,970 aries_cloudagent.utils.tracing INFO acapy.events {"msg_id": "N/A", "thread_id": "5e645af6-8b39-45a0-83cc-23dbcf334e1e", "traced_type": "V20PresExRecord", "timestamp": 1726075470.970916, "str_time": "2024-09-11 17:24:30.970916", "handler": "faber.agent.trace", "elapsed_milli": 106, "outcome": "presentation_exchange_verify.END"}
Faber | 2024-09-11 17:24:30,971 aries_cloudagent.utils.tracing INFO acapy.events {"msg_id": "4cef63c3-c3eb-4c4a-964b-843140a832ef", "thread_id": "5e645af6-8b39-45a0-83cc-23dbcf334e1e", "traced_type": "https://didcomm.org/present-proof/2.0/ack", "timestamp": 1726075470.9714046, "str_time": "2024-09-11 17:24:30.971405", "handler": "faber.agent.trace", "elapsed_milli": 0, "outcome": "OutboundTransportManager.ENCODE.START"}
Faber | 2024-09-11 17:24:30,971 aries_cloudagent.utils.tracing INFO acapy.events {"msg_id": "4cef63c3-c3eb-4c4a-964b-843140a832ef", "thread_id": "5e645af6-8b39-45a0-83cc-23dbcf334e1e", "traced_type": "https://didcomm.org/present-proof/2.0/ack", "timestamp": 1726075470.9715161, "str_time": "2024-09-11 17:24:30.971516", "handler": "faber.agent.trace", "elapsed_milli": 0, "outcome": "OutboundTransportManager.ENCODE.END"}
Faber | 2024-09-11 17:24:30,973 aries_cloudagent.utils.tracing INFO acapy.events {"msg_id": "4cef63c3-c3eb-4c4a-964b-843140a832ef", "thread_id": "5e645af6-8b39-45a0-83cc-23dbcf334e1e", "traced_type": "https://didcomm.org/present-proof/2.0/ack", "timestamp": 1726075470.973466, "str_time": "2024-09-11 17:24:30.973466", "handler": "faber.agent.trace", "elapsed_milli": 0, "outcome": "OutboundTransportManager.DELIVER.START.http://host.docker.internal:8030"}
Faber | 2024-09-11 17:24:30,973 aries_cloudagent.utils.tracing INFO acapy.events {"msg_id": "4cef63c3-c3eb-4c4a-964b-843140a832ef", "thread_id": "5e645af6-8b39-45a0-83cc-23dbcf334e1e", "traced_type": "https://didcomm.org/present-proof/2.0/ack", "timestamp": 1726075470.9736018, "str_time": "2024-09-11 17:24:30.973602", "handler": "faber.agent.trace", "elapsed_milli": 0, "outcome": "OutboundTransportManager.DELIVER.END.http://host.docker.internal:8030"}
(1) Issue Credential
(1a) Set Credential Type (indy)
(2) Send Proof Request
(2a) Send \_Connectionless* Proof Request (requires a Mobile client)
(3) Send Message
(4) Create New Invitation
(T) Toggle tracing on credential/proof exchange
(X) Exit?
[1/2/3/4/T/X] 3
Enter message: Message1
Faber | Received message: alice.agent received your message
(1) Issue Credential
(1a) Set Credential Type (indy)
(2) Send Proof Request
(2a) Send _Connectionless_ Proof Request (requires a Mobile client)
(3) Send Message
(4) Create New Invitation
(T) Toggle tracing on credential/proof exchange
(X) Exit?
[1/2/3/4/T/X] 3
Enter message: Message2
Faber | Received message: alice.agent received your message
Faber | Received message: Message3
Faber | Received message: Message4
(1) Issue Credential
(1a) Set Credential Type (indy)
(2) Send Proof Request
(2a) Send _Connectionless_ Proof Request (requires a Mobile client)
(3) Send Message
(4) Create New Invitation
(T) Toggle tracing on credential/proof exchange
(X) Exit?
[1/2/3/4/T/X]
```
