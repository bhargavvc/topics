### **Stage 1: General and Opening Questions**

---

#### **1. Can you briefly introduce yourself?**  
- **Answer:**  
  I have over 5 years of experience developing web applications and implementing business solutions using Python, Django, REST APIs, and cloud technologies like AWS and GCP. My expertise includes building scalable backends, designing APIs, handling data transformation, and exploring AI and deployment technologies in my free time. I also have experience managing teams and contributing as both a developer and leader.

---

#### **2. What are some key projects you’ve worked on?**  
- **Answer:**  
  - **Bulk Upload Process Implementation:** Designed a robust system for validating and processing bulk data uploads efficiently.  
  - **Single Sign-On (SSO):** Implemented SSO using JWT for secure authentication across multiple services.  
  - **FastAPI Services:** Built services using FastAPI for faster and scalable API handling.  
  - **Data Cleaning and Transformation:** Segregated redundant data into a normalized structure and optimized server requests to reduce costs.  

---

#### **3. What are your current responsibilities in your role?**  
- **Answer:**  
  I lead a team of 5–6 members, including backend developers, frontend developers, and testers. I manage API development, guide the team on project deliverables, and occasionally act as an individual contributor. Additionally, I oversee end-to-end project lifecycles, including query and standalone project development.

---

#### **4. How do you explore technologies in your free time?**  
- **Answer:**  
  I dedicate time after work to exploring technologies beyond my role, such as front-end tools, deployment techniques, and AI applications. For example, I’ve worked with Node.js, GraphQL, and MongoDB to extend my skill set.

---

### **Stage 2: Technical Concepts**

---

#### **5. How do you handle large datasets that do not fit into memory?**  
- **Answer:**  
  - **Chunk Processing:** Read data in chunks using Pandas or SQL `LIMIT` and `OFFSET`.  
  - **Lazy Evaluation:** Use generators to load data incrementally.  
  - **Binary Formats:** Utilize Parquet or HDF5 for compact storage and efficient reads.  
  - **Data Cleaning:** Remove unnecessary rows or columns to minimize data size before processing.  
  - **Libraries:** Use tools like Dask or PySpark for distributed data processing.

---

#### **6. How do you integrate data from external APIs into a Python application? What challenges do you face?**  
- **Answer:**  
  - **Integration Process:**
    - Fetch data using `requests` or `httpx` libraries.
    - Validate responses and handle authentication tokens.
    - Transform data into a usable format (e.g., JSON to DataFrame).  
  - **Challenges:**  
    - Handling rate limits and retries.
    - Dealing with authentication token expiration.
    - Validating malformed inputs or responses.  
  - **Solutions:** Implement retries with exponential backoff and use libraries like `tenacity` for robust error handling.

---

#### **7. How do you handle paginated responses while fetching large datasets from an API?**  
- **Answer:**  
  - Pass parameters like `page`, `limit`, and `offset` to API requests.  
  - Use a loop to iterate through pages until all data is retrieved.  
  - Example:
    ```python
    page = 1
    while True:
        response = requests.get(f"https://api.example.com/data?page={page}")
        data = response.json()
        if not data:
            break
        process(data)
        page += 1
    ```

---

#### **8. How do you debug performance issues in Python applications?**  
- **Answer:**  
  - Use **Python Debugger (PDB):** To inspect and control program execution step by step.  
  - **Django Debug Toolbar:** Analyze query execution times and optimize database queries.  
  - **Remote Debugging (RDB):** Debug background tasks in Celery using `telnet`.  
  - **Retry Timeouts:** Configure retry mechanisms for tasks prone to network issues.  
  - **Profiling Tools:** Use `cProfile` or `Pyinstrument` to identify bottlenecks.

---

### **Stage 3: Problem Solving**

---

#### **9. Write a program to find the longest substring without repeating characters.**  
- **Answer:**  
  ```python
  def longest_unique_substring(s):
      start, max_length = 0, 0
      char_map = {}

      for end in range(len(s)):
          if s[end] in char_map:
              start = max(start, char_map[s[end]] + 1)
          char_map[s[end]] = end
          max_length = max(max_length, end - start + 1)
      
      return max_length

  print(longest_unique_substring("abcabcbb"))  # Output: 3
  ```

---

#### **10. What is the difference between SQL and NoSQL databases? When would you use each?**  
- **Answer:**  
  - **SQL Databases:**  
    - Structured schema with relationships.  
    - Suitable for applications requiring ACID compliance (e.g., financial systems).  
    - Use cases: E-commerce, CRM, and ERP systems.  
  - **NoSQL Databases:**  
    - Schema-less and scalable horizontally.  
    - Ideal for unstructured or semi-structured data (e.g., JSON, logs).  
    - Use cases: Real-time analytics, IoT, and social media data.  

---

#### **11. Explain the sliding window technique.**  
- **Answer:**  
  The sliding window technique is used to find subarrays or substrings within a dataset. It maintains a subset of elements by dynamically resizing the window based on a condition.  
  - Example: Longest substring without repeating characters.  

---

### **Stage 4: Behavioral and Miscellaneous**

---

#### **12. How do you handle tight deadlines and high-pressure tasks?**  
- **Answer:**  
  I communicate with the manager to explain constraints and outline achievable deliverables. If necessary, I prioritize tasks and focus on incremental progress while maintaining transparency.

---

#### **13. Do you have experience with cloud platforms?**  
- **Answer:**  
  I have worked extensively with AWS, and recently, I attended GCP events where I earned recognition for integrating cloud solutions with DevOps tools.  

---

Let me know if you'd like me to elaborate further or if I missed any details!