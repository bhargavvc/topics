### **Stage 1: General and Opening Questions**

---

#### **1. Can you briefly introduce yourself?**  
- **Answer:**  
  I have 5 years of experience in backend development, building both monolithic and microservices-based applications. I’m proficient in Python, Django, FastAPI, and Flask. My expertise includes cloud deployments, scalable architecture design, and data handling. I am also currently exploring Generative AI.

---

#### **2. Can you describe the projects you’ve worked on?**  
- **Answer:**  
  - **Heinz Project:**  
    - A healthcare claims processing tool.  
    - Validates patient insurance details by integrating with third-party US providers.  
    - Handles claim processing and validation efficiently.  

  - **Curie Project:**  
    - A healthcare coding tool for managing CPT and HCPC codes.  
    - Features: Global search with auto-suggestions, frequent query caching using Redis, and a bulk upload functionality for validating thousands of rows.  
    - Used single sign-on (SSO) via JWT to integrate multiple clients securely.  

---

#### **3. How did you optimize token generation in one of your projects?**  
- **Answer:**  
  Previously, multiple team members were generating separate tokens for third-party services, incurring unnecessary costs. I implemented a centralized **FastAPI-based module** to generate a single shared token valid for 5 minutes. This reduced token generation requests from multiple hits to one, saving costs and time.

---

#### **4. What steps did you take to secure patient information in your healthcare projects?**  
- **Answer:**  
  - Implemented Django’s default encryption for sensitive fields like name, address, and date of birth.  
  - Used JSON responses for front-end and back-end communication, ensuring secure data exchange.  
  - Stored files on a secure media server and applied custom functions for controlled access.  

---

### **Stage 2: Technical Concepts**

---

#### **5. What is monkey patching in Python?**  
- **Answer:**  
  Monkey patching refers to dynamically modifying or extending the behavior of libraries or classes at runtime. It’s commonly used in testing to replace methods with mock implementations.

---

#### **6. What are Dunder (double underscore) methods in Python?**  
- **Answer:**  
  Dunder methods, also called magic methods, are predefined methods with double underscores (e.g., `__init__`, `__str__`). They allow customization of object behavior.  
  - Example:  
    ```python
    class Example:
        def __init__(self, name):
            self.name = name

        def __str__(self):
            return f"Name: {self.name}"

    obj = Example("Python")
    print(obj)  # Output: Name: Python
    ```

---

#### **7. What is the purpose of abstract classes in Python?**  
- **Answer:**  
  Abstract classes provide a blueprint for derived classes, ensuring that specific methods are implemented.  
  - Example:  
    ```python
    from abc import ABC, abstractmethod

    class Animal(ABC):
        @abstractmethod
        def speak(self):
            pass

    class Dog(Animal):
        def speak(self):
            return "Bark"

    dog = Dog()
    print(dog.speak())  # Output: Bark
    ```

---

#### **8. What is the difference between abstract classes and metaclasses in Python?**  
- **Answer:**  
  - **Abstract Classes:** Define a template with methods that must be implemented by derived classes.  
  - **Metaclasses:** Control the creation and behavior of classes themselves, adding features like class ordering or attribute validation.

---

#### **9. What is the Global Interpreter Lock (GIL) in Python?**  
- **Answer:**  
  The GIL ensures that only one thread executes Python bytecode at a time, even in multi-threaded programs. This limits CPU-bound operations in multi-threading but can be bypassed using multiprocessing.

---

### **Stage 3: Problem Solving**

---

#### **10. Write a Python program to find the Fibonacci series without built-in functions.**  
- **Answer:**  
  ```python
  def fibonacci(n):
      a, b = 0, 1
      for _ in range(n):
          print(a, end=" ")
          a, b = b, a + b

  fibonacci(10)  # Output: 0 1 1 2 3 5 8 13 21 34
  ```

---

#### **11. How would you find the nth largest number in a list without using built-in functions like `sort` or `max`?**  
- **Answer:**  
  ```python
  def nth_largest(arr, n):
      for _ in range(n):
          max_val = float('-inf')
          for num in arr:
              if num > max_val:
                  max_val = num
          arr.remove(max_val)
      return max_val

  print(nth_largest([3, 2, 5, 1, 4], 2))  # Output: 4
  ```

---

#### **12. Write a program to check if a number is prime.**  
- **Answer:**  
  ```python
  def is_prime(num):
      if num <= 1:
          return False
      for i in range(2, int(num**0.5) + 1):
          if num % i == 0:
              return False
      return True

  print(is_prime(7))  # Output: True
  print(is_prime(10))  # Output: False
  ```

---

### **Stage 4: Behavioral and Miscellaneous**

---

#### **13. How do you handle feedback during interviews?**  
- **Answer:**  
  I consider feedback as a valuable opportunity for self-improvement. I analyze the feedback to identify gaps in my knowledge or skills and work actively to bridge them.

---

#### **14. What motivates you to explore Generative AI?**  
- **Answer:**  
  The growing applications of AI in industries and its potential to transform traditional workflows motivate me to explore this field. It’s both a career growth opportunity and a chance to contribute to innovative solutions.

---

#### **15. How do you manage and mentor junior developers?**  
- **Answer:**  
  - Provide hands-on guidance for understanding models, indexes, and deployments.  
  - Encourage them to handle smaller features independently to build confidence.  
  - Ensure they are familiar with essential tools like VPNs and web scrapers for tasks.  

---

This structured format ensures all questions and responses from the file are addressed. Let me know if you'd like to add or adjust anything!