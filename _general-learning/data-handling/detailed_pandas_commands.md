# Detailed Pandas Commands

## Table of Contents
- [1. Data Loading](#1-data-loading)
- [2. Basic Data Inspection](#2-basic-data-inspection)
- [3. Data Cleaning](#3-data-cleaning)
- [4. Data Transformation](#4-data-transformation)
- [5. Data Visualization](#5-data-visualization)
- [6. Statistical Analysis](#6-statistical-analysis)
- [7. Indexing and Selection](#7-indexing-and-selection)
- [8. Data Formatting and Conversion](#8-data-formatting-and-conversion)
- [9. Advanced Data Transformation](#9-advanced-data-transformation)
- [10. Time Series Operations](#10-time-series-operations)
- [11. File Export](#11-file-export)
- [12. Data Exploration Techniques](#12-data-exploration-techniques)
- [13. Advanced Data Queries](#13-advanced-data-queries)
- [14. Memory Optimization](#14-memory-optimization)
- [15. Multi-Index Operations](#15-multi-index-operations)
- [16. Data Merging Techniques](#16-data-merging-techniques)
- [17. Dealing with Duplicates](#17-dealing-with-duplicates)
- [18. Custom Operations with Apply](#18-custom-operations-with-apply)
- [19. Handling Large Datasets](#19-handling-large-datasets)
- [20. Integration with Matplotlib](#20-integration-with-matplotlib)
- [21. Specialized Data Types](#21-specialized-data-types)
- [22. Performance Tuning](#22-performance-tuning)
- [23. Visualization Enhancement](#23-visualization-enhancement)
- [24. Advanced Grouping and Aggregation](#24-advanced-grouping-and-aggregation)
- [25. Time Series Specific Operations](#25-time-series-specific-operations)
- [26. Text Data Operations](#26-text-data-operations)
- [27. Data Normalization](#27-data-normalization)
- [28. Working with JSON and XML](#28-working-with-json-and-xml)
- [29. Advanced File Handling](#29-advanced-file-handling)


Absolutely! Let's dive deeper into each command, providing more detailed explanations and additional code examples.

---

### 1. **Data Loading**

#### 1.1 `read_csv()`
```python
df = pd.read_csv('file.csv')
```
- **Purpose**: Reads a CSV file into a pandas DataFrame, a two-dimensional, size-mutable, and potentially heterogeneous tabular data structure.
- **Explanation**: The `read_csv()` function is used to import CSV files where columns are separated by commas (or another delimiter). By default, the first row of the file is treated as the column names.
- **Example**:
  ```python
  # Read a CSV file into DataFrame
  df = pd.read_csv('data.csv')

  # Read CSV with custom separator and specify column headers
  df = pd.read_csv('data.csv', sep=';', header=0)
  print(df.head())
  ```

#### 1.2 `read_excel()`
```python
df = pd.read_excel('file.xlsx', sheet_name='Sheet1')
```
- **Purpose**: Reads an Excel file into a pandas DataFrame.
- **Explanation**: `read_excel()` can handle both `.xls` and `.xlsx` file formats. You can specify which sheet to load by passing the sheet's name or index to the `sheet_name` parameter.
- **Example**:
  ```python
  # Read specific sheet from Excel file
  df = pd.read_excel('data.xlsx', sheet_name='Sales')
  print(df.head())
  ```

#### 1.3 `read_sql()`
```python
df = pd.read_sql('SELECT * FROM table_name', connection)
```
- **Purpose**: Executes a SQL query and loads the result into a DataFrame.
- **Explanation**: Use this function to retrieve data from a SQL database, either from a query or by specifying a table. You must first create a connection object (e.g., using `sqlite3.connect()` or `SQLAlchemy`).
- **Example**:
  ```python
  import sqlite3
  conn = sqlite3.connect('database.db')
  df = pd.read_sql('SELECT * FROM employees', conn)
  print(df.head())
  ```

---

### 2. **Basic Data Inspection**

#### 2.1 `head()`
```python
df.head(3)
```
- **Purpose**: Displays the first few rows of a DataFrame.
- **Explanation**: By default, `head()` returns the first 5 rows, but you can specify any number as an argument. It's useful for quickly inspecting the first few records.
- **Example**:
  ```python
  # Show the first 3 rows
  print(df.head(3))
  ```

#### 2.2 `tail()`
```python
df.tail(3)
```
- **Purpose**: Displays the last few rows of a DataFrame.
- **Explanation**: Just like `head()`, but it returns the last few rows. You can specify how many rows to display.
- **Example**:
  ```python
  # Show the last 3 rows
  print(df.tail(3))
  ```

#### 2.3 `info()`
```python
df.info()
```
- **Purpose**: Provides a concise summary of a DataFrame.
- **Explanation**: This is useful for understanding the types of columns, the number of non-null values, and memory usage. It helps when you're getting to know the structure of the DataFrame.
- **Example**:
  ```python
  # Get info about the DataFrame
  df.info()
  ```

---

### 3. **Data Cleaning**

#### 3.1 `fillna()`
```python
df.fillna(value=0)
```
- **Purpose**: Fills missing (NaN) values with a specified value.
- **Explanation**: This method replaces NaN values in your DataFrame with a specified value (such as 0 or the mean). You can also use methods like forward-fill (`ffill`) or backward-fill (`bfill`).
- **Example**:
  ```python
  # Replace NaN values with 0
  df['column_name'] = df['column_name'].fillna(0)
  ```

#### 3.2 `dropna()`
```python
df.dropna(axis=0)
```
- **Purpose**: Removes missing values from a DataFrame.
- **Explanation**: You can drop rows (axis=0) or columns (axis=1) with NaN values. `how='any'` removes rows with any NaN, and `how='all'` removes rows where all values are NaN.
- **Example**:
  ```python
  # Drop rows with any NaN value
  df = df.dropna(axis=0, how='any')

  # Drop columns with any NaN value
  df = df.dropna(axis=1, how='any')
  ```

---

### 4. **Data Transformation**

#### 4.1 `apply()`
```python
df.apply(lambda x: x + 1)
```
- **Purpose**: Applies a function along an axis of the DataFrame (either rows or columns).
- **Explanation**: `apply()` allows you to apply a custom function to each row or column. For example, you can use it to transform each value in a column.
- **Example**:
  ```python
  # Add 1 to each element in the DataFrame
  df = df.apply(lambda x: x + 1)
  ```

#### 4.2 `groupby()`
```python
df.groupby('column_name').sum()
```
- **Purpose**: Groups the DataFrame by a specific column and then applies an aggregation function (like sum, mean, etc.).
- **Explanation**: `groupby()` is useful for performing operations on subsets of the data. After grouping, you can apply functions like `sum()`, `mean()`, `count()`, etc.
- **Example**:
  ```python
  # Group by 'region' and calculate the sum of sales for each region
  df_grouped = df.groupby('region')['sales'].sum()
  print(df_grouped)
  ```

---

### 5. **Data Visualization**

#### 5.1 `plot()`
```python
df['column'].plot(kind='line')
```
- **Purpose**: Plots a simple graph (line, bar, etc.) using Matplotlib.
- **Explanation**: `plot()` is a flexible method for visualizing data. You can specify the type of plot (`line`, `bar`, `hist`, etc.) and customize various plot attributes.
- **Example**:
  ```python
  # Plot a line chart of 'sales' over time
  df['sales'].plot(kind='line', title="Sales over Time")
  ```

---

### 6. **Statistical Analysis**

#### 6.1 `describe()`
```python
df.describe()
```
- **Purpose**: Generates descriptive statistics like mean, standard deviation, and percentiles.
- **Explanation**: This method is great for getting a quick overview of numerical columns in your DataFrame. It helps you understand the distribution of the data.
- **Example**:
  ```python
  # Get summary statistics for numeric columns
  print(df.describe())
  ```

---

### 7. **Indexing and Selection**

#### 7.1 `loc[]`
```python
df.loc[1:5, ['column1', 'column2']]
```
- **Purpose**: Access a group of rows and columns by labels.
- **Explanation**: `loc[]` is label-based, meaning you use row and column labels to access data. You can use a boolean array or specific labels for more flexible querying.
- **Example**:
  ```python
  # Select rows from index 1 to 5 and specific columns
  df_selected = df.loc[1:5, ['column1', 'column2']]
  ```

#### 7.2 `iloc[]`
```python
df.iloc[1:5, 0:2]
```
- **Purpose**: Access a group of rows and columns by integer position.
- **Explanation**: `iloc[]` is position-based, meaning you use integer indices to select rows and columns.
- **Example**:
  ```python
  # Select rows from index 1 to 5 and columns from index 0 to 2
  df_selected = df.iloc[1:5, 0:2]
  ```

---

### 8. **Data Formatting and Conversion**

#### 8.1 `astype()`
```python
df['column'] = df['column'].astype('float')
```
- **Purpose**: Converts the data type of a column.
- **Explanation**: `astype()` is used to change the type of a column. This is particularly useful when you need to convert between types (e.g., from `int` to `float`).
- **Example**:
  ```python
  # Convert 'column' to float type
  df['column'] = df['column'].astype('float')
  ```

---

### 9. **Advanced Data Transformation**

#### 9.1 `pivot_table()`
```python
df.pivot_table(values='sales', index='region', columns='product', aggfunc='sum')
```
- **Purpose**: Creates a pivot table.
- **Explanation**: Pivot tables are useful for aggregating data in a more structured format, summarizing numerical data based on categories.
- **Example**:
  ```python
  # Create a pivot table summarizing sales by region and product
  df_pivot = df.pivot_table(values='sales', index='region', columns='product', aggfunc='sum')
  print(df_pivot)
  ```

---

### 10. **Time Series Operations**

#### 10.1 `resample()`
```python
df.resample('M').sum()
```
- **Purpose**: Resample time series data to a different frequency.
- **Explanation**: Resampling is used when you need to convert time series data to a different frequency (e.g., daily to monthly).
- **Example**:
  ```python
  # Resample by month and calculate the sum for each month
  df_resampled = df.resample('M').sum()
  ```

---

### 11. **File Export**

#### 11.1 `to_csv()`
```python
df.to_csv('output.csv')
```
- **Purpose**: Writes a DataFrame to a CSV file.
- **Explanation**: This function is used to export a DataFrame to a CSV file for storage or sharing. You can control options like including the index or specifying a different delimiter.
- **Example**:
  ```python
  # Export the DataFrame to a CSV file
  df.to_csv('output.csv', index=False)
  ```

#### 11.2 `to_excel()`
```python
df.to_excel('output.xlsx', sheet_name='Sheet1')
```
- **Purpose**: Writes a DataFrame to an Excel file.
- **Explanation**: `to_excel()` allows you to save DataFrames to Excel, including specifying the sheet name and other options.
- **Example**:
  ```python
  # Export DataFrame to an Excel file
  df.to_excel('output.xlsx', sheet_name='Sales Report', index=False)
  ```

---

Absolutely! Let's continue explaining the remaining pandas functions and commands in the same detailed format.

---

### 12. **Handling Duplicates**

#### 12.1 `drop_duplicates()`
```python
df.drop_duplicates()
```
- **Purpose**: Removes duplicate rows from a DataFrame.
- **Explanation**: This function is useful for cleaning data when you have rows that appear more than once. By default, it removes rows that are identical across all columns, but you can specify which columns to check for duplicates.
- **Example**:
  ```python
  # Remove duplicate rows based on all columns
  df_cleaned = df.drop_duplicates()

  # Remove duplicates based on specific columns
  df_cleaned = df.drop_duplicates(subset=['column_name'])
  ```

#### 12.2 `duplicated()`
```python
df.duplicated()
```
- **Purpose**: Identifies duplicate rows in the DataFrame.
- **Explanation**: Unlike `drop_duplicates()`, `duplicated()` returns a boolean Series indicating whether each row is a duplicate (True) or not (False).
- **Example**:
  ```python
  # Find duplicate rows
  duplicate_rows = df.duplicated()
  print(duplicate_rows)
  ```

---

### 13. **Column and Row Operations**

#### 13.1 `rename()`
```python
df.rename(columns={'old_name': 'new_name'}, inplace=True)
```
- **Purpose**: Renames the columns or indices in the DataFrame.
- **Explanation**: This method allows you to change the column names or index labels. The `inplace=True` argument modifies the original DataFrame, otherwise, it returns a new one.
- **Example**:
  ```python
  # Rename columns
  df.rename(columns={'old_column_name': 'new_column_name'}, inplace=True)
  ```

#### 13.2 `insert()`
```python
df.insert(loc=2, column='new_column', value=[1, 2, 3])
```
- **Purpose**: Inserts a new column at a specified position in the DataFrame.
- **Explanation**: The `insert()` method allows you to add a new column to the DataFrame at a given position (`loc`), along with its corresponding values.
- **Example**:
  ```python
  # Insert a new column 'age' at the second position
  df.insert(1, 'age', [25, 30, 35])
  ```

#### 13.3 `drop()`
```python
df.drop('column_name', axis=1)
```
- **Purpose**: Removes specified rows or columns.
- **Explanation**: `drop()` is used for removing unwanted rows or columns. You specify the row/column name and axis (1 for columns, 0 for rows). Use `inplace=True` to modify the original DataFrame.
- **Example**:
  ```python
  # Drop a column by its name
  df = df.drop('column_name', axis=1)

  # Drop rows by their index
  df = df.drop([0, 1], axis=0)
  ```

---

### 14. **Merging and Joining**

#### 14.1 `merge()`
```python
df_merged = pd.merge(df1, df2, on='key_column')
```
- **Purpose**: Combines two DataFrames based on a common column (like SQL join).
- **Explanation**: `merge()` is similar to SQL joins, allowing you to combine DataFrames by matching values in specified columns. You can also specify the type of join: `inner`, `outer`, `left`, or `right`.
- **Example**:
  ```python
  # Merge two DataFrames based on 'key_column'
  df_merged = pd.merge(df1, df2, on='key_column', how='inner')
  ```

#### 14.2 `join()`
```python
df1.join(df2, on='key_column')
```
- **Purpose**: Joins two DataFrames on an index or a column.
- **Explanation**: `join()` is a simpler alternative to `merge()` for combining DataFrames when you want to join them based on index or a column. It defaults to a left join.
- **Example**:
  ```python
  # Join two DataFrames based on index
  df_joined = df1.join(df2, on='key_column', how='left')
  ```

---

### 15. **Sorting**

#### 15.1 `sort_values()`
```python
df_sorted = df.sort_values(by='column_name', ascending=False)
```
- **Purpose**: Sorts the DataFrame by the values of one or more columns.
- **Explanation**: `sort_values()` sorts the DataFrame by a column's values. You can specify whether to sort in ascending or descending order, and you can sort by multiple columns by passing a list.
- **Example**:
  ```python
  # Sort the DataFrame by 'sales' column in descending order
  df_sorted = df.sort_values(by='sales', ascending=False)
  ```

#### 15.2 `sort_index()`
```python
df_sorted = df.sort_index(axis=0, ascending=True)
```
- **Purpose**: Sorts the DataFrame by its index (row labels).
- **Explanation**: `sort_index()` sorts the DataFrame based on its index rather than its values. You can sort by row or column index.
- **Example**:
  ```python
  # Sort the DataFrame by row index
  df_sorted = df.sort_index(axis=0, ascending=True)
  ```

---

### 16. **Pivoting and Reshaping**

#### 16.1 `pivot()`
```python
df_pivot = df.pivot(index='date', columns='product', values='sales')
```
- **Purpose**: Reshapes data by pivoting the DataFrame.
- **Explanation**: `pivot()` transforms the DataFrame based on column values. It is often used to turn unique identifiers into columns, changing the structure of the data.
- **Example**:
  ```python
  # Pivot data to see 'sales' by 'date' for each 'product'
  df_pivot = df.pivot(index='date', columns='product', values='sales')
  ```

#### 16.2 `melt()`
```python
df_melted = df.melt(id_vars='id', value_vars=['A', 'B', 'C'])
```
- **Purpose**: Converts wide-format data into long-format data.
- **Explanation**: `melt()` is used to unpivot or melt the DataFrame. This is helpful when you want to reshape the data by turning columns into rows.
- **Example**:
  ```python
  # Melt DataFrame to convert columns 'A', 'B', 'C' into rows
  df_melted = df.melt(id_vars='id', value_vars=['A', 'B', 'C'])
  ```

---

### 17. **String Operations**

#### 17.1 `str.contains()`
```python
df['column_name'].str.contains('pattern')
```
- **Purpose**: Checks if a string pattern is present in each element of a column.
- **Explanation**: `str.contains()` is used for string matching. It returns a boolean Series indicating whether the specified pattern appears in each string.
- **Example**:
  ```python
  # Check if 'product_name' contains the word 'shirt'
  df['contains_shirt'] = df['product_name'].str.contains('shirt')
  ```

#### 17.2 `str.replace()`
```python
df['column_name'].str.replace('old', 'new')
```
- **Purpose**: Replaces substrings in each element of a string column.
- **Explanation**: `str.replace()` is useful for replacing specific patterns or substrings within a column of strings.
- **Example**:
  ```python
  # Replace 'old' with 'new' in 'product_name'
  df['product_name'] = df['product_name'].str.replace('old', 'new')
  ```

---

### 18. **Handling Time Series**

#### 18.1 `to_datetime()`
```python
df['date'] = pd.to_datetime(df['date'])
```
- **Purpose**: Converts a column to datetime format.
- **Explanation**: This method is used to convert columns containing date-like data into actual datetime objects, allowing for time-based indexing and operations.
- **Example**:
  ```python
  # Convert 'date' column to datetime format
  df['date'] = pd.to_datetime(df['date'])
  ```

#### 18.2 `dt.year`
```python
df['year'] = df['date'].dt.year
```
- **Purpose**: Extracts the year from a datetime column.
- **Explanation**: `dt` is an accessor for datetime-like data. You can extract components like year, month, day, etc., from a datetime column.
- **Example**:
  ```python
  # Extract the year from a 'date' column
  df['year'] = df['date'].dt.year
  ```

---

### 19. **Memory Management**

#### 19.1 `memory_usage()`
```python
df.memory_usage(deep=True)
```
- **Purpose**: Returns the memory usage of each column in a DataFrame.
- **Explanation**: This function is useful when working with large datasets. By passing `deep=True`, you can also measure the memory used by object-type columns (e.g., strings).
- **Example**:
  ```python
  # Check memory usage of each column
  print(df.memory_usage(deep=True))
  ```

---

### 20. **Window Functions**

#### 20.1 `rolling()`
```python
df['moving_avg'] = df['sales'].rolling(window=3).mean()
```
- **Purpose**: Applies a rolling window operation (like moving averages).
- **Explanation**: `rolling()` creates a rolling window over the DataFrame and allows you to apply aggregation functions like mean, sum, etc., on a sliding window.
- **Example**:
  ```python
  # Calculate the 3-day moving average for 'sales'
  df['moving_avg'] = df['sales'].rolling(window=3).mean()
  ```

#### 20.2 `expanding()`
```python
df['expanding_avg'] = df['sales'].expanding().mean()
```
- **Purpose**: Applies an expanding window operation (cumulative calculation).
- **Explanation**: `expanding()` allows for cumulative calculations where the window size grows as the dataset progresses.
- **Example**:
  ```python
  # Calculate the cumulative average for 'sales'
  df['expanding_avg'] = df['sales'].expanding().mean()
  ```

---
 

 Sure! Let's continue with the remaining pandas functions.

---

### 21. **Aggregation Functions**

#### 21.1 `agg()`
```python
df.groupby('category')['sales'].agg(['sum', 'mean', 'max'])
```
- **Purpose**: Allows applying multiple aggregation functions at once.
- **Explanation**: `agg()` allows you to specify multiple aggregation functions for each column or group. This is particularly useful after using `groupby()`.
- **Example**:
  ```python
  # Group by 'category' and calculate the sum, mean, and max of 'sales'
  result = df.groupby('category')['sales'].agg(['sum', 'mean', 'max'])
  ```

#### 21.2 `sum()`
```python
df['sales'].sum()
```
- **Purpose**: Returns the sum of all the values in a column.
- **Explanation**: `sum()` adds up all the values in a column or along a specific axis. It's commonly used for numerical data.
- **Example**:
  ```python
  # Calculate the sum of 'sales'
  total_sales = df['sales'].sum()
  ```

#### 21.3 `mean()`
```python
df['sales'].mean()
```
- **Purpose**: Returns the average of all the values in a column.
- **Explanation**: `mean()` calculates the average of the numerical values in a specified column or along a specified axis.
- **Example**:
  ```python
  # Calculate the mean of 'sales'
  avg_sales = df['sales'].mean()
  ```

#### 21.4 `min()`
```python
df['sales'].min()
```
- **Purpose**: Returns the minimum value of the column.
- **Explanation**: `min()` finds the smallest value in a column.
- **Example**:
  ```python
  # Find the minimum 'sales' value
  min_sales = df['sales'].min()
  ```

#### 21.5 `max()`
```python
df['sales'].max()
```
- **Purpose**: Returns the maximum value of the column.
- **Explanation**: `max()` finds the largest value in a column.
- **Example**:
  ```python
  # Find the maximum 'sales' value
  max_sales = df['sales'].max()
  ```

---

### 22. **Statistics and Descriptive Analysis**

#### 22.1 `describe()`
```python
df.describe()
```
- **Purpose**: Generates descriptive statistics of numeric columns.
- **Explanation**: `describe()` provides a summary of statistics like count, mean, std, min, max, and quartiles for numerical columns in the DataFrame.
- **Example**:
  ```python
  # Get descriptive statistics for all numeric columns
  df_summary = df.describe()
  ```

#### 22.2 `std()`
```python
df['sales'].std()
```
- **Purpose**: Returns the standard deviation of the column.
- **Explanation**: `std()` calculates the standard deviation, which is a measure of the spread of values in a column.
- **Example**:
  ```python
  # Calculate the standard deviation of 'sales'
  sales_std = df['sales'].std()
  ```

#### 22.3 `median()`
```python
df['sales'].median()
```
- **Purpose**: Returns the median value of the column.
- **Explanation**: `median()` calculates the median, which is the middle value of the column when sorted.
- **Example**:
  ```python
  # Calculate the median of 'sales'
  sales_median = df['sales'].median()
  ```

---

### 23. **Handling Missing Data**

#### 23.1 `isna()`
```python
df.isna()
```
- **Purpose**: Identifies missing (NaN) values in the DataFrame.
- **Explanation**: `isna()` returns a boolean DataFrame where `True` represents missing values (NaN) and `False` represents non-missing values.
- **Example**:
  ```python
  # Check for missing values in the DataFrame
  missing_values = df.isna()
  ```

#### 23.2 `fillna()`
```python
df.fillna(value=0)
```
- **Purpose**: Replaces missing values with a specified value.
- **Explanation**: `fillna()` is used to replace NaN values with a specific value (like 0 or the mean of the column). It helps in filling missing data before further analysis.
- **Example**:
  ```python
  # Replace missing values in the 'sales' column with 0
  df['sales'] = df['sales'].fillna(0)
  ```

#### 23.3 `dropna()`
```python
df.dropna()
```
- **Purpose**: Drops rows or columns with missing values.
- **Explanation**: `dropna()` removes any rows or columns that contain NaN values, which can be useful for cleaning the data.
- **Example**:
  ```python
  # Drop rows with any missing values
  df_cleaned = df.dropna()
  ```

---

### 24. **Categorical Data**

#### 24.1 `astype()`
```python
df['column'] = df['column'].astype('category')
```
- **Purpose**: Converts a column to a specific data type.
- **Explanation**: `astype()` allows for changing the data type of a column, which is useful for converting numerical values to categorical or date types.
- **Example**:
  ```python
  # Convert 'category' column to categorical type
  df['category'] = df['category'].astype('category')
  ```

#### 24.2 `cat.codes`
```python
df['category_codes'] = df['category'].cat.codes
```
- **Purpose**: Converts categorical values to numeric codes.
- **Explanation**: After converting a column to categorical type, `cat.codes` can be used to assign numeric codes to each category.
- **Example**:
  ```python
  # Convert 'category' to numeric codes
  df['category_codes'] = df['category'].cat.codes
  ```

---

### 25. **Data Type Conversion**

#### 25.1 `to_numeric()`
```python
df['sales'] = pd.to_numeric(df['sales'], errors='coerce')
```
- **Purpose**: Converts a column to numeric values.
- **Explanation**: `to_numeric()` converts the values in a column to numeric types. If a value cannot be converted, it can be coerced to NaN using `errors='coerce'`.
- **Example**:
  ```python
  # Convert 'sales' column to numeric, coercing errors to NaN
  df['sales'] = pd.to_numeric(df['sales'], errors='coerce')
  ```

---

### 26. **Working with Dates**

#### 26.1 `pd.to_datetime()`
```python
df['date'] = pd.to_datetime(df['date'])
```
- **Purpose**: Converts a column to datetime format.
- **Explanation**: `to_datetime()` parses a column containing date-like data and converts it to a proper datetime object.
- **Example**:
  ```python
  # Convert 'date' column to datetime
  df['date'] = pd.to_datetime(df['date'])
  ```

#### 26.2 `dt.weekday`
```python
df['weekday'] = df['date'].dt.weekday
```
- **Purpose**: Extracts the weekday from a datetime column.
- **Explanation**: Using the `dt` accessor, you can extract parts of a date. `weekday` gives the day of the week (0 = Monday, 6 = Sunday).
- **Example**:
  ```python
  # Extract the weekday from the 'date' column
  df['weekday'] = df['date'].dt.weekday
  ```

---

### 27. **Sampling Data**

#### 27.1 `sample()`
```python
df_sample = df.sample(n=5)
```
- **Purpose**: Randomly selects a specified number of rows.
- **Explanation**: `sample()` is useful for quickly inspecting a random subset of your data. You can specify the number of rows to sample or the fraction of the total data.
- **Example**:
  ```python
  # Randomly select 5 rows
  df_sample = df.sample(n=5)
  ```

---

### 28. **Apply Functions**

#### 28.1 `apply()`
```python
df['sales'] = df['sales'].apply(lambda x: x * 2)
```
- **Purpose**: Applies a function along a DataFrame axis.
- **Explanation**: `apply()` allows you to apply a function along an axis (either rows or columns) in the DataFrame. It's a powerful tool for performing custom transformations.
- **Example**:
  ```python
  # Multiply each 'sales' value by 2
  df['sales'] = df['sales'].apply(lambda x: x * 2)
  ```

---

### 29. **Concatenating DataFrames**

#### 29.1 `concat()`
```python
df_concat = pd.concat([df1, df2], axis=0)
```
- **Purpose**: Concatenates multiple DataFrames along a specified axis.
- **Explanation**: `concat()` is used to concatenate DataFrames either row-wise (`axis=0`) or column-wise (`axis=1`). It’s useful for combining data from different sources or tables.
- **Example**:
  ```python
  # Concatenate two DataFrames vertically (along rows)
  df_concat = pd.concat([df1, df2], axis=0)
  ```

---

 