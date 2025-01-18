Here’s a refined set of **most frequently asked OOPs interview questions** with **real-world relevance** for backend development roles. These questions are designed to test both theoretical understanding and practical application:

---

### **1. What is Object-Oriented Programming (OOP) and why is it important?**
- **Key Concept**: OOP is a programming paradigm based on the concept of "objects," which encapsulate data and behavior.
- **Relevance**: 
  - Used in frameworks like Django, Spring, and others.
  - Encourages modular and reusable code, which is essential for backend systems.
- **Example**:
  - An e-commerce application where `Product`, `User`, and `Order` are modeled as objects.

---

### **2. Explain the Four Pillars of OOP (Abstraction, Encapsulation, Inheritance, Polymorphism)**
- **Abstraction**:
  - Hiding complex implementation details and exposing only essential features.
  - **Example**: A database interface in a backend system abstracts raw SQL queries.
- **Encapsulation**:
  - Bundling data and methods together and restricting access using access modifiers.
  - **Example**: Securing user data in a class by using private variables.
- **Inheritance**:
  - Enables reusability by allowing a class to derive from another.
  - **Example**: A `BaseController` class with shared methods inherited by multiple API controllers.
- **Polymorphism**:
  - Allows objects to take on many forms (method overloading and overriding).
  - **Example**: A payment gateway interface that supports `CreditCardPayment`, `PayPalPayment`, etc.

---

### **3. What is a Class and an Object? How do they relate in backend systems?**
- **Class**: A blueprint or template for creating objects.
- **Object**: An instance of a class containing actual data.
- **Relevance**:
  - A `User` class in a backend system could model fields like `username` and `email`.
  - An object of `User` represents an individual user instance.

---

### **4. What is the difference between Method Overloading and Method Overriding?**
- **Method Overloading**:
  - Multiple methods in the same class with the same name but different parameters.
  - **Example**: A logging utility with methods to log messages or exceptions.
- **Method Overriding**:
  - Redefining a method in a child class that exists in the parent class.
  - **Example**: Customizing an authentication mechanism by overriding the `login` method.

---

### **5. What is the difference between an Interface and an Abstract Class?**
- **Abstract Class**:
  - Can have both abstract (undefined) and concrete (defined) methods.
  - Used when classes share common behavior.
- **Interface**:
  - All methods are abstract by default (no implementation).
  - Used for defining contracts between unrelated classes.
- **Relevance**:
  - In backend systems, `AbstractRepository` can define common methods for database operations, while interfaces like `PaymentGateway` define the structure for payment processing classes.

---

### **6. What is the use of a Constructor in a Class?**
- **Explanation**:
  - A constructor initializes an object's state when it is created.
  - **Example**: Initializing a database connection in the `DatabaseConnection` class constructor.

---

### **7. How is Polymorphism used in real-world backend systems?**
- **Explanation**:
  - Enables designing systems where the exact behavior of a method depends on the runtime object.
  - **Example**:
    - A `Notification` class with subclasses like `EmailNotification` and `SMSNotification`. The `send` method behaves differently depending on the subclass.

---


---

### **9. What is Dependency Injection, and how is it related to OOP?**
- **Explanation**:
  - A design pattern that provides objects their dependencies rather than creating them internally.
  - **Example**: Injecting a `Logger` service into a `UserService` class.
- **Relevance**:
  - Used in frameworks like Spring and dependency injection containers like Python's `dependency-injector`.

---

### **10. How does Encapsulation help in API security?**
- **Explanation**:
  - Encapsulation hides sensitive data and exposes only necessary information.
  - **Example**:
    - An `Account` class with a private field `__balance` and public methods for controlled access.

---

### **11. What is the difference between Composition and Inheritance? When would you prefer one over the other?**
- **Composition**:
  - A "has-a" relationship where one class contains another.
  - **Example**: A `Car` class has a `Engine` object.
- **Inheritance**:
  - An "is-a" relationship where a class derives from another.
  - **Example**: `Car` is a subclass of `Vehicle`.
