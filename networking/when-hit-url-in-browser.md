
When a user types `example.com` into the browser:

![url-flow](https://raw.githubusercontent.com/bhargavvc/topics/main/img/networking/url-flow-process.png)


### **1. Entering the URL (`example.com`) in the Browser**
- The browser begins by trying to resolve the **IP address** of the entered domain.

---

### **2. DNS (Domain Name System) Resolution**
DNS helps translate the domain name (`example.com`) into its corresponding IP address (`93.184.216.34`) that computers can understand. Here's how it works:
1. **Cache Check**:
   - The browser first checks if the IP address is stored in its **cache** (browser, operating system, router, or ISP cache).
   - If found, the process skips the DNS query and proceeds directly to connecting to the server.
2. **If Cache Miss**:
   - The browser sends a query to resolve the domain name through the **DNS hierarchy**:
     - **Root Domain Name Server**: Provides details of the `.com` domain (the TLD).
     - **Top-Level Domain (TLD) Name Server**: Identifies where `.com` domains are managed.
     - **Second/Third-Level Name Server**: Provides the IP address for Name Sever (`example.com`).

Once resolved, the DNS returns the IP address (`93.184.216.34`), and the browser proceeds to connect to it.

---

### **3. Initiating a TCP/IP Connection**
After obtaining the IP address, the browser establishes a connection to the server hosting the website. This is done using the **TCP (Transmission Control Protocol)**, which ensures a reliable connection:
1. **SYN (Synchronize)**:
   - The browser (client) sends a request(SYN) to the server to start communication.
2. **SYN-ACK (Acknowledge)**:
   - The server acknowledges the request and agrees to establish communication by sending request(SYN-ACK).
3. **ACK (Acknowledge)**:
   - The browser confirms the connection, completing the **three-way handshake**.

Now the browser and server can exchange data over this connection.

---

### **4. HTTP Request**
Once the TCP connection is established, the browser sends an **HTTP (or HTTPS)** request to the server. For example:
- `GET http://example.com`
   - This requests the homepage of the website.

The request contains metadata (headers) such as:
- Browser type
- Cookies
- Preferred languages
- Other relevant information needed by the server.

---

### **5. Server Response**
The server processes the request and responds with the requested data. This response includes:
- **Status Code**: Indicates the result of the request:
   - `1xx`: Informational messages (e.g., connection progress).
   - `2xx`: Success (e.g., `200 OK`).
   - `3xx`: Redirection (e.g., `301 Moved Permanently`).
   - `4xx`: Client errors (e.g., `404 Not Found` for missing pages).
   - `5xx`: Server errors (e.g., `500 Internal Server Error`).

The response also includes:
- **HTML**: The structure of the page.
- **CSS**: Styling rules for the page.
- **JavaScript**: Functionality and interactivity for the page.

---

### **6. Parsing and Rendering (Browser Rendering Engine)**
The browser now processes the server's response and renders the web page:
1. **HTML Parsing**:
   - The browser reads the HTML and constructs a **DOM (Document Object Model) Tree**.
   - This tree represents the structure and elements of the webpage.

2. **CSS Parsing**:
   - CSS files are parsed to create a **CSSOM (CSS Object Model) Tree**.
   - This defines the styling (colors, fonts, layouts, etc.) of the page.

3. **Render Tree**:
   - The DOM and CSSOM are combined into a **Render Tree**, which describes the visual representation of the page.

4. **Layout**:
   - The browser calculates the positions and sizes of all elements on the screen.

5. **Painting**:
   - The browser paints the elements pixel by pixel on the screen.

6. **JavaScript Execution**:
   - If JavaScript is included in the page, it runs during or after the rendering process.
   - JavaScript can modify the DOM or CSSOM, potentially triggering a re-render.

---

### **7. Final Web Page Display**
Once the rendering process is complete, the browser displays the fully loaded and interactive web page to the user. Any additional functionality (e.g., animations, API calls) is handled asynchronously.

---
