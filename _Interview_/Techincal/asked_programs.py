








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