- **Relevance**:
  - Prefer composition when you want greater flexibility and reusability.

---

### **12. How does Python implement Access Modifiers (Public, Protected, Private)?**
- **Explanation**:
  - Public: No underscore prefix (`variable`).
  - Protected: Single underscore prefix (`_variable`).
  - Private: Double underscore prefix (`__variable`).
- **Example**:
  ```python
  class User:
      def __init__(self):
          self._protected = "Protected"
          self.__private = "Private"

  user = User()
  print(user._protected)  # Accessible
  print(user.__private)   # AttributeError
  ```

---

### **13. What is a Singleton Pattern? How is it implemented in Python?**
- **Explanation**:
  - Ensures that a class has only one instance.
  - **Relevance**:
    - Used for logging, configuration, or database connections in backend systems.
  - **Example**:
    ```python
    class Singleton:
        _instance = None

        def __new__(cls, *args, **kwargs):
            if not cls._instance:
                cls._instance = super(Singleton, cls).__new__(cls, *args, **kwargs)
            return cls._instance
    ```

---

### **14. How are Exceptions handled in OOP, and why are they important for backend development?**
- **Explanation**:
  - Exceptions provide a mechanism to handle runtime errors gracefully.
  - **Relevance**:
    - Prevent application crashes in backend systems.
  - **Example**:
    ```python
    try:
        # Perform database operation
        result = 10 / 0
    except ZeroDivisionError as e:
        print(f"Error occurred: {e}")
    ```

---

### **15. How is Data Abstraction implemented in real-world applications?**
- **Explanation**:
  - Abstract classes and interfaces define a high-level blueprint, hiding implementation details.
  - **Example**:
    - A `PaymentProcessor` interface defines methods like `process_payment()` implemented by specific classes like `StripeProcessor` and `PayPalProcessor`.

---

### **Real-World Scenarios for Backend Systems:**
1. **Authentication System**:
   - Encapsulation: Restrict access to password storage.
   - Polymorphism: Different authentication mechanisms (`OAuth`, `JWT`, etc.).
2. **Microservices Architecture**:
   - Dependency Injection: Injecting services like logging and database connectors.
3. **REST API Development**:
   - Abstraction: Expose only necessary methods in the API layer.

---

Master these questions and their applications in real-world backend development scenarios to be fully prepared for interviews. Let me know if you'd like to dive deeper into any specific topic!


Here are additional frequently asked **OOPs interview questions** for backend development roles, focusing on **real-world use cases** and practical relevance:

---

### **16. What is the difference between Abstract Classes and Concrete Classes?**
- **Abstract Classes**:
  - Cannot be instantiated.
  - Used as a blueprint for other classes.
  - **Example**:
    ```python
    from abc import ABC, abstractmethod

    class PaymentGateway(ABC):
        @abstractmethod
        def process_payment(self, amount):
            pass

    class StripeGateway(PaymentGateway):
        def process_payment(self, amount):
            print(f"Processing ${amount} via Stripe")
    ```
- **Concrete Classes**:
  - Can be instantiated directly.
  - Fully implemented methods.

---

### **17. How does Polymorphism support extensibility in backend systems?**
- **Explanation**:
  - Polymorphism allows backend systems to define a common interface for multiple implementations.
  - **Example**:
    - A `Serializer` interface for converting objects to JSON or XML:
    ```python
    class Serializer:
        def serialize(self, data):
            pass

    class JsonSerializer(Serializer):
        def serialize(self, data):
            import json
            return json.dumps(data)

    class XmlSerializer(Serializer):
        def serialize(self, data):
            return f"<data>{data}</data>"
    ```

---

### **18. What is the difference between "is-a" and "has-a" relationships?**
- **"is-a" Relationship**:
  - Implemented using **inheritance**.
  - **Example**: A `Dog` is an `Animal`.
- **"has-a" Relationship**:
  - Implemented using **composition**.
  - **Example**: A `Car` has an `Engine`.

---

