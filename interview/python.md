
---

### **1. Explain the difference between Python 2 and Python 3.**  
#### **Answer**:  
Python 2 and Python 3 are two major versions of Python with the following differences:  
1. **Syntax**:  
   - **Python 2**: `print` is treated as a statement: `print "Hello World"`.  
   - **Python 3**: `print` is a function: `print("Hello World")`.  

2. **Unicode Support**:  
   - **Python 2**: Strings are ASCII by default. To work with Unicode, you explicitly use a `u` prefix: `u"hello"`.  
   - **Python 3**: Strings are Unicode by default, making it easier to handle international text.  

3. **Division Behavior**:  
   - **Python 2**: Division of integers truncates the decimal: `5 / 2` results in `2`.  
   - **Python 3**: Division returns a float: `5 / 2` results in `2.5`. Use `//` for floor division.  

4. **Libraries**:  
   - Many Python 2 libraries are not forward-compatible with Python 3, but Python 3 libraries are the standard now.  

5. **End of Life**:  
   - Python 2 is no longer maintained (end of life was January 1, 2020), so Python 3 is recommended for all development.  

---

### **2. How does Python's Global Interpreter Lock (GIL) work, and how does it affect multithreading?**  
#### **Answer**:  
- The **Global Interpreter Lock (GIL)** is a mutex that protects access to Python objects in CPython, ensuring that only one thread executes Python bytecode at a time.  
- It simplifies memory management but limits the true parallel execution of threads.  

#### **Effect on Multithreading**:  
1. **I/O-Bound Tasks**: Multithreading works well for tasks like web scraping or file operations because the GIL releases during I/O operations.  
2. **CPU-Bound Tasks**: For computational tasks (e.g., matrix multiplication), threads can’t execute in parallel, resulting in performance bottlenecks.  

#### **Solution**:  
- Use the **multiprocessing** module to bypass the GIL since each process has its own Python interpreter and memory space.  
- Alternatively, use libraries like **NumPy** or **Cython** that release the GIL for specific operations.  

---

### **3. What are Python's data types? Provide examples for each.**  
#### **Answer**:  
Python has several built-in data types:  
1. **Numeric Types**:  
   - `int`: Integer values. Example: `x = 10`.  
   - `float`: Floating-point numbers. Example: `pi = 3.14`.  
   - `complex`: Complex numbers. Example: `z = 3 + 4j`.  

2. **Sequence Types**:  
   - `str`: Strings. Example: `name = "Python"`.  
   - `list`: Mutable ordered collection. Example: `fruits = ["apple", "banana"]`.  
   - `tuple`: Immutable ordered collection. Example: `coordinates = (10, 20)`.  

3. **Set Types**:  
   - `set`: Unordered collection of unique elements. Example: `numbers = {1, 2, 3}`.  
   - `frozenset`: Immutable set. Example: `fs = frozenset([1, 2, 3])`.  

4. **Mapping Types**:  
   - `dict`: Key-value pairs. Example: `person = {"name": "Alice", "age": 25}`.  

5. **Boolean Type**:  
   - `bool`: Boolean values. Example: `is_active = True`.  

6. **None Type**:  
   - `NoneType`: Represents the absence of a value. Example: `x = None`.  

---

### **4. What are Python decorators? Provide a use case.**  
#### **Answer**:  
- **Decorators** are functions that modify the behavior of another function or method. They are applied using the `@decorator_name` syntax.  

#### **Example Use Case**:  
Let’s create a decorator to log the execution time of a function:  
```python
import time

def timer(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"{func.__name__} executed in {end_time - start_time:.2f}s")
        return result
    return wrapper

@timer
def slow_function():
    time.sleep(2)
    print("Function executed!")

slow_function()
```  
#### **Output**:  
```
Function executed!
slow_function executed in 2.00s
```  

---

### **5. Explain the difference between shallow copy and deep copy.**  
#### **Answer**:  
1. **Shallow Copy**:  
   - Creates a new object, but references the same nested objects as the original. Changes in nested objects affect both copies.  
   - Use `copy.copy()`.  
   - Example:  
     ```python
     import copy
     original = [[1, 2], [3, 4]]
     shallow = copy.copy(original)
     shallow[0][0] = 99
     print(original)  # Output: [[99, 2], [3, 4]]
     ```  

