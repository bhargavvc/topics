Certainly! Each SOLID principle leverages various OOP concepts such as inheritance, polymorphism, encapsulation, abstraction, and composition to guide design decisions. Below, each principle is discussed in detail, outlining the relevant OOP techniques and providing illustrative code examples.

---

## 1. Single Responsibility Principle (SRP)

**SRP**: A class should have only one reason to change, meaning one responsibility.

**OOP Concepts Used**:
- **Encapsulation**: Group related data and behavior in one class.
- **Separation of Concerns**: Using multiple classes to handle distinct responsibilities.
- **Composition/Delegation**: Composing complex behavior by delegating tasks to specialized classes.

**Methods to Achieve SRP**:
- **Separate Classes**: Create distinct classes for different responsibilities.
- **Delegation**: A class can delegate tasks to other classes, each handling a single responsibility.

**Example**:
```python
# Responsibility: Managing user data persistence
class UserRepository:
    def save_user(self, user):
        # Save user to database
        print(f"User {user} saved to database.")

# Responsibility: Handling email sending
class EmailService:
    def send_email(self, user):
        # Send an email to user
        print(f"Email sent to {user}.")

# Usage demonstrating separation of responsibilities
user_repo = UserRepository()
email_service = EmailService()

user_repo.save_user("Alice")
email_service.send_email("Alice")
```
**Explanation**: 
- **Encapsulation**: `UserRepository` and `EmailService` encapsulate specific responsibilities.
- By separating concerns, each class has only one reason to change.

---

## 2. Open/Closed Principle (OCP)

**OCP**: A class should be open for extension but closed for modification.

**OOP Concepts Used**:
- **Inheritance**: Extend behavior through subclassing.
- **Polymorphism**: Override or implement methods in subclasses.
- **Abstraction**: Define abstract base classes (interfaces) to enforce a contract.

**Methods to Achieve OCP**:
- **Abstract Classes/Interfaces**: Define abstract methods that subclasses implement.
- **Subclassing**: Extend existing functionality without altering existing code.

**Example**:
```python
from abc import ABC, abstractmethod

# Abstraction: Shape provides a common interface
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

# Inheritance & Polymorphism: Specific shapes implement the interface
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

# Extending functionality without modifying existing code
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
- **Abstraction**: `Shape` is an abstract class providing a template.
- **Inheritance/Polymorphism**: `Circle`, `Rectangle`, and `Triangle` extend `Shape` and override `area`.
- Adding a new shape (`Triangle`) extends functionality without modifying existing code.

---

## 3. Liskov Substitution Principle (LSP)

**LSP**: Subtypes must be substitutable for their base types without altering program correctness.

**OOP Concepts Used**:
- **Inheritance**: Subclasses extend base classes.
- **Polymorphism**: Substituting subclass objects where base class objects are expected.

**Methods to Achieve LSP**:
- **Correct Overriding**: Ensure overridden methods behave consistently with the base class's contract.
- **Design by Contract**: Base class defines expectations that subclasses must honor.

**Example**:
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

# Usage: Substituting subclasses without altering expected behavior
def make_bird_move(bird: Bird):
    bird.move()

birds = [Sparrow(), Penguin()]
for bird in birds:
    make_bird_move(bird)
```
**Explanation**:
- **Inheritance/Polymorphism**: `Sparrow` and `Penguin` are substitutable for `Bird`.
- Both subclasses implement `move` without violating expectations of what a `Bird` should do, preserving LSP.

---

## 4. Interface Segregation Principle (ISP)

**ISP**: Clients should not be forced to depend on interfaces they do not use.

**OOP Concepts Used**:
- **Abstraction**: Define small, specific interfaces.
- **Polymorphism**: Classes implement only the interfaces they need.

**Methods to Achieve ISP**:
- **Smaller Interfaces**: Split large interfaces into smaller ones.
- **Selective Implementation**: Classes implement only relevant interfaces.

**Example**:
```python
from abc import ABC, abstractmethod

# Smaller, specific interfaces
class Printer(ABC):
    @abstractmethod
    def print(self):
        pass

class Scanner(ABC):
    @abstractmethod
    def scan(self):
        pass

# Implements both Printer and Scanner
class AllInOnePrinter(Printer, Scanner):
    def print(self):
        return "Printing document..."

    def scan(self):
        return "Scanning document..."

# Implements only Printer
class SimplePrinter(Printer):
    def print(self):
        return "Printing document..."

# Usage
printer = SimplePrinter()
print(printer.print())
```
**Explanation**:
- **Abstraction**: `Printer` and `Scanner` interfaces are separate.
- **Polymorphism**: `SimplePrinter` implements only the interface it needs.
- By splitting interfaces, classes aren't forced to implement unnecessary methods.

---

## 5. Dependency Inversion Principle (DIP)

**DIP**: High-level modules should not depend on low-level modules. Both should depend on abstractions.

**OOP Concepts Used**:
- **Abstraction**: Depend on interfaces/abstract classes.
- **Polymorphism**: Swap implementations through polymorphic behavior.
- **Dependency Injection (a form of composition)**: Inject dependencies rather than creating them inside classes.

**Methods to Achieve DIP**:
- **Use Abstract Interfaces**: High-level modules interact with abstractions.
- **Inject Dependencies**: Provide dependencies from the outside (constructor injection, setter injection).

**Example**:
```python
from abc import ABC, abstractmethod

# Abstraction defining contract for notifications
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

# High-level module depends on abstraction
class NotificationManager:
    def __init__(self, service: NotificationService):
        self.service = service  # Dependency Injection

    def notify(self, message):
        self.service.send(message)

# Usage: injecting different implementations without altering NotificationManager
email_service = EmailNotification()
sms_service = SMSNotification()

manager = NotificationManager(email_service)  # Using EmailNotification
manager.notify("This is an email notification.")

manager = NotificationManager(sms_service)   # Using SMSNotification
manager.notify("This is an SMS notification.")
```
**Explanation**:
- **Abstraction/Polymorphism**: `NotificationService` is an abstraction; `EmailNotification` and `SMSNotification` implement it.
- **Dependency Injection**: `NotificationManager` receives its dependency via the constructor, not creating it internally.
- This allows `NotificationManager` to work with any `NotificationService` implementation, adhering to DIP.

---

### Summary of OOP Concepts in SOLID Principles

- **SRP**: Uses encapsulation, separation of concerns, composition, and delegation.
- **OCP**: Relies on inheritance, polymorphism, and abstraction to extend behavior without modification.
- **LSP**: Requires correct use of inheritance and polymorphism to ensure subclass substitutability.
- **ISP**: Uses abstraction to create small interfaces and polymorphism to implement only what's needed.
- **DIP**: Depends on abstraction, polymorphism, and composition (through dependency injection) to decouple high-level and low-level modules.

Each SOLID principle leverages various facets of OOP to achieve cleaner, more maintainable, and scalable designs. The provided examples illustrate how these principles can be implemented using inheritance, abstraction, polymorphism, encapsulation, and composition.