### **19. What is the difference between Aggregation and Composition?**
- **Aggregation**:
  - A weak association where the lifecycle of objects is independent.
  - **Example**: A `Department` can exist independently of a `Teacher`.
- **Composition**:
  - A strong association where the lifecycle of objects is dependent.
  - **Example**: A `Car` cannot exist without an `Engine`.

---

### **20. How do you handle multithreading in OOP for backend systems?**
- **Explanation**:
  - Backend systems often handle multithreading for concurrency.
  - Threads can be implemented using Python's `threading` module.
- **Example**:
  ```python
  import threading

  def process_data():
      print("Processing data...")

  thread = threading.Thread(target=process_data)
  thread.start()
  thread.join()
  ```

---

### **21. What is the difference between Static and Dynamic Polymorphism?**
- **Static Polymorphism**:
  - Achieved through method overloading.
  - Resolved at compile-time.
- **Dynamic Polymorphism**:
  - Achieved through method overriding.
  - Resolved at runtime.

---

### **22. What is the role of the `super` keyword in OOP?**
- **Explanation**:
  - Used to call the parent class’s methods or constructors.
  - **Example**:
    ```python
    class Parent:
        def greet(self):
            print("Hello from Parent")

    class Child(Parent):
        def greet(self):
            super().greet()
            print("Hello from Child")

    obj = Child()
    obj.greet()
    ```

---

### **23. What is the Singleton Design Pattern, and where is it used in backend systems?**
- **Explanation**:
  - Ensures a class has only one instance.
  - **Use Case**:
    - Database connections, configuration files, or logging systems.
  - **Example**:
    ```python
    class Singleton:
        _instance = None

        def __new__(cls, *args, **kwargs):
            if not cls._instance:
                cls._instance = super().__new__(cls, *args, **kwargs)
            return cls._instance
    ```

---

### **24. What is the difference between Exception Handling and Error Handling?**
- **Exception Handling**:
  - Handles runtime exceptions using `try`, `catch` (or `except` in Python).
- **Error Handling**:
  - Refers to preventing or dealing with anticipated errors.
  - Includes validation, logging, and fallbacks.

---

### **25. How does OOP support database modeling in backend systems?**
- **Explanation**:
  - Classes map directly to database tables in Object-Relational Mapping (ORM).
  - **Example**:
    - In Django:
      ```python
      class User(models.Model):
          username = models.CharField(max_length=255)
          email = models.EmailField()
      ```

---

### **26. What is the Factory Design Pattern, and how is it applied in backend systems?**
- **Explanation**:
  - Creates objects without specifying the exact class to instantiate.
  - **Example**:
    ```python
    class PaymentFactory:
        @staticmethod
        def get_payment_processor(payment_type):
            if payment_type == "Stripe":
                return StripeGateway()
            elif payment_type == "PayPal":
                return PayPalGateway()
    ```

---

### **27. How is data encapsulation implemented in Python?**
- **Explanation**:
  - Restrict access to data using private (`__`) and protected (`_`) attributes.
  - **Example**:
    ```python
    class Account:
        def __init__(self):
            self.__balance = 0  # Private

        def deposit(self, amount):
            if amount > 0:
                self.__balance += amount
                print(f"Balance: {self.__balance}")
    ```

---

### **28. What is a Virtual Function?**
- **Explanation**:
  - A virtual function is defined in a parent class and overridden in a child class.
  - Ensures dynamic method resolution.

---

### **29. What is Dependency Inversion Principle (DIP)?**
- **Explanation**:
  - High-level modules should not depend on low-level modules but on abstractions.
  - **Example**:
    ```python
    class Database:
        def save(self, data):
            pass

    class MySQLDatabase(Database):
        def save(self, data):
            print("Saving data in MySQL")

    class UserService:
        def __init__(self, db: Database):
            self.db = db

        def save_user(self, user):
            self.db.save(user)

    db = MySQLDatabase()
    service = UserService(db)
    service.save_user("John")
    ```

---

### **30. What is the difference between Multithreading and Multiprocessing in backend systems?**
- **Multithreading**:
  - Multiple threads share the same memory space.
  - Ideal for I/O-bound tasks.
