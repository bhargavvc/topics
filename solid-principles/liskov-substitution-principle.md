# Liskov Substitution Principle (LSP)

## **Simple Explanation in Plain English**

The Liskov Substitution Principle states that **objects of a superclass should be replaceable with objects of their subclasses without affecting the correctness of the program**. In other words, if class B is a subclass of class A, then objects of A should be able to be replaced with objects of B without altering the desired functionality.

---

## **Explanation in Terms of Software Application Definition**

In software development, LSP emphasizes that a subclass should enhance, not weaken, the functionality of its superclass. Subclasses must adhere to the contracts and expectations set by their superclasses. This means that methods in the subclass should behave in ways that are consistent with the superclass, ensuring that the application remains stable and predictable when subclasses are used in place of superclasses.

---

## **Example 1: Real-World Sample (Non-Programming Scenario)**

### **Scenario: Transportation Vehicles**

**Initial Situation:**

Consider a transportation system where:

- **Vehicle** is the general category (superclass).
- **Car** is a type of Vehicle (subclass).
- **Bicycle** is another type of Vehicle (subclass).

**Assumptions:**

- All Vehicles can carry passengers.
- Vehicles have a method to **start the engine**.

**Applying LSP:**

- **Correct Replacement:** Replacing a Vehicle with a Car works seamlessly because a Car has an engine and can start it.
- **Violation of LSP:** Replacing a Vehicle with a Bicycle may cause issues because a Bicycle doesn't have an engine to start.

**Explanation:**

- **LSP Adherence:** If we treat all Vehicles as having an engine, then substituting a Car for a Vehicle is acceptable.
- **LSP Violation:** Substituting a Bicycle where a Vehicle with an engine is expected breaks the program's expectations, leading to errors or incorrect behavior.

---

## **Example 2: Real-World Programming Scenario in Software Application**

### **Scenario: File Systems and Read-Only Files**

**Incorrect Implementation (Violating LSP):**

We have a `File` class with methods to read and write data.

```python
class File:
    def read(self):
        # Code to read data from the file
        pass

    def write(self, data):
        # Code to write data to the file
        pass
```

We create a subclass `ReadOnlyFile` that is supposed to represent files that cannot be written to.

```python
class ReadOnlyFile(File):
    def write(self, data):
        raise Exception("Cannot write to a read-only file")
```

**Problem:**

- The `ReadOnlyFile` class overrides the `write` method to raise an exception.
- This violates LSP because code that expects to write to a `File` may break when a `ReadOnlyFile` is used in its place.

**Example of LSP Violation:**

```python
def save_data(file, data):
    file.write(data)

file = File()
readonly_file = ReadOnlyFile()

save_data(file, "Some data")          # Works fine
save_data(readonly_file, "Some data") # Raises Exception: Cannot write to a read-only file
```

**Explanation:**

- The function `save_data` expects any `File` object to be writable.
- Substituting `ReadOnlyFile` breaks this expectation, violating LSP.

**Correct Implementation (Adhering to LSP):**

Use composition instead of inheritance or redesign the class hierarchy.

```python
from abc import ABC, abstractmethod

class AbstractFile(ABC):
    @abstractmethod
    def read(self):
        pass

    @abstractmethod
    def write(self, data):
        pass

class ReadWriteFile(AbstractFile):
    def read(self):
        # Code to read data
        pass

    def write(self, data):
        # Code to write data
        pass

class ReadOnlyFile(AbstractFile):
    def read(self):
        # Code to read data
        pass

    def write(self, data):
        raise NotImplementedError("Write operation not supported")
```

**Alternative Solution:**

Separate interfaces for readable and writable files.

```python
class ReadableFile(ABC):
    @abstractmethod
    def read(self):
        pass

class WritableFile(ABC):
    @abstractmethod
    def write(self, data):
        pass

class ReadWriteFile(ReadableFile, WritableFile):
    def read(self):
        # Code to read data
        pass

    def write(self, data):
        # Code to write data
        pass

class ReadOnlyFile(ReadableFile):
    def read(self):
        # Code to read data
        pass
```

**Explanation:**

- By separating the interfaces, `ReadOnlyFile` does not inherit a `write` method it cannot support.
- Code that requires a writable file will explicitly depend on the `WritableFile` interface, preventing substitution with a `ReadOnlyFile`.

**Revised Usage:**

```python
def save_data(file: WritableFile, data):
    file.write(data)

file = ReadWriteFile()
readonly_file = ReadOnlyFile()

save_data(file, "Some data")          # Works fine
save_data(readonly_file, "Some data") # TypeError at runtime or IDE warning
```

---

## **Explanation of Examples**

### **Example 1 Analysis:**

- **Issue:** Treating all Vehicles as having an engine when not all subclasses (e.g., Bicycle) have one.
- **Violation:** Substituting a Bicycle where a Vehicle with an engine is expected causes failure.
- **Solution:** Redefine the class hierarchy or use interfaces to represent capabilities like `EnginePoweredVehicle`.

### **Example 2 Analysis:**

- **Issue:** `ReadOnlyFile` cannot perform all actions that `File` promises.
- **Violation:** Substituting `ReadOnlyFile` for `File` leads to exceptions, breaking the program's correctness.
- **Solution:** Use separate interfaces or abstract base classes to ensure that subclasses only implement behaviors they can support.

---

## **Key Takeaways**

- **Ensure Behavioral Consistency:** Subclasses should not alter the expected behavior of the superclass methods.
- **Respect Contracts:** Methods in subclasses should honor the contracts (inputs, outputs, side effects) established by the superclass.
- **Design Robust Inheritance Hierarchies:** Only use inheritance when the subclass genuinely is a subtype of the superclass.
- **Use Interfaces Wisely:** Consider using interfaces or abstract base classes to define specific capabilities, reducing the risk of LSP violations.

---

Would you like to proceed to the next principle or discuss any aspect in more detail?