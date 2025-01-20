### **Stage 1: Opening and General Questions**

---

#### **1. Can you brief about your experience?**  
- **Answer:**  
  I have over 5+ years of experience in backend development, building web applications, and designing scalable systems. I’m proficient in Python, Django, and REST APIs. I have also worked on cloud technologies, deployment, and data cleaning. My key contributions include implementing caching mechanisms like Redis for frequent queries, bulk upload features, and global search functionalities.

---

#### **2. What projects have you worked on recently?**  
- **Answer:**  
  - **Medical Coding and Claims Processing Projects (Waterlabs):**  
    - Developed bulk upload features.  
    - Integrated global search functionality with auto-suggestions.  
    - Implemented Redis caching for frequent DB queries.  
  - **SMB Project:**  
    - Worked on data cleaning, user templates, and managing Excel file operations.

---

#### **3. Can you explain the logic of JWT token-based authentication?**  
- **Answer:**  
  - **JWT Token Authentication Logic:**
    - Authentication requires defining permission classes and authentication classes.
    - Use JWT base authentication classes for validating tokens.
    - Tokens are generated using default libraries and configured in the settings file.
    - Token lifetime and refresh intervals are defined to ensure secure access.
    - Middleware extracts bearer tokens from headers and validates them.

---

#### **4. Can you explain joins in SQL (e.g., left join, right join, self-join)?**  
- **Answer:**  
  - **Left Join:** Returns all rows from the left table and matching rows from the right table. Non-matching rows in the right table are null.  
  - **Right Join:** Returns all rows from the right table and matching rows from the left table. Non-matching rows in the left table are null.  
  - **Self-Join:** A table is joined with itself, often using aliases, to compare rows within the same table.  

Example:  
```sql
SELECT a.name, b.manager_name
FROM employees a
LEFT JOIN employees b ON a.manager_id = b.id;
```

---

### **Stage 2: Problem Solving**

---

#### **5. How would you handle a dynamic data frame to perform operations based on user input?**  
- **Answer:**  
  - Use `pandas` to load and manipulate the data frame dynamically:
    ```python
    import pandas as pd

    # Example DataFrame
    data = {'Region': ['North', 'South'], 'Value': [10, 20]}
    df = pd.DataFrame(data)

    # Perform operations based on user input
    region_input = "North"
    value_multiplier = 2
    df['Value'] = df.apply(
        lambda row: row['Value'] * value_multiplier if row['Region'] == region_input else row['Value'],
        axis=1
    )
    print(df)
    ```

---

#### **6. How do you handle missing values in a data frame?**  
- **Answer:**  
  - Fill missing values using `fillna()`:
    ```python
    df.fillna(value=0, inplace=True)
    ```
  - Drop rows with missing values:
    ```python
    df.dropna(inplace=True)
    ```
  - Interpolate to estimate missing values:
    ```python
    df.interpolate(method='linear', inplace=True)
    ```

---

#### **7. Explain the iterative approach for handling large datasets.**  
- **Answer:**  
  - Use chunking to process large files:
    ```python
    chunk_size = 1000
    for chunk in pd.read_csv("large_file.csv", chunksize=chunk_size):
        process(chunk)
    ```
  - Use memory-efficient data types (e.g., `float32` instead of `float64`).
  - Avoid loading entire datasets into memory; use database queries or lazy evaluation.

---

### **Stage 3: OOP and System Design**

---

#### **8. Can you design a scalable system to handle bulk data uploads and queries?**  
- **Answer:**  
  - **Architecture:**
    - Use a message queue (e.g., RabbitMQ or Kafka) to handle bulk data uploads asynchronously.
    - Implement a caching layer (e.g., Redis) for frequently accessed data.
    - Use scalable storage (e.g., AWS S3) for file uploads.
  - **Components:**
    - **API Gateway:** Handles user authentication and request routing.
    - **Worker Services:** Processes bulk uploads and performs validations.
    - **Database:** Stores processed data in a normalized format.
    - **Search Engine (e.g., Elasticsearch):** Provides fast query responses.

---

#### **9. How would you approach building an AI-focused feature for a contact center?**  
- **Answer:**  
  - **Components:**
    - AI agents for handling domain-specific queries.
    - NLP models to understand and process user input.
    - Integration with existing CRM systems to fetch and update customer data.
  - **Implementation:**
    - Use pre-trained models (e.g., GPT or BERT) for conversational AI.
    - Continuously train models with domain-specific data to improve accuracy.

---

### **Stage 4: Behavioral and Miscellaneous**

---

#### **10. How do you approach learning new technologies like AI?**  
- **Answer:**  
  - Start with the fundamentals, such as machine learning pipelines and basic NLP concepts.
  - Experiment with pre-trained models and open-source frameworks.
  - Work on small, real-world projects to solidify understanding.

---

#### **11. What motivates you to focus on AI as part of your career growth?**  
- **Answer:**  
  - The rapid adoption of AI in various industries and its potential to replace traditional roles motivates me to upskill. AI proficiency will help me remain competitive and contribute to building innovative solutions.

---

#### **12. How do you handle feedback during interviews?**  
- **Answer:**  
  - I view feedback as an opportunity for growth. I take notes, analyze areas of improvement, and work on refining my skills and approach to better align with expectations.

---

Let me know if you’d like to expand on any specific sections or add more detailed problem-solving examples!