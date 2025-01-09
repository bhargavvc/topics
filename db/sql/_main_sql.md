Below is a comprehensive beginner-to-advanced explanation of the main SQL concepts illustrated in the mindmap. We will use **Customers** and **Orders** tables for examples. For each topic/command, we’ll follow this format:

1. **Topic/Command Name**  
2. **When to use this topic/command**  
3. **Example**  
4. **SQL Syntax**  
5. **Output**  

---

## 1. DDL (Data Definition Language)

---

### A. CREATE
1. **Topic/Command Name:** `CREATE` (Database, Table, View)  
2. **When to use:**  
   - To create a new database object (table, view, etc.).  
3. **Example:** Creating a new **Customers** table.  
4. **SQL Syntax:**
   ```sql
   CREATE TABLE Customers (
       CustomerID INT PRIMARY KEY,
       FirstName  VARCHAR(50),
       LastName   VARCHAR(50),
       Email      VARCHAR(100),
       Phone      VARCHAR(20)
   );
   ```
5. **Output:**  
   - If successful, your SQL client typically shows something like:  
     ```
     Table Customers created successfully
     ```
   - The new table structure will be available in the database.

---

### B. DROP
1. **Topic/Command Name:** `DROP` (Database, Table, View)  
2. **When to use:**  
   - To *permanently* remove a database object.  
   - This **cannot** be undone (all data is lost).  
3. **Example:** Dropping the **Customers** table.  
4. **SQL Syntax:**
   ```sql
   DROP TABLE Customers;
   ```
5. **Output:**  
   - Example message:  
     ```
     Table Customers dropped successfully
     ```
   - The `Customers` table will no longer exist in the database.

---

### C. TRUNCATE
1. **Topic/Command Name:** `TRUNCATE`  
2. **When to use:**  
   - To quickly remove *all* rows from a table while keeping its structure.  
   - Often faster than `DELETE` without `WHERE`, because it deallocates data pages instead of deleting row by row.  
3. **Example:** Truncating the **Orders** table.  
4. **SQL Syntax:**
   ```sql
   TRUNCATE TABLE Orders;
   ```
5. **Output:**  
   - Example message:  
     ```
     Table Orders truncated successfully
     ```
   - After truncation, the `Orders` table will be empty but still exists in the database.

---

### D. ALTER
1. **Topic/Command Name:** `ALTER`  
2. **When to use:**  
   - To modify an existing table’s structure (adding/removing/changing columns or constraints).  
3. **Example:** Adding a new column `Address` to the **Customers** table.  
4. **SQL Syntax:**
   ```sql
   ALTER TABLE Customers
   ADD Address VARCHAR(200);
   ```
5. **Output:**  
   - Example message:  
     ```
     Table Customers altered successfully
     ```
   - The `Customers` table now has a new `Address` column.

---

## 2. DML (Data Manipulation Language)

---

### A. SELECT
1. **Topic/Command Name:** `SELECT`  
2. **When to use:**  
   - To read/retrieve data from one or more tables.  
3. **Example:** Selecting all columns from the **Customers** table.  
4. **SQL Syntax:**
   ```sql
   SELECT *
   FROM Customers;
   ```
5. **Output:**  
   - Displays all rows and columns from the `Customers` table, e.g.:

     | CustomerID | FirstName | LastName | Email             | Phone       | Address         |
     |------------|-----------|----------|-------------------|-------------|-----------------|
     | 1          | John      | Doe      | [email protected]  | 123-456-7890 | 123 Elm Street  |
     | 2          | Jane      | Smith    | [email protected]   | 555-555-1212 | 456 Oak Avenue  |
     | ...        | ...       | ...      | ...               | ...         | ...             |

---

### B. INSERT
1. **Topic/Command Name:** `INSERT`  
2. **When to use:**  
   - To add new rows into a table.  
3. **Example:** Adding a new record into **Customers**.  
4. **SQL Syntax:**
   ```sql
   INSERT INTO Customers (CustomerID, FirstName, LastName, Email, Phone, Address)
   VALUES (3, 'Alice', 'Johnson', 'alice.johnson@example.com', '987-654-3210', '789 Pine Road');
   ```
5. **Output:**  
   - Example message:  
     ```
     1 row inserted
     ```
   - A new row with CustomerID = 3 is added to the `Customers` table.

---

### C. UPDATE
1. **Topic/Command Name:** `UPDATE`  
2. **When to use:**  
   - To modify existing rows in a table.  
   - Often used with a `WHERE` clause to avoid updating all rows accidentally.  
