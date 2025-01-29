

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
