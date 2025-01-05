### **SQL Interview Questions and Answers**

### **1. What is the difference between `DELETE`, `TRUNCATE`, and `DROP`?**
#### **Answer**:
1. **`DELETE`**:
   - Removes specific rows from a table.
   - Can use `WHERE` clause to filter rows.
   - Logs individual row deletions; slower than `TRUNCATE`.
   - Can be rolled back.
   - Example:  
     ```sql
     DELETE FROM employees WHERE department = 'Sales';
     ```

2. **`TRUNCATE`**:
   - Removes all rows from a table without logging individual row deletions.
   - Resets table indexes (e.g., auto-increment counters).
   - Cannot use `WHERE` clause.
   - Faster than `DELETE` but cannot be rolled back in most databases.
   - Example:  
     ```sql
     TRUNCATE TABLE employees;
     ```

3. **`DROP`**:
   - Deletes the table structure and all its data.
   - Completely removes the table from the database.
   - Cannot be rolled back.
   - Example:  
     ```sql
     DROP TABLE employees;
     ```

---

### **2. What is the difference between an INNER JOIN, LEFT JOIN, RIGHT JOIN, and FULL OUTER JOIN?**
#### **Answer**:
1. **`INNER JOIN`**:
   - Returns rows where there is a match in both tables.
   - Example:  
     ```sql
     SELECT e.name, d.name
     FROM employees e
     INNER JOIN departments d ON e.department_id = d.id;
     ```

2. **`LEFT JOIN`** (or **`LEFT OUTER JOIN`**):
   - Returns all rows from the left table and matched rows from the right table.
   - Unmatched rows in the right table are filled with `NULL`.
   - Example:  
     ```sql
     SELECT e.name, d.name
     FROM employees e
     LEFT JOIN departments d ON e.department_id = d.id;
     ```

3. **`RIGHT JOIN`** (or **`RIGHT OUTER JOIN`**):
   - Returns all rows from the right table and matched rows from the left table.
   - Unmatched rows in the left table are filled with `NULL`.

4. **`FULL OUTER JOIN`**:
   - Returns all rows from both tables, filling unmatched rows with `NULL`.
   - Example:  
     ```sql
     SELECT e.name, d.name
     FROM employees e
     FULL OUTER JOIN departments d ON e.department_id = d.id;
     ```

---

### **3. What are indexes in SQL? Why are they important?**
#### **Answer**:
1. **Definition**:
   - Indexes are database objects that improve query performance by enabling faster data retrieval.

2. **Types of Indexes**:
   - **Clustered Index**: Sorts and stores data rows in the table based on the indexed column.
   - **Non-clustered Index**: Stores a pointer to the actual data.

3. **Advantages**:
   - Speeds up SELECT queries.
   - Reduces I/O operations.

4. **Disadvantages**:
   - Slows down `INSERT`, `UPDATE`, and `DELETE` operations.
   - Consumes additional storage.

5. **Example**:  
   ```sql
   CREATE INDEX idx_employee_name ON employees(name);
   ```

---

### **4. How would you optimize a slow query?**
#### **Answer**:
1. **Analyze the Query**:
   - Use `EXPLAIN` or `EXPLAIN PLAN` to understand the query execution path.

2. **Optimize Joins**:
   - Use proper join conditions and minimize the number of joins.

3. **Use Indexes**:
   - Create indexes on frequently queried columns, especially in `WHERE`, `GROUP BY`, or `ORDER BY` clauses.

4. **Avoid SELECT ***:
   - Retrieve only necessary columns.

5. **Partitioning**:
   - Split large tables into smaller, manageable pieces.

6. **Query Caching**:
   - Leverage caching mechanisms to store frequently accessed data.

---

### **5. What is a primary key? Can a table have multiple primary keys?**
#### **Answer**:
1. **Primary Key**:
   - Uniquely identifies each record in a table.
   - Automatically creates a unique index.
   - Cannot contain `NULL` values.

2. **Can a table have multiple primary keys?**
   - No, a table can only have one primary key, but the primary key can consist of multiple columns (composite primary key).

3. **Example**:
   ```sql
   CREATE TABLE employees (
       id INT PRIMARY KEY,
       name VARCHAR(100)
   );
   ```

---

### **6. What is the difference between `HAVING` and `WHERE`?**
#### **Answer**:
1. **`WHERE`**:
   - Filters rows before grouping occurs.
   - Cannot use aggregate functions.
   - Example:  
     ```sql
     SELECT department, COUNT(*)
     FROM employees
     WHERE salary > 50000
     GROUP BY department;
     ```

2. **`HAVING`**:
   - Filters groups after grouping occurs.
   - Can use aggregate functions.
   - Example:  
     ```sql
     SELECT department, COUNT(*)
     FROM employees
     GROUP BY department
     HAVING COUNT(*) > 10;
     ```

---

### **7. Explain normalization and its types.**
#### **Answer**:
1. **Normalization**:
   - Process of organizing data to reduce redundancy and improve data integrity.

2. **Types**:
   - **1NF (First Normal Form)**:
     - Eliminate duplicate columns and ensure atomic values.
   - **2NF (Second Normal Form)**:
     - Satisfy 1NF and ensure that non-key attributes depend on the primary key.
   - **3NF (Third Normal Form)**:
     - Satisfy 2NF and ensure no transitive dependencies.
   - **BCNF (Boyce-Codd Normal Form)**:
     - Stronger version of 3NF.

---

### **8. What is a foreign key? How does it ensure referential integrity?**
#### **Answer**:
1. **Foreign Key**:
   - A column or combination of columns used to establish a relationship between two tables.
   - Ensures that values in the foreign key column match values in the referenced primary key column.

2. **Referential Integrity**:
   - Prevents insertion of invalid foreign key values.
   - Prevents deletion of rows referenced by foreign keys (unless cascading is enabled).

3. **Example**:
   ```sql
   CREATE TABLE orders (
       id INT PRIMARY KEY,
       customer_id INT,
       FOREIGN KEY (customer_id) REFERENCES customers(id)
   );
   ```

---

### **9. Explain the difference between `UNION` and `UNION ALL`.**
#### **Answer**:
1. **`UNION`**:
   - Combines results of two queries and removes duplicates.
   - Slower due to the duplicate elimination step.
   - Example:  
     ```sql
     SELECT name FROM employees
     UNION
     SELECT name FROM managers;
     ```

2. **`UNION ALL`**:
   - Combines results of two queries without removing duplicates.
   - Faster as it does not check for duplicates.
   - Example:  
     ```sql
     SELECT name FROM employees
     UNION ALL
     SELECT name FROM managers;
     ```

---

### **10. What is a stored procedure? How is it different from a function?**
#### **Answer**:
1. **Stored Procedure**:
   - Precompiled SQL code that performs a specific task.
   - Can have input/output parameters.
   - Does not return a value but can return result sets.

2. **Function**:
   - Returns a single value.
   - Can be used in queries like any other expression.

3. **Example of Stored Procedure**:
   ```sql
   CREATE PROCEDURE AddEmployee (IN name VARCHAR(100), IN salary INT)
   BEGIN
       INSERT INTO employees (name, salary) VALUES (name, salary);
   END;
   ```

4. **Example of Function**:
   ```sql
   CREATE FUNCTION GetEmployeeCount() RETURNS INT
   BEGIN
       RETURN (SELECT COUNT(*) FROM employees);
   END;
   ```

Would you like to continue with more SQL questions or move to RESTful APIs, microservices, or Docker/Kubernetes topics?