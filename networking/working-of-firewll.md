**Firewall's working**

---
![img](https://raw.githubusercontent.com/bhargavvc/topics/main/img/networking/firewall.png)

### **What is a Firewall?**
A **firewall** is a network security device or software that **filters** traffic between a private network and the internet, blocking malicious traffic and allowing legitimate traffic. It analyzes network traffic to detect and prevent attacks such as unauthorized access or malicious data from entering a network.

- **Incoming traffic**: Data coming into the private network (e.g., a request to connect to a server).
- **Outgoing traffic**: Data leaving the private network (e.g., a request to access a website).

---

### **Step 1: Packet Filtering Firewall**
- **Function**: This is one of the simplest types of firewalls, where the firewall inspects each packet (unit of data transmitted over a network) based on predefined rules.
  
- **How it works**: 
  - The firewall checks the header information of the packet to determine:
    - **Source IP Address**: The address from where the packet originates.
    - **Destination IP Address**: The address to which the packet is being sent.
    - **Protocol**: The type of communication (e.g., TCP, UDP).
    - **Port Number**: The destination port number (e.g., port 80 for HTTP, port 443 for HTTPS).

- **Example Rule**: 
  - If the rule allows IP address `142.10.11.12` and port `443` (for HTTPS) in TCP format, the packet will be allowed through.
  - If the source address does not meet the criteria, the packet is blocked.

- **Limitation**: It only inspects packet headers and does not inspect the actual content of the data being transferred. This means it is less secure compared to other types of firewalls.

---

### **Step 2: Circuit-Level Gateway**
- **Function**: A circuit-level gateway works at a lower level and establishes a connection between trusted machines and remote hosts.
  
- **How it works**:
  - Instead of inspecting each individual packet, it focuses on the **session initiation** messages, which are part of the network protocol (e.g., TCP handshake).
  - It checks whether the connection request is legitimate and if the session is allowed.

- **Example**: 
  - A local machine requests a connection to a remote host. The firewall verifies whether the session initiation is allowed according to its rules.
  - Once the session is initiated, the firewall does not inspect the contents of the data being transferred (i.e., it does not inspect network packets after the connection is established).

- **Limitation**: It doesn't inspect the content of the data transferred after the session starts, making it less granular compared to more advanced firewalls.

---

### **Step 3: Application-Level Gateway (Proxy Firewall)**
- **Function**: This firewall operates at the **application layer** (Layer 7 of the OSI model) and inspects traffic based on the type of application.

- **How it works**:
  - The firewall checks not only the network protocol but also **application-level protocols** such as HTTP, FTP, etc.
  - It inspects the **services** that are being used and checks the **destination port** (e.g., port 80 for HTTP, port 443 for HTTPS).
  - It can also look into specific details like **HTTP request strings**, analyzing the actual request to ensure it follows security rules.

- **Example**: 
  - The firewall might block HTTP traffic to certain websites or inspect HTTPS requests for malicious code.
  
- **Advantages**: Since it works at a higher layer, it can enforce more strict security policies, including content filtering, user authentication, and specific service-level control.
  
- **Limitation**: Since it inspects data at the application level, it can introduce latency and may be complex to configure and maintain.

---

### **Step 4: Stateful Inspection Firewall**
- **Function**: A stateful inspection firewall is an advanced type of firewall that monitors the **state of active connections** and makes decisions based on the context of the traffic.

- **How it works**:
  - Instead of just looking at the header of each packet (like in packet filtering firewalls), it tracks the **state** of the connections (i.e., whether the packet is part of an existing connection or a new connection).
  - It ensures that each data packet belongs to a valid, established session.
  
- **Example**: 
  - If a connection was established with an incoming request, the firewall will allow related outgoing packets. If a packet tries to bypass the established session (e.g., a packet with an unexpected source), it will be blocked.
  
- **Advantages**: It offers higher security than basic packet filtering, as it understands the context of the communication and ensures that the packets are part of a valid session.
  
- **Limitation**: Stateful firewalls may require more resources to track the state of all connections, and they are vulnerable to attacks that involve hijacking or manipulating the state.

---

### **Step 5: Next-Generation Firewall (NGFW)**
- **Function**: NGFWs are the most advanced firewalls, combining multiple security features to provide more comprehensive protection.

- **How it works**:
  - **Packet Inspection**: Similar to packet filtering but with more sophisticated analysis.
  - **Stateful Inspection**: Retains the stateful inspection features.
  - **Deep Packet Inspection (DPI)**: Analyzes the data payload of packets (not just headers) to detect malicious content such as viruses, malware, and exploits.
  - **Intrusion Detection and Prevention**: Detects and blocks potential intrusions and attacks, such as DDoS, malware, and other vulnerabilities.
  - **Malware Filtering**: It can filter out malicious files, block malware, and even provide sandboxing to test suspicious content.
  
- **Example**: 
  - NGFWs inspect data at multiple layers, making it difficult for attackers to bypass the firewall using tactics like encryption, obfuscation, or evasion techniques.

- **Advantages**: NGFWs offer the highest level of protection as they combine packet inspection, deep packet inspection, application awareness, and intrusion prevention.
  
- **Limitation**: These firewalls are more complex to configure and manage, and they require more computational resources due to their in-depth analysis.

---

### **Summary of Firewall Types:**
1. **Packet Filtering Firewall**: Basic filtering based on IP addresses, ports, and protocols.
2. **Circuit-Level Gateway**: Verifies session initiation messages but does not inspect traffic after the connection is established.
3. **Application-Level Gateway (Proxy)**: Inspects traffic at the application level, enforcing strict rules for services and protocols.
4. **Stateful Inspection Firewall**: Monitors the state of connections and validates that packets are part of a valid session.
5. **Next-Generation Firewall (NGFW)**: Combines all the previous features along with advanced detection techniques like deep packet inspection and malware filtering.

Each firewall type offers different levels of security, and organizations often use a combination of these to ensure comprehensive protection.