- **Multiprocessing**:
  - Processes have separate memory spaces.
  - Ideal for CPU-bound tasks.

---

### **31. How is the Observer Pattern used in real-world backend systems?**
- **Explanation**:
  - Notifies dependent objects of changes in state.
  - **Example**:
    - Event-driven systems where observers listen for changes, like stock updates.

---

### **32. What is Late Binding in OOP?**
- **Explanation**:
  - Method calls are resolved at runtime.
  - **Example**:
    - Polymorphism: The exact method to be executed is determined dynamically.

---

### **33. What are Access Modifiers and their importance in backend systems?**
- **Explanation**:
  - Control the visibility of class members.
  - **Private**: Restricted to the class.
  - **Protected**: Accessible to subclasses.
  - **Public**: Accessible everywhere.

---

### **34. What is a Decorator Pattern, and how is it useful in backend systems?**
- **Explanation**:
  - Adds functionality to objects dynamically.
  - **Example**:
    ```python
    def authentication_required(func):
        def wrapper(*args, **kwargs):
            print("Authenticating user...")
            return func(*args, **kwargs)
        return wrapper

    @authentication_required
    def get_data():
        print("Fetching data...")

    get_data()
    ```

---

### **35. What is the role of Interfaces in API development?**
- **Explanation**:
  - Interfaces define contracts for classes implementing APIs.
  - **Example**:
    - A `Serializer` interface for defining methods `to_json` and `to_xml`.

---

Mastering these **real-world OOP concepts** with their applications ensures readiness for backend development interviews. Let me know if you need further explanations or hands-on examples!

Here’s the next set of **real-world OOP interview questions**, tailored for backend development scenarios:

---

### **36. What is the difference between Deep Copy and Shallow Copy in OOP?**
- **Shallow Copy**:
  - Creates a new object but references the same nested objects.
  - **Example**:
    ```python
    import copy
    original = {"key": [1, 2, 3]}
    shallow = copy.copy(original)
    shallow["key"].append(4)
    print(original)  # {'key': [1, 2, 3, 4]}
    ```
- **Deep Copy**:
  - Recursively copies all objects to create a completely independent object.
  - **Example**:
    ```python
    deep = copy.deepcopy(original)
    deep["key"].append(5)
    print(original)  # {'key': [1, 2, 3, 4]}
    print(deep)      # {'key': [1, 2, 3, 4, 5]}
    ```

---

### **37. What is the Builder Design Pattern?**
- **Explanation**:
  - Separates the construction of a complex object from its representation.
  - **Example**:
    ```python
    class CarBuilder:
        def __init__(self):
            self.car = {}

        def add_engine(self, engine):
            self.car["engine"] = engine
            return self

        def add_color(self, color):
            self.car["color"] = color
            return self

        def build(self):
            return self.car

    car = CarBuilder().add_engine("V8").add_color("Red").build()
    print(car)  # {'engine': 'V8', 'color': 'Red'}
    ```

---

### **38. What is the difference between Association, Aggregation, and Composition?**
- **Association**:
  - A relationship between two objects, but they can exist independently.
  - **Example**: A `Teacher` and a `Student` can exist independently of each other.
- **Aggregation**:
  - A weak relationship where the contained object can exist independently.
  - **Example**: A `Department` contains `Teachers`, but teachers can exist without the department.
- **Composition**:
  - A strong relationship where the contained object cannot exist without the container.
  - **Example**: A `Car` contains an `Engine`. Without the car, the engine is meaningless.

---

### **39. How do you implement Polymorphism in Python?**
- **Explanation**:
  - Polymorphism allows a single interface to be used for different types.
  - **Example**:
    ```python
    class Bird:
        def make_sound(self):
            pass

    class Sparrow(Bird):
        def make_sound(self):
            print("Chirp Chirp")

    class Duck(Bird):
        def make_sound(self):
            print("Quack Quack")

    birds = [Sparrow(), Duck()]
    for bird in birds:
        bird.make_sound()
    ```

