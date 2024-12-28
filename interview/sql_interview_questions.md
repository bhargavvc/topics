# SQL and Databases Interview Questions and Answers

### **3. SQL and Databases**

21. **What are the differences between SQL and NoSQL databases?**
   - **SQL Databases**: 
     - Structured data with a predefined schema.
     - Use SQL (Structured Query Language) for querying.
     - Examples: MySQL, PostgreSQL, Oracle.
   - **NoSQL Databases**: 
     - Unstructured or semi-structured data with flexible schemas.
     - Use various data models (document, key-value, graph).
     - Examples: MongoDB, Cassandra, Redis.

22. **Write a SQL query to find duplicate entries in a table.**
   ```sql
   SELECT column_name, COUNT(*)
   FROM table_name
   GROUP BY column_name
   HAVING COUNT(*) > 1;
   ```

23. **How do you optimize SQL queries for performance?**
   - Use indexing to speed up data retrieval.
   - Avoid SELECT *; specify only the columns needed.
   - Use WHERE clauses to filter data early.
   - Analyze and optimize query execution plans.

24. **What is indexing, and how does it improve query performance?**
   - Indexing is a data structure technique that improves the speed of data retrieval operations on a database table. It creates a separate data structure that allows the database to find rows more quickly, reducing the amount of data scanned during queries.

25. **Explain the difference between INNER JOIN, LEFT JOIN, and RIGHT JOIN.**
   - **INNER JOIN**: Returns records that have matching values in both tables.
   - **LEFT JOIN**: Returns all records from the left table and matched records from the right table; if no match, NULL values are returned for right table columns.
   - **RIGHT JOIN**: Returns all records from the right table and matched records from the left table; if no match, NULL values are returned for left table columns.

26. **What are the ACID properties of a database?**
   - **Atomicity**: Ensures that all operations within a transaction are completed successfully; if not, the transaction is aborted.
   - **Consistency**: Ensures that a transaction brings the database from one valid state to another, maintaining all predefined rules.
   - **Isolation**: Ensures that transactions are executed in isolation from one another, preventing concurrent transactions from affecting each other.
   - **Durability**: Ensures that once a transaction is committed, it remains so, even in the event of a system failure.

27. **Write a query to fetch the top 3 highest salaries from an employee table.**
   ```sql
   SELECT *
   FROM employee
   ORDER BY salary DESC
   LIMIT 3;
   ```

28. **How do transactions work in SQL, and how can you implement them in Python?**
   - Transactions in SQL are a sequence of operations performed as a single logical unit of work. They ensure data integrity. In Python, you can implement transactions using the `commit()` and `rollback()` methods with a database connection.
   ```python
   connection = sqlite3.connect('database.db')
   cursor = connection.cursor()
   try:
       cursor.execute("INSERT INTO table_name (column) VALUES (value)")
       connection.commit()  # Commit the transaction
   except:
       connection.rollback()  # Rollback in case of error
   ```

29. **How does connection pooling work in databases?**
   - Connection pooling is a technique used to maintain a pool of database connections that can be reused, rather than opening a new connection for each request. This improves performance by reducing the overhead of establishing connections. When a connection is no longer needed, it is returned to the pool for reuse.

30. **What is the difference between UNION and UNION ALL?**
   - **UNION**: Combines the result sets of two or more SELECT statements and removes duplicate rows.
   - **UNION ALL**: Combines the result sets of two or more SELECT statements and includes all rows, including duplicates.
