
### **Example 2: Purchasing Soap from a Shopkeeper**

**Scenario:**

- **Customer**: Wants to buy soap.
- **Shopkeeper**: Provides the soap.
- **Soap**: Different types (e.g., antibacterial, herbal, luxury) are available.
- **Customer**: Receives the soap without knowing how it was made or who manufactured it.

**Applying the Factory Method Pattern:**

- **Product Interface**: `Soap`
- **Concrete Products**: `AntibacterialSoap`, `HerbalSoap`, `LuxurySoap`
- **Creator (Factory)**: `Shopkeeper`
- **Concrete Creators**: `LocalShopkeeper`, `SupermarketShopkeeper`, `OnlineShopkeeper`

**Implementation in Python:**

```python
from abc import ABC, abstractmethod

# Product Interface
class Soap(ABC):
    @abstractmethod
    def get_soap(self):
        pass

# Concrete Products
class AntibacterialSoap(Soap):
    def get_soap(self):
        return "Antibacterial Soap provided."

class HerbalSoap(Soap):
    def get_soap(self):
        return "Herbal Soap provided."

class LuxurySoap(Soap):
    def get_soap(self):
        return "Luxury Soap provided."

# Creator (Factory) Interface
class Shopkeeper(ABC):
    @abstractmethod
    def provide_soap(self):
        pass

    def sell_soap(self):
        soap = self.provide_soap()
        result = soap.get_soap()
        return result

# Concrete Creators
class LocalShopkeeper(Shopkeeper):
    def provide_soap(self):
        return AntibacterialSoap()

class SupermarketShopkeeper(Shopkeeper):
    def provide_soap(self):
        return HerbalSoap()

class OnlineShopkeeper(Shopkeeper):
    def provide_soap(self):
        return LuxurySoap()

# Client Code
def customer_request(shopkeeper: Shopkeeper):
    print(shopkeeper.sell_soap())

# Usage
if __name__ == "__main__":
    print("Customer buys soap from a local shop:")
    customer_request(LocalShopkeeper())

    print("\nCustomer buys soap from a supermarket:")
    customer_request(SupermarketShopkeeper())

    print("\nCustomer buys soap online:")
    customer_request(OnlineShopkeeper())
```

**Explanation:**

1. **Soap (Product Interface)**: An abstract class with the method `get_soap`.
   ```python
   class Soap(ABC):
       @abstractmethod
       def get_soap(self):
           pass
   ```
2. **Concrete Soaps (Products)**: `AntibacterialSoap`, `HerbalSoap`, and `LuxurySoap` implement `get_soap`.
   ```python
   class AntibacterialSoap(Soap):
       def get_soap(self):
           return "Antibacterial Soap provided."
   ```
3. **Shopkeeper (Creator)**: An abstract class with the factory method `provide_soap` and a method `sell_soap` that uses it.
   ```python
   class Shopkeeper(ABC):
       @abstractmethod
       def provide_soap(self):
           pass

       def sell_soap(self):
           soap = self.provide_soap()
           result = soap.get_soap()
           return result
   ```
4. **Concrete Shopkeepers (Concrete Creators)**: `LocalShopkeeper`, `SupermarketShopkeeper`, and `OnlineShopkeeper` implement `provide_soap`, returning a specific `Soap` instance.
   ```python
   class LocalShopkeeper(Shopkeeper):
       def provide_soap(self):
           return AntibacterialSoap()
   ```
5. **Client Code**: The customer interacts with the `Shopkeeper` interface, not knowing the details of soap production.
   ```python
   def customer_request(shopkeeper: Shopkeeper):
       print(shopkeeper.sell_soap())
   ```

**Output:**

```
Customer buys soap from a local shop:
Antibacterial Soap provided.

Customer buys soap from a supermarket:
Herbal Soap provided.

Customer buys soap online:
Luxury Soap provided.
```

**Key Points:**

- **Abstraction**: The customer requests soap without knowing how it's made.
- **Factory Method**: `provide_soap` decides which concrete `Soap` to provide.
- **Loose Coupling**: The customer depends on the `Shopkeeper` abstraction.

---

### **Understanding the Factory Method Pattern in These Examples**

**Core Components:**

1. **Product Interface**: Defines the interface for objects the factory method creates.
2. **Concrete Products**: Implement the product interface.
3. **Creator (Factory) Interface**: Declares the factory method that returns an object of the product interface.
4. **Concrete Creators**: Override the factory method to return an instance of a concrete product.

**Benefits:**

- **Abstraction of Creation**: Clients are decoupled from the creation of objects.
- **Open/Closed Principle**: New products can be added without changing existing code.
- **Single Responsibility Principle**: Creation logic is separated from business logic.

**When to Use:**

- When you have a superclass that delegates the responsibility of creating objects to its subclasses.
- When you want to provide flexibility in instantiating objects.

### **Conclusion**

By applying the Factory Method Pattern in these examples, we:

- **Simplified Client Interaction**: Clients don't need to know the specifics of object creation.
- **Enhanced Maintainability**: Changes in creation logic don't affect client code.
- **Promoted Extensibility**: New product types can be introduced with minimal changes.
