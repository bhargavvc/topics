
In Python, we can implement the Singleton Pattern in several ways. Below, we'll explore a common method using a class with a private constructor and a static method to access the instance.

#### **Step 1: Define the Singleton Class**

```python
class SingletonMeta(type):
    """
    This is a thread-safe implementation of Singleton.
    """
    _instance = None

    def __call__(cls, *args, **kwargs):
        if cls._instance is None:
            # Create and save the instance
            cls._instance = super().__call__(*args, **kwargs)
        return cls._instance
```

**Explanation:**

- **Metaclass (`SingletonMeta`)**: We use a metaclass to control the creation of the Singleton instance.
- **`__call__` Method**: Overrides the instantiation process.
  - Checks if an instance already exists.
  - If not, creates a new one.
  - Returns the singleton instance.

#### **Step 2: Create the Singleton Class Using the Metaclass**

```python
class PrinterService(metaclass=SingletonMeta):
    def __init__(self):
        self.mode = "Idle"

    def get_mode(self):
        return self.mode

    def set_mode(self, mode):
        self.mode = mode
```

**Explanation:**

- **`PrinterService` Class**: Uses `SingletonMeta` as its metaclass.
- **Instance Variables**: `mode` represents the state shared across the application.
- **Methods**:
  - `get_mode()`: Returns the current mode.
  - `set_mode(mode)`: Sets a new mode.

#### **Step 3: Use the Singleton in Client Code**

```python
if __name__ == "__main__":
    # First instance
    printer1 = PrinterService()
    printer1.set_mode("Printing")

    # Second instance
    printer2 = PrinterService()
    print(printer2.get_mode())  # Output: Printing

    # Check if both instances are the same
    print(printer1 is printer2)  # Output: True
```

**Explanation:**

- **Instantiation**: Both `printer1` and `printer2` are references to the same instance.
- **Shared State**: Setting the mode via `printer1` affects `printer2`.
- **Identity Check**: `printer1 is printer2` confirms that both variables point to the same object.
