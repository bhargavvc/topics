 
## **Commonly Used Top 10 Patterns in Orderwise**

Based on the image, the design patterns are ranked in terms of their **common usage in real-world applications**.
 
### **Ranked Order of the Patterns**

1. **[Singleton Pattern](https://github.com/bhargavvc/topics/tree/main/design-patterns/singleton)**  
   - **Usage**: Global configurations, database connections, caching, logging.  
   - **Why Important**: Ensures one instance of a class is created, controlling access to shared resources.

2. **[Factory Pattern](https://github.com/bhargavvc/topics/tree/main/design-patterns/factory)**  
   - **Usage**: Dependency Injection frameworks (e.g., Spring), dynamic object creation in frameworks or APIs.  
   - **Why Important**: Decouples object creation logic, improving scalability and flexibility.

3. **[Observer Pattern](https://github.com/bhargavvc/topics/tree/main/design-patterns/observer)**  
   - **Usage**: Event-driven systems like real-time notifications, messaging queues, and UI listeners.  
   - **Why Important**: Efficiently manages dependencies by notifying subscribers of state changes.

4. **[Strategy Pattern](https://github.com/bhargavvc/topics/tree/main/design-patterns/strategy)**  
   - **Usage**: Implementing algorithms or business rules that vary at runtime (e.g., payment gateways, tax calculations).  
   - **Why Important**: Promotes open-closed principle by encapsulating interchangeable algorithms.

5. **[Builder Pattern](https://github.com/bhargavvc/topics/tree/main/design-patterns/builder)**  
   - **Usage**: Creating complex objects step-by-step like configurations, documents, and UI elements.  
   - **Why Important**: Helps manage the construction of objects with multiple optional components.

6. **[Decorator Pattern](https://github.com/bhargavvc/topics/tree/main/design-patterns/decorator)**  
   - **Usage**: Extending behavior dynamically, such as adding features to GUI components or middleware in web frameworks.  
   - **Why Important**: Provides an alternative to subclassing by dynamically extending an object’s functionality.

7. **[Adapter Pattern](https://github.com/bhargavvc/topics/tree/main/design-patterns/adapter)**  
   - **Usage**: Bridging incompatible interfaces, such as integrating legacy systems or third-party libraries.  
   - **Why Important**: Acts as a translator to enable compatibility between different systems.

8. **[Facade Pattern](https://github.com/bhargavvc/topics/tree/main/design-patterns/facade)**  
   - **Usage**: Simplifying interactions with complex systems, such as providing a unified API for microservices.  
   - **Why Important**: Hides complexities and provides a simpler interface to clients.

---

### **Categorization of Patterns**

#### **Creational Patterns**
**[Singleton Pattern](https://github.com/bhargavvc/topics/tree/main/design-patterns/singleton)**|**[Factory Pattern](https://github.com/bhargavvc/topics/tree/main/design-patterns/factory)**|**[Builder Pattern](https://github.com/bhargavvc/topics/tree/main/design-patterns/builder)**  

- **Why Important**: These patterns are foundational in enterprise systems for managing object creation in a scalable and flexible way.

---

#### **Structural Patterns**
**[Decorator Pattern](https://github.com/bhargavvc/topics/tree/main/design-patterns/decorator)**|**[Adapter Pattern](https://github.com/bhargavvc/topics/tree/main/design-patterns/adapter)**|**[Facade Pattern](https://github.com/bhargavvc/topics/tree/main/design-patterns/facade)**, 

- **Why Important**: Crucial for building maintainable and modular systems, especially when integrating legacy systems or working with complex architectures.

---

#### **Behavioral Patterns**
**[Observer Pattern](https://github.com/bhargavvc/topics/tree/main/design-patterns/observer)**|**[Strategy Pattern](https://github.com/bhargavvc/topics/tree/main/design-patterns/strategy)**  

- **Why Important**: Key for managing dynamic and event-driven systems, enabling objects to collaborate and adapt at runtime.

---

**Understanding the Common Structure in Design Patterns**

---

Many design patterns involve defining interfaces or abstract classes, creating concrete implementations, and then using these implementations in client code. This structure facilitates flexibility, extensibility, and maintainability in software design.

However, while this is a common theme, it is not a blueprint for **all** design patterns. Design patterns are general reusable solutions to common problems in software design. They are not one-size-fits-all templates but rather guidelines that can be adapted to specific contexts.

---

### **Why Interfaces and Abstract Classes are Common**

In object-oriented programming (OOP), interfaces and abstract classes are fundamental tools that promote:

- **Abstraction:** Hiding complex implementation details behind simple interfaces.
- **Encapsulation:** Bundling data with methods that operate on that data.
- **Polymorphism:** Allowing different classes to be treated as instances of the same class through a common interface.
- **Loose Coupling:** Reducing dependencies between components.

Many design patterns leverage these principles to achieve their goals. For example:

- **Factory Patterns:** Use interfaces to define objects that can be created without specifying the exact class.
- **Strategy Pattern:** Encapsulates algorithms behind interfaces, allowing them to be interchangeable.
- **Decorator Pattern:** Uses interfaces to wrap objects and add behavior dynamically.

---

### **Not All Design Patterns Follow the Same Structure**

While interfaces and client calls are prevalent, not all design patterns rely on them in the same way. Some patterns focus on different aspects of software design:

1. **Singleton Pattern:**

   - **Purpose:** Ensures a class has only one instance and provides a global point of access to it.
   - **Structure:** Involves a class that self-manages its instance, without necessarily using interfaces.

   ```python
   # singleton.py
   class Singleton:
       _instance = None

       def __new__(cls):
           if cls._instance is None:
               cls._instance = super(Singleton, cls).__new__(cls)
           return cls._instance
   ```

2. **Observer Pattern:**

   - **Purpose:** Defines a one-to-many dependency between objects so that when one object changes state, all its dependents are notified.
   - **Structure:** May use interfaces for observers, but the focus is on the communication between subjects and observers.

3. **Iterator Pattern:**

   - **Purpose:** Provides a way to access the elements of an aggregate object sequentially without exposing its underlying representation.
   - **Structure:** Often relies on a specific interface, but the key is the traversal mechanism.

4. **Prototype Pattern:**

   - **Purpose:** Creates new objects by cloning existing ones.
   - **Structure:** Centers around object cloning rather than interface implementation.

---

### **Design Patterns Categorized**

Design patterns are typically categorized into three groups:

1. **Creational Patterns:**

   - **Focus:** Object creation mechanisms.
   - **Examples:** Singleton, Factory Method, Abstract Factory, Builder, Prototype.
   - **Observation:** Often involve interfaces or abstract classes to define the types of objects to create.

2. **Structural Patterns:**

   - **Focus:** Composition of classes and objects to form larger structures.
   - **Examples:** Adapter, Decorator, Facade, Composite, Bridge, Flyweight, Proxy.
   - **Observation:** Frequently use interfaces to define how components fit together, but some, like Facade, might simplify interfaces rather than define new ones.

3. **Behavioral Patterns:**

   - **Focus:** Communication between objects.
   - **Examples:** Observer, Strategy, Command, Iterator, Mediator, Memento, State, Visitor.
   - **Observation:** Emphasize algorithms and object interaction, sometimes without needing interfaces.

---

### **Interfaces vs. Implementation**

While interfaces (or abstract base classes in Python) are a common tool to achieve abstraction and polymorphism, they are not the defining characteristic of all design patterns.

- **Purpose Over Structure:** The essence of a design pattern lies in the problem it solves, not just in its structural components.
- **Flexibility in Implementation:** Design patterns can be implemented in various ways, depending on the programming language and specific requirements.
- **Python's Dynamic Typing:** In Python, due to its dynamic typing and duck typing, strict interfaces are less common than in statically typed languages like Java or C++. Python relies more on protocols and less on formal interfaces.

---

### **Examples Without Explicit Interfaces**

**1. Singleton in Python:**

   ```python
   # singleton.py
   class DatabaseConnection:
       _instance = None

       def __new__(cls):
           if cls._instance is None:
               cls._instance = super(DatabaseConnection, cls).__new__(cls)
               # Initialize the instance
           return cls._instance
   ```

   - **Explanation:** There's no interface or abstract class; the pattern ensures a single instance.

**2. Chain of Responsibility Pattern:**

   - **Purpose:** Passes a request along a chain of handlers.
   - **Implementation:** Handlers are linked, and each decides whether to handle the request or pass it along.
   - **Structure:** May not require interfaces, especially in dynamically typed languages.

   ```python
   # chain_of_responsibility.py
   class Handler:
       def __init__(self, successor=None):
           self.successor = successor

       def handle(self, request):
           handled = self._handle(request)
           if not handled and self.successor:
               self.successor.handle(request)

       def _handle(self, request):
           raise NotImplementedError("Must provide implementation in subclass")
   ```

**3. Memento Pattern:**

   - **Purpose:** Captures and restores an object's internal state.
   - **Implementation:** Involves storing state without necessarily using interfaces.

---

### **Understanding the Blueprint**

While it's tempting to look for a unifying blueprint among design patterns, it's important to recognize that:

- **Design Patterns are Solutions:** Each pattern addresses a specific design problem and provides a solution that can be adapted.
- **Common Principles:** Patterns often share common OOP principles (e.g., abstraction, encapsulation), but their implementations can differ significantly.
- **Not One-Size-Fits-All:** Relying solely on interfaces and classes does not capture the diversity and nuance of design patterns.

---

### **Why Interfaces are Common**

- **Language Influence:** In statically typed languages like Java and C#, interfaces are a primary means of achieving abstraction and polymorphism.
- **Design for Extension:** Interfaces allow for components to be extended or replaced without modifying existing code.
- **Dependency Inversion Principle:** Depend upon abstractions, not concretions.

---

### **In Python's Context**

- **Dynamic Typing:** Python's flexibility reduces the need for formal interfaces.
- **Duck Typing:** "If it looks like a duck and quacks like a duck, it's a duck." This allows objects to be used interchangeably if they have the required methods.
- **Abstract Base Classes (ABCs):** Python provides `abc` module for defining abstract base classes, but they are not as commonly used as interfaces in other languages.

---

### **Conclusion**

Your observation highlights a common pattern in OOP design, where interfaces and classes play crucial roles in structuring code and enabling flexibility. However, design patterns are more about the relationships and interactions between objects to solve specific problems rather than adhering to a strict structural blueprint.

- **Not All Patterns Use Interfaces:** While interfaces are prevalent, some patterns focus on object composition, delegation, or other principles without relying heavily on interfaces.
- **Adaptability:** The beauty of design patterns lies in their adaptability to different programming paradigms and languages.
- **Focus on Principles:** Understanding the underlying principles and intents of design patterns is more valuable than looking for structural similarities.

---

### **Further Exploration**

- **Study Different Patterns:** Examine patterns like **Singleton**, **Memento**, or **Mediator**, which may not emphasize interfaces.
- **Understand the Problem Domain:** Focus on the specific problems each pattern aims to solve and how they achieve it.
- **Language-Specific Implementations:** Recognize how different languages may influence the implementation of patterns.

---

**Remember:** Design patterns are tools in your software design toolkit. They provide proven solutions but should be applied judiciously, considering the specific needs and constraints of your project.