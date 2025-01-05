# FastAPI Interview Questions and Answers

### **2. FastAPI Framework**

11. **Explain the core features of FastAPI.**
   - FastAPI is a modern, fast (high-performance) web framework for building APIs with Python 3.6+ based on standard Python type hints. Its core features include:
     - **Fast**: Very high performance, on par with NodeJS and Go (thanks to Starlette and Pydantic).
     - **Easy**: Designed to be easy to use and learn, with a simple and intuitive API.
     - **Automatic interactive API documentation**: Automatically generates OpenAPI and JSON Schema documentation.
     - **Data validation**: Uses Pydantic for data validation and serialization.
     - **Asynchronous support**: Fully supports asynchronous programming with async and await.

12. **How does FastAPI compare to Flask or Django for building APIs?**
   - **Flask**: FastAPI is more feature-rich and provides automatic data validation and serialization, while Flask is more minimalistic and requires additional libraries for similar functionality. FastAPI is also asynchronous by default, making it more suitable for high-performance applications.
   - **Django**: Django is a full-fledged web framework with built-in ORM, admin panel, and more, while FastAPI focuses solely on building APIs. FastAPI is generally faster and more lightweight for API development, while Django is better for full-stack applications.

13. **What is Pydantic, and how does FastAPI use it?**
   - Pydantic is a data validation and settings management library for Python. FastAPI uses Pydantic to validate request and response data, ensuring that the data conforms to the specified types and constraints. This allows for automatic data validation and serialization, reducing boilerplate code.

14. **How do you define and validate request body schemas in FastAPI?**
   - You can define request body schemas using Pydantic models. FastAPI automatically validates the incoming request data against these models. For example:
   ```python
   from pydantic import BaseModel

   class Item(BaseModel):
       name: str
       price: float
       is_offer: bool = None

   @app.post("/items/")
   async def create_item(item: Item):
       return item
   ```

15. **Demonstrate how to handle query parameters in FastAPI.**
   - Query parameters can be defined as function parameters in your route functions. FastAPI automatically extracts them from the request. For example:
   ```python
   @app.get("/items/")
   async def read_items(skip: int = 0, limit: int = 10):
       return {"skip": skip, "limit": limit}
   ```

16. **How can you implement dependency injection in FastAPI?**
   - FastAPI supports dependency injection through the use of function parameters. You can define dependencies as functions and use them in your route handlers. For example:
   ```python
   from fastapi import Depends

   def get_query_param(q: str = None):
       return q

   @app.get("/items/")
   async def read_items(query: str = Depends(get_query_param)):
       return {"query": query}
   ```

17. **Write a simple FastAPI route that accepts a JSON payload and returns a response.**
   ```python
   from fastapi import FastAPI

   app = FastAPI()

   @app.post("/items/")
   async def create_item(item: Item):
       return {"item_name": item.name, "item_price": item.price}
   ```

18. **How do you configure CORS in a FastAPI application?**
   - You can configure CORS in FastAPI using the `CORSMiddleware`. For example:
   ```python
   from fastapi.middleware.cors import CORSMiddleware

   app.add_middleware(
       CORSMiddleware,
       allow_origins=["*"],  # Allows all origins
       allow_credentials=True,
       allow_methods=["*"],  # Allows all methods
       allow_headers=["*"],  # Allows all headers
   )
   ```

19. **Explain how middleware works in FastAPI.**
   - Middleware in FastAPI is a function that runs before and after each request. It can be used to process requests, add headers, handle exceptions, etc. You can add middleware using the `add_middleware` method on the FastAPI app instance.

20. **How do you test FastAPI routes using Pytest?**
   - You can test FastAPI routes using the `TestClient` provided by FastAPI. For example:
   ```python
   from fastapi.testclient import TestClient

   client = TestClient(app)

   def test_create_item():
       response = client.post("/items/", json={"name": "item1", "price": 10.5})
       assert response.status_code == 200
       assert response.json() == {"item_name": "item1", "item_price": 10.5}