3. **Example:** Updating a **Customer**’s phone number.  
4. **SQL Syntax:**
   ```sql
   UPDATE Customers
   SET Phone = '111-222-3333'
   WHERE CustomerID = 3;
   ```
5. **Output:**  
   - Example message:  
     ```
     1 row updated
     ```
   - The row with `CustomerID = 3` now has the updated phone number.

---

### D. DELETE
1. **Topic/Command Name:** `DELETE`  
2. **When to use:**  
   - To remove one or more rows from a table.  
3. **Example:** Deleting a **Customer** record by ID.  
4. **SQL Syntax:**
   ```sql
   DELETE FROM Customers
   WHERE CustomerID = 3;
   ```
5. **Output:**  
   - Example message:  
     ```
     1 row deleted
     ```
   - The row with `CustomerID = 3` is removed from the table.

---

## 3. DCL (Data Control Language)

---

### A. GRANT
1. **Topic/Command Name:** `GRANT`  
2. **When to use:**  
   - To give user(s) privileges (e.g., SELECT, INSERT, UPDATE) on database objects.  
3. **Example:** Granting SELECT permission on the **Customers** table to user `bob`.  
4. **SQL Syntax:**
   ```sql
   GRANT SELECT ON Customers TO bob;
   ```
5. **Output:**  
   - Example message:
     ```
     Grant succeeded
     ```
   - User `bob` can now run `SELECT` queries on the `Customers` table.

---

### B. REVOKE
1. **Topic/Command Name:** `REVOKE`  
2. **When to use:**  
   - To remove previously granted privileges from user(s).  
3. **Example:** Revoking SELECT permission on **Customers** from user `bob`.  
4. **SQL Syntax:**
   ```sql
   REVOKE SELECT ON Customers FROM bob;
   ```
5. **Output:**  
   - Example message:
     ```
     Revoke succeeded
     ```
   - User `bob` will no longer have permission to `SELECT` from `Customers`.

---

## 4. TCL (Transaction Control Language)

---

### A. COMMIT
1. **Topic/Command Name:** `COMMIT`  
2. **When to use:**  
   - To permanently save all changes (INSERT/UPDATE/DELETE) made in the current transaction.  
3. **Example:** After multiple data changes in **Orders**, you want to save them.  
4. **SQL Syntax:**
   ```sql
   COMMIT;
   ```
5. **Output:**  
   - Example message:
     ```
     Transaction committed
     ```
   - All changes in the transaction are now permanent.

---

### B. ROLLBACK
1. **Topic/Command Name:** `ROLLBACK`  
2. **When to use:**  
   - To undo changes made in the current transaction since the last `COMMIT` or `SAVEPOINT`.  
3. **Example:** You inserted incorrect data into **Orders** and want to revert it.  
4. **SQL Syntax:**
   ```sql
   ROLLBACK;
   ```
5. **Output:**  
   - Example message:
     ```
     Transaction rolled back
     ```
   - All changes are reverted to the state before the transaction began (or last savepoint).

---

### C. SAVEPOINT
1. **Topic/Command Name:** `SAVEPOINT`  
2. **When to use:**  
   - To create a sub-transaction checkpoint you can roll back to without rolling back the entire transaction.  
3. **Example:** Updating multiple rows in **Customers**, but setting a savepoint before each row.  
4. **SQL Syntax:**
   ```sql
   SAVEPOINT sp1;
   ```
5. **Output:**  
   - No direct output message in many systems, but you can see:
     ```
     Savepoint created
     ```
   - You can `ROLLBACK TO sp1;` to revert to that point.

---

## 5. Aliases (AS)

1. **Topic/Command Name:** Alias using `AS` (for columns, tables)  
2. **When to use:**  
   - To give a temporary name (alias) to a table or a column in a query result for readability.  
3. **Example:** Selecting `FirstName` and aliasing it as `CustomerFirstName`.  
4. **SQL Syntax:**
   ```sql
   SELECT 
       FirstName AS CustomerFirstName, 
       LastName AS CustomerLastName
   FROM Customers AS C;
   ```
5. **Output:**  
   - Column headers in the result set are now `CustomerFirstName` and `CustomerLastName`.  
   - Example:

     | CustomerFirstName | CustomerLastName |
     |-------------------|------------------|
     | John              | Doe             |
     | Jane              | Smith           |

---

## 6. ORDER BY

1. **Topic/Command Name:** `ORDER BY` (ASC or DESC)  
2. **When to use:**  
   - To sort the result set by one or more columns in ascending (ASC) or descending (DESC) order.  
3. **Example:** Get all customers ordered by last name descending.  
4. **SQL Syntax:**
   ```sql
   SELECT *
   FROM Customers
   ORDER BY LastName DESC;
   ```
