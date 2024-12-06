

###DNS Workflow

**working of DNS (Domain Name System)**, a crucial process that translates domain names (like `example.com`) into IP addresses (e.g., `217.64.213.12`). Here's a step-by-step explanation:

---
![img](https://raw.githubusercontent.com/bhargavvc/topics/main/img/networking/dns-workflow.png)


### **1. User Input: Typing the Domain Name**
 
- **Action**: A user types `example.com` into their browser.
- **What Happens**: The browser sends a request to the **DNS Resolver**, asking it to resolve the domain name into an IP address.
- **Example**: You enter `www.example.com` into your browser to access Google.

---

### **2. DNS Resolver Queries Root Name Server**
 
- **Role**: The DNS resolver queries a **Root Name Server** for information about the domain.  
- **What Happens**: The root server doesn’t have the IP address but directs the resolver to the correct **Top-Level Domain (TLD) Name Server** for `.com`.
- **Link**: After the browser sends the request, the resolver starts querying servers step by step.
- **Example**: The DNS resolver asks the root server, "Where can I find the `.com` TLD server?"

---

### **3. TLD Server Response**
 
- **Role**: The root server responds with the address of the `.com` **TLD Name Server**.
- **What Happens**: The resolver is directed to the server responsible for `.com` domains.
- **Example**: The `.com` TLD server tells the resolver, "I don’t know the IP address, but here’s the authoritative server for `example.com`."

---

### **4. Resolver Contacts Authoritative Name Server**
 
- **Role**: The resolver queries the **Authoritative Name Server** for `example.com`.
- **What Happens**: The authoritative name server holds the actual IP address of the domain.
- **Example**: The resolver asks, "What is the IP address of `example.com`?"

---

### **5. IP Address Retrieval**
 
- **Role**: The authoritative server responds with the IP address `217.64.213.12`.
- **What Happens**: The resolver retrieves the IP address from the authoritative name server and prepares to return it to the browser.
- **Example**: The authoritative name server tells the resolver, "The IP address for `example.com` is `217.64.213.12`."

---

### **6. Browser Receives IP Address**
 
- **Role**: The DNS resolver sends the IP address back to the browser.
- **What Happens**: The browser can now use the IP address to establish a connection with the web server hosting `example.com`.
- **Example**: The browser uses the IP address `217.64.213.12` to load Google’s homepage.

---


 
### **Flow Overview**
- **Browser** → DNS Resolver → Root Server → TLD Server (.com) → Authoritative Name Server → IP Address (217.64.213.12) → Browser Access to Google.


### **Final Overview: Flow of DNS Resolution**
 
- **DNS Components**:
  - **Browser**: Sends the domain name query.
  - **DNS Resolver**: Intermediary that queries servers step by step.
  - **Root Server**: Points to the correct TLD server.
  - **TLD Server**: Points to the authoritative server for the domain.
  - **Authoritative Name Server**: Provides the final IP address.
- **Result**: The browser uses the IP address to connect to the web server and display the requested website.

---