---

### **40. What is the Adapter Pattern?**
- **Explanation**:
  - Allows incompatible interfaces to work together.
  - **Example**:
    - Adapting a legacy payment system to a new interface:
    ```python
    class OldPaymentSystem:
        def process_old_payment(self, amount):
            print(f"Processing payment of {amount} in the old system.")

    class NewPaymentSystem:
        def __init__(self, old_system):
            self.old_system = old_system

        def process_payment(self, amount):
            self.old_system.process_old_payment(amount)

    adapter = NewPaymentSystem(OldPaymentSystem())
    adapter.process_payment(100)
    ```

---

### **41. What is Duck Typing, and how is it used in Python?**
- **Explanation**:
  - In Python, the type of an object is determined by its behavior rather than its class.
  - **Example**:
    ```python
    class Dog:
        def speak(self):
            return "Woof"

    class Cat:
        def speak(self):
            return "Meow"

    def animal_sound(animal):
        print(animal.speak())

    animal_sound(Dog())  # Woof
    animal_sound(Cat())  # Meow
    ```

---

### **42. How does the Observer Pattern work in real-world applications?**
- **Explanation**:
  - Used to notify multiple objects when a state change occurs.
  - **Use Case**:
    - Notification systems (e.g., email and SMS notifications when an order is placed).
  - **Example**:
    ```python
    class Observer:
        def update(self, message):
            pass

    class EmailNotifier(Observer):
        def update(self, message):
            print(f"Email: {message}")

    class SMSNotifier(Observer):
        def update(self, message):
            print(f"SMS: {message}")

    class Subject:
        def __init__(self):
            self.observers = []

        def register(self, observer):
            self.observers.append(observer)

        def notify_all(self, message):
            for observer in self.observers:
                observer.update(message)

    subject = Subject()
    subject.register(EmailNotifier())
    subject.register(SMSNotifier())
    subject.notify_all("Order Placed!")
    ```

---

### **43. What is the Open/Closed Principle (OCP) in OOP?**
- **Explanation**:
  - Classes should be open for extension but closed for modification.
  - **Example**:
    - Instead of modifying a class to add new behavior, extend it:
    ```python
    class Logger:
        def log(self, message):
            pass

    class FileLogger(Logger):
        def log(self, message):
            print(f"Logging to file: {message}")

    class DatabaseLogger(Logger):
        def log(self, message):
            print(f"Logging to database: {message}")

    def log_message(logger, message):
        logger.log(message)

    log_message(FileLogger(), "File log message")
    log_message(DatabaseLogger(), "Database log message")
    ```

---

### **44. How is the Proxy Pattern used in backend development?**
- **Explanation**:
  - Provides a surrogate or placeholder to control access to an object.
  - **Use Case**:
    - Proxying access to a remote service or controlling access to expensive objects.
  - **Example**:
    ```python
    class RealService:
        def fetch_data(self):
            print("Fetching data from the real service")

    class ProxyService:
        def __init__(self):
            self.real_service = None

        def fetch_data(self):
            if not self.real_service:
                self.real_service = RealService()
            print("Accessing via Proxy")
            self.real_service.fetch_data()

    proxy = ProxyService()
    proxy.fetch_data()
    ```

---

### **45. What is Method Resolution Order (MRO) in Python?**
- **Explanation**:
  - Defines the order in which methods are resolved when multiple inheritance is used.
  - **Example**:
    ```python
    class A:
        def show(self):
            print("A")

    class B(A):
        def show(self):
            print("B")

    class C(A):
        def show(self):
            print("C")

    class D(B, C):
        pass

    obj = D()
    obj.show()  # Output: B (as B is before C in the order)
    print(D.mro())  # Shows the resolution order
    ```

---

### **46. What is the difference between `is` and `==` in Python?**
- **`is`**:
  - Compares object identity (memory location).
  - **`==`**:
  - Compares object value.
  - **Example**:
    ```python
    a = [1, 2, 3]
    b = [1, 2, 3]
    print(a == b)  # True (same value)
    print(a is b)  # False (different memory location)
    ```