5. **Output:**  
   - The result set is sorted so the `LastName` that comes last alphabetically appears first.

---

## 7. JOIN

There are several types of joins (INNER, FULL, LEFT, RIGHT). We’ll use **Customers** and **Orders** for example.

### A. INNER JOIN
1. **Topic/Command Name:** `INNER JOIN`  
2. **When to use:**  
   - To retrieve only matching records from both tables.  
3. **Example:** Get all orders along with the matching customer details.  
4. **SQL Syntax:**
   ```sql
   SELECT C.CustomerID, C.FirstName, C.LastName, O.OrderID, O.OrderDate
   FROM Customers AS C
   INNER JOIN Orders AS O
     ON C.CustomerID = O.CustomerID;
   ```
5. **Output:**  
   - Only shows rows where `Customers.CustomerID = Orders.CustomerID`.  
   - Example:

     | CustomerID | FirstName | LastName | OrderID | OrderDate   |
     |------------|-----------|----------|---------|-------------|
     | 1          | John      | Doe      | 101     | 2025-01-05  |
     | 1          | John      | Doe      | 102     | 2025-01-06  |
     | 2          | Jane      | Smith    | 103     | 2025-01-07  |
     | ...        | ...       | ...      | ...     | ...         |

---

### B. LEFT JOIN
1. **Topic/Command Name:** `LEFT JOIN`  
2. **When to use:**  
   - To retrieve all rows from the left table (`Customers`) and matched rows from the right table (`Orders`).  
   - If no match, the result for the right side is `NULL`.  
3. **Example:** Get customers and their orders if available.  
4. **SQL Syntax:**
   ```sql
   SELECT C.CustomerID, C.FirstName, C.LastName, O.OrderID, O.OrderDate
   FROM Customers AS C
   LEFT JOIN Orders AS O
     ON C.CustomerID = O.CustomerID;
   ```
5. **Output:**  
   - Includes all `Customers`, even those with no `Orders` (those rows show `NULL` in order fields).  
   - Example:

     | CustomerID | FirstName | LastName | OrderID | OrderDate   |
     |------------|-----------|----------|---------|-------------|
     | 1          | John      | Doe      | 101     | 2025-01-05  |
     | 1          | John      | Doe      | 102     | 2025-01-06  |
     | 3          | Alice     | Johnson  | NULL    | NULL        | <-- No matching order

---

### C. RIGHT JOIN
1. **Topic/Command Name:** `RIGHT JOIN`  
2. **When to use:**  
   - To retrieve all rows from the right table (`Orders`) and matched rows from the left table (`Customers`).  
   - If no match, the result for the left side is `NULL`.  
3. **Example:** Get all orders and their customers if available.  
4. **SQL Syntax:**
   ```sql
   SELECT C.CustomerID, C.FirstName, C.LastName, O.OrderID, O.OrderDate
   FROM Customers AS C
   RIGHT JOIN Orders AS O
     ON C.CustomerID = O.CustomerID;
   ```
5. **Output:**  
   - Includes all `Orders`, even if there’s no matching customer (which would yield `NULL` for customer columns).  

---

### D. FULL JOIN (or FULL OUTER JOIN)
1. **Topic/Command Name:** `FULL JOIN` / `FULL OUTER JOIN`  
2. **When to use:**  
   - To retrieve all rows when there’s a match in either table.  
   - Rows that don’t have matching data in the other table will have `NULL` in the columns for that table.  
3. **Example:** Get all records from `Customers` and `Orders`.  
4. **SQL Syntax:** (Not supported in some systems like MySQL without workarounds)
   ```sql
   SELECT C.CustomerID, C.FirstName, C.LastName, O.OrderID, O.OrderDate
   FROM Customers AS C
   FULL OUTER JOIN Orders AS O
     ON C.CustomerID = O.CustomerID;
   ```
5. **Output:**  
   - All rows from both `Customers` and `Orders`.  
   - Rows that don’t match in the other table are filled with `NULL` for that table’s columns.

---

## 8. GROUP BY

1. **Topic/Command Name:** `GROUP BY`  
2. **When to use:**  
   - Often used with aggregate functions (e.g., `COUNT`, `SUM`, `AVG`) to group rows by one or more columns.  
3. **Example:** Count how many orders each customer made.  
4. **SQL Syntax:**
   ```sql
   SELECT CustomerID, COUNT(*) AS NumberOfOrders
   FROM Orders
   GROUP BY CustomerID;
   ```
5. **Output:**  
   - Shows each `CustomerID` with the total count of orders.  
   - Example:

     | CustomerID | NumberOfOrders |
     |------------|----------------|
     | 1          | 2              |
     | 2          | 1              |
     | 3          | 0              | <-- If there's no matching row, might not appear unless using an OUTER JOIN

