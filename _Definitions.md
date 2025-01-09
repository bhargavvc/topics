

**Throughput**
   - **Concept**:  Throughput is a measure of the rate at which a system processes transactions or data units over a defined period,expressed in transactions per second (TPS), requests per second (RPS), or bytes per second (BPS)

   - **Advantage**: High throughput allows a system to handle more transactions and serve more users effectively.
   - **Disadvantage**: May require more powerful hardware or complex system configurations to handle high levels of data processing, impacting costs.
   - **Real-World Example**: High Request traffic websites like Netflix or YouTube that manage data streaming and user requests at massive scales to ensure smooth video playback and responsive user interfaces.

**Latency**
   - **Concept**: The time it takes for data to travel from one point in the network to another; crucial in networking and real-time processing.
   - **Advantage**: Low latency improves user experience by providing faster responses and real-time interaction capabilities.
   - **Disadvantage**: Achieving low latency across global systems can be challenging due to physical limitations(distance, infrastructure, and the inherent properties of data transmission), often requiring significant investment in optimized network solutions.
   - **Real-World Example**: Online gaming and stock trading platforms depend on real-time responsiveness, making low latency critical for user success and satisfaction.

Amazon SQS (Simple Queue Service), "to decouple and buffer incoming requests" means:

1. **Decoupling**: SQS helps to separate different parts of your application so that they can operate independently. For example, if you have a web server that processes user requests and a backend server that performs heavy computations, you can use SQS to send messages from the web server to the backend server. This way, the web server doesn't need to wait for the backend server to finish processing; it can continue handling other requests.

2. **Buffering**: SQS acts as a temporary storage for messages. When incoming requests are received, they are placed in the queue. This helps to handle situations where the rate of incoming requests is higher than the rate at which they can be processed. The queue buffers these requests and ensures that they are processed in a controlled manner, preventing system overload.

In summary, Amazon SQS helps to manage the flow of data between different components of your application, ensuring that they can work independently and efficiently handle varying loads.

serverless: means building and running applications and services without managing the infrastructure