```bash
austinhunt@Austins-MBP-2 demo % ./run_demo alice
Resolution not specified or invalid.
You can utilize the 'build' option to build the agent or the 'run' option to run the agent.
Preparing agent image...
[+] Building 33.1s (15/21) docker:desktop-linux
=> [internal] load build definition from Dockerfile 0.0s
=> => transferring dockerfile: 3.38kB 0.0s
=> [internal] load metadata for docker.io/library/python:3.12- 0.1s
=> [internal] load .dockerignore 0.0s
=> => transferring context: 220B 0.0s
=> [build 1/5] FROM docker.io/library/python:3.12-slim-bullsey 2.0s
=> => resolve docker.io/library/python:3.12-slim-bullseye@sha2 0.0s
=> => sha256:6532d3187193a1ac4ee129abcd6f470c8 9.12kB / 9.12kB 0.0s
=> => sha256:734698b8a29b548b43706ea052617d9f8 1.94kB / 1.94kB 0.0s
=> => sha256:a9894256982c41094d48715ea2f39d6c9 6.73kB / 6.73kB 0.0s
=> => sha256:8e5b24c77263180693ae4f1be8e9b8851 1.08MB / 1.08MB 0.4s
=> => sha256:7de299b6ce136721cb376aa184ee07eb6f0f9 232B / 232B 0.5s
=> => sha256:e1224c12dc504b18be9958e30f0c2cb63 1.75MB / 1.75MB 0.9s
=> => sha256:6533c3eba3f3cd4c840877f9245b269 31.43MB / 31.43MB 0.9s
=> => sha256:ce577c75572d26b2b0a3bb01fd46cb3 10.95MB / 10.95MB 1.0s
=> => extracting sha256:6533c3eba3f3cd4c840877f9245b26929fc8c2 0.7s
=> => extracting sha256:8e5b24c77263180693ae4f1be8e9b88516f7ad 0.0s
=> => extracting sha256:ce577c75572d26b2b0a3bb01fd46cb35cf732e 0.2s
=> => extracting sha256:7de299b6ce136721cb376aa184ee07eb6f0f90 0.0s
=> => extracting sha256:e1224c12dc504b18be9958e30f0c2cb63855d3 0.1s
=> [main 2/12] RUN useradd -U -ms /bin/bash -u 1001 aries 0.2s
=> [build 2/5] WORKDIR /src 0.1s
=> [main 3/12] RUN apt-get update -y && apt-get install 17.3s
=> [internal] load build context 0.2s
=> => transferring context: 20.04MB 0.2s
=> [main 4/12] WORKDIR /home/aries 0.0s
=> [main 5/12] RUN usermod -a -G 0 aries 0.2s
=> [main 6/12] RUN mkdir -p /home/aries/.aries_cloudagent 0.2s
=> [main 7/12] RUN chown -R aries:root /home/aries/.indy_clie 0.3s
=> [main 8/12] RUN mkdir -p /home/indy 0.2s
=> [main 9/12] RUN ln -s /home/aries/.indy_client /home/indy/ 0.3s
=> exporting to image 0.5s
=> => exporting layers 0.5s
=> => writing image sha256:9cf89a67fc62a5a093aaad352f3bc09d86b 0.0s
=> => naming to docker.io/library/acapy-base 0.0s

What's Next?
View a summary of image vulnerabilities and recommendations → docker scout quickview
[+] Building 38.0s (8/17) docker:desktop-linux
=> [internal] load build definition from Dockerfile.demo 0.0s
=> => transferring dockerfile: 1.04kB 0.0s
=> [internal] load metadata for docker.io/library/acapy-base:l 0.0s
=> [internal] load .dockerignore 0.0s
=> => transferring context: 220B 0.0s
=> [ 1/12] FROM docker.io/library/acapy-base:latest 0.1s
=> [internal] load build context 0.0s
=> => transferring context: 150.49kB 0.0s
=> [ 2/12] RUN mkdir -p bin && curl -L -o bin/jq https://gith 0.8s
=> [ 3/12] RUN pip install --no-cache-dir poetry 9.1s
=> exporting to image 0.8s
=> => exporting layers 0.8s
=> => writing image sha256:308caad3f815b0c3ab732ada3a1cc0f5d33 0.0s
=> => naming to docker.io/library/faber-alice-demo 0.0s

What's Next?
View a summary of image vulnerabilities and recommendations → docker scout quickview
You can utilize the 'build' option to build the agent or the 'run' option to run the agent.
Trying to detect ngrok service endpoint
ngrok not detected for agent endpoint
DOCKERHOST=host.docker.internal
DOCKER_ENV=-e LOG_LEVEL= -e RUNMODE=docker -e DOCKERHOST=host.docker.internal -e AGENT_PORT=8030 -e TRACE_TARGET=log -e TRACE_TAG=acapy.events -e TRACE_ENABLED=
Starting [alice] agent with args [--port 8030]
/home/aries/demo/runners/alice.py:265: DeprecationWarning: There is no current event loop
asyncio.get_event_loop().run_until_complete(main(args))
Initializing demo agent alice with AIP 20 and credential type None

#7 Provision an agent and wallet, get back configuration details
Started webhook listener on port: 8032
Alice | ['/usr/local/bin/python', '-m', 'aries_cloudagent', 'start', '--endpoint', 'http://host.docker.internal:8030', '--label', 'alice.agent', '--auto-ping-connection', '--auto-respond-messages', '--inbound-transport', 'http', '0.0.0.0', '8030', '--outbound-transport', 'http', '--admin', '0.0.0.0', '8031', '--admin-insecure-mode', '--wallet-type', 'askar', '--wallet-name', 'alice.agent4acc86c0', '--wallet-key', 'alice.agent4acc86c0', '--preserve-exchange-records', '--auto-provision', '--public-invites', '--emit-new-didcomm-prefix', '--genesis-transactions', '{"reqSignature":{},"txn":{"data":{"data":{"alias":"Node1","blskey":"4N8aUNHSgjQVgkpm8nhNEfDf6txHznoYREg9kirmJrkivgL4oSEimFF6nsQ6M41QvhM2Z33nves5vfSn9n1UwNFJBYtWVnHYMATn76vLuL3zU88KyeAYcHfsih3He6UHcXDxcaecHVz6jhCYz1P2UZn2bDVruL5wXpehgBfBaLKm3Ba","blskey_pop":"RahHYiCvoNCtPTrVtP7nMC5eTYrsUA8WjXbdhNc8debh1agE9bGiJxWBXYNFbnJXoXhWFMvyqhqhRoq737YQemH5ik9oL7R4NTTCz2LEZhkgLJzB3QRQqJyBNyv7acbdHrAT8nQ9UkLbaVL9NBpnWXBTw4LEMePaSHEw66RzPNdAX1","client_ip":"host.docker.internal","client_port":9702,"node_ip":"host.docker.internal","node_port":9701,"services":["VALIDATOR"]},"dest":"Gw6pDLhcBcoQesN72qfotTgFa7cbuqZpkX3Xo6pLhPhv"},"metadata":{"from":"Th7MpTaRZVRYnPiabds81Y"},"type":"0"},"txnMetadata":{"seqNo":1,"txnId":"fea82e10e894419fe2bea7d96296a6d46f50f93f9eeda954ec461b2ed2950b62"},"ver":"1"}\n{"reqSignature":{},"txn":{"data":{"data":{"alias":"Node2","blskey":"37rAPpXVoxzKhz7d9gkUe52XuXryuLXoM6P6LbWDB7LSbG62Lsb33sfG7zqS8TK1MXwuCHj1FKNzVpsnafmqLG1vXN88rt38mNFs9TENzm4QHdBzsvCuoBnPH7rpYYDo9DZNJePaDvRvqJKByCabubJz3XXKbEeshzpz4Ma5QYpJqjk","blskey_pop":"Qr658mWZ2YC8JXGXwMDQTzuZCWF7NK9EwxphGmcBvCh6ybUuLxbG65nsX4JvD4SPNtkJ2w9ug1yLTj6fgmuDg41TgECXjLCij3RMsV8CwewBVgVN67wsA45DFWvqvLtu4rjNnE9JbdFTc1Z4WCPA3Xan44K1HoHAq9EVeaRYs8zoF5","client_ip":"host.docker.internal","client_port":9704,"node_ip":"host.docker.internal","node_port":9703,"services":["VALIDATOR"]},"dest":"8ECVSk179mjsjKRLWiQtssMLgp6EPhWXtaYyStWPSGAb"},"metadata":{"from":"EbP4aYNeTHL6q385GuVpRV"},"type":"0"},"txnMetadata":{"seqNo":2,"txnId":"1ac8aece2a18ced660fef8694b61aac3af08ba875ce3026a160acbc3a3af35fc"},"ver":"1"}\n{"reqSignature":{},"txn":{"data":{"data":{"alias":"Node3","blskey":"3WFpdbg7C5cnLYZwFZevJqhubkFALBfCBBok15GdrKMUhUjGsk3jV6QKj6MZgEubF7oqCafxNdkm7eswgA4sdKTRc82tLGzZBd6vNqU8dupzup6uYUf32KTHTPQbuUM8Yk4QFXjEf2Usu2TJcNkdgpyeUSX42u5LqdDDpNSWUK5deC5","blskey_pop":"QwDeb2CkNSx6r8QC8vGQK3GRv7Yndn84TGNijX8YXHPiagXajyfTjoR87rXUu4G4QLk2cF8NNyqWiYMus1623dELWwx57rLCFqGh7N4ZRbGDRP4fnVcaKg1BcUxQ866Ven4gw8y4N56S5HzxXNBZtLYmhGHvDtk6PFkFwCvxYrNYjh","client_ip":"host.docker.internal","client_port":9706,"node_ip":"host.docker.internal","node_port":9705,"services":["VALIDATOR"]},"dest":"DKVxG2fXXTU8yT5N7hGEbXB3dfdAnYv1JczDUHpmDxya"},"metadata":{"from":"4cU41vWW82ArfxJxHkzXPG"},"type":"0"},"txnMetadata":{"seqNo":3,"txnId":"7e9f355dffa78ed24668f0e0e369fd8c224076571c51e2ea8be5f26479edebe4"},"ver":"1"}\n{"reqSignature":{},"txn":{"data":{"data":{"alias":"Node4","blskey":"2zN3bHM1m4rLz54MJHYSwvqzPchYp8jkHswveCLAEJVcX6Mm1wHQD1SkPYMzUDTZvWvhuE6VNAkK3KxVeEmsanSmvjVkReDeBEMxeDaayjcZjFGPydyey1qxBHmTvAnBKoPydvuTAqx5f7YNNRAdeLmUi99gERUU7TD8KfAa6MpQ9bw","blskey_pop":"RPLagxaR5xdimFzwmzYnz4ZhWtYQEj8iR5ZU53T2gitPCyCHQneUn2Huc4oeLd2B2HzkGnjAff4hWTJT6C7qHYB1Mv2wU5iHHGFWkhnTX9WsEAbunJCV2qcaXScKj4tTfvdDKfLiVuU2av6hbsMztirRze7LvYBkRHV3tGwyCptsrP","client_ip":"host.docker.internal","client_port":9708,"node_ip":"host.docker.internal","node_port":9707,"services":["VALIDATOR"]},"dest":"4PS3EDQ3dW1tci1Bp6543CfuuebjFrg36kLAUcskGfaA"},"metadata":{"from":"TWwCRQRZ2ZHMJFn9TzLp7W"},"type":"0"},"txnMetadata":{"seqNo":4,"txnId":"aa5e817d7cc626170eca175822029339a444eb0ee8f0bd20d3b0b76e566fb008"},"ver":"1"}', '--webhook-url', 'http://host.docker.internal:8032/webhooks', '--monitor-revocation-notification', '--trace-target', 'log', '--trace-tag', 'acapy.events', '--trace-label', 'alice.agent.trace', '--auto-accept-invites', '--auto-accept-requests', '--auto-store-credential']
Alice | Created new profile
Alice | Profile backend: askar
Alice | Profile name: alice.agent4acc86c0
Alice | No public DID
Alice |
Alice | ::::::::::::::::::::::::::::::::::::::::::::::
Alice | :: alice.agent ::
Alice | :: ::
Alice | :: ::
Alice | :: Inbound Transports: ::
Alice | :: ::
Alice | :: - http://0.0.0.0:8030 ::
Alice | :: ::
Alice | :: Outbound Transports: ::
Alice | :: ::
Alice | :: - http ::
Alice | :: - https ::
Alice | :: ::
Alice | :: Administration API: ::
Alice | :: ::
Alice | :: - http://0.0.0.0:8031 ::
Alice | ::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
Alice | :: ⚠ DEPRECATION NOTICE: ⚠ ::
Alice | :: -------------------------------------------------------------------------------- ::
Alice | :: Receiving a core DIDComm protocol with the `did:sov:BzCbsNYhMrjHiqZDTUASHg;spec` ::
Alice | :: prefix is deprecated. All parties sending this prefix should be notified that ::
Alice | :: support for receiving such messages will be removed in a future release. Use ::
Alice |Alice | :: https://didcomm.org/ instead. ::
Alice | :: -------------------------------------------------------------------------------- ::
Alice | :: Aries RFC 0160: Connection Protocol is deprecated and support will be removed in ::
Alice | :: a future release; use RFC 0023: DID Exchange instead. ::
Alice | :: -------------------------------------------------------------------------------- ::
Alice | :: Aries RFC 0036: Issue Credential 1.0 is deprecated and support will be removed ::
Alice | :: in a future release; use RFC 0453: Issue Credential 2.0 instead. ::
Alice | :: -------------------------------------------------------------------------------- ::
:: ::
Alice | :: ver: 1.0.0 ::
Alice |Alice | :: Aries RFC 0037: Present Proof 1.0 is deprecated and support will be removed in a ::
Alice | :: future release; use RFC 0454: Present Proof 2.0 instead. ::
Alice | ::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
::::::::::::::::::::::::::::::::::::::::::::::
Alice |
Alice | Listening...
Alice |
Alice |
Startup duration: 4.07s
Admin URL is at: http://host.docker.internal:8031
Endpoint URL is at: http://host.docker.internal:8030

#9 Input faber.py invitation details
Invite details: %
austinhunt@Austins-MBP-2 demo %
austinhunt@Austins-MBP-2 demo % ./run_demo alice
Resolution not specified or invalid.
You can utilize the 'build' option to build the agent or the 'run' option to run the agent.
Preparing agent image...
[+] Building 0.4s (21/21) FINISHED docker:desktop-linux
=> [internal] load build definition from Dockerfile 0.0s
=> => transferring dockerfile: 3.38kB 0.0s
=> [internal] load metadata for docker.io/library/python:3.12- 0.3s
=> [internal] load .dockerignore 0.0s
=> => transferring context: 220B 0.0s
=> [internal] load build context 0.1s
=> => transferring context: 1.73MB 0.1s
=> [build 1/5] FROM docker.io/library/python:3.12-slim-bullsey 0.0s
=> CACHED [main 2/12] RUN useradd -U -ms /bin/bash -u 1001 ar 0.0s
=> CACHED [main 3/12] RUN apt-get update -y && apt-get in 0.0s
=> CACHED [main 4/12] WORKDIR /home/aries 0.0s
=> CACHED [main 5/12] RUN usermod -a -G 0 aries 0.0s
=> CACHED [main 6/12] RUN mkdir -p /home/aries/.aries_clo 0.0s
=> CACHED [main 7/12] RUN chown -R aries:root /home/aries/.in 0.0s
=> CACHED [main 8/12] RUN mkdir -p /home/indy 0.0s
=> CACHED [main 9/12] RUN ln -s /home/aries/.indy_client /hom 0.0s
=> CACHED [build 2/5] WORKDIR /src 0.0s
=> CACHED [build 3/5] ADD . . 0.0s
=> CACHED [build 4/5] RUN pip install --no-cache-dir poetry 0.0s
=> CACHED [build 5/5] RUN poetry build 0.0s
=> CACHED [main 10/12] COPY --from=build /src/dist/aries_cloud 0.0s
=> CACHED [main 11/12] RUN aries_cloudagent_package=$(find ./ 0.0s
=> CACHED [main 12/12] RUN apt-get purge -y --auto-remove buil 0.0s
=> exporting to image 0.0s
=> => exporting layers 0.0s
=> => writing image sha256:9cf89a67fc62a5a093aaad352f3bc09d86b 0.0s
=> => naming to docker.io/library/acapy-base 0.0s

What's Next?
View a summary of image vulnerabilities and recommendations → docker scout quickview
[+] Building 0.1s (17/17) FINISHED docker:desktop-linux
=> [internal] load build definition from Dockerfile.demo 0.0s
=> => transferring dockerfile: 1.04kB 0.0s
=> [internal] load metadata for docker.io/library/acapy-base:l 0.0s
=> [internal] load .dockerignore 0.0s
=> => transferring context: 220B 0.0s
=> [ 1/12] FROM docker.io/library/acapy-base:latest 0.0s
=> [internal] load build context 0.0s
=> => transferring context: 150.49kB 0.0s
=> CACHED [ 2/12] RUN mkdir -p bin && curl -L -o bin/jq https 0.0s
=> CACHED [ 3/12] RUN pip install --no-cache-dir poetry 0.0s
=> CACHED [ 4/12] ADD README.md pyproject.toml poetry.lock ./ 0.0s
=> CACHED [ 5/12] RUN if ! [ -z 0 ]; then poetry install --no- 0.0s
=> CACHED [ 6/12] ADD aries_cloudagent ./aries_cloudagent 0.0s
=> CACHED [ 7/12] ADD scripts ./scripts 0.0s
=> CACHED [ 8/12] RUN pip3 install --no-cache-dir -e . 0.0s
=> CACHED [ 9/12] RUN mkdir demo && chown -R aries:aries demo 0.0s
=> CACHED [10/12] ADD demo/requirements.txt ./demo/requirement 0.0s
=> CACHED [11/12] RUN pip3 install --no-cache-dir -r demo/requ 0.0s
=> CACHED [12/12] ADD demo ./demo 0.0s
=> exporting to image 0.0s
=> => exporting layers 0.0s
=> => writing image sha256:308caad3f815b0c3ab732ada3a1cc0f5d33 0.0s
=> => naming to docker.io/library/faber-alice-demo 0.0s

What's Next?
View a summary of image vulnerabilities and recommendations → docker scout quickview
You can utilize the 'build' option to build the agent or the 'run' option to run the agent.
Trying to detect ngrok service endpoint
ngrok not detected for agent endpoint
DOCKERHOST=host.docker.internal
DOCKER_ENV=-e LOG_LEVEL= -e RUNMODE=docker -e DOCKERHOST=host.docker.internal -e AGENT_PORT=8030 -e TRACE_TARGET=log -e TRACE_TAG=acapy.events -e TRACE_ENABLED=
Starting [alice] agent with args [--port 8030]
/home/aries/demo/runners/alice.py:265: DeprecationWarning: There is no current event loop
asyncio.get_event_loop().run_until_complete(main(args))
Initializing demo agent alice with AIP 20 and credential type None

#7 Provision an agent and wallet, get back configuration details
Started webhook listener on port: 8032
Alice | ['/usr/local/bin/python', '-m', 'aries_cloudagent', 'start', '--endpoint', 'http://host.docker.internal:8030', '--label', 'alice.agent', '--auto-ping-connection', '--auto-respond-messages', '--inbound-transport', 'http', '0.0.0.0', '8030', '--outbound-transport', 'http', '--admin', '0.0.0.0', '8031', '--admin-insecure-mode', '--wallet-type', 'askar', '--wallet-name', 'alice.agent8a1d5534', '--wallet-key', 'alice.agent8a1d5534', '--preserve-exchange-records', '--auto-provision', '--public-invites', '--emit-new-didcomm-prefix', '--genesis-transactions', '{"reqSignature":{},"txn":{"data":{"data":{"alias":"Node1","blskey":"4N8aUNHSgjQVgkpm8nhNEfDf6txHznoYREg9kirmJrkivgL4oSEimFF6nsQ6M41QvhM2Z33nves5vfSn9n1UwNFJBYtWVnHYMATn76vLuL3zU88KyeAYcHfsih3He6UHcXDxcaecHVz6jhCYz1P2UZn2bDVruL5wXpehgBfBaLKm3Ba","blskey_pop":"RahHYiCvoNCtPTrVtP7nMC5eTYrsUA8WjXbdhNc8debh1agE9bGiJxWBXYNFbnJXoXhWFMvyqhqhRoq737YQemH5ik9oL7R4NTTCz2LEZhkgLJzB3QRQqJyBNyv7acbdHrAT8nQ9UkLbaVL9NBpnWXBTw4LEMePaSHEw66RzPNdAX1","client_ip":"host.docker.internal","client_port":9702,"node_ip":"host.docker.internal","node_port":9701,"services":["VALIDATOR"]},"dest":"Gw6pDLhcBcoQesN72qfotTgFa7cbuqZpkX3Xo6pLhPhv"},"metadata":{"from":"Th7MpTaRZVRYnPiabds81Y"},"type":"0"},"txnMetadata":{"seqNo":1,"txnId":"fea82e10e894419fe2bea7d96296a6d46f50f93f9eeda954ec461b2ed2950b62"},"ver":"1"}\n{"reqSignature":{},"txn":{"data":{"data":{"alias":"Node2","blskey":"37rAPpXVoxzKhz7d9gkUe52XuXryuLXoM6P6LbWDB7LSbG62Lsb33sfG7zqS8TK1MXwuCHj1FKNzVpsnafmqLG1vXN88rt38mNFs9TENzm4QHdBzsvCuoBnPH7rpYYDo9DZNJePaDvRvqJKByCabubJz3XXKbEeshzpz4Ma5QYpJqjk","blskey_pop":"Qr658mWZ2YC8JXGXwMDQTzuZCWF7NK9EwxphGmcBvCh6ybUuLxbG65nsX4JvD4SPNtkJ2w9ug1yLTj6fgmuDg41TgECXjLCij3RMsV8CwewBVgVN67wsA45DFWvqvLtu4rjNnE9JbdFTc1Z4WCPA3Xan44K1HoHAq9EVeaRYs8zoF5","client_ip":"host.docker.internal","client_port":9704,"node_ip":"host.docker.internal","node_port":9703,"services":["VALIDATOR"]},"dest":"8ECVSk179mjsjKRLWiQtssMLgp6EPhWXtaYyStWPSGAb"},"metadata":{"from":"EbP4aYNeTHL6q385GuVpRV"},"type":"0"},"txnMetadata":{"seqNo":2,"txnId":"1ac8aece2a18ced660fef8694b61aac3af08ba875ce3026a160acbc3a3af35fc"},"ver":"1"}\n{"reqSignature":{},"txn":{"data":{"data":{"alias":"Node3","blskey":"3WFpdbg7C5cnLYZwFZevJqhubkFALBfCBBok15GdrKMUhUjGsk3jV6QKj6MZgEubF7oqCafxNdkm7eswgA4sdKTRc82tLGzZBd6vNqU8dupzup6uYUf32KTHTPQbuUM8Yk4QFXjEf2Usu2TJcNkdgpyeUSX42u5LqdDDpNSWUK5deC5","blskey_pop":"QwDeb2CkNSx6r8QC8vGQK3GRv7Yndn84TGNijX8YXHPiagXajyfTjoR87rXUu4G4QLk2cF8NNyqWiYMus1623dELWwx57rLCFqGh7N4ZRbGDRP4fnVcaKg1BcUxQ866Ven4gw8y4N56S5HzxXNBZtLYmhGHvDtk6PFkFwCvxYrNYjh","client_ip":"host.docker.internal","client_port":9706,"node_ip":"host.docker.internal","node_port":9705,"services":["VALIDATOR"]},"dest":"DKVxG2fXXTU8yT5N7hGEbXB3dfdAnYv1JczDUHpmDxya"},"metadata":{"from":"4cU41vWW82ArfxJxHkzXPG"},"type":"0"},"txnMetadata":{"seqNo":3,"txnId":"7e9f355dffa78ed24668f0e0e369fd8c224076571c51e2ea8be5f26479edebe4"},"ver":"1"}\n{"reqSignature":{},"txn":{"data":{"data":{"alias":"Node4","blskey":"2zN3bHM1m4rLz54MJHYSwvqzPchYp8jkHswveCLAEJVcX6Mm1wHQD1SkPYMzUDTZvWvhuE6VNAkK3KxVeEmsanSmvjVkReDeBEMxeDaayjcZjFGPydyey1qxBHmTvAnBKoPydvuTAqx5f7YNNRAdeLmUi99gERUU7TD8KfAa6MpQ9bw","blskey_pop":"RPLagxaR5xdimFzwmzYnz4ZhWtYQEj8iR5ZU53T2gitPCyCHQneUn2Huc4oeLd2B2HzkGnjAff4hWTJT6C7qHYB1Mv2wU5iHHGFWkhnTX9WsEAbunJCV2qcaXScKj4tTfvdDKfLiVuU2av6hbsMztirRze7LvYBkRHV3tGwyCptsrP","client_ip":"host.docker.internal","client_port":9708,"node_ip":"host.docker.internal","node_port":9707,"services":["VALIDATOR"]},"dest":"4PS3EDQ3dW1tci1Bp6543CfuuebjFrg36kLAUcskGfaA"},"metadata":{"from":"TWwCRQRZ2ZHMJFn9TzLp7W"},"type":"0"},"txnMetadata":{"seqNo":4,"txnId":"aa5e817d7cc626170eca175822029339a444eb0ee8f0bd20d3b0b76e566fb008"},"ver":"1"}', '--webhook-url', 'http://host.docker.internal:8032/webhooks', '--monitor-revocation-notification', '--trace-target', 'log', '--trace-tag', 'acapy.events', '--trace-label', 'alice.agent.trace', '--auto-accept-invites', '--auto-accept-requests', '--auto-store-credential']
Alice | Created new profile
Alice | Profile backend: askar
Alice | Profile name: alice.agent8a1d5534
Alice | No public DID
Alice |
Alice | ::::::::::::::::::::::::::::::::::::::::::::::
Alice | :: alice.agent ::
Alice | :: ::
Alice | :: ::
Alice | ::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
Alice | :: ⚠ DEPRECATION NOTICE: ⚠ ::
Alice | :: -------------------------------------------------------------------------------- ::
Alice | :: Receiving a core DIDComm protocol with the `did:sov:BzCbsNYhMrjHiqZDTUASHg;spec` ::
Alice | :: prefix is deprecated. All parties sending this prefix should be notified that ::
Alice | :: support for receiving such messages will be removed in a future release. Use ::
Alice | :: https://didcomm.org/ instead. ::
Alice | :: -------------------------------------------------------------------------------- ::
Alice | :: Aries RFC 0160: Connection Protocol is deprecated and support will be removed in ::
Alice | :: a future release; use RFC 0023: DID Exchange instead. ::
Alice | :: -------------------------------------------------------------------------------- ::
Alice | :: Aries RFC 0036: Issue Credential 1.0 is deprecated and support will be removed ::
Alice | :: in a future release; use RFC 0453: Issue Credential 2.0 instead. ::
Alice | :: -------------------------------------------------------------------------------- ::
Alice | :: Aries RFC 0037: Present Proof 1.0 is deprecated and support will be removed in a ::
Alice | :: future release; use RFC 0454: Present Proof 2.0 instead. ::
Alice | ::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
Alice | :: Inbound Transports: ::
Alice | :: ::
Alice | :: - http://0.0.0.0:8030 ::
Alice | :: ::
Alice | :: Outbound Transports: ::
Alice | :: ::
Alice | :: - http ::
Alice | :: - https ::
Alice | :: ::
Alice | :: Administration API: ::
Alice | :: ::
Alice | :: - http://0.0.0.0:8031 ::
Alice | :: ::
Alice | :: ver: 1.0.0 ::
Alice | ::::::::::::::::::::::::::::::::::::::::::::::
Alice |
Alice | Listening...
Alice |
Alice |
Startup duration: 2.53s
Admin URL is at: http://host.docker.internal:8031
Endpoint URL is at: http://host.docker.internal:8030

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
Alice | Connected
Alice | Check for endorser role ...
Connect duration: 0.23s
Alice | Received message: Hello
Alice | Received message: What's up
Alice | Received message: Hello
Alice | 2024-09-11 17:24:04,519 aries_cloudagent.utils.tracing INFO acapy.events {"msg_id": "ff0bbb34-5c17-4ac3-b830-b80fd21023e4", "thread_id": "ff0bbb34-5c17-4ac3-b830-b80fd21023e4", "traced_type": "https://didcomm.org/issue-credential/2.0/offer-credential", "timestamp": 1726075444.5191915, "str_time": "2024-09-11 17:24:04.519192", "handler": "alice.agent.trace", "elapsed_milli": 0, "outcome": "Dispatcher.handle_message.START"}
Alice | Credential: state = offer-received, cred_ex_id = bef3912b-e92f-4631-8779-df3d46f2bfb1

#15 After receiving credential offer, send credential request
Alice | 2024-09-11 17:24:04,528 aries_cloudagent.utils.tracing INFO acapy.events {"msg_id": "N/A", "thread_id": "ff0bbb34-5c17-4ac3-b830-b80fd21023e4", "traced_type": "dict:Exchange", "timestamp": 1726075444.5287354, "str_time": "2024-09-11 17:24:04.528735", "handler": "alice.agent.trace", "elapsed_milli": 0, "outcome": "OutboundTransportManager.DELIVER.START.http://host.docker.internal:8032/webhooks/topic/issue_credential_v2_0/"}
Alice | 2024-09-11 17:24:04,529 aries_cloudagent.utils.tracing INFO acapy.events {"msg_id": "N/A", "thread_id": "ff0bbb34-5c17-4ac3-b830-b80fd21023e4", "traced_type": "dict:Exchange", "timestamp": 1726075444.5290682, "str_time": "2024-09-11 17:24:04.529068", "handler": "alice.agent.trace", "elapsed_milli": 0, "outcome": "OutboundTransportManager.DELIVER.END.http://host.docker.internal:8032/webhooks/topic/issue_credential_v2_0/"}
Alice | 2024-09-11 17:24:04,529 aries_cloudagent.utils.tracing INFO acapy.events {"msg_id": "ff0bbb34-5c17-4ac3-b830-b80fd21023e4", "thread_id": "ff0bbb34-5c17-4ac3-b830-b80fd21023e4", "traced_type": "https://didcomm.org/issue-credential/2.0/offer-credential", "timestamp": 1726075444.5296054, "str_time": "2024-09-11 17:24:04.529605", "handler": "alice.agent.trace", "elapsed_milli": 7, "outcome": "V20CredOfferHandler.handle.END"}
Alice | 2024-09-11 17:24:04,529 aries_cloudagent.utils.tracing INFO acapy.events {"msg_id": "ff0bbb34-5c17-4ac3-b830-b80fd21023e4", "thread_id": "ff0bbb34-5c17-4ac3-b830-b80fd21023e4", "traced_type": "https://didcomm.org/issue-credential/2.0/offer-credential", "timestamp": 1726075444.529714, "str_time": "2024-09-11 17:24:04.529714", "handler": "alice.agent.trace", "elapsed_milli": 19, "outcome": "Dispatcher.handle_message.END"}
Alice | Credential: state = request-sent, cred_ex_id = bef3912b-e92f-4631-8779-df3d46f2bfb1
Alice | 2024-09-11 17:24:04,881 aries_cloudagent.utils.tracing INFO acapy.events {"msg_id": "N/A", "thread_id": "ff0bbb34-5c17-4ac3-b830-b80fd21023e4", "traced_type": "dict:Exchange", "timestamp": 1726075444.8815641, "str_time": "2024-09-11 17:24:04.881564", "handler": "alice.agent.trace", "elapsed_milli": 0, "outcome": "OutboundTransportManager.DELIVER.START.http://host.docker.internal:8032/webhooks/topic/issue_credential_v2_0/"}
Alice | 2024-09-11 17:24:04,881 aries_cloudagent.utils.tracing INFO acapy.events {"msg_id": "N/A", "thread_id": "ff0bbb34-5c17-4ac3-b830-b80fd21023e4", "traced_type": "dict:Exchange", "timestamp": 1726075444.8818536, "str_time": "2024-09-11 17:24:04.881854", "handler": "alice.agent.trace", "elapsed_milli": 0, "outcome": "OutboundTransportManager.DELIVER.END.http://host.docker.internal:8032/webhooks/topic/issue_credential_v2_0/"}
Alice | Credential: state = credential-received, cred_ex_id = bef3912b-e92f-4631-8779-df3d46f2bfb1
Alice | 2024-09-11 17:24:04,884 aries_cloudagent.utils.tracing INFO acapy.events {"msg_id": "46b68771-aef7-4ccf-9e17-ecbaedf652d7", "thread_id": "ff0bbb34-5c17-4ac3-b830-b80fd21023e4", "traced_type": "https://didcomm.org/issue-credential/2.0/request-credential", "timestamp": 1726075444.8846078, "str_time": "2024-09-11 17:24:04.884608", "handler": "alice.agent.trace", "elapsed_milli": 143, "outcome": "credential_exchange_send_bound_request.END"}

#18.1 Stored credential 2bac60aa-738c-4c51-824d-bb83bcad7c99 in wallet
Alice | Credential: state = done, cred_ex_id = bef3912b-e92f-4631-8779-df3d46f2bfb1
Credential details:
{
"referent": "2bac60aa-738c-4c51-824d-bb83bcad7c99",
"schema_id": "VX3a3ZJ5tqrp33QKRGv8N4:2:degree schema:41.56.92",
"cred_def_id": "VX3a3ZJ5tqrp33QKRGv8N4:3:CL:8:faber.agent.degree_schema",
"rev_reg_id": null,
"cred_rev_id": null,
"attrs": {
"name": "Alice Smith",
"timestamp": "1726075444",
"birthdate_dateint": "20000911",
"degree": "Maths",
"date": "2018-05-28"
}
}

Alice | credential_id 2bac60aa-738c-4c51-824d-bb83bcad7c99
Alice | cred_def_id VX3a3ZJ5tqrp33QKRGv8N4:3:CL:8:faber.agent.degree_schema
Alice | schema_id VX3a3ZJ5tqrp33QKRGv8N4:2:degree schema:41.56.92
Alice | 2024-09-11 17:24:04,885 aries_cloudagent.utils.tracing INFO acapy.events {"msg_id": "46b68771-aef7-4ccf-9e17-ecbaedf652d7", "thread_id": "ff0bbb34-5c17-4ac3-b830-b80fd21023e4", "traced_type": "https://didcomm.org/issue-credential/2.0/request-credential", "timestamp": 1726075444.8849795, "str_time": "2024-09-11 17:24:04.884979", "handler": "alice.agent.trace", "elapsed_milli": 0, "outcome": "OutboundTransportManager.ENCODE.START"}
Alice | 2024-09-11 17:24:04,885 aries_cloudagent.utils.tracing INFO acapy.events {"msg_id": "46b68771-aef7-4ccf-9e17-ecbaedf652d7", "thread_id": "ff0bbb34-5c17-4ac3-b830-b80fd21023e4", "traced_type": "https://didcomm.org/issue-credential/2.0/request-credential", "timestamp": 1726075444.8850904, "str_time": "2024-09-11 17:24:04.885090", "handler": "alice.agent.trace", "elapsed_milli": 0, "outcome": "OutboundTransportManager.ENCODE.END"}
Alice | 2024-09-11 17:24:04,887 aries_cloudagent.utils.tracing INFO acapy.events {"msg_id": "46b68771-aef7-4ccf-9e17-ecbaedf652d7", "thread_id": "ff0bbb34-5c17-4ac3-b830-b80fd21023e4", "traced_type": "https://didcomm.org/issue-credential/2.0/request-credential", "timestamp": 1726075444.8870697, "str_time": "2024-09-11 17:24:04.887070", "handler": "alice.agent.trace", "elapsed_milli": 0, "outcome": "OutboundTransportManager.DELIVER.START.http://host.docker.internal:8010"}
Alice | 2024-09-11 17:24:04,887 aries_cloudagent.utils.tracing INFO acapy.events {"msg_id": "46b68771-aef7-4ccf-9e17-ecbaedf652d7", "thread_id": "ff0bbb34-5c17-4ac3-b830-b80fd21023e4", "traced_type": "https://didcomm.org/issue-credential/2.0/request-credential", "timestamp": 1726075444.8872385, "str_time": "2024-09-11 17:24:04.887239", "handler": "alice.agent.trace", "elapsed_milli": 0, "outcome": "OutboundTransportManager.DELIVER.END.http://host.docker.internal:8010"}
Alice | 2024-09-11 17:24:05,002 aries_cloudagent.utils.tracing INFO acapy.events {"msg_id": "f06d25ec-e49b-429d-b3d8-628a4c4c52fe", "thread_id": "ff0bbb34-5c17-4ac3-b830-b80fd21023e4", "traced_type": "https://didcomm.org/issue-credential/2.0/issue-credential", "timestamp": 1726075445.002847, "str_time": "2024-09-11 17:24:05.002847", "handler": "alice.agent.trace", "elapsed_milli": 0, "outcome": "Dispatcher.handle_message.START"}
Alice | 2024-09-11 17:24:05,016 aries_cloudagent.utils.tracing INFO acapy.events {"msg_id": "N/A", "thread_id": "ff0bbb34-5c17-4ac3-b830-b80fd21023e4", "traced_type": "dict:Exchange", "timestamp": 1726075445.0165331, "str_time": "2024-09-11 17:24:05.016533", "handler": "alice.agent.trace", "elapsed_milli": 0, "outcome": "OutboundTransportManager.DELIVER.START.http://host.docker.internal:8032/webhooks/topic/issue_credential_v2_0/"}
Alice | 2024-09-11 17:24:05,016 aries_cloudagent.utils.tracing INFO acapy.events {"msg_id": "N/A", "thread_id": "ff0bbb34-5c17-4ac3-b830-b80fd21023e4", "traced_type": "dict:Exchange", "timestamp": 1726075445.0168433, "str_time": "2024-09-11 17:24:05.016843", "handler": "alice.agent.trace", "elapsed_milli": 0, "outcome": "OutboundTransportManager.DELIVER.END.http://host.docker.internal:8032/webhooks/topic/issue_credential_v2_0/"}
Alice | 2024-09-11 17:24:05,017 aries_cloudagent.utils.tracing INFO acapy.events {"msg_id": "f06d25ec-e49b-429d-b3d8-628a4c4c52fe", "thread_id": "ff0bbb34-5c17-4ac3-b830-b80fd21023e4", "traced_type": "https://didcomm.org/issue-credential/2.0/issue-credential", "timestamp": 1726075445.0175676, "str_time": "2024-09-11 17:24:05.017568", "handler": "alice.agent.trace", "elapsed_milli": 12, "outcome": "V20CredIssueHandler.handle.END"}
Alice | 2024-09-11 17:24:05,055 aries_cloudagent.utils.tracing INFO acapy.events {"msg_id": "N/A", "thread_id": "ff0bbb34-5c17-4ac3-b830-b80fd21023e4", "traced_type": "dict:Exchange", "timestamp": 1726075445.0549266, "str_time": "2024-09-11 17:24:05.054927", "handler": "alice.agent.trace", "elapsed_milli": 0, "outcome": "OutboundTransportManager.DELIVER.START.http://host.docker.internal:8032/webhooks/topic/issue_credential_v2_0/"}
Alice | 2024-09-11 17:24:05,055 aries_cloudagent.utils.tracing INFO acapy.events {"msg_id": "N/A", "thread_id": "ff0bbb34-5c17-4ac3-b830-b80fd21023e4", "traced_type": "dict:Exchange", "timestamp": 1726075445.055246, "str_time": "2024-09-11 17:24:05.055246", "handler": "alice.agent.trace", "elapsed_milli": 0, "outcome": "OutboundTransportManager.DELIVER.END.http://host.docker.internal:8032/webhooks/topic/issue_credential_v2_0/"}
Alice | 2024-09-11 17:24:05,056 aries_cloudagent.utils.tracing INFO acapy.events {"msg_id": "f06d25ec-e49b-429d-b3d8-628a4c4c52fe", "thread_id": "ff0bbb34-5c17-4ac3-b830-b80fd21023e4", "traced_type": "https://didcomm.org/issue-credential/2.0/issue-credential", "timestamp": 1726075445.0566223, "str_time": "2024-09-11 17:24:05.056622", "handler": "alice.agent.trace", "elapsed_milli": 55, "outcome": "Dispatcher.handle_message.END"}
Alice | 2024-09-11 17:24:05,056 aries_cloudagent.utils.tracing INFO acapy.events {"msg_id": "40e7f196-c41c-4ac4-9736-2c234377f32f", "thread_id": "ff0bbb34-5c17-4ac3-b830-b80fd21023e4", "traced_type": "https://didcomm.org/issue-credential/2.0/ack", "timestamp": 1726075445.0567682, "str_time": "2024-09-11 17:24:05.056768", "handler": "alice.agent.trace", "elapsed_milli": 0, "outcome": "OutboundTransportManager.ENCODE.START"}
Alice | 2024-09-11 17:24:05,056 aries_cloudagent.utils.tracing INFO acapy.events {"msg_id": "40e7f196-c41c-4ac4-9736-2c234377f32f", "thread_id": "ff0bbb34-5c17-4ac3-b830-b80fd21023e4", "traced_type": "https://didcomm.org/issue-credential/2.0/ack", "timestamp": 1726075445.0568643, "str_time": "2024-09-11 17:24:05.056864", "handler": "alice.agent.trace", "elapsed_milli": 0, "outcome": "OutboundTransportManager.ENCODE.END"}
Alice | 2024-09-11 17:24:05,059 aries_cloudagent.utils.tracing INFO acapy.events {"msg_id": "40e7f196-c41c-4ac4-9736-2c234377f32f", "thread_id": "ff0bbb34-5c17-4ac3-b830-b80fd21023e4", "traced_type": "https://didcomm.org/issue-credential/2.0/ack", "timestamp": 1726075445.059695, "str_time": "2024-09-11 17:24:05.059695", "handler": "alice.agent.trace", "elapsed_milli": 0, "outcome": "OutboundTransportManager.DELIVER.START.http://host.docker.internal:8010"}
Alice | 2024-09-11 17:24:05,060 aries_cloudagent.utils.tracing INFO acapy.events {"msg_id": "40e7f196-c41c-4ac4-9736-2c234377f32f", "thread_id": "ff0bbb34-5c17-4ac3-b830-b80fd21023e4", "traced_type": "https://didcomm.org/issue-credential/2.0/ack", "timestamp": 1726075445.0600958, "str_time": "2024-09-11 17:24:05.060096", "handler": "alice.agent.trace", "elapsed_milli": 0, "outcome": "OutboundTransportManager.DELIVER.END.http://host.docker.internal:8010"}
Alice | 2024-09-11 17:24:30,665 aries_cloudagent.utils.tracing INFO acapy.events {"msg_id": "5e645af6-8b39-45a0-83cc-23dbcf334e1e", "thread_id": "5e645af6-8b39-45a0-83cc-23dbcf334e1e", "traced_type": "https://didcomm.org/present-proof/2.0/request-presentation", "timestamp": 1726075470.6652958, "str_time": "2024-09-11 17:24:30.665296", "handler": "alice.agent.trace", "elapsed_milli": 0, "outcome": "Dispatcher.handle_message.START"}
Alice | Presentation: state = request-received, pres_ex_id = 10f1f817-1904-4f8d-9f26-b6354c610cd0

#24 Query for credentials in the wallet that satisfy the proof request
Presentation: state = request-received, pres_ex_id = 10f1f817-1904-4f8d-9f26-b6354c610cd0

#25 Generate the indy proof

#26 Send the proof to X: {"indy": {"requested_predicates": {"0_birthdate_dateint_GE_uuid": {"cred_id": "2bac60aa-738c-4c51-824d-bb83bcad7c99"}}, "requested_attributes": {"0_name_uuid": {"cred_id": "2bac60aa-738c-4c51-824d-bb83bcad7c99", "revealed": false}, "0_date_uuid": {"cred_id": "2bac60aa-738c-4c51-824d-bb83bcad7c99", "revealed": true}, "0_degree_uuid": {"cred_id": "2bac60aa-738c-4c51-824d-bb83bcad7c99", "revealed": true}}, "self_attested_attributes": {}}}
Alice | 2024-09-11 17:24:30,675 aries_cloudagent.utils.tracing INFO acapy.events {"msg_id": "N/A", "thread_id": "5e645af6-8b39-45a0-83cc-23dbcf334e1e", "traced_type": "dict:Exchange", "timestamp": 1726075470.6750815, "str_time": "2024-09-11 17:24:30.675081", "handler": "alice.agent.trace", "elapsed_milli": 0, "outcome": "OutboundTransportManager.DELIVER.START.http://host.docker.internal:8032/webhooks/topic/present_proof_v2_0/"}
Alice | 2024-09-11 17:24:30,675 aries_cloudagent.utils.tracing INFO acapy.events {"msg_id": "N/A", "thread_id": "5e645af6-8b39-45a0-83cc-23dbcf334e1e", "traced_type": "dict:Exchange", "timestamp": 1726075470.6753557, "str_time": "2024-09-11 17:24:30.675356", "handler": "alice.agent.trace", "elapsed_milli": 0, "outcome": "OutboundTransportManager.DELIVER.END.http://host.docker.internal:8032/webhooks/topic/present_proof_v2_0/"}
Alice | 2024-09-11 17:24:30,675 aries_cloudagent.utils.tracing INFO acapy.events {"msg_id": "5e645af6-8b39-45a0-83cc-23dbcf334e1e", "thread_id": "5e645af6-8b39-45a0-83cc-23dbcf334e1e", "traced_type": "https://didcomm.org/present-proof/2.0/request-presentation", "timestamp": 1726075470.6758707, "str_time": "2024-09-11 17:24:30.675871", "handler": "alice.agent.trace", "elapsed_milli": 7, "outcome": "V20PresRequestHandler.handle.END"}
Alice | Presentation: state = presentation-sent, pres_ex_id = 10f1f817-1904-4f8d-9f26-b6354c610cd0
Presentation: state = presentation-sent, pres_ex_id = 10f1f817-1904-4f8d-9f26-b6354c610cd0
Alice | 2024-09-11 17:24:30,676 aries_cloudagent.utils.tracing INFO acapy.events {"msg_id": "5e645af6-8b39-45a0-83cc-23dbcf334e1e", "thread_id": "5e645af6-8b39-45a0-83cc-23dbcf334e1e", "traced_type": "https://didcomm.org/present-proof/2.0/request-presentation", "timestamp": 1726075470.6759663, "str_time": "2024-09-11 17:24:30.675966", "handler": "alice.agent.trace", "elapsed_milli": 22, "outcome": "Dispatcher.handle_message.END"}
Alice | Presentation: state = done, pres_ex_id = 10f1f817-1904-4f8d-9f26-b6354c610cd0
Presentation: state = done, pres_ex_id = 10f1f817-1904-4f8d-9f26-b6354c610cd0
Alice | 2024-09-11 17:24:30,825 aries_cloudagent.utils.tracing INFO acapy.events {"msg_id": "N/A", "thread_id": "5e645af6-8b39-45a0-83cc-23dbcf334e1e", "traced_type": "dict:Exchange", "timestamp": 1726075470.8252838, "str_time": "2024-09-11 17:24:30.825284", "handler": "alice.agent.trace", "elapsed_milli": 0, "outcome": "OutboundTransportManager.DELIVER.START.http://host.docker.internal:8032/webhooks/topic/present_proof_v2_0/"}
Alice | 2024-09-11 17:24:30,825 aries_cloudagent.utils.tracing INFO acapy.events {"msg_id": "N/A", "thread_id": "5e645af6-8b39-45a0-83cc-23dbcf334e1e", "traced_type": "dict:Exchange", "timestamp": 1726075470.82579, "str_time": "2024-09-11 17:24:30.825790", "handler": "alice.agent.trace", "elapsed_milli": 0, "outcome": "OutboundTransportManager.DELIVER.END.http://host.docker.internal:8032/webhooks/topic/present_proof_v2_0/"}
Alice | 2024-09-11 17:24:30,828 aries_cloudagent.utils.tracing INFO acapy.events {"msg_id": "0373e94e-6da3-44da-8c3b-591688213aa4", "thread_id": "5e645af6-8b39-45a0-83cc-23dbcf334e1e", "traced_type": "https://didcomm.org/present-proof/2.0/presentation", "timestamp": 1726075470.8283095, "str_time": "2024-09-11 17:24:30.828310", "handler": "alice.agent.trace", "elapsed_milli": 135, "outcome": "presentation_exchange_send_request.END"}
Alice | 2024-09-11 17:24:30,828 aries_cloudagent.utils.tracing INFO acapy.events {"msg_id": "0373e94e-6da3-44da-8c3b-591688213aa4", "thread_id": "5e645af6-8b39-45a0-83cc-23dbcf334e1e", "traced_type": "https://didcomm.org/present-proof/2.0/presentation", "timestamp": 1726075470.8288581, "str_time": "2024-09-11 17:24:30.828858", "handler": "alice.agent.trace", "elapsed_milli": 0, "outcome": "OutboundTransportManager.ENCODE.START"}
Alice | 2024-09-11 17:24:30,829 aries_cloudagent.utils.tracing INFO acapy.events {"msg_id": "0373e94e-6da3-44da-8c3b-591688213aa4", "thread_id": "5e645af6-8b39-45a0-83cc-23dbcf334e1e", "traced_type": "https://didcomm.org/present-proof/2.0/presentation", "timestamp": 1726075470.8290217, "str_time": "2024-09-11 17:24:30.829022", "handler": "alice.agent.trace", "elapsed_milli": 0, "outcome": "OutboundTransportManager.ENCODE.END"}
Alice | 2024-09-11 17:24:30,831 aries_cloudagent.utils.tracing INFO acapy.events {"msg_id": "0373e94e-6da3-44da-8c3b-591688213aa4", "thread_id": "5e645af6-8b39-45a0-83cc-23dbcf334e1e", "traced_type": "https://didcomm.org/present-proof/2.0/presentation", "timestamp": 1726075470.8315887, "str_time": "2024-09-11 17:24:30.831589", "handler": "alice.agent.trace", "elapsed_milli": 0, "outcome": "OutboundTransportManager.DELIVER.START.http://host.docker.internal:8010"}
Alice | 2024-09-11 17:24:30,831 aries_cloudagent.utils.tracing INFO acapy.events {"msg_id": "0373e94e-6da3-44da-8c3b-591688213aa4", "thread_id": "5e645af6-8b39-45a0-83cc-23dbcf334e1e", "traced_type": "https://didcomm.org/present-proof/2.0/presentation", "timestamp": 1726075470.8317404, "str_time": "2024-09-11 17:24:30.831740", "handler": "alice.agent.trace", "elapsed_milli": 0, "outcome": "OutboundTransportManager.DELIVER.END.http://host.docker.internal:8010"}
Alice | 2024-09-11 17:24:30,976 aries_cloudagent.utils.tracing INFO acapy.events {"msg_id": "4cef63c3-c3eb-4c4a-964b-843140a832ef", "thread_id": "5e645af6-8b39-45a0-83cc-23dbcf334e1e", "traced_type": "https://didcomm.org/present-proof/2.0/ack", "timestamp": 1726075470.9767995, "str_time": "2024-09-11 17:24:30.976799", "handler": "alice.agent.trace", "elapsed_milli": 0, "outcome": "Dispatcher.handle_message.START"}
Alice | 2024-09-11 17:24:30,993 aries_cloudagent.utils.tracing INFO acapy.events {"msg_id": "N/A", "thread_id": "5e645af6-8b39-45a0-83cc-23dbcf334e1e", "traced_type": "dict:Exchange", "timestamp": 1726075470.993048, "str_time": "2024-09-11 17:24:30.993048", "handler": "alice.agent.trace", "elapsed_milli": 0, "outcome": "OutboundTransportManager.DELIVER.START.http://host.docker.internal:8032/webhooks/topic/present_proof_v2_0/"}
Alice | 2024-09-11 17:24:30,993 aries_cloudagent.utils.tracing INFO acapy.events {"msg_id": "N/A", "thread_id": "5e645af6-8b39-45a0-83cc-23dbcf334e1e", "traced_type": "dict:Exchange", "timestamp": 1726075470.9936516, "str_time": "2024-09-11 17:24:30.993652", "handler": "alice.agent.trace", "elapsed_milli": 0, "outcome": "OutboundTransportManager.DELIVER.END.http://host.docker.internal:8032/webhooks/topic/present_proof_v2_0/"}
Alice | 2024-09-11 17:24:30,994 aries_cloudagent.utils.tracing INFO acapy.events {"msg_id": "4cef63c3-c3eb-4c4a-964b-843140a832ef", "thread_id": "5e645af6-8b39-45a0-83cc-23dbcf334e1e", "traced_type": "https://didcomm.org/present-proof/2.0/ack", "timestamp": 1726075470.9943545, "str_time": "2024-09-11 17:24:30.994354", "handler": "alice.agent.trace", "elapsed_milli": 15, "outcome": "V20PresAckHandler.handle.END"}
Alice | 2024-09-11 17:24:30,994 aries_cloudagent.utils.tracing INFO acapy.events {"msg_id": "4cef63c3-c3eb-4c4a-964b-843140a832ef", "thread_id": "5e645af6-8b39-45a0-83cc-23dbcf334e1e", "traced_type": "https://didcomm.org/present-proof/2.0/ack", "timestamp": 1726075470.9944606, "str_time": "2024-09-11 17:24:30.994461", "handler": "alice.agent.trace", "elapsed_milli": 18, "outcome": "Dispatcher.handle_message.END"}
Alice | Received message: Message1
Alice | Received message: Message2
(3) Send Message
(4) Input New Invitation
(X) Exit?
[3/4/X] 3
Enter message: Message3
Alice | Received message: faber.agent received your message
(3) Send Message
(4) Input New Invitation
(X) Exit?
[3/4/X] 3
Enter message: Message4
Alice | Received message: faber.agent received your message
(3) Send Message
(4) Input New Invitation
(X) Exit?
[3/4/X]
```
