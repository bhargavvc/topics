# RESTful API Interview Questions and Answers

### **5. RESTful APIs**

41. **What is a RESTful API? What are its key principles?**
   - A RESTful API (Representational State Transfer) is an architectural style for designing networked applications. It relies on a stateless, client-server communication model and uses standard HTTP methods. Key principles include:
     - **Statelessness**: Each request from a client contains all the information needed to process the request.
     - **Client-Server Separation**: The client and server are independent, allowing for flexibility in development.
     - **Cacheability**: Responses must define themselves as cacheable or not to improve performance.
     - **Layered System**: The architecture can be composed of multiple layers, with each layer having its own responsibilities.

42. **Explain the difference between HTTP methods GET, POST, PUT, DELETE, and PATCH.**
   - **GET**: Retrieve data from the server. It should not change the state of the server.
   - **POST**: Send data to the server to create a new resource.
   - **PUT**: Update an existing resource or create a new resource if it does not exist.
   - **DELETE**: Remove a resource from the server.
   - **PATCH**: Apply partial modifications to a resource.

43. **What are idempotent methods in REST APIs?**
   - Idempotent methods are HTTP methods that can be called multiple times without different outcomes. For example, a PUT request to update a resource is idempotent because calling it multiple times with the same data will not change the result beyond the initial application.

44. **How can you implement authentication in RESTful APIs?**
   - Authentication can be implemented using:
     - **Basic Authentication**: Sending a username and password with each request.
     - **Token-Based Authentication**: Using tokens (e.g., JWT) that are sent with each request after the user logs in.
     - **OAuth**: A more complex authentication mechanism that allows third-party services to exchange information without sharing credentials.

45. **What are the advantages of using JSON over XML in APIs?**
   - **Lightweight**: JSON is less verbose than XML, resulting in smaller payloads.
   - **Easier to read and write**: JSON syntax is simpler and more intuitive.
   - **Native support in JavaScript**: JSON can be easily parsed and generated in JavaScript, making it ideal for web applications.
   - **Better performance**: JSON parsing is generally faster than XML parsing.

46. **What is HATEOAS, and how does it enhance REST APIs?**
   - HATEOAS (Hypermedia as the Engine of Application State) is a constraint of the REST application architecture that allows clients to interact with the application entirely through hypermedia links provided dynamically by the server. It enhances REST APIs by enabling clients to discover actions dynamically, reducing the need for hardcoded URLs.

47. **How do you implement pagination in RESTful APIs?**
   - Pagination can be implemented by adding query parameters to the API endpoint, such as `page` and `limit`. For example:
   ```http
   GET /items?page=2&limit=10
   ```
   The server then returns the specified subset of results based on these parameters.

48. **What is a 429 HTTP status code, and when would you use it?**
   - The 429 Too Many Requests status code indicates that the user has sent too many requests in a given amount of time. It is commonly used for rate limiting to prevent abuse of the API.

49. **How do you handle versioning in REST APIs?**
   - Versioning can be handled in several ways:
     - **URI versioning**: Including the version in the URL (e.g., `/api/v1/resource`).
     - **Header versioning**: Specifying the version in the request headers.
     - **Query parameter versioning**: Using a query parameter to specify the version (e.g., `/api/resource?version=1`).

50. **Write a RESTful API endpoint to upload a file in FastAPI.**
   ```python
   from fastapi import FastAPI, File, UploadFile

   app = FastAPI()

   @app.post("/uploadfile/")
   async def upload_file(file: UploadFile = File(...)):
       return {"filename": file.filename}
