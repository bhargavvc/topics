
# two sum problem 
def two_sum(nums, target):
    # Dictionary to store visited numbers and their indices
    '''
    [2, 7, 11, 15]
    seen = {}
    we need to find complimment for each number so that u can find pairs
    here in first case 2' complement to 9 is 7 
    here in first case 7' complement to 9 is 2 

    first we are storing complemnt of each number 
    - dictionary with key as number and index as value
    - so next time if any of complement found for other numebrs it ieasily gives index of pair
   
    '''
    

    seen = {}
    
    for index, number in enumerate(nums):
        # Calculate the complement
        complement = target - number
        
        # Check if complement is already in the seen 
        if complement in seen:
            return [seen[complement], index]
        
        # Store the current number and its index in the dictionary
        seen[number] = index

    return []  # Return empty if no solution exists

# Example Usage
nums = [2, 7, 11, 15]
target = 9
result = two_sum(nums, target)
print(f"Indices of numbers that sum to {target}: {result}")



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




def maxConsecutiveZero(nums, k):
    left = 0
    max_length = 0
    zero_count = 0
    
    for right in range(len(nums)):
        
        # count zeros
        if nums[right] == 0:
            zero_count +=1
        
        while zero_count > k:
            if nums[left] == 0:
                zero_count -=1
            left +=1
    max_length = max(max_length, right - left+1)
    
    return max_length

nums,k = [1,1,1,0,0,0,1,1,1,1,0], 2

print(maxConsecutiveZero(nums, k))


















































# import re

# str_var = "sadnlwjrkwejk42kiraaas472hajkhsaqqoo978"


# pattern_output = re.findall(r"\b\d{3}\b", str_var)

# output = [int(num) for num in pattern_output]
# print(output)