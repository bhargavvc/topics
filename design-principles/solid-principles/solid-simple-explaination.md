
---

### 📚 Index Page

1. [**SOLID Principles Detailed Explanation with Examples**](#1-solid-principles)
    - [1.1 Single Responsibility Principle (SRP)](#11-single-responsibility-principle-srp)
    - [1.2 Open Closed Principle (OCP)](#12-open-closed-principle-ocp)
    - [1.3 Liskov Substitution Principle (LSP)](#13-liskov-substitution-principle-lsp)
    - [1.4 Interface Segregation Principle (ISP)](#14-interface-segregation-principle-isp)
    - [1.5 Dependency Inversion Principle (DIP)](#15-dependency-inversion-principle-dip)

2. [**Comprehensive Guide to SOLID Principles with OOP Context and Code Examples**](#comprehensive-guide-to-solid-principles-with-oop-context-and-code-examples)
    - [What are SOLID Principles?](#what-are-solid-principles)
    - [Relation Between SOLID Principles and OOP Concepts](#relation-between-solid-principles-and-oop-concepts)
    - [Key Differences Between OOP and SOLID Principles](#key-differences-between-oop-and-solid-principles)
    - [SOLID Principles Explained with Simple Code Examples](#solid-principles-explained-with-simple-code-examples)
        - [Single Responsibility Principle (SRP)](#solid-single-responsibility-principle-srp)
        - [Open/Closed Principle (OCP)](#solid-openclosed-principle-ocp)
        - [Liskov Substitution Principle (LSP)](#solid-liskov-substitution-principle-lsp)
        - [Interface Segregation Principle (ISP)](#solid-interface-segregation-principle-isp)
        - [Dependency Inversion Principle (DIP)](#solid-dependency-inversion-principle-dip)
    - [Conclusion](#conclusion)
    - [Comparison Between OOP and SOLID](#comparison-between-oop-and-solid)

---

**Overview**
1. **Single Responsibility Principle (SRP)**: Ensures each class has one clear purpose.
2. **Open/Closed Principle (OCP)**: Enables adding new functionality without modifying existing code.
3. **Liskov Substitution Principle (LSP)**: Ensures subclasses can be used interchangeably with their base class.
4. **Interface Segregation Principle (ISP)**: Prevents forcing classes to implement unnecessary methods.
5. **Dependency Inversion Principle (DIP)**: Emphasizes dependency on abstractions rather than concrete implementations.
# ocp and lsp are looks liek similar but ocp u can extend base clas fucntioncality without chnaging the code 
# but lsp is about subclasses can  replace thier parent classes 


## Part 1: Detailed SOLID Principles with Examples

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

**Example**:
```python
class Report:
    def __init__(self, title, content):
        self.title = title
        self.content = content

    def generate_report(self):
        return f"Title: {self.title}\nContent: {self.content}"

# Separate class for handling file operations
class FileHandler:
    @staticmethod
    def save_to_file(report, filename):
        with open(filename, 'w') as file:
            file.write(report)

# Usage
report = Report("Monthly Report", "This is the content of the report.")
generated_report = report.generate_report()
FileHandler.save_to_file(generated_report, "report.txt")
```

**Explanation**:
- **Report** handles report generation.
- **FileHandler** handles file operations. This separation ensures each class has a single responsibility.


---

#### **1.2 Open Closed Principle (OCP)**
*A class should be open for extension but closed for modification.*

- **Why?** You shouldn't modify existing code to add new functionality—it can introduce bugs.
- **Analogy:** Adding a new type of masala doesnt change the food quantify.
- **Hint:** You have to Use on Abstract Class and abstarct method in other classes 

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

**Example**:
```python
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

# Adding a new shape (Triangle) without modifying existing code
class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return 0.5 * self.base * self.height

# Usage
shapes = [Circle(5), Rectangle(4, 6), Triangle(3, 4)]
for shape in shapes:
    print(f"Area: {shape.area()}")
```

**Explanation**:
- Adding new shapes like **Triangle** doesn't require modifying existing classes, adhering to the OCP.



---

#### **1.3 Liskov Substitution Principle (LSP)**
*Subtypes must be substitutable for their base types.*

- **Why?** A derived class should fit into a program without breaking it.
- **Analogy:** a door key can be used to open Villa and small room.
- **Hint:** You need to use Base class and  function and function response can be override but still dont chnaeg the existing functionality

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

**Example**:
```python
class Bird:
    def fly(self):
        return "I can fly!"

class Sparrow(Bird):
    pass

class Penguin(Bird):
    def fly(self):
        return "I can't fly, but I can swim!"

# Usage
birds = [Sparrow(), Penguin()]
for bird in birds:
    print(bird.fly())
```

**Explanation**:
- Subclasses like **Penguin** override the `fly` method but still conform to the **Bird** interface, ensuring substitutability.

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

**Example**:
```python
from abc import ABC, abstractmethod

class Printer(ABC):
    @abstractmethod
    def print(self):
        pass

class Scanner(ABC):
    @abstractmethod
    def scan(self):
        pass

class AllInOnePrinter(Printer, Scanner):
    def print(self):
        return "Printing document..."

    def scan(self):
        return "Scanning document..."

class SimplePrinter(Printer):
    def print(self):
        return "Printing document..."

# Usage
printer = SimplePrinter()
print(printer.print())
```

**Explanation**:
- **SimplePrinter** only implements the **Printer** interface without being forced to implement **Scanner**.


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


**Example**:
```python
from abc import ABC, abstractmethod

class NotificationService(ABC):
    @abstractmethod
    def send(self, message):
        pass

class EmailNotification(NotificationService):
    def send(self, message):
        print(f"Sending Email: {message}")

class SMSNotification(NotificationService):
    def send(self, message):
        print(f"Sending SMS: {message}")

class NotificationManager:
    def __init__(self, service: NotificationService):
        self.service = service

    def notify(self, message):
        self.service.send(message)

# Usage
email_service = EmailNotification()
sms_service = SMSNotification()

manager = NotificationManager(email_service)
manager.notify("This is an email notification.")

manager = NotificationManager(sms_service)
manager.notify("This is an SMS notification.")
```

**Explanation**:
- **NotificationManager** depends on the abstraction **NotificationService** rather than concrete implementations, enabling flexibility.


---

## Part 2: Comprehensive Guide to SOLID Principles with OOP Context and Code Examples

### **What are SOLID Principles?**

SOLID principles are **guidelines for object-oriented design** that improve code maintainability, scalability, and readability. They serve as practical recommendations to ensure a clean and robust implementation of Object-Oriented Programming (OOP).

---

### **Relation Between SOLID Principles and OOP Concepts**

| **OOP Concept**         | **Related SOLID Principle**               | **Explanation**                                                                                                          |
|-------------------------|-------------------------------------------|--------------------------------------------------------------------------------------------------------------------------|
| **Encapsulation**       | Single Responsibility Principle (SRP)     | SRP enforces that a class should have one responsibility, aligning with encapsulating related behavior and data.        |
| **Inheritance**         | Liskov Substitution Principle (LSP)       | LSP ensures subclasses can replace their base classes without altering behavior, supporting proper inheritance.          |
| **Polymorphism**        | Open/Closed Principle (OCP), ISP          | OCP supports extending functionality without modifying existing code, while ISP ensures interfaces are appropriately specific. |
| **Abstraction**         | Dependency Inversion Principle (DIP)      | DIP emphasizes relying on abstractions (interfaces) instead of concrete implementations, directly leveraging abstraction. |

---

### **Key Differences Between OOP and SOLID Principles**

1. **OOP Concepts**:
   - Provide the **theoretical foundation** for object-oriented design.
   - Focus on **how to structure code** using classes, objects, inheritance, polymorphism, etc.
   - Example: Use inheritance to share behavior between classes.

2. **SOLID Principles**:
   - Provide **practical guidelines** for better OOP implementation.
   - Focus on **avoiding pitfalls** like tightly coupled, rigid, or overly complex systems.
   - Example: Ensure a class has a single responsibility (SRP) or depend on abstractions, not implementations (DIP).
 
  
### **Comparison Between OOP and SOLID**

| **Aspect**      | **OOP**                                        | **SOLID**                                                      |
|-----------------|------------------------------------------------|----------------------------------------------------------------|
| **Focus**       | Theoretical foundation for designing systems.  | Practical guidelines to write maintainable OOP code.           |
| **Scope**       | General structure of classes and objects.      | Specific strategies to avoid design issues.                    |
| **Examples**    | Encapsulation, Inheritance, Polymorphism.      | SRP, OCP, LSP, ISP, DIP.                                        |

By combining **OOP** with **SOLID**, you can achieve maintainable, scalable, and testable systems that adhere to the best coding practices.