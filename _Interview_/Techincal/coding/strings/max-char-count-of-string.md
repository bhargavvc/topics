### Concise Main Logic
1. **Count Characters:** Iterate over the string and maintain a count for each character using a dictionary.
2. **Track Maximum:** While counting, update the maximum count and corresponding character.
3. **Return Result:** After processing, return the character with the highest frequency and its count.

### Code

```python
def most_repeat_char_count(s1):
    if not s1:
        return "String is empty"
    
    char_count = {}
    max_char, max_count = '', 0
    
    for char in s1:
        # Update the count for the current character
        char_count[char] = char_count.get(char, 0) + 1
        
        # Check if this character now has the highest count
        if char_count[char] > max_count:
            max_char, max_count = char, char_count[char]
    
    return {"key": max_char, "value": max_count}

# Example usage
s = "aaaaaaaabbcccccccccdd"
print(most_repeat_char_count(s))
```