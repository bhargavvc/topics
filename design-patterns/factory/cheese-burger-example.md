
### **The Restaurant Analogy in Code**

Imagine we are building a system for a restaurant that offers different types of burgers: **Cheeseburger**, **Vegan Burger**, **Deluxe Burger**, and so on. A naive implementation to create these burgers might involve a series of `if` or `elif` statements:

```python
if burger_type == "cheese":
    burger = CheeseBurger()
elif burger_type == "vegan":
    burger = VeganBurger()
elif burger_type == "deluxe":
    burger = DeluxeBurger()
# Additional burger types...
```

**Problems with This Approach:**

- **Scalability Issues**: Every time a new burger type is added, you must modify this code.
- **Maintenance Headaches**: Duplicated code and long conditional statements make the codebase hard to manage.
- **Violation of Design Principles**: Specifically, the **Open/Closed Principle** is breached since the class isn't closed for modification.

---

### **Attempting a Simple Factory**

One might think to encapsulate the creation logic within a **Simple Factory**:

```python
class BurgerFactory:
    @staticmethod
    def create_burger(burger_type):
        if burger_type == "cheese":
            return CheeseBurger()
        elif burger_type == "vegan":
            return VeganBurger()
        elif burger_type == "deluxe":
            return DeluxeBurger()
        # Additional burger types...
```

**Limitations of the Simple Factory:**

- **Still Violates Open/Closed Principle**: Adding new burger types requires modifying the `BurgerFactory` class.
- **Potential for Bugs**: Changes in the factory affect all clients relying on it, increasing the risk of introducing bugs.
- **Dependency on Concrete Classes**: Clients still need to know about the specific types of burgers.

---

### **Embracing the Factory Method Pattern**

The **Factory Method Pattern** offers a more robust solution by:

- Defining an **interface** or **abstract class** for creating an object.
- Allowing **subclasses** to decide which class to instantiate.
- Promoting **loose coupling** by working with abstractions rather than concrete implementations.

---

### **Structure of the Factory Method Pattern**

Let's break down the components using the burger example:

1. **Product Interface (`Burger`)**: An abstract base class that defines the type of objects the factory method creates.

    ```python
    from abc import ABC, abstractmethod

    class Burger(ABC):
        @abstractmethod
        def prepare(self):
            pass

        @abstractmethod
        def cook(self):
            pass

        @abstractmethod
        def box(self):
            pass
    ```

2. **Concrete Products (`CheeseBurger`, `VeganBurger`, etc.)**: Classes that implement the `Burger` interface.

    ```python
    class CheeseBurger(Burger):
        def prepare(self):
            print("Preparing Cheeseburger")

        def cook(self):
            print("Cooking Cheeseburger")

        def box(self):
            print("Boxing Cheeseburger")

    class VeganBurger(Burger):
        def prepare(self):
            print("Preparing Vegan Burger")

        def cook(self):
            print("Cooking Vegan Burger")

        def box(self):
            print("Boxing Vegan Burger")
    ```

3. **Creator (`BurgerStore`)**: An abstract class that declares the factory method, which returns an object of type `Burger`.

    ```python
    class BurgerStore(ABC):
        @abstractmethod
        def create_burger(self):
            pass

        def order_burger(self):
            burger = self.create_burger()
            burger.prepare()
            burger.cook()
            burger.box()
            return burger
    ```

4. **Concrete Creators (`CheeseBurgerStore`, `VeganBurgerStore`, etc.)**: Subclasses that override the factory method to return instances of concrete products.

    ```python
    class CheeseBurgerStore(BurgerStore):
        def create_burger(self):
            return CheeseBurger()

    class VeganBurgerStore(BurgerStore):
        def create_burger(self):
            return VeganBurger()
    ```

---

### **Explanation of the Code Components**

- **Product Interface (`Burger`)**: Defines the methods that all concrete products must implement. This ensures that all burger types adhere to a common interface.

- **Concrete Products**: Implement the `Burger` interface. Each burger type provides its own implementation of the preparation, cooking, and boxing processes.

- **Creator (`BurgerStore`)**: Declares the factory method `create_burger()`. It also contains the `order_burger()` method, which uses the factory method to create a burger and then perform common operations (prepare, cook, box).

- **Concrete Creators**: Override the factory method to return a specific `Burger` instance. This allows for the creation of specific burger types without modifying the creator's code.

---

### **How This Solves Our Problems**

- **Open/Closed Principle Adherence**: New burger types can be added by creating new subclasses without modifying existing code.

- **Reduced Risk of Bugs**: Existing code remains untouched when adding new types, minimizing the chance of introducing bugs.

- **Dependency Inversion Principle**: High-level modules depend on abstractions (`Burger` and `BurgerStore`), not concrete implementations.

- **Polymorphism and Flexibility**: The system can work with any `BurgerStore` and `Burger` without knowing their concrete classes.

---

### **Implementing Dependency Inversion**

Previously, classes that needed burgers were responsible for creating them, thus tightly coupling them to concrete implementations. With the Factory Method Pattern, these classes now depend on abstractions.

**Example:**

```python
class Restaurant:
    def __init__(self, burger_store: BurgerStore):
        self.burger_store = burger_store

    def serve_burger(self):
        burger = self.burger_store.order_burger()
        print("Serving:", type(burger).__name__)
```

Now, `Restaurant` depends on the `BurgerStore` abstraction. We can inject any concrete `BurgerStore` (e.g., `CheeseBurgerStore`, `VeganBurgerStore`) without changing the `Restaurant` code.

**Usage:**

```python
if __name__ == "__main__":
    cheese_store = CheeseBurgerStore()
    vegan_store = VeganBurgerStore()

    restaurant = Restaurant(cheese_store)
    restaurant.serve_burger()

    restaurant = Restaurant(vegan_store)
    restaurant.serve_burger()
```

**Output:**

```
Preparing Cheeseburger
Cooking Cheeseburger
Boxing Cheeseburger
Serving: CheeseBurger

Preparing Vegan Burger
Cooking Vegan Burger
Boxing Vegan Burger
Serving: VeganBurger
```
