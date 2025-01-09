
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
def merge_sorted_lists(list1, list2):
    i, j = 0, 0
    merged = []
    while i < len(list1) and j < len(list2):
        if list1[i] < list2[j]:
            merged.append(list1[i])
            i += 1
        else:
            merged.append(list2[j])
            j += 1
    while i < len(list1):
        merged.append(list1[i])
        i += 1
    while j < len(list2):
        merged.append(list2[j])
        j += 1
    return merged