---

### **47. How are Design Patterns like Strategy used in backend systems?**
- **Explanation**:
  - Defines a family of algorithms and makes them interchangeable.
  - **Example**:
    ```python
    class PaymentStrategy:
        def pay(self, amount):
            pass

    class CreditCardPayment(PaymentStrategy):
        def pay(self, amount):
            print(f"Paying ${amount} using Credit Card.")

    class PayPalPayment(PaymentStrategy):
        def pay(self, amount):
            print(f"Paying ${amount} using PayPal.")

    payment = CreditCardPayment()
    payment.pay(100)
    ```

---

### **48. What is the difference between Class Methods and Static Methods?**
- **Class Method**:
  - Bound to the class, not the instance.
  - **Static Method**:
  - Independent of class or instance.
  - **Example**:
    ```python
    class MyClass:
        @classmethod
        def class_method(cls):
            print("Class method")

        @staticmethod
        def static_method():
            print("Static method")

    MyClass.class_method()
    MyClass.static_method()
    ```

---

Let me know if you'd like explanations on additional questions!

Here’s a new set of **OOPs interview questions**, focusing on advanced concepts and practical scenarios that are relevant for backend systems and interviews for senior roles:

---

### **49. What is Multiple Inheritance, and how does Python handle it?**
- **Explanation**:
  - Multiple inheritance allows a class to inherit from more than one parent class.
  - Python resolves method calls using **Method Resolution Order (MRO)** with the **C3 Linearization Algorithm**.
- **Example**:
    ```python
    class A:
        def show(self):
            print("A")

    class B:
        def show(self):
            print("B")

    class C(A, B):
        pass

    obj = C()
    obj.show()  # Output: A (based on MRO)
    print(C.mro())  # [C, A, B, object]
    ```

---

### **50. What is the difference between Abstract Classes and Interfaces in Python?**
- **Abstract Classes**:
  - Can have both concrete (implemented) and abstract (unimplemented) methods.
  - Use `abc` module in Python.
- **Interfaces**:
  - In Python, interfaces are not a separate feature but can be emulated using abstract classes with only abstract methods.
- **Example**:
    ```python
    from abc import ABC, abstractmethod

    class AbstractRepository(ABC):
        @abstractmethod
        def save(self, data):
            pass

    class DatabaseRepository(AbstractRepository):
        def save(self, data):
            print("Saving to database:", data)
    ```

---

### **51. What is a Metaclass in Python?**
- **Explanation**:
  - A metaclass is a class of a class that defines how classes behave.
  - **Use Case**:
    - Used to enforce rules or modify class behavior during creation.
- **Example**:
    ```python
    class Meta(type):
        def __new__(cls, name, bases, dct):
            print(f"Creating class: {name}")
            return super().__new__(cls, name, bases, dct)

    class MyClass(metaclass=Meta):
        pass
    ```

---

### **52. What is the difference between Composition and Aggregation?**
- **Composition**:
  - Strong relationship, contained objects cannot exist independently.
- **Aggregation**:
  - Weak relationship, contained objects can exist independently.
- **Example**:
    ```python
    class Engine:
        pass

    class Car:
        def __init__(self):
            self.engine = Engine()  # Composition (Car owns Engine)

    class Department:
        def __init__(self, teacher):
            self.teacher = teacher  # Aggregation (Teacher exists independently)
    ```

---

### **53. What is the Command Design Pattern?**
- **Explanation**:
  - Encapsulates a request as an object, allowing parameterization of requests and queuing.
- **Use Case**:
  - Undo/Redo operations in backend systems.
- **Example**:
    ```python
    class Command:
        def execute(self):
            pass

    class PrintCommand(Command):
        def __init__(self, message):
            self.message = message

        def execute(self):
            print(self.message)

    command = PrintCommand("Hello, World!")
    command.execute()
    ```

---

### **54. What is the Template Method Pattern?**
- **Explanation**:
  - Defines the skeleton of an algorithm in a base class and lets subclasses implement specific steps.
