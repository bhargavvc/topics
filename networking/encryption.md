# Encryption Class Notes

## Introduction to Encryption

![encryption](https://raw.githubusercontent.com/bhargavvc/topics/main/img/networking/encryption.png)
- **Confidentiality**: Ensures that only the intended recipient can interpret the transmitted data.
- **Plain Text (Clear Text)**: The original, unencrypted data (e.g., the word "hello").
- **Cipher Text**: The encrypted version of the plain text, making it undecipherable to unauthorized parties.
- **Encryption Process**:
  - Sender encrypts plain text into cipher text.
  - Sends cipher text to the intended recipient.
  - Recipient decrypts cipher text back to plain text (decryption).

## Simple Encryption
![simple-encrytption](https://raw.githubusercontent.com/bhargavvc/topics/main/img/networking/simple-encrytption.png)
- **Concept**: Transforming plain text into cipher text using an encryption algorithm.
- **Limitations**:
  - **Scalability Issues**: 
    - Each new recipient requires a unique encryption algorithm.
    - Difficult to manage and securely create multiple algorithms.
  - **Security Challenges**:
    - Publicly known algorithms can be easily decrypted by anyone.
    - Creating secure, unique transformations is complex and resource-intensive.

## Key-Based Encryption
![Key-Based Encryption](https://raw.githubusercontent.com/bhargavvc/topics/main/img/networking/key-based-encrytption.png)
- **Solution to Simple Encryption Problems**:
  - Combines a publicly vetted algorithm with a secret key.
  - **Algorithm**: Developed and validated by cryptographers and mathematicians for security.
  - **Secret Key**: A random set of ones and zeros unique to each user.
- **Benefits**:
  - **Scalability**: Easily manage encryption for multiple users by generating unique keys.
  - **Security**: Public algorithms remain secure as only the key can decrypt the cipher text.

## Types of Key-Based Encryption
![Types of Key-Based Encryption](https://raw.githubusercontent.com/bhargavvc/topics/main/img/networking/symmetric-vs-asymmetric-diagram-example.png)

### Symmetric Encryption
- **Definition**: Uses the same key for both encryption and decryption.
- **Example**:
  - **Encryption**: Shift each letter forward by a fixed number (e.g., 3 positions).
    - "hello" → "khoor"
  - **Decryption**: Shift each letter backward by the same number.
    - "khoor" → "hello"
- **Characteristics**:
  - Faster and more efficient for bulk data.
  - Cipher text size remains approximately the same as plain text.

### Asymmetric Encryption
- **Definition**: Uses different keys for encryption and decryption (public and private keys).
- **Example**:
  - **Encryption Key**: Shift each letter forward by 5 positions.
    - "hello" → "mjqqt"
  - **Decryption Key**: Shift each letter forward by 21 positions (since 5 + 21 = 26).
    - "mjqqt" → "hello"
- **Characteristics**:
  - More secure as the private key is never shared.
  - Cipher text expansion occurs, making the encrypted data larger.
  - Slower and more computationally intensive due to complex mathematics.

## Strengths and Weaknesses
![Strengths and Weaknesses](https://raw.githubusercontent.com/bhargavvc/topics/main/img/networking/symmetric-vs-asymmetric-differents.png)
### Symmetric Encryption
- **Strengths**:
  - **Speed**: Faster encryption and decryption processes.
  - **Efficiency**: Suitable for encrypting large amounts of data without significant overhead.
  - **Cipher Text Size**: Maintains similar size to plain text.
- **Weaknesses**:
  - **Key Distribution**: The same secret key must be securely shared between parties.
  - **Security**: Considered less secure if the key is compromised.

### Asymmetric Encryption
- **Strengths**:
  - **Security**: Private key remains confidential, enhancing security.
  - **Key Management**: Easier to manage since the private key is not shared.
- **Weaknesses**:
  - **Performance**: Slower due to complex mathematical operations.
  - **Cipher Text Expansion**: Encrypted data is larger, leading to increased bandwidth usage.

## Use Cases
- **Symmetric Encryption**:
  - Ideal for bulk data protection.
  - Suitable when speed and efficiency are priorities.
- **Asymmetric Encryption**:
  - Best for encrypting smaller data sets.
  - Used when enhanced security is required without significant performance trade-offs.

## Encryption Algorithms
### Asymmetric Encryption Algorithms
- **DSA (Digital Signature Algorithm)**
- **RSA (Rivest–Shamir–Adleman)**
- **Diffie-Hellman**
- **Elliptic Curve Cryptography (ECC)**
- **Note**: Algorithms like DES and RC4 are **insecure** and should be avoided.

### Symmetric Encryption Algorithms
- **DES (Data Encryption Standard)**: **Insecure** by modern standards.
- **RC4**: **Insecure** and deprecated.
- **Triple DES**: Offers better security (168-bit key strength) but is considered less secure compared to newer algorithms.
- **AES (Advanced Encryption Standard)** and **ChaCha20**: Recommended for strong symmetric encryption.

## Key Size Comparison
- **Symmetric Encryption**:
  - Typically uses smaller key sizes (e.g., AES-256).
  - Generally more efficient in terms of processing power.
- **Asymmetric Encryption**:
  - Requires larger key sizes for equivalent security (e.g., RSA-2048).
  - Increased computational requirements due to larger keys.

## Conclusion and Next Steps
- **Main Takeaways**:
  - Understanding key-based encryption and the differences between symmetric and asymmetric methods.
  - Recognizing the strengths and weaknesses of each encryption type.
- **Upcoming Topics**:
  - Detailed exploration of asymmetric encryption.
  - Operations and uses of public and private keys.
  - Combining symmetric and asymmetric encryption to leverage their respective strengths.

## Additional Resources
- **Practical TLS Course**:
  - Deep dive into SSL and TLS.
  - Covers cryptography, certificates, private keys, handshakes, and more.
  - Suitable for becoming an expert in TLS.
  - Visit [packet.net TLS](https://packet.net/tls) for more information and free lesson previews.

---

*Thank you for attending the encryption class! See you in the next lesson.*