
### 4. **Further Design Principles**

#### **4.1 KISS (Keep It Simple, Stupid)**
*Simplify to reduce complexity.*

**Example:**
```python
# Avoid complex one-liners
result = sum([x**2 for x in data if x > 0 and x % 2 == 0])

# Simplify
result = 0
for x in data:
    if x > 0 and x % 2 == 0:
        result += x**2
```

---

#### **4.2 DRY (Don't Repeat Yourself)**
*Avoid duplication.*

**Example (Without DRY):**
```python
def calculate_circle_area(radius):
    return 3.14 * radius * radius

def calculate_sphere_area(radius):
    return 4 * 3.14 * radius * radius
```
**Example (With DRY):**
```python
PI = 3.14

def calculate_circle_area(radius):
    return PI * radius * radius

def calculate_sphere_area(radius):
    return 4 * calculate_circle_area(radius)
```

---

#### **4.3 YAGNI (You Ain't Gonna Need It)**
*Build only what you need.*

**Example:**  
Don’t add a logging system for a small script unless there’s a need for it.

---

#### **4.4 Law of Demeter (LoD)**
*Talk only to immediate friends.*

**Example (Without LoD):**
```python
user.get_address().get_city().get_zipcode()
```
**Example (With LoD):**
```python
user.get_zipcode()
```
Delegate responsibility to the `User` class instead of chaining calls.

---
