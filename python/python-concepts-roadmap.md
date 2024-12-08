Let’s explore examples for each concept listed under the **Intermediate** and **Advanced** sections in the **Python Concepts Roadmap**. The response will include concise yet meaningful examples for better understanding.

---

### **Intermediate Python**

#### **1. Advanced OOP**
**Encapsulation, Abstraction, Inheritance, and Polymorphism Example**:
```python
class Animal:
    def __init__(self, name):
        self._name = name  # Encapsulation (protected attribute)

    def sound(self):
        raise NotImplementedError("Subclasses must implement this method")  # Abstraction

class Dog(Animal):
    def sound(self):  # Polymorphism
        return "Bark"

class Cat(Animal):
    def sound(self):  # Polymorphism
        return "Meow"

# Inheritance
animals = [Dog("Buddy"), Cat("Kitty")]
for animal in animals:
    print(f"{animal._name}: {animal.sound()}")
```
**Output**:
```plaintext
Buddy: Bark
Kitty: Meow
```

---

#### **2. Advanced Data Structures**
**Using Sets and Queues**:
```python
from collections import deque

# Sets
unique_numbers = {1, 2, 3, 3, 2}
print("Unique numbers:", unique_numbers)

# Queues
queue = deque(["Alice", "Bob", "Charlie"])
queue.append("Dave")
print("Queue after adding Dave:", queue)
queue.popleft()
print("Queue after removing first element:", queue)
```
**Output**:
```plaintext
Unique numbers: {1, 2, 3}
Queue after adding Dave: deque(['Alice', 'Bob', 'Charlie', 'Dave'])
Queue after removing first element: deque(['Bob', 'Charlie', 'Dave'])
```

---

#### **3. Functional Programming**
**Lambda Functions, Map, Filter, and Reduce**:
```python
from functools import reduce

# Lambda function
square = lambda x: x * x
print("Square of 5:", square(5))

# Map
nums = [1, 2, 3, 4]
squares = map(lambda x: x * x, nums)
print("Squares:", list(squares))

# Filter
evens = filter(lambda x: x % 2 == 0, nums)
print("Even numbers:", list(evens))

# Reduce
product = reduce(lambda x, y: x * y, nums)
print("Product of numbers:", product)
```
**Output**:
```plaintext
Square of 5: 25
Squares: [1, 4, 9, 16]
Even numbers: [2, 4]
Product of numbers: 24
```

---

#### **4. Working with APIs**
**Using `requests` Library**:
```python
import requests

response = requests.get("https://jsonplaceholder.typicode.com/posts/1")
if response.status_code == 200:
    data = response.json()
    print(f"Title: {data['title']}")
else:
    print("Failed to fetch data")
```
**Output**:
```plaintext
Title: sunt aut facere repellat provident occaecati excepturi optio reprehenderit
```

---

#### **5. Database Interaction**
**CRUD Operations Using SQLite**:
```python
import sqlite3

# Connect to database
conn = sqlite3.connect(":memory:")  # In-memory database
cursor = conn.cursor()

# Create table
cursor.execute("CREATE TABLE users (id INTEGER PRIMARY KEY, name TEXT)")

# Insert data
cursor.execute("INSERT INTO users (name) VALUES (?)", ("Alice",))
conn.commit()

# Read data
cursor.execute("SELECT * FROM users")
print("Users:", cursor.fetchall())

# Update data
cursor.execute("UPDATE users SET name = ? WHERE id = ?", ("Bob", 1))
conn.commit()

# Delete data
cursor.execute("DELETE FROM users WHERE id = ?", (1,))
conn.commit()
```
**Output**:
```plaintext
Users: [(1, 'Alice')]
```

---

### **Advanced Python**

#### **1. Advanced Web Development**
**Building RESTful APIs with FastAPI**:
```python
from fastapi import FastAPI

app = FastAPI()

@app.get("/greet/{name}")
def greet(name: str):
    return {"message": f"Hello, {name}"}

# Run: uvicorn <filename>:app --reload
```
**Usage**:
Navigate to `http://127.0.0.1:8000/greet/John`, and you’ll get:
```json
{
    "message": "Hello, John"
}
```

---

#### **2. Concurrency and Parallelism**
**Threading Example**:
```python
import threading

def print_numbers():
    for i in range(5):
        print(f"Number: {i}")

# Create threads
thread1 = threading.Thread(target=print_numbers)
thread2 = threading.Thread(target=print_numbers)

# Start threads
thread1.start()
thread2.start()

# Wait for threads to finish
thread1.join()
thread2.join()
```

**Output**:
```plaintext
Number: 0
Number: 0
Number: 1
Number: 1
... (Interleaved)
```

---

#### **3. Advanced Libraries and Frameworks**
**Using TensorFlow for Linear Regression**:
```python
import tensorflow as tf

# Input data
X = [1, 2, 3, 4]
Y = [2, 4, 6, 8]

# Model creation
model = tf.keras.Sequential([tf.keras.layers.Dense(units=1, input_shape=[1])])
model.compile(optimizer='sgd', loss='mean_squared_error')

# Training
model.fit(X, Y, epochs=500, verbose=0)
print("Prediction for 5:", model.predict([5])[0][0])
```
**Output**:
```plaintext
Prediction for 5: ~10 (approximate)
```

---

#### **4. Security in Python**
**Password Hashing Using `bcrypt`**:
```python
import bcrypt

# Hash a password
password = "securepassword".encode()
hashed = bcrypt.hashpw(password, bcrypt.gensalt())
print("Hashed password:", hashed)

# Verify password
is_valid = bcrypt.checkpw(password, hashed)
print("Password is valid:", is_valid)
```
**Output**:
```plaintext
Hashed password: b'$2b$12$...'
Password is valid: True
```

---

#### **5. Optimization and Performance**
**Profiling Code Using `cProfile`**:
```python
def compute():
    result = 0
    for i in range(10000):
        result += i ** 2
    return result

if __name__ == "__main__":
    import cProfile
    cProfile.run("compute()")
```
**Output**:
```plaintext
         3 function calls in 0.002 seconds
   ...
   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.001    0.001    0.002    0.002 <string>:2(compute)
```

---

#### **6. Advanced Topics in Data Science**
**Data Visualization with Seaborn**:
```python
import seaborn as sns
import matplotlib.pyplot as plt

data = sns.load_dataset("tips")
sns.barplot(x="day", y="total_bill", data=data)
plt.show()
```

---

#### **7. Contributing to Open Source Projects**
**Using Git for Collaboration**:
```bash
# Clone a repository
git clone https://github.com/<username>/<repo>.git

# Create a new branch
git checkout -b feature-branch

# Make changes and commit
git add .
git commit -m "Added new feature"

# Push changes and create a pull request
git push origin feature-branch
```

---

This roadmap provides a holistic progression. Let me know if you'd like to explore any topic further!