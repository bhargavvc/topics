Blocking incoming requests to different devices like a **System**, **Server**, **VM (Virtual Machine)**, or **IP-assigned Device** requires different approaches based on their nature and the level of control over the network. Here's how to block incoming requests for each:

### 1. **System (Operating System-level protection)**:
   - **Firewall Configuration**: The primary method to block incoming requests to a system is through a firewall. You can configure firewall rules to drop traffic based on IP, port, or protocol. For example:
     - **Linux (iptables/firewalld)**: Use `iptables` or `firewalld` to specify rules to drop or reject traffic on certain ports or IPs.
     - **Windows (Windows Defender Firewall)**: Use built-in Windows Firewall to block specific IPs or ports.
   - **Network Security Software**: Install security software that includes additional protection, like intrusion detection and prevention systems (IDPS), to block malicious incoming requests.

### 2. **Server (Web server, Database server, etc.)**:
   - **Web Application Firewall (WAF)**: For web servers, a WAF can be used to block incoming traffic that seems suspicious or malicious, including DDoS (Distributed Denial of Service) attacks.
   - **Server-level Firewalls**: Like **iptables** on Linux or **Windows Firewall** on a Windows server, these are used to restrict incoming connections by IP address, port, and protocol.
   - **Rate Limiting**: Implementing rate limiting on the server can prevent an overload of requests, especially useful against brute force or DDoS attempts.

### 3. **Virtual Machine (VM)**:
   - **VM-specific Firewalls**: Configure the firewall at the hypervisor level (like **VMware ESXi** or **Microsoft Hyper-V**) to block traffic destined for specific virtual machines.
   - **Hypervisor Security Features**: Many hypervisors have built-in security features that can isolate virtual machines from each other and the external network, restricting incoming connections to specific VM instances.
   - **Host-based Firewall**: Just like on a physical server, install a firewall on the VM itself to filter incoming traffic.

### 4. **IP-assigned Device (IoT, Network Device)**:
   - **Device-Level Firewalls**: Many network devices (like routers or IoT devices) come with integrated firewalls. Configure these devices to block incoming connections from certain IPs or ranges.
   - **Network Segmentation**: Devices can be isolated on separate subnets to prevent unwanted traffic from accessing them directly. This is often done in enterprise networks.
   - **Access Control Lists (ACLs)**: For routers and network switches, configure ACLs to block or restrict traffic to devices based on IP address or subnet.

### Summary of Methods:
- **System**: OS-level firewall (iptables, Windows Defender Firewall).
- **Server**: WAF, server firewall, rate limiting.
- **VM**: VM firewall, hypervisor-level security, host firewall.
- **IP-assigned Device**: Device firewall, network segmentation, ACLs.

In general, the method of blocking requests depends on whether the device operates at the operating system level (System), web server level (Server), virtual machine level (VM), or specific device level (IP-assigned Device).