2. **Deep Copy**:  
   - Creates a new object along with recursively copying all nested objects. Changes in nested objects do not affect the original.  
   - Use `copy.deepcopy()`.  
   - Example:  
     ```python
     deep = copy.deepcopy(original)
     deep[0][0] = 0
     print(original)  # Output: [[99, 2], [3, 4]]
     ```  

---

### **6. What are Python's built-in data structures? Explain their use cases.**  
#### **Answer**:  
Python provides several built-in data structures for efficient data storage and manipulation:  
1. **List**:  
   - **Definition**: Ordered, mutable, allows duplicates.  
   - **Use Case**: Suitable for dynamic arrays where you frequently add, remove, or access elements by index.  
   - Example:  
     ```python
     items = [1, 2, 3]
     items.append(4)
     print(items)  # Output: [1, 2, 3, 4]
     ```  

2. **Tuple**:  
   - **Definition**: Ordered, immutable, allows duplicates.  
   - **Use Case**: Use when the dataset should not be changed, such as coordinates or fixed data collections.  
   - Example:  
     ```python
     coordinates = (10, 20)
     print(coordinates[0])  # Output: 10
     ```  

3. **Set**:  
   - **Definition**: Unordered, mutable, no duplicates.  
   - **Use Case**: Use for membership testing, removing duplicates, or mathematical operations like union and intersection.  
   - Example:  
     ```python
     unique_items = {1, 2, 3, 3}
     print(unique_items)  # Output: {1, 2, 3}
     ```  

4. **Dictionary**:  
   - **Definition**: Unordered collection of key-value pairs. Keys are unique and immutable.  
   - **Use Case**: Fast lookups and mappings between keys and values, such as configuration or user data.  
   - Example:  
     ```python
     user = {"name": "Alice", "age": 25}
     print(user["name"])  # Output: Alice
     ```  

---

### **7. What is the difference between `is` and `==` in Python?**  
#### **Answer**:  
1. **`is`**:  
   - Compares the memory addresses of two objects. Returns `True` if they refer to the same object.  

2. **`==`**:  
   - Compares the values of two objects. Returns `True` if the values are equal, even if they are different objects in memory.  

#### **Example**:  
```python
a = [1, 2, 3]
b = [1, 2, 3]
c = a

print(a == b)  # Output: True (values are the same)
print(a is b)  # Output: False (different memory locations)
print(a is c)  # Output: True (same memory location)
```

---

### **8. What is Python's `@staticmethod` and `@classmethod`? Explain with examples.**  
#### **Answer**:  
1. **`@staticmethod`**:  
   - A method that belongs to a class but does not access instance or class-level data.  
   - Used for utility functions.  
   - Example:  
     ```python
     class Math:
         @staticmethod
         def add(x, y):
             return x + y

     print(Math.add(3, 5))  # Output: 8
     ```  

2. **`@classmethod`**:  
   - A method that takes the class itself (`cls`) as the first parameter and can modify class-level data.  
   - Example:  
     ```python
     class Counter:
         count = 0

         @classmethod
         def increment(cls):
             cls.count += 1

     Counter.increment()
     print(Counter.count)  # Output: 1
     ```

---

### **9. How does Python handle memory management?**  
#### **Answer**:  
Python uses an automatic memory management system with the following components:  
1. **Reference Counting**:  
   - Each object has a reference count that tracks the number of references pointing to it.  
   - When the reference count drops to zero, the object is deallocated.  

2. **Garbage Collection**:  
   - Handles cyclic references (e.g., objects referencing each other).  
   - Uses the `gc` module to detect and clean up cycles.  

3. **Heap Memory**:  
   - Python objects and data structures are stored in a private heap, managed by the interpreter.  

#### **Code Example**:  
```python
import gc

a = []
b = [a]
a.append(b)  # Creates a circular reference
del a, b     # Removes the references
gc.collect()  # Force garbage collection
```

---

### **10. How do Python's `args` and `kwargs` work?**  
#### **Answer**:  
- **`*args`**: Allows a function to accept any number of positional arguments.  
- **`**kwargs`**: Allows a function to accept any number of keyword arguments.  

