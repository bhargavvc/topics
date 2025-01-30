
### **Main Logic**
The function merges two **sorted arrays** into one **sorted array** by:
1. Comparing the smallest unprocessed elements from both arrays.
2. Appending the smaller element to the result.
3. Repeating until all elements from both arrays are processed.
4. Appending any remaining elements from the unfinished array.

---

### **Need of the Code**
1. **Efficient Merging**:
   - Combines two sorted arrays into one sorted array in **O(n + m)** time, where `n` and `m` are the lengths of the two arrays.
   - This is a key step in the **merge sort algorithm**.

2. **Handling Sorted Data**:
   - Useful when working with pre-sorted data (e.g., merging sorted lists, databases, or streams).

3. **Foundation for Merge Sort**:
   - This logic is the core of the **merge step** in the merge sort algorithm, which divides and conquers by splitting, sorting, and merging arrays.

---

### **Key Idea**
- Use two pointers (`i` and `j`) to track progress in both arrays.
- Compare elements at the pointers and append the smaller one to the result.
- Append any leftover elements after one array is fully processed.

#merge two sorted list
def merge_sorted_arrays(arr1, arr2):
    merged_array = []
    i = j = 0
    n, m = len(arr1), len(arr2)

    # Merge elements from both arrays
    # why i < n and j < m (this condition for handling out of bouds or 
    # maintain the lenght of elements to be sorted)
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
