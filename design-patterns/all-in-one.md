Here’s a **detailed explanation of Design Patterns** as showcased in the chart, divided into three major categories: **Creational Patterns**, **Structural Patterns**, and **Behavioral Patterns**. I will explain each pattern in-depth with its purpose, how it works, UML explanation, and real-world examples.

---

### **1. Creational Patterns**
Creational patterns focus on how objects are created. These patterns abstract the object creation process to make the system more flexible and reusable.

---

#### **1.1 Singleton**
- **Definition**: Ensures that a class has only **one instance** and provides a global point of access to it.
- **Purpose**:
  - Prevent multiple instances of a class.
  - Useful for managing shared resources like logging, database connections, or configuration files.
- **How It Works**:
  - The constructor is private.
  - A static method provides access to the instance.
- **Example**:
  - **Logger Class**: Ensures a single instance of the logger to record application logs.

---

#### **1.2 Factory Method**
- **Definition**: Defines an interface for creating objects, but allows **subclasses to decide** which class to instantiate.
- **Purpose**:
  - Promotes loose coupling by removing direct object instantiation.
- **How It Works**:
  - A factory method in a base class delegates the instantiation to derived classes.
- **Example**:
  - **Shape Factory**: Returns instances of `Circle`, `Rectangle`, or `Square` based on user input.

---

#### **1.3 Builder**
- **Definition**: Separates the construction of a complex object from its representation.
- **Purpose**:
  - Simplifies the creation of complex objects.
- **How It Works**:
  - Use a step-by-step process (a `Builder` class) to construct an object.
- **Example**:
  - **Building a House**: Step-by-step construction includes building walls, roof, and plumbing.

---

#### **1.4 Prototype**
- **Definition**: Creates objects by copying an existing object, called a prototype.
- **Purpose**:
  - Avoids the cost of creating objects from scratch.
- **How It Works**:
  - Implements a `clone()` method.
- **Example**:
  - **Document Templates**: Copy existing templates for new documents.

---

#### **1.5 Abstract Factory**
- **Definition**: Provides an interface for creating families of related or dependent objects.
- **Purpose**:
  - Ensures related objects are used together.
- **How It Works**:
  - Returns factories that can create related objects.
- **Example**:
  - **UI Themes**: A factory that creates `DarkThemeButton` and `DarkThemeTextField`.

---

### **2. Structural Patterns**
Structural patterns deal with how objects and classes are composed to form larger structures.

---

#### **2.1 Adapter**
- **Definition**: Converts an interface of a class into another interface that the client expects.
- **Purpose**:
  - Bridges incompatibilities between two interfaces.
- **How It Works**:
  - Implements a wrapper class that translates calls.
- **Example**:
  - **Power Adapter**: Converts a two-pin plug to a three-pin socket.

---

#### **2.2 Facade**
- **Definition**: Provides a simplified interface to a complex subsystem.
- **Purpose**:
  - Reduces the complexity of accessing subsystems.
- **How It Works**:
  - A single `Facade` class wraps and delegates requests to subsystems.
- **Example**:
  - **Hotel Booking**: A `BookingFacade` wraps subsystems for flights, hotels, and car rentals.

---

#### **2.3 Composite**
- **Definition**: Composes objects into tree structures to represent part-whole hierarchies.
- **Purpose**:
  - Treats individual objects and composites uniformly.
- **How It Works**:
  - Implements a component interface that both individual objects and composites use.
- **Example**:
  - **File System**: Folders contain files and other folders.

---

#### **2.4 Proxy**
- **Definition**: Provides a surrogate or placeholder for another object.
- **Purpose**:
  - Controls access to an object.
- **How It Works**:
  - The `Proxy` class delegates requests to the real object.
- **Example**:
  - **Virtual Proxy**: Load large objects (e.g., images) only when needed.

---

#### **2.5 Decorator**
- **Definition**: Adds responsibilities to an object dynamically.
- **Purpose**:
  - Extends functionality without modifying the original class.
- **How It Works**:
  - Wraps the object in a decorator class.
- **Example**:
  - **Text Formatting**: Add bold, italic, or underline decorators.

---

### **3. Behavioral Patterns**
Behavioral patterns are concerned with algorithms and communication between objects.

---

#### **3.1 Strategy**
- **Definition**: Defines a family of algorithms and makes them interchangeable.
- **Purpose**:
  - Encapsulates algorithms for flexibility.
- **How It Works**:
  - Uses a context class to switch between strategies.
- **Example**:
  - **Payment Systems**: Supports multiple strategies like credit cards, PayPal, or bank transfers.

---

#### **3.2 Observer**
- **Definition**: Defines a one-to-many dependency where multiple observers are notified of changes to a subject.
- **Purpose**:
  - Promotes event-driven programming.
- **How It Works**:
  - The `Subject` notifies observers when its state changes.
- **Example**:
  - **News Feed**: Notify users when new content is published.

---

#### **3.3 Command**
- **Definition**: Encapsulates a request as an object.
- **Purpose**:
  - Decouples the sender and receiver of the request.
- **How It Works**:
  - Commands are executed via an `Invoker`.
- **Example**:
  - **Undo/Redo Systems**: Each action is encapsulated as a command.

---

#### **3.4 Template Method**
- **Definition**: Defines the skeleton of an algorithm and allows subclasses to override specific steps.
- **Purpose**:
  - Reuse common logic while customizing parts.
- **How It Works**:
  - Uses abstract methods for customizable steps.
- **Example**:
  - **Sorting Algorithms**: Define a common sorting structure but allow custom comparison logic.

---

#### **3.5 State**
- **Definition**: Allows an object to alter its behavior when its internal state changes.
- **Purpose**:
  - Avoids complex conditionals in code.
- **How It Works**:
  - Changes behavior by switching states.
- **Example**:
  - **Vending Machine**: Behavior changes based on `HasMoney`, `DispenseItem` states.

---

#### **3.6 Iterator**
- **Definition**: Provides a way to sequentially access elements of a collection.
- **Purpose**:
  - Separates traversal logic from the collection.
- **How It Works**:
  - Implements an `Iterator` interface.
- **Example**:
  - **Playlist**: Iterates through songs.

---

### **Key Takeaways**
- **Creational Patterns**: Focus on efficient object creation.
- **Structural Patterns**: Focus on organizing and simplifying system structure.
- **Behavioral Patterns**: Focus on communication and algorithms between objects.

Let me know if you’d like to dive deeper into any specific pattern!