---

### HAVING
1. **Topic/Command Name:** `HAVING`  
2. **When to use:**  
   - To filter groups after the `GROUP BY` based on some condition.  
   - Similar to `WHERE` but for grouped results.  
3. **Example:** Return only customers who have made more than 1 order.  
4. **SQL Syntax:**
   ```sql
   SELECT CustomerID, COUNT(*) AS NumberOfOrders
   FROM Orders
   GROUP BY CustomerID
   HAVING COUNT(*) > 1;
   ```
5. **Output:**  
   - Only shows rows (groups) that have more than 1 order.  
   - Example:

     | CustomerID | NumberOfOrders |
     |------------|----------------|
     | 1          | 2              |

---

## 9. Functions

### A. AVG(), SUM(), COUNT(), MIN(), MAX()
1. **Topic/Command Name:** Aggregate Functions (`AVG`, `SUM`, `COUNT`, `MIN`, `MAX`)  
2. **When to use:**  
   - To perform calculations on multiple rows of a table’s column (numeric data, or counting rows).  
3. **Example:** Get the total quantity of orders (assuming `Quantity` in **Orders**).  
4. **SQL Syntax (example with SUM):**
   ```sql
   SELECT SUM(Quantity) AS TotalQuantity
   FROM Orders;
   ```
5. **Output:**  
   - One row with the aggregated value, e.g.:

     | TotalQuantity |
     |--------------|
     | 150          |

   - Similar logic for `AVG()`, `COUNT()`, `MIN()`, `MAX()`.

---

## 10. Window Functions

(SQL window functions are used to perform calculations across sets of rows that are related to the current query row.)

### A. OVER(), ROW_NUMBER(), RANK(), DENSE_RANK(), LAG(), LEAD()
1. **Topic/Command Name:** Window functions  
2. **When to use:**  
   - To calculate running totals, rankings, or aggregated values over a partition of data while still returning individual rows.  
3. **Example:** Assign a row number to each customer based on LastName sorting.  
4. **SQL Syntax (example with ROW_NUMBER):**
   ```sql
   SELECT 
       CustomerID,
       LastName,
       ROW_NUMBER() OVER (ORDER BY LastName) AS RowNum
   FROM Customers;
   ```
5. **Output:**  
   - Example:

     | CustomerID | LastName | RowNum |
     |------------|----------|--------|
     | 2          | Anderson | 1      |
     | 1          | Doe      | 2      |
     | 3          | Johnson  | 3      |
     | ...        | ...      | ...    |

---

## 11. Subqueries / Conditions (IN, BETWEEN, LIKE, ANY, ALL, EXISTS)

1. **Topic/Command Name:** Subqueries (using `IN`, `BETWEEN`, `LIKE`, `ANY`, `ALL`, `EXISTS`)  
2. **When to use:**  
   - When you need to base your query on the result of another query.  
   - `IN`: to filter rows that match a set of values.  
   - `BETWEEN`: to filter rows based on a range.  
   - `LIKE`: to filter rows by partial string matching.  
   - `ANY`/`ALL`: to compare a value to each value in a list or subquery.  
   - `EXISTS`: to check if a subquery returns any row.  
3. **Example:** Find customers who have placed an order.  
   ```sql
   SELECT *
   FROM Customers
   WHERE CustomerID IN (SELECT CustomerID FROM Orders);
   ```
4. **SQL Syntax (example for EXISTS):**
   ```sql
   SELECT *
   FROM Customers AS C
   WHERE EXISTS (
       SELECT 1
       FROM Orders AS O
       WHERE O.CustomerID = C.CustomerID
   );
   ```
5. **Output:**  
   - Displays only customers who have matching rows in `Orders`.  
   - Example:

     | CustomerID | FirstName | LastName | Email                | Phone       | Address         |
     |------------|-----------|----------|----------------------|-------------|-----------------|
     | 1          | John      | Doe      | [email protected]     | 123-456-7890 | 123 Elm Street  |
     | 2          | Jane      | Smith    | [email protected]  | 555-555-1212 | 456 Oak Avenue  |

---

## Putting It All Together

These commands and concepts cover the bulk of SQL operations, from creating and removing tables (DDL), to reading and manipulating data (DML), managing permissions (DCL), controlling transactions (TCL), and performing complex queries (JOINs, GROUP BY, Window Functions, Subqueries).

By understanding **when** to use each command, **how** to write the syntax, and what the typical **output** or result set looks like, you can effectively manage and query your relational database from beginner to advanced scenarios.