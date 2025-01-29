
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

