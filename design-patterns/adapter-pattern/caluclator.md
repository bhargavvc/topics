

### **Implementing the Adapter Pattern in Python**

Due to Python's dynamic typing and support for duck typing, implementing the adapter pattern can be straightforward.

**Example: Using Duck Typing for Adapters**

```python
# adaptee.py

class OldCalculator:
    def calculate(self, expression):
        # Simple implementation
        return eval(expression)
```

```python
# target.py

class NewCalculatorInterface:
    def execute(self, expression):
        pass
```

```python
# adapter.py

class CalculatorAdapter:
    def __init__(self, adaptee):
        self.adaptee = adaptee
    
    def execute(self, expression):
        return self.adaptee.calculate(expression)
```

```python
# client.py

def main():
    old_calculator = OldCalculator()
    calculator = CalculatorAdapter(old_calculator)
    result = calculator.execute("2 + 3 * 4")
    print(f"Result: {result}")

if __name__ == "__main__":
    main()
```

**Output:**

```
Result: 14
```

**Explanation:**

- The client code expects an object with an `execute` method.
- The `CalculatorAdapter` adapts the `OldCalculator`'s `calculate` method to the expected `execute` method.
- This allows the old calculator to be used where the new interface is expected.

---
