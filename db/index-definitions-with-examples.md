# Index Definitions with Examples

## Navigation
1. [Overview of Indexes](#overview-of-indexes)  
2. **Types of Indexes**  
   - [Primary Index](#primary-index-implicit-index-on-primary-key)  
   - [Unique Index](#unique-index)  
   - [Single-Column Index](#single-column-index)  
   - [Multi-Column (Composite) Index](#multi-column-composite-index)  
   - [Partial Index](#partial-index)  
   - [GIN (Generalized Inverted Index)](#gin-generalized-inverted-index-for-full-text-search)  
   - [BTREE Index (Default)](#btree-index-default)  
   - [Hash Index](#hash-index)  
3. [Real-World Use Cases](#real-world-use-cases)  
   - [E-commerce: Filtering by Category and Price](#1-e-commerce-website-filtering-products-by-category-and-price)  
   - [Social Media: Searching Posts by Keywords](#2-social-media-searching-posts-with-keywords)  
   - [Banking: Transactions by Date and Account](#3-banking-system-transactions-by-date-and-account)  
   - [Healthcare: Active Patients by Last Name](#4-healthcare-system-active-patients-by-last-name)  
   - [Ride-Sharing: Searching Rides by Location](#5-ride-sharing-app-searching-rides-by-location)  
   - [Inventory Management: Tracking Low Stock Items](#6-inventory-management-tracking-low-stock-items)  
   - [Analytics: Aggregations by Time](#7-analytics-platform-aggregations-by-time)  

---

## Overview of Indexes

An **index** is a database structure that improves the speed of data retrieval operations. In Django with PostgreSQL, you can define indexes in models to optimize database queries, such as filtering, sorting, or joining data. However, indexes have trade-offs, such as additional storage and slower write operations.

---

## Types of Indexes with Definitions and Implementations

### 1. Primary Index (Implicit Index on Primary Key)  
- **Definition**: Automatically created for the primary key field in a table. Ensures fast lookups by primary key.
- **Usage Example**: Retrieving a user by their `id`.

   **Django Implementation**:
   ```python
   from django.db import models

   class User(models.Model):
       id = models.AutoField(primary_key=True)  # Primary index automatically created
       name = models.CharField(max_length=100)
       email = models.EmailField(unique=True)

    # fetch record using get method get(id=1)

   ```
 

---

### 2. Unique Index  
- **Definition**: Ensures all values in a column or group of columns are unique. Automatically indexed by default.
- **Usage Example**: Ensuring unique email addresses in the `User` model.

   **Django Implementation**:
   ```python
   class User(models.Model):
       email = models.EmailField(unique=True)  # Creates a unique index

    # fetch record using get method
   ```
---

### 3. Single-Column Index  
- **Definition**: Created on a single column to speed up queries filtering by that column.
- **Usage Example**: Frequently querying users by their `name`.

   **Django Implementation**:
   ```python
   class User(models.Model):
       name = models.CharField(max_length=100, db_index=True)  # Explicit single-column index
   ```

   **Real-World Usage**:  
   - Querying by indexed field:  
     ```python
     users = User.objects.filter(name="Alice")
     ```

---

### 4. Multi-Column (Composite) Index  
- **Definition**: Index created on multiple fields to speed up queries involving those fields together.
- **Usage Example**: Searching users by both `name` and `email`.

   **Django Implementation**:
   ```python
   from django.db.models import Index

   class User(models.Model):
       name = models.CharField(max_length=100)
       email = models.EmailField(unique=True)

       class Meta:
           indexes = [
               Index(fields=["name", "email"]),  # Composite index
           ]
   ```

   **Real-World Usage**:  
   - Querying using both indexed fields:  
     ```python
     users = User.objects.filter(name="Alice", email="alice@example.com")
     ```

---

### 5. Partial Index  
- **Definition**: Index created on a subset of rows based on a condition.  
  Example: Index only users who are active.
- **Usage Example**: Filtering active users in a large dataset.

   **Django Implementation**:
   ```python
   from django.contrib.postgres.indexes import Index
   from django.db.models import Q

   class User(models.Model):
       name = models.CharField(max_length=100)
       is_active = models.BooleanField(default=True)

       class Meta:
           indexes = [
               Index(fields=["name"], condition=Q(is_active=True)),  # Partial index
           ]
   ```

   **Real-World Usage**:  
   - Querying active users:
     ```python
     users = User.objects.filter(is_active=True, name="Alice")
     ```

---

### 6. GIN (Generalized Inverted Index) for Full-Text Search  
- **Definition**: Index for efficiently searching text fields.
- **Usage Example**: Searching for keywords in a `description` field.

   **Django Implementation**:
   ```python
   from django.contrib.postgres.search import SearchVector
   from django.db.models import Index
   from django.contrib.postgres.indexes import GinIndex

   class Article(models.Model):
       title = models.CharField(max_length=200)
       description = models.TextField()

       class Meta:
           indexes = [
               GinIndex(fields=["description"]),  # GIN index for full-text search
           ]
   ```

   **Real-World Usage**:  
   - Full-text search:
     ```python
     from django.contrib.postgres.search import SearchQuery

     query = SearchQuery("Django")
     articles = Article.objects.annotate(search=SearchVector("description")).filter(search=query)
     ```

---

### 7. BTREE Index (Default)  
- **Definition**: Default index type in PostgreSQL, useful for equality and range queries.
- **Usage Example**: Querying or sorting a `created_at` timestamp.

   **Django Implementation**:
   ```python
   class User(models.Model):
       created_at = models.DateTimeField(auto_now_add=True, db_index=True)  # BTREE index
   ```

   **Real-World Usage**:  
   - Querying and ordering:  
     ```python
     users = User.objects.filter(created_at__year=2024).order_by("created_at")
     ```

---

### 8. Hash Index  
- **Definition**: Index type optimized for equality comparisons. Less commonly used due to limited functionality.
- **Usage Example**: Indexing a field used only in equality comparisons, e.g., `user_id_hash`.

   **Django Implementation**: Currently, Django does not natively support hash indexes, but you can use a custom migration to implement one.

---

## Real-World Use Cases

### 1. E-commerce Website: Filtering Products by Category and Price
#### Problem:
A product catalog allows filtering by category and price range.

#### Implementation:
```python
from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=255)
    category = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    is_available = models.BooleanField(default=True)

    class Meta:
        indexes = [
            models.Index(fields=["category", "price"]),  # Composite index
            models.Index(fields=["is_available"]),  # Single-column index
        ]
```

#### Query Example:
```python
# Retrieve products in a category with a price range and availability
products = Product.objects.filter(category="Electronics", price__lt=500, is_available=True)
```

#### Real-World Impact:
- **Without indexes**: Filtering through millions of rows can take seconds.
- **With indexes**: Composite index on `category` and `price` ensures the database efficiently narrows down the results, reducing query time.

---

### 2. Social Media: Searching Posts with Keywords
#### Problem:
Users need to search posts based on keywords in the `content` field.

#### Implementation:
```python
class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        indexes = [
            GinIndex(fields=["content"]),  # GIN index for full-text search
        ]
```

#### Query Example:
```python
# Search for posts containing the keyword "Django"
query = SearchQuery("Django")
posts = Post.objects.annotate(search=SearchVector("content")).filter(search=query)
```

#### Real-World Impact:
- **Without indexes**: Scanning the `content` field for every row takes significant time.
- **With GIN index**: Full-text search becomes almost instantaneous.

---

### 3. Banking System: Transactions by Date and Account
#### Problem:
Retrieve all transactions for a user’s account within a specific date range.

#### Implementation:
```python
class Transaction(models.Model):
    account_number = models.CharField(max_length=20)
    amount = models.DecimalField(max_digits=12, decimal_places=2)
    transaction_date = models.DateTimeField()
    transaction_type = models.CharField(max_length=10, choices=[("credit", "Credit"), ("debit", "Debit")])

    class Meta:
        indexes = [
            models.Index(fields=["account_number", "transaction_date"]),  # Composite index
            models.Index(fields=["transaction_type"]),  # Single-column index
        ]
```

#### Query Example:
```python
# Get transactions for a specific account in the last 30 days
transactions = Transaction.objects.filter(
    account_number="1234567890",
    transaction_date__range=(start_date, datetime.now())
)
```

#### Real-World Impact:
- **Without indexes**: Query takes longer to scan rows for matching account numbers and dates.
- **With indexes**: Composite index improves performance for range queries.

---

### 4. Healthcare System: Active Patients by Last Name
#### Problem:
Doctors need a list of active patients whose last names start with a given letter.

#### Implementation:
```python
class Patient(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)

    class Meta:
        indexes = [
            models.Index(fields=["last_name", "is_active"]),  # Composite index
        ]
```

#### Query Example:
```python
# Get active patients whose last names start with "A"
patients = Patient.objects.filter(last_name__startswith="A", is_active=True)
```

#### Real-World Impact:
- **Without indexes**: Searching by last name and filtering active patients would take a long time with millions of rows.
- **With indexes**: The query is optimized by using the composite index.

---

### 5. Ride-Sharing App: Searching Rides by Location
#### Problem:
Matching users to rides based on pickup and drop-off locations.

#### Implementation:
```python
class Ride(models.Model):
    pickup_location = models.PointField()  # GeoDjango point field
    dropoff_location = models.PointField()
    driver = models.CharField(max_length=100)

    class Meta:
        indexes = [
            models.Index(fields=["pickup_location"]),  # Index for geospatial queries
            models.Index(fields=["dropoff_location"]),
        ]
```

#### Query Example:
```python
# Get rides near a given location within 10 km
user_location = Point(77.5946, 12.9716)  # Example coordinates (Bangalore)
rides = Ride.objects.annotate(distance=Distance("pickup_location", user_location)).filter(distance__lte=10000)
```

#### Real-World Impact:
- **Without indexes**: Geospatial queries could take minutes to process.
- **With indexes**: Geospatial indexes make location-based filtering and distance calculations much faster.

---

### 6. Inventory Management: Tracking Low Stock Items
#### Problem:
Managers need a list of items with stock below a threshold.

#### Implementation:
```python
class Inventory(models.Model):
    item_name = models.CharField(max_length=255)
    stock = models.PositiveIntegerField()

    class Meta:
        indexes = [
            models.Index(fields=["stock"]),  # Single-column index
        ]
```

#### Query Example:
```python
# Get items with stock below 10
low_stock_items = Inventory.objects.filter(stock__lt=10)
```

#### Real-World Impact:
- **Without indexes**: The database must scan the entire table.
- **With indexes**: Queries for low-stock items are significantly faster.

---

### 7. Analytics Platform: Aggregations by Time
#### Problem:
Daily user activity reports require aggregating actions by `created_at`.

#### Implementation:
```python
class UserAction(models.Model):
    user_id = models.CharField(max_length=100)
    action_type = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        indexes = [
            models.Index(fields=["created_at"]),  # Single-column index for time-based queries
        ]
```

#### Query Example:
```python
# Count user actions per day
daily_actions = UserAction.objects.extra({
    "day": "DATE(created_at)"
}).values("day").annotate(action_count=Count("id"))
```

#### Real-World Impact:
- **Without indexes**: Query time grows with the size of the dataset.
- **With indexes**: Aggregations by date become feasible for large datasets.

---

### Key Metrics for Real-World Performance
- **Query Execution Time**: Measure before and after adding indexes using Django’s query profiler or PostgreSQL `EXPLAIN ANALYZE`.
- **Disk Space Usage**: Monitor storage overhead introduced by indexes.
- **Write Performance**: Test insert/update speeds to assess the trade-offs.

---

This structured approach provides a comprehensive overview of index definitions, implementations, and real-world use cases, making it easier to understand their importance in database optimization.
