Certainly! Below is a comprehensive and well-structured guide for defining Django models and routes for **LOB Logistics**. This guide encompasses the creation of models, serializers, viewsets, URL configurations, authentication mechanisms, optimization techniques, and additional advanced features to ensure a robust and scalable backend system tailored to the logistics workflow.

---

# **LOB Logistics Backend Development Guide**

Establishing a robust backend for **LOB Logistics** involves defining Django models that represent essential entities such as **Trucks**, **Loads**, and **Shipments**. Additionally, setting up RESTful routes to handle CRUD operations ensures efficient data management and retrieval. This guide provides a structured approach to defining these components, along with advanced features to optimize and secure the logistics workflow.

---

## **Table of Contents**

1. [Django Models](#1-django-models)
    - [Truck Model](#truck-model)
    - [Load Model](#load-model)
    - [Shipment Model](#shipment-model)
2. [Django Serializers](#2-django-serializers)
    - [Serializers for the Models](#serializers-for-the-models)
3. [Django ViewSets](#3-django-viewsets)
    - [ViewSets for CRUD Operations](#viewsets-for-crud-operations)
4. [Django URLs](#4-django-urls)
    - [Setting Up the URLs for the API](#setting-up-the-urls-for-the-api)
5. [Code Optimization Techniques](#5-code-optimization-techniques)
    - [Optimizing Querysets](#optimizing-querysets)
    - [Caching](#caching)
6. [Implementing Authentication and Permissions](#6-implementing-authentication-and-permissions)
    - [Adding Authentication and Permissions to the API](#adding-authentication-and-permissions-to-the-api)
7. [Testing the API](#7-testing-the-api)
    - [Using Django's Test Framework](#using-djangos-test-framework)
8. [Frontend Integration](#8-frontend-integration)
    - [Considerations for Integrating with a Frontend Application](#considerations-for-integrating-with-a-frontend-application)
9. [Deployment Considerations](#9-deployment-considerations)
    - [Best Practices for Deploying the Django Application](#best-practices-for-deploying-the-django-application)
10. [Advanced Features](#10-advanced-features)
    - [Monitoring and Logging](#monitoring-and-logging)
    - [Continuous Integration/Continuous Deployment (CI/CD)](#continuous-integrationcontinuous-deployment-cicd)
    - [User Role Management](#user-role-management)
    - [Notifications](#notifications)
    - [Search Functionality](#search-functionality)
    - [Pagination](#pagination)
    - [Rate Limiting](#rate-limiting)
    - [Asynchronous Task Handling](#asynchronous-task-handling)
    - [Geolocation Services](#geolocation-services)
    - [Data Visualization](#data-visualization)
    - [Custom Middleware](#custom-middleware)
    - [API Documentation](#api-documentation)
    - [User Registration and Login](#user-registration-and-login)
    - [File Uploads](#file-uploads)
    - [Data Encryption](#data-encryption)
11. [Comprehensive API Endpoints](#11-comprehensive-api-endpoints)
    - [User Authentication Endpoints](#user-authentication-endpoints)
    - [Shipment Management Endpoints](#shipment-management-endpoints)
    - [Feedback and Profile Endpoints](#feedback-and-profile-endpoints)
12. [Conclusion](#12-conclusion)

---

## **1. Django Models**

Defining Django models is crucial for representing the core entities of **LOB Logistics**. Below are the models for **Truck**, **Load**, and **Shipment**.

### **Truck Model**

```python
from django.db import models

class Truck(models.Model):
    truck_id = models.CharField(max_length=20, unique=True)
    capacity = models.FloatField()  # Capacity in tons
    driver_name = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.truck_id} - {self.driver_name}"
```

- **Fields:**
  - `truck_id`: Unique identifier for each truck.
  - `capacity`: Load capacity in tons.
  - `driver_name`: Name of the truck driver.

### **Load Model**

```python
from django.db import models

class Load(models.Model):
    load_id = models.CharField(max_length=20, unique=True)
    weight = models.FloatField()  # Weight in tons
    destination = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.load_id} - {self.destination}"
```

- **Fields:**
  - `load_id`: Unique identifier for each load.
  - `weight`: Weight of the load in tons.
  - `destination`: Destination address for the load.

### **Shipment Model**

```python
from django.db import models

class Shipment(models.Model):
    STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('In Transit', 'In Transit'),
        ('Delivered', 'Delivered'),
        ('Cancelled', 'Cancelled'),
    ]

    shipment_id = models.CharField(max_length=20, unique=True)
    load = models.ForeignKey(Load, on_delete=models.CASCADE)
    truck = models.ForeignKey(Truck, on_delete=models.CASCADE)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES)
    document = models.FileField(upload_to='shipment_documents/', blank=True, null=True)
    current_location = models.CharField(max_length=255, blank=True, null=True)  # Geolocation data

    def __str__(self):
        return f"{self.shipment_id} - {self.status}"
```

- **Fields:**
  - `shipment_id`: Unique identifier for each shipment.
  - `load`: Foreign key linking to the **Load** model.
  - `truck`: Foreign key linking to the **Truck** model.
  - `status`: Current status of the shipment.
  - `document`: Optional file upload for shipment-related documents.
  - `current_location`: Optional field for tracking the shipment's current location.

---

## **2. Django Serializers**

Serializers convert complex data types, such as querysets and model instances, into native Python datatypes that can then be easily rendered into JSON, XML, or other content types.

### **2.1. Creating Serializers for the Models**

```python
from rest_framework import serializers
from .models import Truck, Load, Shipment

class TruckSerializer(serializers.ModelSerializer):
    class Meta:
        model = Truck
        fields = '__all__'

class LoadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Load
        fields = '__all__'

class ShipmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shipment
        fields = '__all__'
```

- **Explanation:**
  - Each serializer corresponds to a Django model.
  - The `fields = '__all__'` directive includes all model fields in the serialization process.

---

## **3. Django ViewSets**

ViewSets provide a way to combine logic for a set of related views in a single class. They automatically provide actions like `list`, `create`, `retrieve`, `update`, and `destroy`.

### **3.1. ViewSets for CRUD Operations**

```python
from rest_framework import viewsets
from .models import Truck, Load, Shipment
from .serializers import TruckSerializer, LoadSerializer, ShipmentSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from django_filters import rest_framework as filters
from rest_framework.pagination import PageNumberPagination

class StandardResultsSetPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 100

class TruckViewSet(viewsets.ModelViewSet):
    queryset = Truck.objects.all()
    serializer_class = TruckSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_fields = ['capacity', 'driver_name']

class LoadViewSet(viewsets.ModelViewSet):
    queryset = Load.objects.all()
    serializer_class = LoadSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_fields = ['destination', 'weight']

class ShipmentViewSet(viewsets.ModelViewSet):
    queryset = Shipment.objects.select_related('load', 'truck').all()
    serializer_class = ShipmentSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_fields = ['status', 'truck__truck_id']
    pagination_class = StandardResultsSetPagination
```

- **Key Components:**
  - **Authentication and Permissions:**
    - `TokenAuthentication`: Secures the API endpoints using token-based authentication.
    - `IsAuthenticated`: Ensures that only authenticated users can access the endpoints.
  
  - **Filtering:**
    - Utilizes `DjangoFilterBackend` to enable filtering based on specified fields.
  
  - **Pagination:**
    - Implements `PageNumberPagination` to handle large datasets efficiently.

- **Optimization:**
  - `select_related('load', 'truck')`: Reduces the number of database queries by fetching related `Load` and `Truck` objects in a single query.

---

## **4. Django URLs**

Setting up URLs is essential for routing API requests to the appropriate viewsets.

### **4.1. Setting Up the URLs for the API**

```python
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TruckViewSet, LoadViewSet, ShipmentViewSet

router = DefaultRouter()
router.register(r'trucks', TruckViewSet)
router.register(r'loads', LoadViewSet)
router.register(r'shipments', ShipmentViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
```

- **Explanation:**
  - **DefaultRouter**: Automatically generates the standard set of CRUD URLs for each registered viewset.
  - **Registered Routes:**
    - `truck`: Handles all operations related to trucks.
    - `load`: Manages load-related operations.
    - `shipment`: Oversees shipment-related functionalities.

---

## **5. Code Optimization Techniques**

Enhancing the performance and efficiency of the Django application is crucial, especially for a logistics system that may handle large volumes of data.

### **5.1. Optimizing Querysets**

- **Use `select_related` and `prefetch_related`:**
  
  These methods reduce the number of database queries by fetching related objects in bulk.

  ```python
  class ShipmentViewSet(viewsets.ModelViewSet):
      queryset = Shipment.objects.select_related('load', 'truck').all()
      serializer_class = ShipmentSerializer
  ```

- **Bulk Create and Update:**
  
  Perform bulk operations to minimize database hits when handling multiple records.

  ```python
  # Example of bulk creating shipments
  Shipment.objects.bulk_create([
      Shipment(load=load_instance, truck=truck_instance, shipment_id='SH001', status='Pending'),
      Shipment(load=load_instance, truck=truck_instance, shipment_id='SH002', status='Pending'),
  ])
  ```

- **Optimize Querysets with `.values()` and `.values_list()`:**
  
  Retrieve only the necessary fields to improve performance.

  ```python
  def get_truck_loads(truck_id):
      return Load.objects.filter(shipment__truck__truck_id=truck_id).values('load_id', 'weight')
  ```

### **5.2. Caching**

Implement caching to store frequently accessed data, thereby reducing database load and improving response times.

```python
from django.core.cache import cache

def get_truck_details(truck_id):
    truck = cache.get(f'truck_{truck_id}')
    if not truck:
        truck = Truck.objects.get(truck_id=truck_id)
        cache.set(f'truck_{truck_id}', truck, timeout=300)  # Cache for 5 minutes
    return truck
```

- **Explanation:**
  - **`cache.get`**: Attempts to retrieve the truck details from the cache.
  - **`cache.set`**: If not found, fetches from the database and stores it in the cache for future requests.

---

## **6. Implementing Authentication and Permissions**

Securing the API ensures that only authorized users can access or modify data.

### **6.1. Adding Authentication and Permissions to the API**

```python
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication

class TruckViewSet(viewsets.ModelViewSet):
    queryset = Truck.objects.all()
    serializer_class = TruckSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

class LoadViewSet(viewsets.ModelViewSet):
    queryset = Load.objects.all()
    serializer_class = LoadSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

class ShipmentViewSet(viewsets.ModelViewSet):
    queryset = Shipment.objects.select_related('load', 'truck').all()
    serializer_class = ShipmentSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
```

- **Components:**
  - **Authentication Classes:**
    - `TokenAuthentication`: Secures API endpoints using token-based authentication.
  
  - **Permission Classes:**
    - `IsAuthenticated`: Restricts access to authenticated users only.

---

## **7. Testing the API**

Ensuring the API behaves as expected is vital for reliability and stability.

### **7.1. Using Django's Test Framework**

```python
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Truck

class TruckTests(APITestCase):
    def setUp(self):
        self.url = reverse('truck-list')
        self.truck_data = {'truck_id': 'TRK001', 'capacity': 15.0, 'driver_name': 'John Doe'}
        self.user = CustomUser.objects.create_user(username='testuser', password='testpass')
        self.client.force_authenticate(user=self.user)

    def test_create_truck(self):
        response = self.client.post(self.url, self.truck_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Truck.objects.count(), 1)
        self.assertEqual(Truck.objects.get().truck_id, 'TRK001')

    def test_get_trucks(self):
        Truck.objects.create(**self.truck_data)
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
```

- **Explanation:**
  - **`setUp` Method:**
    - Initializes test data and authenticates a test user.
  
  - **Test Cases:**
    - **`test_create_truck`**: Verifies that a truck can be successfully created.
    - **`test_get_trucks`**: Ensures that the API returns the correct number of trucks.

---

## **8. Frontend Integration**

Seamless integration with frontend applications enhances user experience and operational efficiency.

### **8.1. Considerations for Integrating with a Frontend Application**

- **API Documentation:**
  
  Utilize tools like **Swagger** or **Postman** to document API endpoints, aiding frontend developers in understanding available operations.

- **CORS Configuration:**
  
  Allow cross-origin requests if the frontend is hosted on a different domain.

  ```python
  # settings.py
  INSTALLED_APPS = [
      ...
      'corsheaders',
      ...
  ]

  MIDDLEWARE = [
      'corsheaders.middleware.CorsMiddleware',
      ...
  ]

  CORS_ALLOWED_ORIGINS = [
      "http://localhost:3000",  # Example frontend URL
      "https://yourfrontend.com",  # Production frontend URL
  ]
  ```

  - **Installation:**
    
    ```bash
    pip install django-cors-headers
    ```

  - **Explanation:**
    - **`corsheaders`**: A Django app for handling Cross-Origin Resource Sharing (CORS), making cross-origin AJAX possible.

---

## **9. Deployment Considerations**

Deploying the Django application effectively ensures reliability, scalability, and security in a production environment.

### **9.1. Best Practices for Deploying the Django Application**

- **Use a WSGI Server:**
  
  Deploy using **Gunicorn** or **uWSGI** behind a reverse proxy like **Nginx**.

  ```bash
  # Example command to run Gunicorn
  gunicorn your_project.wsgi:application --bind 0.0.0.0:8000
  ```

- **Database Migrations:**
  
  Run migrations on the production database after deployment.

  ```bash
  python manage.py migrate
  ```

- **Environment Variables:**
  
  Manage sensitive information using environment variables.

  ```bash
  # Example in bash
  export SECRET_KEY='your_secret_key'
  export DATABASE_PASSWORD='your_db_password'
  ```

  - **Security Tip:** Avoid hardcoding sensitive information in the codebase.

- **Static Files:**
  
  Collect static files using `collectstatic`.

  ```bash
  python manage.py collectstatic
  ```

- **Secure Settings:**
  
  - **Debug Mode:**
    
    Ensure `DEBUG = False` in production.
  
  - **Allowed Hosts:**
    
    Define `ALLOWED_HOSTS` to include your domain names.

    ```python
    # settings.py
    ALLOWED_HOSTS = ['yourdomain.com', 'www.yourdomain.com']
    ```

- **SSL/TLS:**
  
  Implement SSL/TLS to secure data transmission.

  - **Using Let's Encrypt:**
    
    Obtain free SSL certificates from Let's Encrypt.

- **Monitoring:**
  
  Continuously monitor the application for performance and errors using tools like **Sentry** or **New Relic**.

---

## **10. Advanced Features**

Enhancing the backend system with advanced functionalities ensures scalability, security, and an improved user experience.

### **10.1. Monitoring and Logging**

- **Django's Built-in Logging:**

  ```python
  # settings.py
  LOGGING = {
      'version': 1,
      'disable_existing_loggers': False,
      'handlers': {
          'file': {
              'level': 'DEBUG',
              'class': 'logging.FileHandler',
              'filename': 'django_debug.log',
          },
      },
      'loggers': {
          'django': {
              'handlers': ['file'],
              'level': 'DEBUG',
              'propagate': True,
          },
      },
  }
  ```

  - **Explanation:**
    - Logs all Django-related activities at the DEBUG level to `django_debug.log`.

- **Integrate with Monitoring Tools:**
  
  Use tools like **Sentry** or **New Relic** for real-time monitoring and error tracking.

  - **Sentry Integration Example:**
    
    ```bash
    pip install sentry-sdk
    ```

    ```python
    import sentry_sdk
    from sentry_sdk.integrations.django import DjangoIntegration

    sentry_sdk.init(
        dsn="your_sentry_dsn",
        integrations=[DjangoIntegration()],
        traces_sample_rate=1.0,
        send_default_pii=True
    )
    ```

### **10.2. Continuous Integration/Continuous Deployment (CI/CD)**

- **Set Up CI/CD Pipelines:**
  
  Automate testing and deployment using platforms like **GitHub Actions** or **GitLab CI**.

  - **GitHub Actions Workflow Example:**

    ```yaml
    # .github/workflows/ci.yml
    name: CI

    on:
      push:
        branches:
          - main

    jobs:
      test:
        runs-on: ubuntu-latest
        steps:
          - name: Checkout code
            uses: actions/checkout@v2
          - name: Set up Python
            uses: actions/setup-python@v2
            with:
              python-version: '3.8'
          - name: Install dependencies
            run: |
              python -m pip install --upgrade pip
              pip install -r requirements.txt
          - name: Run tests
            run: |
              python manage.py test
    ```

  - **Explanation:**
    - **Triggers:** Runs the workflow on pushes to the `main` branch.
    - **Jobs:** Includes steps to checkout code, set up Python, install dependencies, and run tests.

### **10.3. User Role Management**

- **Define Roles and Assign Permissions:**

  ```python
  from django.contrib.auth.models import Group, Permission

  # Create groups for roles
  admin_group, created = Group.objects.get_or_create(name='Admin')
  driver_group, created = Group.objects.get_or_create(name='Driver')
  dispatcher_group, created = Group.objects.get_or_create(name='Dispatcher')

  # Assign permissions to groups as needed
  admin_permissions = Permission.objects.all()
  admin_group.permissions.set(admin_permissions)

  # Example: Assign specific permissions to the Driver group
  driver_permissions = Permission.objects.filter(codename__in=['view_shipment', 'change_shipment'])
  driver_group.permissions.set(driver_permissions)
  ```

  - **Explanation:**
    - **Groups:** Define roles such as Admin, Driver, and Dispatcher.
    - **Permissions:** Assign specific permissions to each group based on their responsibilities.

### **10.4. Notifications**

- **Real-Time Notifications Using Django Channels:**

  ```python
  # consumers.py
  from channels.generic.websocket import AsyncWebsocketConsumer
  import json

  class NotificationConsumer(AsyncWebsocketConsumer):
      async def connect(self):
          await self.channel_layer.group_add("notifications", self.channel_name)
          await self.accept()

      async def disconnect(self, close_code):
          await self.channel_layer.group_discard("notifications", self.channel_name)

      async def send_notification(self, event):
          message = event['message']
          await self.send(text_data=json.dumps({
              'message': message
          }))
  ```

  - **Explanation:**
    - **`connect` Method:** Adds the WebSocket connection to a group named "notifications".
    - **`send_notification` Method:** Sends real-time notifications to connected clients.

- **Routing Configuration:**

  ```python
  # routing.py
  from django.urls import re_path
  from .consumers import NotificationConsumer

  websocket_urlpatterns = [
      re_path(r'ws/notifications/$', NotificationConsumer.as_asgi()),
  ]
  ```

  - **Explanation:**
    - Defines the WebSocket URL for notifications.

- **ASGI Configuration:**

  ```python
  # asgi.py
  import os
  from channels.routing import ProtocolTypeRouter, URLRouter
  from django.core.asgi import get_asgi_application
  from channels.auth import AuthMiddlewareStack
  from .routing import websocket_urlpatterns

  os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'your_project.settings')

  application = ProtocolTypeRouter({
      "http": get_asgi_application(),
      "websocket": AuthMiddlewareStack(
          URLRouter(
              websocket_urlpatterns
          )
      ),
  })
  ```

  - **Explanation:**
    - Configures ASGI to handle both HTTP and WebSocket protocols.

### **10.5. Search Functionality**

- **Enhanced Search Using Django Filter Backend:**

  ```python
  from django_filters import rest_framework as filters

  class TruckFilter(filters.FilterSet):
      capacity_min = filters.NumberFilter(field_name='capacity', lookup_expr='gte')
      capacity_max = filters.NumberFilter(field_name='capacity', lookup_expr='lte')
      driver_name = filters.CharFilter(field_name='driver_name', lookup_expr='icontains')

      class Meta:
          model = Truck
          fields = ['capacity_min', 'capacity_max', 'driver_name']

  class TruckViewSet(viewsets.ModelViewSet):
      queryset = Truck.objects.all()
      serializer_class = TruckSerializer
      filter_backends = (filters.DjangoFilterBackend,)
      filterset_class = TruckFilter
  ```

  - **Explanation:**
    - **Custom Filters:** Allows filtering trucks based on capacity ranges and partial matches of driver names.

### **10.6. Pagination**

- **Implementing Pagination to Manage Large Datasets:**

  ```python
  from rest_framework.pagination import PageNumberPagination

  class StandardResultsSetPagination(PageNumberPagination):
      page_size = 10
      page_size_query_param = 'page_size'
      max_page_size = 100

  class ShipmentViewSet(viewsets.ModelViewSet):
      queryset = Shipment.objects.select_related('load', 'truck').all()
      serializer_class = ShipmentSerializer
      pagination_class = StandardResultsSetPagination
  ```

  - **Explanation:**
    - **`page_size`:** Number of records per page.
    - **`page_size_query_param`:** Allows clients to set the page size via query parameters.
    - **`max_page_size`:** Maximum allowed page size to prevent excessive data retrieval.

### **10.7. Rate Limiting**

- **Preventing API Abuse Using Django Ratelimit:**

  ```python
  from ratelimit.decorators import ratelimit
  from rest_framework import viewsets
  from .models import Shipment
  from .serializers import ShipmentSerializer

  class ShipmentViewSet(viewsets.ModelViewSet):
      queryset = Shipment.objects.all()
      serializer_class = ShipmentSerializer

      @ratelimit(key='ip', rate='5/m', method='ALL', block=True)
      def list(self, request, *args, **kwargs):
          return super().list(request, *args, **kwargs)
  ```

  - **Explanation:**
    - **`@ratelimit` Decorator:** Limits the `list` action to 5 requests per minute per IP address.
    - **`block=True`:** Automatically blocks the request if the rate limit is exceeded.

  - **Installation:**
    
    ```bash
    pip install django-ratelimit
    ```

  - **Configuration:**
    
    Add `'ratelimit'` to `INSTALLED_APPS` in `settings.py`.

### **10.8. Asynchronous Task Handling**

- **Handling Long-Running Tasks with Celery:**

  ```python
  from celery import shared_task

  @shared_task
  def send_shipment_notification(shipment_id):
      # Logic to send notification
      shipment = Shipment.objects.get(shipment_id=shipment_id)
      # Example: Send email notification
      send_mail(
          subject=f"Shipment {shipment.shipment_id} Update",
          message=f"Your shipment is now {shipment.status}.",
          from_email='noreply@lobb.com',
          recipient_list=['user@example.com'],
      )
  ```

  - **Explanation:**
    - **`@shared_task`:** Decorator to define a Celery task.
    - **Usage:** Tasks like sending notifications can be executed asynchronously, improving API response times.

  - **Setup:**
    
    - **Install Celery:**
      
      ```bash
      pip install celery
      ```

    - **Configure Celery in `settings.py`:**
      
      ```python
      CELERY_BROKER_URL = 'redis://localhost:6379/0'  # Example using Redis
      CELERY_RESULT_BACKEND = 'redis://localhost:6379/0'
      ```

    - **Initialize Celery in `your_project/celery.py`:**
      
      ```python
      import os
      from celery import Celery

      os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'your_project.settings')

      app = Celery('your_project')
      app.config_from_object('django.conf:settings', namespace='CELERY')
      app.autodiscover_tasks()
      ```

    - **Update `__init__.py` in `your_project`:**
      
      ```python
      from .celery import app as celery_app

      __all__ = ('celery_app',)
      ```

### **10.9. Geolocation Services**

- **Integrating Geolocation APIs to Track Truck Locations:**

  ```python
  import requests

  def get_truck_location(truck_id):
      response = requests.get(f"https://api.example.com/trucks/{truck_id}/location")
      if response.status_code == 200:
          return response.json()
      return None
  ```

  - **Explanation:**
    - Fetches real-time location data for a specific truck using an external geolocation API.

  - **Usage Example:**
    
    ```python
    location = get_truck_location('TRK001')
    if location:
        shipment = Shipment.objects.get(truck__truck_id='TRK001')
        shipment.current_location = location['address']
        shipment.save()
    ```

### **10.10. Data Visualization**

- **Using Libraries like Chart.js or D3.js for Data Visualization in the Admin Dashboard:**

  - **Create Endpoints to Fetch Data for Charts:**

    ```python
    from django.http import JsonResponse
    from django.db.models import Count

    def shipment_statistics(request):
        shipments = Shipment.objects.values('status').annotate(count=Count('id'))
        return JsonResponse(list(shipments), safe=False)
    ```

  - **Frontend Integration:**
    
    - **Example with Chart.js:**
      
      ```javascript
      import Chart from 'chart.js';

      fetch('/api/shipment_statistics/')
          .then(response => response.json())
          .then(data => {
              const ctx = document.getElementById('shipmentChart').getContext('2d');
              new Chart(ctx, {
                  type: 'pie',
                  data: {
                      labels: data.map(item => item.status),
                      datasets: [{
                          data: data.map(item => item.count),
                          backgroundColor: ['#FF6384', '#36A2EB', '#FFCE56', '#AAAAAA'],
                      }]
                  },
              });
          });
      ```

### **10.11. Custom Middleware**

- **Creating Custom Middleware for Logging Requests and Responses:**

  ```python
  # middleware.py
  import logging

  logger = logging.getLogger(__name__)

  class LoggingMiddleware:
      def __init__(self, get_response):
          self.get_response = get_response

      def __call__(self, request):
          # Log request data
          logger.debug(f"Request: {request.method} {request.get_full_path()} from {request.META.get('REMOTE_ADDR')}")
          
          response = self.get_response(request)
          
          # Log response data
          logger.debug(f"Response: {response.status_code} for {request.method} {request.get_full_path()}")
          
          return response
  ```

  - **Configuration:**
    
    Add the middleware to `MIDDLEWARE` in `settings.py`:

    ```python
    MIDDLEWARE = [
        ...
        'your_app.middleware.LoggingMiddleware',
        ...
    ]
    ```

  - **Explanation:**
    - Logs the HTTP method, path, and IP address for each request and the corresponding response status code.

### **10.12. API Documentation**

- **Using `drf-yasg` to Generate Swagger API Documentation:**

  - **Installation:**
    
    ```bash
    pip install drf-yasg
    ```

  - **Configuration in `settings.py`:**
    
    ```python
    INSTALLED_APPS = [
        ...
        'drf_yasg',
        ...
    ]
    ```

  - **Setup in `urls.py`:**
    
    ```python
    from drf_yasg.views import get_schema_view
    from drf_yasg import openapi
    from rest_framework import permissions

    schema_view = get_schema_view(
       openapi.Info(
          title="LOB Logistics API",
          default_version='v1',
          description="API documentation for LOBB Logistics",
          terms_of_service="https://www.yourcompany.com/terms/",
          contact=openapi.Contact(email="contact@lobb.com"),
          license=openapi.License(name="BSD License"),
       ),
       public=True,
       permission_classes=(permissions.AllowAny,),
    )

    urlpatterns += [
        path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    ]
    ```

  - **Explanation:**
    - **`drf-yasg`**: A Django Rest Framework plugin for generating Swagger/OpenAPI documentation.
    - **Accessing Documentation:** Navigate to `/swagger/` in your application to view the interactive API documentation.

### **10.13. User Registration and Login**

Implement user registration and login endpoints with email verification to manage user access.

- **Extending Django's User Model:**

  ```python
  from django.contrib.auth.models import AbstractUser
  from django.db import models

  class CustomUser(AbstractUser):
      phone_number = models.CharField(max_length=15, blank=True)
      email_verified = models.BooleanField(default=False)
      verification_token = models.CharField(max_length=100, blank=True, null=True)

      def __str__(self):
          return self.username
  ```

  - **Explanation:**
    - **`phone_number`:** Stores the user's phone number.
    - **`email_verified`:** Indicates whether the user's email has been verified.
    - **`verification_token`:** Token used for email verification.

- **Creating Serializers:**

  ```python
  from rest_framework import serializers
  from .models import CustomUser

  class UserSerializer(serializers.ModelSerializer):
      class Meta:
          model = CustomUser
          fields = ['id', 'username', 'password', 'email', 'phone_number']
          extra_kwargs = {'password': {'write_only': True}}

      def create(self, validated_data):
          user = CustomUser.objects.create_user(
              username=validated_data['username'],
              email=validated_data['email'],
              phone_number=validated_data.get('phone_number', ''),
              password=validated_data['password']
          )
          user.verification_token = generate_verification_token()
          user.save()
          send_verification_email(user)
          return user

  class LoginSerializer(serializers.Serializer):
      username = serializers.CharField()
      password = serializers.CharField(write_only=True)
  ```

  - **Explanation:**
    - **`UserSerializer`:** Handles user creation with password hashing and email verification token generation.
    - **`LoginSerializer`:** Facilitates user login by validating username and password.

- **Utility Functions:**

  ```python
  import uuid
  from django.core.mail import send_mail
  from django.conf import settings

  def generate_verification_token():
      return str(uuid.uuid4())

  def send_verification_email(user):
      subject = 'Verify your email'
      message = f'Hi {user.username},\n\nPlease verify your email by clicking the link below:\nhttp://yourdomain.com/verify/{user.verification_token}/'
      from_email = settings.DEFAULT_FROM_EMAIL
      recipient_list = [user.email]
      send_mail(subject, message, from_email, recipient_list)
  ```

  - **Explanation:**
    - **`generate_verification_token`:** Creates a unique token for email verification.
    - **`send_verification_email`:** Sends an email containing the verification link to the user.

- **Creating Views:**

  ```python
  from rest_framework import generics, status
  from rest_framework.views import APIView
  from rest_framework.response import Response
  from django.contrib.auth import authenticate
  from .serializers import UserSerializer, LoginSerializer
  from .models import CustomUser
  from .utils import send_verification_email

  class UserRegistrationView(generics.CreateAPIView):
      queryset = CustomUser.objects.all()
      serializer_class = UserSerializer

      def perform_create(self, serializer):
          serializer.save()

  class UserLoginView(APIView):
      serializer_class = LoginSerializer

      def post(self, request):
          serializer = self.serializer_class(data=request.data)
          serializer.is_valid(raise_exception=True)
          username = serializer.validated_data['username']
          password = serializer.validated_data['password']
          user = authenticate(username=username, password=password)
          if user:
              # Generate token or perform login
              return Response({'message': 'Login successful'}, status=status.HTTP_200_OK)
          return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)

  class UserLogoutView(APIView):
      def post(self, request):
          # Logic to handle user logout (e.g., deleting the token)
          return Response({'message': 'Logout successful'}, status=status.HTTP_200_OK)
  ```

  - **Explanation:**
    - **`UserRegistrationView`:** Handles user registration and sends a verification email.
    - **`UserLoginView`:** Authenticates users based on username and password.
    - **`UserLogoutView`:** Manages user logout processes.

### **10.14. File Uploads**

- **Adding a File Field to the Shipment Model:**

  *(Already included in Section 1)*

- **Handling File Uploads in the View:**

  ```python
  class ShipmentViewSet(viewsets.ModelViewSet):
      queryset = Shipment.objects.all()
      serializer_class = ShipmentSerializer

      def perform_create(self, serializer):
          serializer.save()
  ```

  - **Explanation:**
    - **`perform_create`:** Automatically saves the uploaded file associated with the shipment.

- **Configuration:**

  ```python
  # settings.py
  MEDIA_URL = '/media/'
  MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
  ```

  - **Explanation:**
    - Defines the URL and root directory for media files.

  - **URL Configuration:**

    ```python
    # your_project/urls.py
    from django.conf import settings
    from django.conf.urls.static import static

    urlpatterns = [
        path('api/', include('your_app.urls')),
    ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    ```

### **10.15. Data Encryption**

- **Encrypting Sensitive Data Using Django's Built-in Encryption:**

  ```python
  from django.db import models
  from django.core import signing

  class EncryptedField(models.TextField):
      def get_prep_value(self, value):
          return signing.dumps(value)

      def from_db_value(self, value, expression, connection):
          if value is None:
              return value
          try:
              return signing.loads(value)
          except signing.BadSignature:
              return None

  class Shipment(models.Model):
      # ... existing fields ...
      secret_notes = EncryptedField(blank=True, null=True)
  ```

  - **Explanation:**
    - **`EncryptedField`:** Custom model field that encrypts data before saving to the database and decrypts it when retrieving.
    - **Usage:** Adds a `secret_notes` field to the **Shipment** model to store sensitive information securely.

  - **Security Tip:** Ensure the `SECRET_KEY` is kept secure, as it's used for signing and encrypting data.

---

## **11. Comprehensive API Endpoints**

A well-defined set of API endpoints ensures that all functionalities are accessible and manageable.

### **11.1. User Authentication Endpoints**

- **User Registration:**

  ```python
  from rest_framework import generics
  from .serializers import UserSerializer
  from .models import CustomUser

  class UserRegistrationView(generics.CreateAPIView):
      queryset = CustomUser.objects.all()
      serializer_class = UserSerializer

      def perform_create(self, serializer):
          serializer.save()
  ```

  - **URL Configuration:**

    ```python
    # your_app/urls.py
    urlpatterns += [
        path('register/', UserRegistrationView.as_view(), name='user-registration'),
    ]
    ```

- **User Login:**

  ```python
  from rest_framework.views import APIView
  from rest_framework.response import Response
  from django.contrib.auth import authenticate
  from rest_framework import status

  class UserLoginView(APIView):
      def post(self, request):
          username = request.data.get('username')
          password = request.data.get('password')
          user = authenticate(username=username, password=password)
          if user:
              # Generate token or perform login
              return Response({'message': 'Login successful'}, status=status.HTTP_200_OK)
          return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)
  ```

  - **URL Configuration:**

    ```python
    urlpatterns += [
        path('login/', UserLoginView.as_view(), name='user-login'),
    ]
    ```

- **User Logout:**

  ```python
  class UserLogoutView(APIView):
      def post(self, request):
          # Logic to handle user logout (e.g., deleting the token)
          return Response({'message': 'Logout successful'}, status=status.HTTP_200_OK)
  ```

  - **URL Configuration:**

    ```python
    urlpatterns += [
        path('logout/', UserLogoutView.as_view(), name='user-logout'),
    ]
    ```

### **11.2. Shipment Management Endpoints**

- **Assign Load to Truck:**

  ```python
  from rest_framework.views import APIView
  from rest_framework.response import Response
  from rest_framework import status
  from .models import Load, Truck, Shipment

  def assign_load_to_truck(load_id, truck_id):
      try:
          load = Load.objects.get(load_id=load_id)
          truck = Truck.objects.get(truck_id=truck_id)
          shipment = Shipment.objects.create(load=load, truck=truck, status='Assigned')
          return shipment
      except (Load.DoesNotExist, Truck.DoesNotExist):
          return None

  class AssignLoadToTruckView(APIView):
      def post(self, request):
          load_id = request.data.get('load_id')
          truck_id = request.data.get('truck_id')
          shipment = assign_load_to_truck(load_id, truck_id)
          if shipment:
              return Response({'message': 'Load assigned successfully', 'shipment_id': shipment.shipment_id}, status=status.HTTP_201_CREATED)
          return Response({'error': 'Load or truck not found'}, status=status.HTTP_404_NOT_FOUND)
  ```

  - **URL Configuration:**

    ```python
    urlpatterns += [
        path('assign-load/', AssignLoadToTruckView.as_view(), name='assign-load'),
    ]
    ```

- **Estimate Shipment Cost:**

  ```python
  from rest_framework.views import APIView
  from rest_framework.response import Response

  def estimate_shipment_cost(weight, distance, urgency_level):
      base_cost = 50  # Base cost for shipment
      cost_per_kg = 5  # Cost per kg
      cost_per_km = 2  # Cost per km
      urgency_multiplier = 1.5 if urgency_level == 'high' else 1.0

      total_cost = (base_cost + (cost_per_kg * weight) + (cost_per_km * distance)) * urgency_multiplier
      return total_cost

  class EstimateShipmentCostView(APIView):
      def post(self, request):
          weight = request.data.get('weight')
          distance = request.data.get('distance')
          urgency_level = request.data.get('urgency_level')
          estimated_cost = estimate_shipment_cost(weight, distance, urgency_level)
          return Response({'estimated_cost': estimated_cost}, status=status.HTTP_200_OK)
  ```

  - **URL Configuration:**

    ```python
    urlpatterns += [
        path('estimate-cost/', EstimateShipmentCostView.as_view(), name='estimate-cost'),
    ]
    ```

- **Cancel Shipment:**

  ```python
  def cancel_shipment_with_policy(shipment_id):
      try:
          shipment = Shipment.objects.get(shipment_id=shipment_id)
          if shipment.status in ['Pending', 'In Transit']:
              shipment.status = 'Cancelled'
              shipment.save()
              return True
          return False
      except Shipment.DoesNotExist:
          return False

  class CancelShipmentView(APIView):
      def post(self, request, shipment_id):
          if cancel_shipment_with_policy(shipment_id):
              return Response({'message': 'Shipment cancelled successfully'}, status=status.HTTP_200_OK)
          return Response({'error': 'Cancellation not allowed for this shipment status'}, status=status.HTTP_400_BAD_REQUEST)
  ```

  - **URL Configuration:**

    ```python
    urlpatterns += [
        path('cancel/<str:shipment_id>/', CancelShipmentView.as_view(), name='cancel-shipment'),
    ]
    ```

- **Confirm Delivery:**

  ```python
  def confirm_delivery(shipment_id):
      try:
          shipment = Shipment.objects.get(shipment_id=shipment_id)
          if shipment.status == 'In Transit':
              shipment.status = 'Delivered'
              shipment.save()
              return True
          return False
      except Shipment.DoesNotExist:
          return False

  class ConfirmDeliveryView(APIView):
      def post(self, request, shipment_id):
          if confirm_delivery(shipment_id):
              return Response({'message': 'Delivery confirmed successfully'}, status=status.HTTP_200_OK)
          return Response({'error': 'Delivery confirmation failed'}, status=status.HTTP_400_BAD_REQUEST)
  ```

  - **URL Configuration:**

    ```python
    urlpatterns += [
        path('confirm-delivery/<str:shipment_id>/', ConfirmDeliveryView.as_view(), name='confirm-delivery'),
    ]
    ```

- **Track Shipment:**

  ```python
  class TrackShipmentView(APIView):
      def get(self, request, shipment_id):
          try:
              shipment = Shipment.objects.get(shipment_id=shipment_id)
              return Response({
                  'shipment_id': shipment.shipment_id,
                  'status': shipment.status,
                  'current_location': shipment.current_location
              }, status=status.HTTP_200_OK)
          except Shipment.DoesNotExist:
              return Response({'error': 'Shipment not found'}, status=status.HTTP_404_NOT_FOUND)
  ```

  - **URL Configuration:**

    ```python
    urlpatterns += [
        path('track/<str:shipment_id>/', TrackShipmentView.as_view(), name='track-shipment'),
    ]
    ```

- **Retrieve Shipment History:**

  ```python
  class ShipmentHistoryView(APIView):
      def get(self, request, shipment_id):
          history = ShipmentHistory.objects.filter(shipment__shipment_id=shipment_id).order_by('-updated_at')
          history_data = [{'status': h.status, 'updated_at': h.updated_at} for h in history]
          return Response(history_data, status=status.HTTP_200_OK)
  ```

  - **URL Configuration:**

    ```python
    urlpatterns += [
        path('history/<str:shipment_id>/', ShipmentHistoryView.as_view(), name='shipment-history'),
    ]
    ```

### **11.3. Feedback and Profile Endpoints**

- **Collect Feedback:**

  ```python
  def collect_feedback(shipment_id, user, rating, comments):
      shipment = Shipment.objects.get(shipment_id=shipment_id)
      feedback = Feedback.objects.create(shipment=shipment, user=user, rating=rating, comments=comments)
      return feedback

  class ShipmentFeedbackView(APIView):
      def post(self, request):
          shipment_id = request.data.get('shipment_id')
          user = request.user
          rating = request.data.get('rating')
          comments = request.data.get('comments')
          feedback = collect_feedback(shipment_id, user, rating, comments)
          return Response({'message': 'Feedback submitted successfully', 'feedback_id': feedback.id}, status=status.HTTP_201_CREATED)
  ```

  - **URL Configuration:**

    ```python
    urlpatterns += [
        path('feedback/', ShipmentFeedbackView.as_view(), name='shipment-feedback'),
    ]
    ```

- **User Profile Management:**

  ```python
  class UserProfileView(APIView):
      def get(self, request):
          user_profile = request.user.userprofile
          return Response({
              'address': user_profile.address,
              'phone_number': user_profile.phone_number
          }, status=status.HTTP_200_OK)

      def put(self, request):
          user_profile = request.user.userprofile
          user_profile.address = request.data.get('address', user_profile.address)
          user_profile.phone_number = request.data.get('phone_number', user_profile.phone_number)
          user_profile.save()
          return Response({'message': 'Profile updated successfully'}, status=status.HTTP_200_OK)
  ```

  - **URL Configuration:**

    ```python
    urlpatterns += [
        path('profile/', UserProfileView.as_view(), name='user-profile'),
    ]
    ```

---

## **12. Conclusion**

By following this comprehensive guide, you can establish a robust and scalable backend system for **LOB Logistics** using Django. The structured approach covers essential components like models, serializers, viewsets, and URLs, along with advanced features that enhance performance, security, and user experience. Implementing these best practices ensures that the application can efficiently manage logistics operations while being adaptable to future growth and evolving business needs.

### **Key Takeaways:**

- **Modular Design:** Organize your code into clear, modular sections for maintainability.
  
- **Security:** Implement authentication, permissions, and rate limiting to secure your API.
  
- **Performance:** Optimize database queries and use caching to enhance performance.
  
- **Scalability:** Design your system to handle growth, both in data volume and feature set.
  
- **User Experience:** Provide comprehensive endpoints and real-time updates to facilitate a seamless experience for users.

### **Final Notes:**

- **Avoiding Duplication:** Ensure that each API endpoint is defined only once to prevent conflicts and maintain clarity.
  
- **Documentation:** Maintain up-to-date API documentation to facilitate collaboration between backend and frontend developers and to aid in future maintenance.
  
- **Continuous Improvement:** Regularly monitor, test, and update your backend to adapt to new requirements and technologies.

By adhering to these guidelines and utilizing the structured approach provided, you can develop a robust backend system tailored to the logistics management needs of **LOB Logistics**.

---