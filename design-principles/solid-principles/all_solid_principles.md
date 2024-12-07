Here’s an in-depth explanation of each design principle with examples and code where relevant. Each principle is explained with a real-world analogy, reasoning, and corresponding Python code examples.

---

### 1. **SOLID Principles**

#### **1.1 Single Responsibility Principle (SRP)**
*A class should have only one reason to change.*

- **Why?** A class doing multiple things becomes hard to maintain and test.
- **Analogy:** A chef should cook, not fix plumbing. If a chef is also a plumber, both activities will interfere with each other.

**Example (Without SRP):**
```python
class UserManager:
    def save_user(self, user):
        # Save user to database
        pass

    def send_email(self, user):
        # Send an email to user
        pass
```
**Problem:** This class handles both persistence and email, violating SRP.

**Example (With SRP):**
```python
class UserRepository:
    def save_user(self, user):
        # Save user to database
        pass

class EmailService:
    def send_email(self, user):
        # Send an email to user
        pass
```

---

#### **1.2 Open Closed Principle (OCP)**
*A class should be open for extension but closed for modification.*

- **Why?** You shouldn't modify existing code to add new functionality—it can introduce bugs.
- **Analogy:** Adding a new topping to a pizza shouldn’t require changing how the base is prepared.

**Example (Without OCP):**
```python
class Invoice:
    def calculate_total(self, type):
        if type == "regular":
            return 100
        elif type == "discounted":
            return 80
```
**Problem:** Adding a new type requires modifying the `calculate_total` method.

**Example (With OCP):**
```python
class Invoice:
    def calculate_total(self):
        pass

class RegularInvoice(Invoice):
    def calculate_total(self):
        return 100

class DiscountedInvoice(Invoice):
    def calculate_total(self):
        return 80
```
Now you can add new invoice types without changing existing code.

---

#### **1.3 Liskov Substitution Principle (LSP)**
*Subtypes must be substitutable for their base types.*

- **Why?** A derived class should fit into a program without breaking it.
- **Analogy:** A car key can be used to start both a sedan and a sports car, regardless of their differences.

**Example (Without LSP):**
```python
class Bird:
    def fly(self):
        pass

class Penguin(Bird):
    def fly(self):
        raise Exception("Penguins can't fly")
```
**Problem:** `Penguin` violates LSP because it breaks the `fly` behavior.

**Example (With LSP):**
```python
class Bird:
    def move(self):
        pass

class Sparrow(Bird):
    def move(self):
        print("Flying")

class Penguin(Bird):
    def move(self):
        print("Swimming")
```

---

#### **1.4 Interface Segregation Principle (ISP)**
*Clients should not be forced to depend on interfaces they do not use.*

- **Why?** Large interfaces make implementing classes unnecessarily complex.
- **Analogy:** A driver doesn’t need to know how the engine works to drive a car.

**Example (Without ISP):**
```python
class Vehicle:
    def start_engine(self):
        pass

    def fly(self):
        pass

class Car(Vehicle):
    def start_engine(self):
        print("Engine started")

    def fly(self):
        raise Exception("Cars can't fly")
```
**Problem:** Cars are forced to implement `fly`, which they don’t need.

**Example (With ISP):**
```python
class Drivable:
    def start_engine(self):
        pass

class Flyable:
    def fly(self):
        pass

class Car(Drivable):
    def start_engine(self):
        print("Engine started")

class Airplane(Drivable, Flyable):
    def start_engine(self):
        print("Engine started")

    def fly(self):
        print("Flying")
```

---

#### **1.5 Dependency Inversion Principle (DIP)**
*Depend on abstractions, not concrete implementations.*

- **Why?** Reduces coupling and makes code more flexible.
- **Analogy:** A TV remote should work with different TV brands.

**Example (Without DIP):**
```python
class MySQLDatabase:
    def connect(self):
        pass

class Application:
    def __init__(self):
        self.db = MySQLDatabase()  # Tight coupling
```
**Example (With DIP):**
```python
class Database:
    def connect(self):
        pass

class MySQLDatabase(Database):
    def connect(self):
        print("Connecting to MySQL")

class Application:
    def __init__(self, db: Database):
        self.db = db
```
Now you can switch to another database (e.g., PostgreSQL) without changing `Application`.
 