#### **Example**:  
```python
def demo(*args, **kwargs):
    print(f"Positional arguments: {args}")
    print(f"Keyword arguments: {kwargs}")

demo(1, 2, 3, name="Alice", age=25)
# Output:
# Positional arguments: (1, 2, 3)
# Keyword arguments: {'name': 'Alice', 'age': 25}
```

---

### **11. Explain Python's `with` statement. Why is it used?**  
#### **Answer**:  
- The `with` statement simplifies resource management, ensuring proper acquisition and release of resources, such as file handles or locks.  
- It is commonly used with context managers.  

#### **Example**:  
```python
with open("example.txt", "r") as file:
    content = file.read()
# The file is automatically closed, even if an error occurs.
```

#### **Why Use It?**  
- Ensures resources are released promptly, avoiding resource leaks.  
- Makes the code cleaner and easier to read.

---

### **12. Explain list comprehension with an example.**  
#### **Answer**:  
List comprehension is a concise way to create lists by iterating over an iterable and optionally applying conditions or transformations.  

#### **Example**:  
```python
# Traditional way
squares = []
for i in range(5):
    squares.append(i ** 2)

# Using list comprehension
squares = [i ** 2 for i in range(5)]
print(squares)  # Output: [0, 1, 4, 9, 16]
```

---

### **13. What are Python's `lambda` functions? Provide an example.**  
#### **Answer**:  
- **Lambda functions** are anonymous functions defined using the `lambda` keyword.  
- They are typically used for short, simple operations.  

#### **Example**:  
```python
add = lambda x, y: x + y
print(add(3, 5))  # Output: 8
```
 

 ### **1. Python Programming Fundamentals**

#### 1. **Explain the difference between Python 2 and Python 3.**

- **Python 2**: 
  - Python 2.x is an older version, and its final release was Python 2.7 (in 2010).
  - It uses `print` as a statement (`print "Hello"`).
  - Division of integers results in integer output (e.g., `3/2 = 1`).
  - Unicode strings must be explicitly defined using `u"string"`.
  
- **Python 3**:
  - Python 3.x is the current and actively supported version (since 2008).
  - `print` is a function (`print("Hello")`).
  - Division of integers results in float output (e.g., `3/2 = 1.5`).
  - Unicode strings are the default (`"string"` is Unicode by default).

**Summary**: Python 3 introduced various improvements, but it is not backward compatible with Python 2. As of January 1, 2020, Python 2 is no longer supported.

#### 2. **How does Python's Global Interpreter Lock (GIL) work, and how does it affect multithreading?**

The **Global Interpreter Lock (GIL)** is a mutex that allows only one thread to execute Python bytecode at a time in a single process. While Python threads can run concurrently, the GIL prevents multiple threads from executing in parallel on multiple cores, making CPU-bound tasks slower in multithreading contexts.

- **Effect on multithreading**: For **I/O-bound tasks** (e.g., network requests, file reading), threads can still be useful because the GIL is released during I/O operations. However, for **CPU-bound tasks**, the GIL can be a bottleneck, and you might see little to no improvement with multithreading. In such cases, you would typically use **multiprocessing** instead of **multithreading**.

#### 3. **What are Python's data types? Provide examples for each.**

Python has various built-in data types, categorized into:

- **Numeric Types**:
  - `int`: Integer values (e.g., `5`, `-3`).
  - `float`: Floating-point numbers (e.g., `3.14`, `-2.7`).
  - `complex`: Complex numbers (e.g., `3+4j`).

- **Sequence Types**:
  - `list`: Ordered, mutable collection (e.g., `[1, 2, 3]`).
  - `tuple`: Ordered, immutable collection (e.g., `(1, 2, 3)`).
  - `range`: Represents an immutable sequence of numbers (e.g., `range(5)`).

- **Text Type**:
  - `str`: String of characters (e.g., `"hello"`, `'world'`).

- **Mapping Type**:
  - `dict`: Key-value pairs (e.g., `{"name": "John", "age": 25}`).

- **Set Types**:
  - `set`: Unordered, mutable collection without duplicates (e.g., `{1, 2, 3}`).
  - `frozenset`: Unordered, immutable set (e.g., `frozenset([1, 2, 3])`).

