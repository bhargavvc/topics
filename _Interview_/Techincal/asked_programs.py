
# two sum problem 

def two_sum(nums, target):
    # Dictionary to store visited numbers and their indices
    num_to_index = {}
    
    for i, num in enumerate(nums):
        # Calculate the complement
        complement = target - num
        
        # Check if complement is already in the dictionary
        if complement in num_to_index:
            return [num_to_index[complement], i]
        
        # Store the current number and its index in the dictionary
        num_to_index[num] = i

    return []  # Return empty if no solution exists

# Example Usage
nums = [2, 7, 11, 15]
target = 9
result = two_sum(nums, target)
print(f"Indices of numbers that sum to {target}: {result}")

#Manual Power Calculation with Float Support
import math

def power(base, exponent):
    # Handle edge case for base 0
    if base == 0 and exponent <= 0:
        raise ValueError("Base 0 cannot have zero or negative exponent")
    if base == 0:
        return 0

    # Handle negative exponent
    if exponent < 0:
        base = 1 / base
        exponent = -exponent

    # Separate integer and fractional parts of the exponent
    int_part = int(exponent)
    frac_part = exponent - int_part

    # Calculate the integer power using iterative multiplication
    result = 1
    for _ in range(int_part):
        result *= base

    # Calculate the fractional part using math.exp and math.log
    if frac_part != 0:
        result *= math.exp(frac_part * math.log(base))

    return result

# Example usage
print(f"2^3 = {power(2, 3)}")         # 2^3 = 8
print(f"2^-3 = {power(2, -3)}")       # 2^-3 = 0.125
print(f"4^-2.5 = {power(4, -2.5)}")   # 4^-2.5 = 0.03125
print(f"5^0.5 = {power(5, 0.5)}")     # 5^0.5 = sqrt(5) = 2.236...
print(f"9^0.5 = {power(9, 0.5)}")     # 9^0.5 = sqrt(9) = 3
print(f"2^2.5 = {power(2, 2.5)}")     # 2^2.5 = ~5.656


#merge two sorted list
def merge_sorted_arrays(arr1, arr2):
    merged_array = []
    i = j = 0
    n, m = len(arr1), len(arr2)

    # Merge elements from both arrays
    while i < n and j < m:
        if arr1[i] < arr2[j]:
            merged_array.append(arr1[i])
            i += 1
        else:
            merged_array.append(arr2[j])
            j += 1

    # Append remaining elements from arr1
    while i < n:
        merged_array.append(arr1[i])
        i += 1

    # Append remaining elements from arr2
    while j < m:
        merged_array.append(arr2[j])
        j += 1

    return merged_array

# Example usage
arr1 = [1, 4, 7, 8, 10]
arr2 = [2, 3, 9]
merged_result = merge_sorted_arrays(arr1, arr2)
print("Merged Array:", merged_result)


#anagram
def ang_checker(s1, s2):
    
    if len(s1) != len(s2):
        return False
    
    s1_dict = {}
    for char in s1:
        if char in s1_dict:
            s1_dict[char] = s1_dict[char].get(char,0)+1
        else:
            s1_dict[char] = 1

    #remove the char for dict to match the count 
    for char in s2:
        if char in s1_dict:
            s1_dict[char] = s1_dict[char] - 1 
            if s1_dict[char] == 0:
                del s1_dict[char]
  
    return len(s1_dict) == 0
         
print(ang_checker("abc","bca"))
print(ang_checker("lidsten","sileqnt"))
print(ang_checker("triangle","integral"))


# multiples corresponding rows and columns with other refrence column
#acuttal case is two cities asm1 asm2 but column is onlu asm u need to multiple these two 
import pandas as pd

def process_city_units(data, cities, units):
    """
    Processes the data to create two DataFrames:
    - Original DataFrame with added 'Units' column.
    - Modified DataFrame containing only cities and their updated 'Units'.

    Args:
        data (dict): Dictionary containing city data.
        cities (list): List of city names.
        units (dict): Dictionary with city names as keys and unit multipliers as values.

    Returns:
        tuple: (original DataFrame, modified DataFrame)
    """
    # Create the original DataFrame
    df = pd.DataFrame(data, index=cities)

    # Add units column to the DataFrame
    df['Units'] = [units[city] for city in cities]

    # Create a new DataFrame for modified values
    modified_df = pd.DataFrame(index=cities, columns=['Units'])

    # Modify the Units column based on the multiplication logic
    for city in cities:
        modified_df.loc[city, 'Units'] = df.loc[city, 'Units'] * units[city]

    return df, modified_df

# Sample data
data = {
    'New York': [1, 2, 3],
    'Los Angeles': [4, 5, 6],
    'Chicago': [7, 8, 9]
}
cities = ['New York', 'Los Angeles', 'Chicago']
units = {'New York': 10, 'Los Angeles': 20, 'Chicago': 30}

# Process the data
original_df, modified_df = process_city_units(data, cities, units)

# Display the DataFrames
print("Original DataFrame:")
print(original_df)
print("\nModified DataFrame with Units:")
print(modified_df)







# Abcabcdba
# str = Abcabcdba

def longest(value):
    

    char_index = {}
    start= 0
    max_length = 0
    
    for index, char in enumerate(value):
        if char in char_index and  char_index[char] >= start:
            start = char_index[char] + 1
        char_index[char] = index
        max_length = max( max_length, index - start+1)
    
    return max_length


str_value = "abcabcdba"
print( longest(str_value))






