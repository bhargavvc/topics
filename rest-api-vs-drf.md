When discussing "REST API" versus "Django REST Framework (DRF)," we are comparing a general architectural style for building APIs to a specific tool designed to make implementing RESTful APIs easier in Django applications.

### REST API (Representational State Transfer API)

REST is an architectural style that defines a set of constraints used to create web services. It operates over HTTP and is designed with specific principles that make it a popular choice for modern web applications and mobile applications. Here are some key characteristics of REST APIs:

1. **Statelessness**: The server does not keep any client context between requests. Each request from the client must contain all the information necessary for the server to understand and process the request.
2. **Client-Server Architecture**: The client application and server application must be able to evolve independently without any dependency on each other.
3. **Cacheable**: Responses must define themselves as cacheable or non-cacheable, improving the efficiency of applications.
4. **Uniform Interface**: The interface between client and server is standardized, simplifying and decoupling the architecture, which allows each part to evolve independently.
5. **Layered System**: A client cannot ordinarily tell whether it is connected directly to the end server, or to an intermediary along the way.

### Django REST Framework (DRF)

Django REST Framework is a powerful and flexible toolkit for building Web APIs in Django. It is an application framework that provides tools for building RESTful APIs with Django, and it simplifies the process of creating complex APIs. Key features of DRF include:

1. **Serialization**: DRF provides a powerful serialization engine compatible with both ORM and non-ORM data sources. This simplifies the task of converting complex data types, such as queryset and model instances, into JSON, XML, or other content types.
2. **Authentication and Permissions**: Out-of-the-box support for authentication and authorization, including packages that support OAuth1a and OAuth2.
3. **Browsable API**: DRF has a browsable API that makes it easy for developers to interact with the API through a web browser.
4. **Throttling**: You can control the rate of API requests a user can make within a given time period.
5. **Versioning**: Supports API versioning to allow API changes over time without breaking existing clients.

### Comparison and Use Cases

- **Use of REST API**: Building a RESTful API can be done using any programming language or framework that supports HTTP. It requires you to handle the details of request handling, serialization, authentication, and other aspects according to the principles of REST.
  
- **Use of DRF**: DRF is specific to Django and is used when you want to implement a RESTful API within a Django project quickly. It handles much of the boilerplate code necessary for creating complex APIs, allowing you to focus on writing your application logic instead of reinventing the wheel.

In summary, if you're working within a Django project and need to create an API, DRF is an invaluable tool that can save you time and effort. If you're not using Django or are working in a different technology stack, you'll need to implement REST principles using other frameworks or libraries suitable for your stack.