- **Boolean Type**:
  - `bool`: Represents `True` or `False`.

- **Binary Types**:
  - `bytes`, `bytearray`, `memoryview`: Used for binary data manipulation.

#### 4. **What are Python decorators? Provide a use case.**

A **decorator** is a function that takes another function or method as input and extends or alters its behavior without modifying its original code.

**Use Case**: Logging the execution time of a function.

```python
import time

def timer_decorator(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"Execution time: {end_time - start_time} seconds")
        return result
    return wrapper

@timer_decorator
def slow_function():
    time.sleep(2)
    print("Function completed!")

slow_function()
```

The decorator `timer_decorator` measures and prints the execution time of `slow_function`.

#### 5. **Explain the difference between shallow copy and deep copy.**

- **Shallow Copy**:
  - A shallow copy creates a new object, but it does not copy the inner objects. Instead, it copies references to the original objects.
  - Use `copy()` or `copy.copy()`.
  
  ```python
  import copy
  original = [1, [2, 3]]
  shallow = copy.copy(original)
  shallow[1][0] = 100
  print(original)  # Output: [1, [100, 3]]
  ```

- **Deep Copy**:
  - A deep copy creates a completely new object and recursively copies all objects within the original object.
  - Use `copy.deepcopy()`.
  
  ```python
  import copy
  original = [1, [2, 3]]
  deep = copy.deepcopy(original)
  deep[1][0] = 100
  print(original)  # Output: [1, [2, 3]]
  ```

#### 6. **How does garbage collection work in Python?**

Python uses **automatic garbage collection** to manage memory. It employs two primary techniques:
- **Reference counting**: Every object in Python has a reference count, which is incremented when a reference to the object is created and decremented when it is deleted. When the reference count reaches zero, the object is deallocated.
  
- **Cycle detector**: For cyclic references (e.g., an object referring to itself), Python uses a garbage collector that identifies and cleans up unreachable cyclic structures.

You can manually invoke garbage collection with the `gc` module using `gc.collect()`.

#### 7. **What are Python's mutable and immutable data types? Give examples.**

- **Mutable**: Objects whose state can be changed after creation.
  - `list`: `[1, 2, 3]`
  - `dict`: `{"name": "John"}`
  - `set`: `{1, 2, 3}`

- **Immutable**: Objects whose state cannot be changed after creation.
  - `int`: `5`
  - `str`: `"hello"`
  - `tuple`: `(1, 2, 3)`
  - `frozenset`: `frozenset([1, 2, 3])`

#### 8. **Write a Python function to check if a string is a palindrome.**

```python
def is_palindrome(s):
    s = s.lower().replace(" ", "")  # Ignore case and spaces
    return s == s[::-1]

# Test
print(is_palindrome("A man a plan a canal Panama"))  # True
```

This function ignores spaces and case to check if a string is a palindrome.

#### 9. **What are list comprehensions? How are they different from generator expressions?**

- **List Comprehension**:
  - A concise way to create lists.
  - Example: `[x * 2 for x in range(5)]` results in `[0, 2, 4, 6, 8]`.
  
- **Generator Expression**:
  - Similar to list comprehensions, but it returns a generator object instead of a list.
  - Example: `(x * 2 for x in range(5))` returns a generator object, which yields items on demand.

**Difference**: 
- List comprehensions store all values in memory, whereas generator expressions are lazy and yield items one by one, which saves memory.

#### 10. **How can you handle missing keys in Python dictionaries?**

- **Using `get()` method**: This method returns `None` (or a specified default value) if the key is not found.
  
  ```python
  my_dict = {"name": "Alice"}
  print(my_dict.get("age", "Not Found"))  # Output: Not Found
  ```

- **Using `setdefault()` method**: This method returns the value for the key if it exists, and inserts the key with a specified default value if it does not.
  
  ```python
  my_dict = {"name": "Alice"}
  print(my_dict.setdefault("age", 25))  # Output: 25
  ```

- **Using `try-except` block**: If you want to catch the `KeyError` exception when accessing a missing key.
  
  ```python
  try:
      value = my_dict["age"]
  except KeyError:
      value = "Key not found"
  ```