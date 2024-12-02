
### **Example 1: Integrating a New Logging Library**

**Scenario:**

Your application uses a custom logging interface, but you want to integrate a third-party logging library without changing your existing codebase.

**Existing Logging Interface (Target):**

```python
# logger_interface.py

class LoggerInterface:
    def log(self, message):
        pass
```

**Existing Logger Implementation:**

```python
# custom_logger.py

from logger_interface import LoggerInterface

class CustomLogger(LoggerInterface):
    def log(self, message):
        print(f"Custom Logger: {message}")
```

**Third-Party Logging Library (Adaptee):**

```python
# third_party_logger.py

class ThirdPartyLogger:
    def write_log(self, msg):
        print(f"Third-Party Logger: {msg}")
```

**Challenge:**

- The method `write_log` in `ThirdPartyLogger` doesn't match the `log` method in `LoggerInterface`.
- We can't modify `ThirdPartyLogger` since it's a third-party library.

**Applying the Adapter Pattern:**

**Create an Adapter:**

```python
# logger_adapter.py

from logger_interface import LoggerInterface
from third_party_logger import ThirdPartyLogger

class LoggerAdapter(LoggerInterface):
    def __init__(self):
        self.third_party_logger = ThirdPartyLogger()
    
    def log(self, message):
        # Adapt the method call
        self.third_party_logger.write_log(message)
```

**Usage in Client Code:**

```python
# client.py

from logger_adapter import LoggerAdapter

def main():
    logger = LoggerAdapter()
    logger.log("Adapter Pattern Example")

if __name__ == "__main__":
    main()
```

**Output:**

```
Third-Party Logger: Adapter Pattern Example
```

**Explanation:**

- The `LoggerAdapter` implements the `LoggerInterface` expected by the client.
- It holds an instance of `ThirdPartyLogger` and translates the `log` method calls to `write_log`.
- The client code uses `LoggerAdapter` without any changes to its own logic.

---