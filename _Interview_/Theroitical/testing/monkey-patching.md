 
### **Monkey Patching Overview**

**Definition**:  
  - `dynamically changes or extends code at runtime`
  or 
  - Monkey patching allows you to dynamically alter or extend the behavior of functions, classes, or modules at runtime without modifying the original source code.
Here's the refined and ordered version:

**Supports**:  
- **Dynamically typed languages**: Python, JavaScript, Ruby  
- **Statically typed languages**: Java, C++

---

### **Monkey Patching Examples**

1. **Basic Monkey Patching**:  
   Replacing a function or method at runtime, e.g., altering an `add` function's behavior by reassigning it.

2. **Monkey Patching in Testing (Pytest)**:  
   Using Pytest's `monkeypatch` fixture to temporarily override functions or attributes for tests, automatically reverting after tests run.

3. **Instance Method Patching**:  
   Altering the method of a specific object instance without affecting other instances.

4. **Patching Third-Party Libraries**:  
   Temporarily modifying external library functions for quick fixes or tests without changing the original library code.

5. **Patching Built-ins**:  
   Modifying built-in functions or attributes (like `print`) at runtime.

---

### **Table: Types of Uses in Monkey Patching**

| Type                         | Purpose                                                 | Key Technique/Concept                               | Simple Implementation Snippet                                   |
|------------------------------|---------------------------------------------------------|-----------------------------------------------------|-------------------------------------------------------------------|
| **Basic Monkey Patching**    | Change behavior of functions or methods at runtime.     | Direct assignment to replace functions.             | See snippet below                                                 |
| **Pytest Monkeypatch**       | Safely override functions during tests.                 | Use `monkeypatch.setattr` fixture.                  | See snippet below                                                 |
| **Instance Method Patching** | Modify behavior for a single object instance.           | Assign new method to instance using `types.MethodType`. | See snippet below                                              |
| **Third-Party Patching**     | Alter external library functions temporarily.           | Assign new function to library attribute.           | See snippet below                                                 |
| **Patching Built-ins**       | Change behavior of built-in functions globally.         | Assign new function to builtins.                    | See snippet below                                                 |

---

### **Simple Implementation Snippets for Each Type**

1. **Basic Monkey Patching**:
   ```python
   def add(a, b):
       return a + b
   print(add(2, 3))  # Output: 5

   def new_add(a, b):
       return a + b + 1
   add = new_add
   print(add(2, 3))  # Output: 6
   ```

2. **Pytest Monkeypatch**:
   ```python
   # time_utils.py
   import time
   def get_current_time():
       return time.time()

   # test_time_utils.py
   def test_get_current_time(monkeypatch):
       def fake_time():
           return 1609459200  # Fixed timestamp
       monkeypatch.setattr(time, 'time', fake_time)
       import time_utils
       assert time_utils.get_current_time() == 1609459200
   ```

3. **Instance Method Patching**:
   ```python
   import types

   class Greeter:
       def greet(self):
           return "Hello, World!"

   greeter = Greeter()
   print(greeter.greet())  # Output: Hello, World!

   def new_greet(self):
       return "Hi there!"
   greeter.greet = types.MethodType(new_greet, greeter)
   print(greeter.greet())  # Output: Hi there!
   ```

4. **Third-Party Patching**:
   ```python
   import some_library

   def patched_function(*args, **kwargs):
       return "patched result"
   some_library.some_function = patched_function
   result = some_library.some_function()  # returns "patched result"
   ```

5. **Patching Built-ins**:
   ```python
   import builtins
   original_print = print

   def silent_print(*args, **kwargs):
       pass

   builtins.print = silent_print
   print("This will not be printed")

   builtins.print = original_print
   print("This will be printed")
   ```

---

### **Example: Patching a Third-Party Library in Tests**

Suppose you're using a third-party library that returns random data, and you want consistent results for testing.

```python
# my_module.py
import random

def get_random_number():
    return random.randint(1, 100)
```

In your test:
```python
import random
import my_module

original_randint = random.randint

def fixed_randint(a, b):
    return 42  # Always return 42 for predictability

random.randint = fixed_randint
assert my_module.get_random_number() == 42

# Revert the patch
random.randint = original_randint
```

Using Pytest's monkeypatch fixture:
```python
def test_get_random_number(monkeypatch):
    monkeypatch.setattr(random, 'randint', lambda a, b: 42)
    import my_module
    assert my_module.get_random_number() == 42
```

---

### **Example: Hotfix in Production**

Imagine a bug in a third-party library function `third_party.calculate()` that's causing critical issues. You could monkey patch it in your production code until the library is updated.

```python
import third_party

# Backup original function
original_calculate = third_party.calculate

def patched_calculate(*args, **kwargs):
    # Workaround bug, perhaps by adjusting arguments or fixing return value
    result = original_calculate(*args, **kwargs)
    # Modify result if needed
    return result

third_party.calculate = patched_calculate

# Now, any call to third_party.calculate uses patched_calculate
```

---

### **Using Context Managers**  
Create a context manager that applies a patch on entry and reverts it on exit.

```python
from contextlib import contextmanager

@contextmanager
def temporary_patch(obj, attr, new_value):
    original = getattr(obj, attr)
    setattr(obj, attr, new_value)
    try:
        yield
    finally:
        setattr(obj, attr, original)

# Usage:
with temporary_patch(module, 'func', new_func):
    # module.func is now new_func
    pass
# Automatically reverted
```

---

### **Patching Imported Objects**

Be aware that if a function or class was imported directly from a module using syntax like `from module import something`, modifying `module.something` won't affect the previously imported reference. You must patch the actual reference that the code is using.

**Example:**

```python
# module_a.py
def foo():
    return "original"

# module_b.py
from module_a import foo

def use_foo():
    return foo()

# In a test
import module_a
import module_b

module_a.foo = lambda: "patched"
print(module_b.use_foo())  # Still prints "original" because module_b imported foo earlier
```

---

### **Key Concepts of Monkey Patching**
- **Dynamic Modification**: Changing attributes, methods, or functions on the fly.
- **Runtime Effect**: Changes take effect immediately until reverted.
- **Scope of Impact**: Affects all parts of the program using the patched entity after the patch is applied.

---

### **Why Use Monkey Patching?**
- **Testing**: Override system behavior during tests for isolation.
- **Bug Fixes**: Apply temporary fixes to third-party libraries.
- **Enhancement**: Extend functionality without modifying original source code.

However, use sparingly to avoid making code hard to debug and maintain.

---

### **Reverting Monkey Patches**
- **Manually Reverting**: Keep original references before patching.
- **Context Managers**: Apply and revert patches within a controlled scope.
- **Pytest's `monkeypatch` Fixture**: Automatically reverts patches after tests.

---

### **Considerations and Best Practices**
- **Limit Scope**: Use patches where necessary, with proper isolation.
- **Document Patches**: Clearly explain why and where patches are applied.
- **Prefer Alternatives**: Dependency injection may provide a cleaner solution.
- **Test Isolation**: Use Pytest's `monkeypatch` fixture for safe testing.

---

### **Pitfalls and Best Practices**
- **Unexpected Effects**: Patches can affect parts of the code unintentionally.
- **Readability**: Code becomes harder to understand if overused.
- **Use Sparingly in Production**: It's best to limit monkey patching in production, preferring permanent fixes.

---

This should now provide a clear, concise, and ordered overview of monkey patching examples and best practices.