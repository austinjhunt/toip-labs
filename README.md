# Upwork Job - Sep 12, 2024 - Client: Abhilash K A

## Job Description

### Need help: Python Programmer help for a prototype

a. Programmer in Python, for a back-end application beginners competency is needed.
**\_\_**Code already exists in git\_\_\_\_ need help in getting solution up and running.
Need to work in Linux environment. - beginners competency is needed.
Need to be familar with git - beginners competency is needed.

Lab 1:
https://github.com/cloudcompass/ToIPLabs/blob/main/docs/LFS173xV2/AliceGetsCredential.md
This is the first lab. you need to work with existing code.

Lab 2:
https://github.com/cloudcompass/ToIPLabs/blob/main/docs/LFS173xV2/HelpAliceGetAJob.md
\*\*This is going to be our Prototype.

Testing via existing interface:
Lab 3:
https://github.com/cloudcompass/ToIPLabs/blob/main/docs/LFS173xV2/OpenAPIIntroduction.md

## Meeting Notes - Sep 12, 2024 8:20AM

Tasks:

- For Lab 1, Abhilash seeks clarity on the code flow; what functions are being called and what attributes are being passed, particularly on the [Issuing and Proving Credentials section of the demo](https://aca-py.org/latest/demo/#issuing-and-proving-credentials).
- For Lab 2, Abhilash seeks assistance with creating and deploying a [prototype](https://github.com/cloudcompass/ToIPLabs/blob/main/docs/LFS173xV2/HelpAliceGetAJob.md) to a Digital Ocean cloud server.
- For Lab 3, the task is to simply test the prototype using the existing OpenAPI interface.

## Lab 1: [Alice Gets a Credential](https://github.com/cloudcompass/ToIPLabs/blob/main/docs/LFS173xV2/AliceGetsCredential.md)

I'll be using Docker to run the demo

## ToIP & aca-py

This job focuses on the use of a Python library called **[ACA-Py (Aries Cloud Agaent - Python)](https://github.com/hyperledger/aries-cloudagent-python)**, a foundation for building Verifiable Credential ecosystems which operates in the Trust Over IP (ToIP) framework.

### Trust Over IP (ToIP)

ToIP (Trust over IP) is a framework that addresses digital trust in a comprehensive, decentralized manner. It's designed to create a layer of trust on the internet, which traditionally relies on centralized authorities (like certificate authorities) or intermediaries to verify identity and relationships. ToIP's aim is to build a more trustworthy digital ecosystem by leveraging decentralized identifiers (DIDs), verifiable credentials (VCs), and other blockchain-related technologies. Here's a breakdown of how it works:

1. **Four-Layer Model**: ToIP is structured into four layers, each addressing different components of trust in digital interactions:

   - 1.1. Layer 1: The Utility Layer (Public Ledger or Utility Network): This is the foundation of the framework. It includes public blockchains or other distributed ledgers that store decentralized identifiers (DIDs) and cryptographic proofs. These public utilities act as tamper-proof, immutable sources of truth for identity management but don't store any personal data.
   - 1.2. Layer 2: The Credential Exchange Layer: This layer involves verifiable credential exchanges. It allows individuals and organizations to create, share, and verify digital credentials securely. Verifiable credentials (VCs) are digitally signed claims, like a driver's license or a university degree, that are cryptographically verifiable without relying on a centralized authority. These can be presented by users to prove their identity or qualifications.
   - 1.3. Layer 3: The Governance Layer: Governance frameworks define the rules and policies for credential issuance, verification, and usage. Each ToIP network can have its own governance framework, setting trust standards and operational guidelines. This layer ensures that interactions follow ethical, legal, and operational requirements.
   - 1.4. Layer 4: The Application Layer: The application layer is where end-user applications interact with the ToIP framework. These could be mobile apps, enterprise solutions, or even government portals that enable the issuance, management, and verification of credentials. The goal is to create seamless, user-friendly experiences for trust-related tasks like verifying someone's identity or qualification.

2. **Decentralized Identifiers (DIDs)**: DIDs are a core concept of the ToIP framework. They are unique, cryptographically verifiable identifiers that individuals, organizations, and even devices can use. Unlike traditional identifiers (e.g., email or social security numbers), DIDs are not tied to a single central authority. The owner of the DID controls it through private keys, allowing them to authenticate themselves and prove ownership without involving intermediaries.

3. **Verifiable Credentials (VCs)**: VCs are digital, cryptographically secure versions of credentials that you might use in the physical world, such as diplomas, IDs, or membership cards. They are issued by a trusted issuer, held by the individual, and can be verified by a third party. The verification process doesn't expose any unnecessary data and uses cryptographic proofs to ensure the credentials haven’t been tampered with.

4. **Interoperability and Privacy**: ToIP emphasizes interoperability between different systems and networks while maintaining user privacy. Users can choose which credentials to share and with whom, ensuring that unnecessary personal information is not exposed. For example, to prove you're of legal age, you don’t need to share your birthdate, just a cryptographic proof that you're over 18.

5. **Decentralization and Trust**: The ToIP model leverages decentralization to remove reliance on single points of failure (e.g., centralized identity providers like Google or Facebook). By shifting trust to cryptographic methods and decentralized networks, users have more control over their digital identities and data. This reduces the risks of data breaches and misuse of personal information.

Use Cases:

- Digital Identity: Verifiable digital identities for individuals, companies, and IoT devices.
- Supply Chain Verification: Trustworthy tracking of goods and certifications across a global supply chain.
- Healthcare: Sharing medical credentials and data securely while maintaining privacy.
- Education: Issuing and verifying educational credentials, like degrees or certifications.

#### Real-World Use Case: Alice & Faber

Let’s imagine a scenario where Faber is a university and Alice is a student applying for a job. Here's how ToIP (Trust over IP) could be used in this real-world situation:

**Scenario: Job Application Process Using ToIP**

1. **Faber Issues a Verifiable Credential**: Alice recently graduated from Faber University with a degree in Computer Science. Instead of giving Alice a paper diploma, Faber University issues a **Verifiable Credential (VC)**, a digital certificate that proves Alice’s degree.
   This VC is stored in Alice’s digital wallet, which is a secure app on her phone designed to hold these types of credentials.

2. Alice Applies for a Job: Alice is applying for a software engineering job at a tech company, and during the application process, the company requests proof of her degree.
   Alice opens her digital wallet, selects the degree VC from Faber, and shares it with the company through their online job application portal.

3. **Verification of the Credential:** The tech company uses a ToIP-compatible application to verify Alice's credential. Instead of having to call Faber or check some centralized database, the company checks the cryptographic proof on the public blockchain (Layer 1, the Utility Layer). Since Faber’s **DID (Decentralized Identifier)** and the cryptographic signature on the credential are stored on the blockchain, the tech company can confirm that the degree is valid and issued by Faber, without any intermediaries. The company doesn’t receive any more information than necessary; they simply verify that Alice holds a valid degree.

4. **Alice Retains Control:** Importantly, Alice is always in control of her credentials. She decided when and with whom to share her degree, and she didn't have to share any personal information beyond what's necessary for the job application.
   Faber University doesn’t need to be directly involved in this verification process, so Alice’s privacy is protected, and the process is faster.

##### Why This Is Better with ToIP:

- Speed and Simplicity: There’s no need for the tech company to contact Faber or wait for slow verification processes. The digital credential can be verified instantly.
- Decentralization: There’s no reliance on any centralized authority to maintain or verify credentials. Everything operates through decentralized identifiers and cryptographic proof.
- Privacy: Alice only shares what is necessary. The tech company doesn’t need to see her transcript or other personal details, only a cryptographic proof that confirms her degree.
- Security: Since the VC is stored in Alice’s digital wallet and backed by cryptographic methods, it’s far more secure than a physical diploma or traditional digital files, which could be forged or tampered with.

In this example, the ToIP framework allows Faber, Alice, and the tech company to interact securely, efficiently, and privately, without needing a central party to mediate or verify the transaction.

### How ACA-Py fits into ToIP

ACA-Py (Aries Cloud Agent - Python) is an open-source project that plays a key role in the implementation of decentralized identity solutions, including those aligned with the Trust over IP (ToIP) framework. ACA-Py is a cloud agent built using the Hyperledger Aries framework, designed for managing decentralized identities, verifiable credentials (VCs), and secure communication between entities. It fits into the ToIP framework by providing a practical, interoperable toolset to implement the decentralized identity layer (i.e., managing DIDs and VCs) and enabling secure, verifiable interactions. Here's an outline:

1. DID Management and Interaction (Layer 1 and Layer 2 of ToIP)
   In the Trust over IP (ToIP) model, the Utility Layer (Layer 1) is where decentralized identifiers (DIDs) are registered and verified on a public ledger. ACA-Py provides the functionality to:
   - Create, manage, and resolve DIDs (decentralized identifiers).
   - Communicate securely using DIDComm protocols, which establish encrypted communication channels between different agents (e.g., between Alice's wallet and Faber's university system).

ACA-Py interacts with the public ledger (often a blockchain network) to register these DIDs and also retrieve cryptographic proofs necessary for trustless verifications, allowing Alice (the user) to share verifiable credentials with others.

2. Credential Issuance, Exchange, and Verification (Layer 2 of ToIP)
   In the Credential Exchange Layer (Layer 2), entities like Faber University can issue credentials to users like Alice. ACA-Py allows the implementation of these interactions by:

   - Acting as an issuer of credentials: Faber could use ACA-Py to issue Alice a verifiable credential after graduation.
   - Supporting credential exchange: When Alice applies for a job and shares her credentials, ACA-Py facilitates the secure, encrypted transmission of those credentials.
   - Enabling verification: The hiring company can use ACA-Py to verify Alice’s credentials by checking the cryptographic proof against the public ledger (using the DID).
   - ACA-Py provides pre-built functionalities to perform these processes securely and in a standardized way.

3. Interoperability and Governance (Layer 3 of ToIP)
   The Governance Layer (Layer 3) defines the rules and standards that organizations and users must follow when issuing or verifying credentials. ACA-Py fits here by:

   - Supporting interoperability standards such as Aries Interop Profile to ensure that different agents (digital wallets, credential issuers, verifiers) can communicate seamlessly, regardless of their specific implementation.
   - ACA-Py allows different actors to follow specific governance frameworks, ensuring trust is maintained according to agreed-upon rules and policies. For example, Faber University might adopt a specific governance model for higher education credentials, ensuring all universities follow similar standards when issuing degrees.

4. Application Layer (Layer 4 of ToIP)
   At the Application Layer (Layer 4), end-users like Alice interact with their credentials, and organizations like Faber manage the issuance of credentials. ACA-Py:
   - Powers cloud-based agents that can be deployed as part of applications to enable decentralized identity features.
   - Integrates with digital wallets (like Alice's wallet) or enterprise systems (like Faber University’s credential management system) to enable easy user interaction with verifiable credentials.

In practice, a developer building a decentralized identity application would use ACA-Py to manage the secure interactions between users, credential issuers, and verifiers. For example:

- Alice could use an app powered by ACA-Py to request her degree credential from Faber.
- Faber uses ACA-Py to issue the degree to Alice's wallet.
- A hiring company uses ACA-Py to verify Alice’s degree during a job application process.

#### How ACA-Py Supports ToIP in a Practical Example:

Let’s return to the scenario with Alice and Faber University:

1. Faber University uses ACA-Py as a backend agent to issue verifiable credentials (e.g., Alice's degree).
2. Alice's wallet (also powered by ACA-Py or another Aries-compliant agent) stores the credential.
3. When Alice applies for a job, she shares her credential with the company via a DIDComm encrypted channel, which is secured by ACA-Py on both ends (Alice's wallet and the company's verification agent).
4. The tech company uses ACA-Py to verify the credential by checking the cryptographic proof on a public ledger, ensuring Alice’s degree is legitimate without ever contacting Faber University.
