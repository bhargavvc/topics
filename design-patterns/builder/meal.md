
### **Example: Building a Complex Meal**

Let's revisit the meal example to understand how the Builder Pattern works.

**Scenario:**

- We have a `Meal` class that can have various components:
  - **Drink**
  - **Main Course**
  - **Dessert**
  - **Side Dish**
  - **Sauce**
- Each component is optional, and there can be many variations of each component.

**Challenges:**

- Constructing a `Meal` object with all possible parameters leads to complex constructors.
- We want flexibility to create different meals without creating numerous subclasses.

**Applying the Builder Pattern:**

1. **Define the Product (`Meal`):**

   ```python
   # meal.py

   class Meal:
       def __init__(self):
           self.drink = None
           self.main_course = None
           self.dessert = None
           self.side_dish = None
           self.sauce = None

       def __str__(self):
           components = []
           if self.drink:
               components.append(f"Drink: {self.drink}")
           if self.main_course:
               components.append(f"Main Course: {self.main_course}")
           if self.side_dish:
               components.append(f"Side Dish: {self.side_dish}")
           if self.sauce:
               components.append(f"Sauce: {self.sauce}")
           if self.dessert:
               components.append(f"Dessert: {self.dessert}")
           return ', '.join(components)
   ```

   **Explanation:**

   - The `Meal` class has attributes for each component, initialized to `None`.
   - The `__str__` method provides a string representation of the meal.

2. **Create the Builder Class with Fluent Interface:**

   ```python
   # meal_builder.py

   class MealBuilder:
       def __init__(self):
           self.meal = Meal()

       def add_drink(self, drink):
           self.meal.drink = drink
           return self

       def add_main_course(self, main_course):
           self.meal.main_course = main_course
           return self

       def add_dessert(self, dessert):
           self.meal.dessert = dessert
           return self

       def add_side_dish(self, side_dish):
           self.meal.side_dish = side_dish
           return self

       def add_sauce(self, sauce):
           self.meal.sauce = sauce
           return self

       def build(self):
           return self.meal
   ```

   **Explanation:**

   - `MealBuilder` methods return `self`, enabling method chaining.
   - Each method sets a component of the meal.
   - The `build` method returns the constructed `Meal` object.

3. **Using the Builder Pattern in Client Code:**

   ```python
   # client.py

   def main():
       # Build a custom meal
       builder = MealBuilder()
       custom_meal = (
           builder
           .add_drink("Iced Tea")
           .add_main_course("Grilled Salmon")
           .add_side_dish("Caesar Salad")
           .add_sauce("Lemon Butter")
           .build()
       )
       print("Custom Meal:")
       print(custom_meal)

       # Build another meal with different components
       another_meal = (
           MealBuilder()
           .add_main_course("Vegan Burger")
           .add_side_dish("Sweet Potato Fries")
           .add_dessert("Fruit Bowl")
           .build()
       )
       print("\nAnother Meal:")
       print(another_meal)

   if __name__ == "__main__":
       main()
   ```

   **Output:**

   ```
   Custom Meal:
   Drink: Iced Tea, Main Course: Grilled Salmon, Side Dish: Caesar Salad, Sauce: Lemon Butter

   Another Meal:
   Main Course: Vegan Burger, Side Dish: Sweet Potato Fries, Dessert: Fruit Bowl
   ```

   **Explanation:**

   - In the client code, we use the builder to construct meals with different components.
   - Method chaining makes the code more readable and expressive.
   - The builder handles optional components gracefully.
