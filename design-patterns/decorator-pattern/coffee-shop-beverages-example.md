
---

### **Example: Coffee Shop Beverages**

Let's revisit the coffee shop example to understand how the Decorator Pattern works.

**Scenario:**

- We have a `Beverage` class that represents a drink.
- Beverages can have various additives (decorators) like milk, sugar, whipped cream, etc.
- Each additive affects the cost and description of the beverage.
- We want to dynamically add additives to beverages without creating a subclass for every possible combination.

**Challenges:**

- Using inheritance to create subclasses for every combination leads to an explosion of classes.
- Modifying the `Beverage` class to handle all additives violates the Open/Closed Principle.

**Applying the Decorator Pattern:**

1. **Define the Component (`Beverage`):**

   ```python
   # beverage.py

   class Beverage:
       def get_description(self):
           return "Unknown Beverage"

       def cost(self):
           pass
   ```

   **Explanation:**

   - The `Beverage` class is the component interface.
   - It defines methods that all beverages should implement.

2. **Create Concrete Components:**

   ```python
   # concrete_beverages.py

   from beverage import Beverage

   class Espresso(Beverage):
       def get_description(self):
           return "Espresso"

       def cost(self):
           return 1.99

   class HouseBlend(Beverage):
       def get_description(self):
           return "House Blend Coffee"

       def cost(self):
           return 0.89
   ```

   **Explanation:**

   - `Espresso` and `HouseBlend` are concrete components.
   - They implement the `Beverage` interface.

3. **Define the Decorator (`CondimentDecorator`):**

   ```python
   # condiment_decorator.py

   from beverage import Beverage

   class CondimentDecorator(Beverage):
       def __init__(self, beverage):
           self.beverage = beverage

       def get_description(self):
           pass

       def cost(self):
           pass
   ```

   **Explanation:**

   - `CondimentDecorator` is an abstract decorator class.
   - It contains a reference to a `Beverage` object.

4. **Create Concrete Decorators:**

   ```python
   # concrete_decorators.py

   from condiment_decorator import CondimentDecorator

   class Milk(CondimentDecorator):
       def get_description(self):
           return self.beverage.get_description() + ", Milk"

       def cost(self):
           return self.beverage.cost() + 0.10

   class Mocha(CondimentDecorator):
       def get_description(self):
           return self.beverage.get_description() + ", Mocha"

       def cost(self):
           return self.beverage.cost() + 0.20

   class Whip(CondimentDecorator):
       def get_description(self):
           return self.beverage.get_description() + ", Whip"

       def cost(self):
           return self.beverage.cost() + 0.30
   ```

   **Explanation:**

   - `Milk`, `Mocha`, and `Whip` are concrete decorators.
   - They extend `CondimentDecorator` and add new behaviors.

5. **Using the Decorator Pattern in Client Code:**

   ```python
   # client.py

   from concrete_beverages import Espresso, HouseBlend
   from concrete_decorators import Mocha, Milk, Whip

   def main():
       # Order an Espresso with no additives
       beverage = Espresso()
       print(f"{beverage.get_description()} $ {beverage.cost():.2f}")

       # Order a House Blend with Mocha and Whip
       beverage2 = HouseBlend()
       beverage2 = Mocha(beverage2)
       beverage2 = Whip(beverage2)
       print(f"{beverage2.get_description()} $ {beverage2.cost():.2f}")

       # Order an Espresso with double Mocha and Whip
       beverage3 = Espresso()
       beverage3 = Mocha(beverage3)
       beverage3 = Mocha(beverage3)
       beverage3 = Whip(beverage3)
       print(f"{beverage3.get_description()} $ {beverage3.cost():.2f}")

   if __name__ == "__main__":
       main()
   ```

   **Output:**

   ```
   Espresso $ 1.99
   House Blend Coffee, Mocha, Whip $ 1.39
   Espresso, Mocha, Mocha, Whip $ 2.69
   ```

   **Explanation:**

   - We create beverage objects and wrap them with decorators.
   - Each decorator adds to the description and cost.
   - We can dynamically compose beverages with any combination of additives.

---