- **Example**:
    ```python
    from abc import ABC, abstractmethod

    class DataParser(ABC):
        def parse_data(self):
            self.read_data()
            self.process_data()

        @abstractmethod
        def read_data(self):
            pass

        @abstractmethod
        def process_data(self):
            pass

    class JsonParser(DataParser):
        def read_data(self):
            print("Reading JSON data")

        def process_data(self):
            print("Processing JSON data")

    parser = JsonParser()
    parser.parse_data()
    ```

---

### **55. What is the Flyweight Pattern?**
- **Explanation**:
  - Reduces memory usage by sharing common data among multiple objects.
- **Use Case**:
  - Managing objects with shared states, like user sessions.
- **Example**:
    ```python
    class FlyweightFactory:
        _instances = {}

        @staticmethod
        def get_instance(key):
            if key not in FlyweightFactory._instances:
                FlyweightFactory._instances[key] = key
            return FlyweightFactory._instances[key]

    obj1 = FlyweightFactory.get_instance("Shared")
    obj2 = FlyweightFactory.get_instance("Shared")
    print(obj1 is obj2)  # True
    ```

---

### **56. What is the difference between `staticmethod`, `classmethod`, and instance methods?**
- **Instance Method**:
  - Operates on an instance of the class.
  - Takes `self` as the first parameter.
- **Class Method**:
  - Operates on the class itself.
  - Takes `cls` as the first parameter.
  - Use `@classmethod` decorator.
- **Static Method**:
  - Does not depend on class or instance.
  - Use `@staticmethod` decorator.
- **Example**:
    ```python
    class Example:
        def instance_method(self):
            print("Instance Method")

        @classmethod
        def class_method(cls):
            print("Class Method")

        @staticmethod
        def static_method():
            print("Static Method")

    obj = Example()
    obj.instance_method()
    Example.class_method()
    Example.static_method()
    ```

---

### **57. What is the Mediator Pattern?**
- **Explanation**:
  - Centralizes communication between objects.
  - **Use Case**:
    - Chat applications where the mediator manages message delivery between users.
- **Example**:
    ```python
    class Mediator:
        def notify(self, sender, event):
            pass

    class User:
        def __init__(self, name, mediator):
            self.name = name
            self.mediator = mediator

        def send_message(self, message):
            self.mediator.notify(self, message)

    class ChatMediator(Mediator):
        def notify(self, sender, message):
            print(f"{sender.name} says: {message}")

    mediator = ChatMediator()
    user1 = User("Alice", mediator)
    user2 = User("Bob", mediator)

    user1.send_message("Hello Bob!")
    ```

---

### **58. How does Python handle garbage collection?**
- **Explanation**:
  - Python uses reference counting and a cyclic garbage collector to free unused objects.
- **Example**:
    ```python
    import gc

    class Example:
        pass

    obj = Example()
    print(gc.isenabled())  # True
    del obj
    ```

---

### **59. What is the Decorator Pattern, and how is it used in Python?**
- **Explanation**:
  - Dynamically adds behavior to objects.
  - **Use Case**:
    - Adding logging, authentication, or caching.
  - **Example**:
    ```python
    def logging_decorator(func):
        def wrapper(*args, **kwargs):
            print(f"Calling {func.__name__}")
            return func(*args, **kwargs)
        return wrapper

    @logging_decorator
    def process_data():
        print("Processing data")

    process_data()
    ```

---

### **60. What is the Visitor Pattern?**
- **Explanation**:
  - Separates algorithms from objects on which they operate.
  - **Use Case**:
    - Performing operations on hierarchical data structures.
  - **Example**:
    ```python
    class Visitor:
        def visit(self, element):
            pass

    class ConcreteVisitor(Visitor):
        def visit(self, element):
            print(f"Visiting {element.name}")

    class Element:
        def __init__(self, name):
            self.name = name

        def accept(self, visitor):
            visitor.visit(self)

    element = Element("Node1")
    visitor = ConcreteVisitor()
    element.accept(visitor)
    ```

---
