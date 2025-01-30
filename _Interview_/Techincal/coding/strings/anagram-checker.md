
---

### **Efficient Implementation**
```python
def ang_checker(s1, s2):
    # Check if lengths are different
    if len(s1) != len(s2):
        return False
    
    # Use a single dictionary to count characters
    char_count = {}
    
    # Increment counts for s1
    for char in s1:
        char_count[char] = char_count.get(char, 0) + 1
    
    # Decrement counts for s2
    for char in s2:
        if char not in char_count:  # If char not in s1, not an anagram
            return False
        char_count[char] -= 1
        
        if char_count[char] == 0: #clean up the dictionary char key when reaches  0 value 
            del char_count[char]
    
    # If the dictionary is empty, it's an anagram
    return not char_count
```

---
# store dictionary character count and check with second string if not found in second string return false if found decrement dictionary count and delete when it reaches 0

### **Key Improvements**
1. **Single Dictionary**:
   - Use one dictionary to count characters for `s1` and decrement for `s2`.
   - This avoids the need for a second dictionary or additional checks.

2. **Early Exit**:
   - If a character in `s2` is not in the dictionary, return `False` immediately (no need to process further).

3. **Simplified Logic**:
   - Directly delete keys when their count reaches `0` to ensure the dictionary is empty for anagrams.

4. **Efficient Lookup**:
   - Dictionary lookups and updates are **O(1)** on average, making this approach efficient.

---

### **Time Complexity**
- **O(n)**, where `n` is the length of the strings.
  - Each character is processed once for counting and once for decrementing.

---

### **Space Complexity**
- **O(k)**, where `k` is the number of unique characters in the strings.
  - The dictionary stores counts for each unique character.

---

### **Example Walkthrough**

#### Input:
```python
s1 = "listen"
s2 = "silent"
```

#### Execution:
1. Count characters in `s1`:
   - `char_count = {'l': 1, 'i': 1, 's': 1, 't': 1, 'e': 1, 'n': 1}`

2. Decrement counts for `s2`:
   - For `s` in `s2`: `char_count = {'l': 1, 'i': 1, 't': 1, 'e': 1, 'n': 1}`
   - For `i` in `s2`: `char_count = {'l': 1, 't': 1, 'e': 1, 'n': 1}`
   - For `l` in `s2`: `char_count = {'t': 1, 'e': 1, 'n': 1}`
   - For `e` in `s2`: `char_count = {'t': 1, 'n': 1}`
   - For `n` in `s2`: `char_count = {'t': 1}`
   - For `t` in `s2`: `char_count = {}`

3. The dictionary is empty, so the strings are anagrams.

#### Output:
```python
True
```

---

### **Alternative: Using `collections.Counter`**
For even more simplicity, you can use Python's `collections.Counter`:

```python
from collections import Counter

def ang_checker(s1, s2):
    return Counter(s1) == Counter(s2)
```

This approach is concise and leverages Python's built-in functionality for counting. However, it may be slightly less efficient due to the creation of two separate counters.