Let’s revisit each algorithm and provide **optimized code solutions** with the best possible **time and space complexity**, considering inputs in the order of millions.

---

## **1. Binary Search**
- **Best Time Complexity**: \( O(\log n) \)
- **Space Complexity**: \( O(1) \)

### Optimized Code:
```python
def binary_search(arr, target):
    low, high = 0, len(arr) - 1
    while low <= high:
        mid = low + (high - low) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1

# Usage
arr = sorted([i for i in range(1, 10**6)])  # Large sorted input
print(binary_search(arr, 999999))  # Output: Index of the target
```

---

## **2. Merge Sort**
- **Best Time Complexity**: \( O(n \log n) \)
- **Space Complexity**: \( O(n) \)

### Optimized Code:
```python
def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)

def merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result

# Usage
arr = [i for i in range(10**6, 0, -1)]  # Reverse sorted input
sorted_arr = merge_sort(arr)
```

---

## **3. Quick Sort**
- **Best Time Complexity**: \( O(n \log n) \)
- **Space Complexity**: \( O(\log n) \) (in-place sorting)

### Optimized Code:
```python
def quick_sort(arr, low, high):
    if low < high:
        pivot_index = partition(arr, low, high)
        quick_sort(arr, low, pivot_index - 1)
        quick_sort(arr, pivot_index + 1, high)

def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

# Usage
arr = [i for i in range(10**6, 0, -1)]
quick_sort(arr, 0, len(arr) - 1)
```

---

## **4. Bubble Sort (Not Suitable for Large Inputs)**
Even with \( O(n) \) best time complexity for sorted inputs, **Bubble Sort** is impractical for millions of elements. Prefer **Merge Sort** or **Quick Sort**.

---

## **5. Insertion Sort (Optimized for Nearly Sorted Data)**
- **Best Time Complexity**: \( O(n) \)
- **Space Complexity**: \( O(1) \)

### Optimized Code:
```python
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

# Usage
arr = [i for i in range(10**6)]
insertion_sort(arr)  # Efficient for already sorted or nearly sorted data
```

---

## **6. Heap Sort**
- **Best Time Complexity**: \( O(n \log n) \)
- **Space Complexity**: \( O(1) \)

### Optimized Code:
```python
def heapify(arr, n, i):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2
    if left < n and arr[left] > arr[largest]:
        largest = left
    if right < n and arr[right] > arr[largest]:
        largest = right
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)

def heap_sort(arr):
    n = len(arr)
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)
    for i in range(n - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        heapify(arr, i, 0)

# Usage
arr = [i for i in range(10**6, 0, -1)]
heap_sort(arr)
```

---

## **7. Selection Sort**
- **Best Time Complexity**: \( O(n^2) \)
- **Space Complexity**: \( O(1) \)

Selection Sort is inefficient for large datasets. Use **Heap Sort** for similar behavior but with \( O(n \log n) \).

---

## **8. Depth-First Search (DFS)**
- **Best Time Complexity**: \( O(V + E) \)
- **Space Complexity**: \( O(V) \)

### Optimized Code:
```python
def dfs(graph, start, visited):
    visited.add(start)
    for neighbor in graph[start]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited)

# Usage
graph = {0: [1, 2], 1: [0, 3], 2: [0, 3], 3: [1, 2]}
visited = set()
dfs(graph, 0, visited)
print(visited)  # Output: {0, 1, 2, 3}
```

---

## **9. Breadth-First Search (BFS)**
- **Best Time Complexity**: \( O(V + E) \)
- **Space Complexity**: \( O(V) \)

### Optimized Code:
```python
from collections import deque

def bfs(graph, start):
    visited = set()
    queue = deque([start])
    visited.add(start)
    while queue:
        node = queue.popleft()
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

# Usage
graph = {0: [1, 2], 1: [0, 3], 2: [0, 3], 3: [1, 2]}
bfs(graph, 0)
```

---

## **10. Dijkstra’s Algorithm**
- **Best Time Complexity**: \( O(E + V \log V) \) (using a priority queue).
- **Space Complexity**: \( O(V) \)

### Optimized Code:
```python
import heapq

def dijkstra(graph, start):
    distances = {node: float('infinity') for node in graph}
    distances[start] = 0
    pq = [(0, start)]
    while pq:
        current_distance, current_node = heapq.heappop(pq)
        if current_distance > distances[current_node]:
            continue
        for neighbor, weight in graph[current_node]:
            distance = current_distance + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(pq, (distance, neighbor))
    return distances

# Usage
graph = {0: [(1, 4), (2, 1)], 1: [(3, 1)], 2: [(1, 2), (3, 5)], 3: []}
print(dijkstra(graph, 0))  # Output: Shortest distances
```

---

I’ve provided the most efficient solutions for sorting, searching, and graph algorithms. Let me know if you’d like more algorithms explained or additional details!


Let’s continue with the remaining algorithms from the list. I’ll provide the **best code solutions** with **optimal time and space complexity**, ensuring they handle large-scale inputs effectively.

---

## **11. Bellman-Ford Algorithm**
- **Purpose**: Finds the shortest path from a source to all vertices, even with negative edge weights.
- **Best Time Complexity**: \( O(VE) \)
- **Space Complexity**: \( O(V) \)

### Optimized Code:
```python
def bellman_ford(graph, V, src):
    dist = [float("inf")] * V
    dist[src] = 0
    for _ in range(V - 1):  # Relax edges |V| - 1 times
        for u, v, w in graph:
            if dist[u] != float("inf") and dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
    # Check for negative weight cycles
    for u, v, w in graph:
        if dist[u] != float("inf") and dist[u] + w < dist[v]:
            print("Graph contains a negative-weight cycle")
            return
    return dist

# Usage
edges = [(0, 1, -1), (0, 2, 4), (1, 2, 3), (1, 3, 2), (1, 4, 2), (3, 2, 5), (3, 1, 1), (4, 3, -3)]
V = 5
print(bellman_ford(edges, V, 0))  # Shortest distances from vertex 0
```

---

## **12. Floyd-Warshall Algorithm**
- **Purpose**: Computes shortest paths between all pairs of vertices.
- **Best Time Complexity**: \( O(V^3) \)
- **Space Complexity**: \( O(V^2) \)

### Optimized Code:
```python
def floyd_warshall(graph):
    dist = [[float("inf")] * len(graph) for _ in range(len(graph))]
    for i in range(len(graph)):
        dist[i][i] = 0
    for u in range(len(graph)):
        for v, w in graph[u]:
            dist[u][v] = w
    for k in range(len(graph)):
        for i in range(len(graph)):
            for j in range(len(graph)):
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
    return dist

# Usage
graph = {0: [(1, 3), (2, 8)], 1: [(2, 1)], 2: [(0, 4)], 3: []}
print(floyd_warshall(graph))  # Output: Shortest paths between all vertices
```

---

## **13. Knapsack Problem**
- **Purpose**: Maximizes value while staying within a weight limit.
- **Best Time Complexity**: \( O(nW) \) (dynamic programming solution).
- **Space Complexity**: \( O(nW) \)

### Optimized Code:
```python
def knapsack(weights, values, W):
    n = len(weights)
    dp = [[0] * (W + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        for w in range(W + 1):
            if weights[i - 1] <= w:
                dp[i][w] = max(dp[i - 1][w], values[i - 1] + dp[i - 1][w - weights[i - 1]])
            else:
                dp[i][w] = dp[i - 1][w]
    return dp[n][W]

# Usage
weights = [1, 2, 3]
values = [10, 20, 30]
capacity = 5
print(knapsack(weights, values, capacity))  # Output: 50
```

---

## **14. Kadane's Algorithm**
- **Purpose**: Finds the maximum sum of a contiguous subarray.
- **Best Time Complexity**: \( O(n) \)
- **Space Complexity**: \( O(1) \)

### Optimized Code:
```python
def kadane(arr):
    max_sum = float("-inf")
    current_sum = 0
    for num in arr:
        current_sum = max(num, current_sum + num)
        max_sum = max(max_sum, current_sum)
    return max_sum

# Usage
arr = [-2, -3, 4, -1, -2, 1, 5, -3]
print(kadane(arr))  # Output: 7
```

---

## **15. Prim's Algorithm**
- **Purpose**: Finds the Minimum Spanning Tree (MST) for a graph.
- **Best Time Complexity**: \( O(E \log V) \) (using a priority queue).
- **Space Complexity**: \( O(V + E) \)

### Optimized Code:
```python
import heapq

def prims(graph, V):
    visited = [False] * V
    pq = [(0, 0)]  # (weight, node)
    total_weight = 0
    while pq:
        weight, node = heapq.heappop(pq)
        if visited[node]:
            continue
        visited[node] = True
        total_weight += weight
        for neighbor, w in graph[node]:
            if not visited[neighbor]:
                heapq.heappush(pq, (w, neighbor))
    return total_weight

# Usage
graph = {0: [(1, 10), (2, 6), (3, 5)], 1: [(0, 10), (3, 15)], 2: [(0, 6), (3, 4)], 3: [(0, 5), (1, 15), (2, 4)]}
print(prims(graph, 4))  # Output: Weight of MST
```

---

## **16. Kruskal's Algorithm**
- **Purpose**: Finds the Minimum Spanning Tree (MST) for a graph.
- **Best Time Complexity**: \( O(E \log E) \)
- **Space Complexity**: \( O(E + V) \)

### Optimized Code:
```python
def kruskal(edges, V):
    parent = list(range(V))

    def find(node):
        if parent[node] != node:
            parent[node] = find(parent[node])
        return parent[node]

    def union(u, v):
        root_u, root_v = find(u), find(v)
        if root_u != root_v:
            parent[root_u] = root_v

    edges.sort(key=lambda x: x[2])
    mst_weight = 0
    for u, v, w in edges:
        if find(u) != find(v):
            union(u, v)
            mst_weight += w
    return mst_weight

# Usage
edges = [(0, 1, 10), (0, 2, 6), (0, 3, 5), (1, 3, 15), (2, 3, 4)]
print(kruskal(edges, 4))  # Output: Weight of MST
```

---

## **17. RSA Algorithm**
- **Purpose**: Encryption and decryption for secure communication.
- **Time Complexity**: Depends on key generation and modular exponentiation.
- **Code**:
```python
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def rsa_key_generation(p, q):
    n = p * q
    phi = (p - 1) * (q - 1)
    e = 2
    while e < phi and gcd(e, phi) != 1:
        e += 1
    d = pow(e, -1, phi)
    return e, d, n

# Example
p, q = 61, 53
e, d, n = rsa_key_generation(p, q)
print(f"Public Key: ({e}, {n}), Private Key: ({d}, {n})")
```

---

This completes the explanations, optimized solutions, and complexity analysis for **all algorithms**. Let me know if you'd like further clarifications or additional examples!

Let’s complete the remaining 3 algorithms: **Hashing Algorithm**, **KMP Algorithm**, and **Boyer-Moore Algorithm**, providing the best time and space complexities along with optimal code.

---

## **18. Hashing Algorithm**
- **Purpose**: Converts data into a fixed-size hash value.
- **Best Time Complexity**: \( O(1) \) (ideal for hash table operations).
- **Space Complexity**: \( O(n) \) (hash table storage).

### Optimized Code:
```python
def hashing_example():
    # Create a hash table
    hash_table = {}
    # Insert key-value pairs
    hash_table["name"] = "Alice"
    hash_table["age"] = 25
    hash_table["city"] = "New York"
    # Retrieve a value using a key
    print("Name:", hash_table["name"])  # Output: Alice

# Usage
hashing_example()
```

### Notes:
- Hashing is the foundation of hash tables, dictionaries, and sets.
- Hash functions like MD5, SHA-256, or Python’s built-in hash are used for cryptographic or general purposes.

---

## **19. Knuth-Morris-Pratt (KMP) Algorithm**
- **Purpose**: Searches for a pattern in a text string efficiently by avoiding redundant comparisons.
- **Best Time Complexity**: \( O(n + m) \) (where \( n \) is the length of the text and \( m \) is the length of the pattern).
- **Space Complexity**: \( O(m) \) (for the LPS array).

### Optimized Code:
```python
def kmp_search(text, pattern):
    def compute_lps(pattern):
        lps = [0] * len(pattern)
        length = 0
        i = 1
        while i < len(pattern):
            if pattern[i] == pattern[length]:
                length += 1
                lps[i] = length
                i += 1
            else:
                if length != 0:
                    length = lps[length - 1]
                else:
                    lps[i] = 0
                    i += 1
        return lps

    lps = compute_lps(pattern)
    i = j = 0
    while i < len(text):
        if text[i] == pattern[j]:
            i += 1
            j += 1
        if j == len(pattern):
            print(f"Pattern found at index {i - j}")
            j = lps[j - 1]
        elif i < len(text) and text[i] != pattern[j]:
            if j != 0:
                j = lps[j - 1]
            else:
                i += 1

# Usage
text = "ababcabcabababd"
pattern = "ababd"
kmp_search(text, pattern)  # Output: Pattern found at index 10
```

---

## **20. Boyer-Moore Algorithm**
- **Purpose**: Searches for a pattern in a text string by using bad character and good suffix heuristics for skipping comparisons.
- **Best Time Complexity**: \( O(n / m) \) (in favorable cases).
- **Worst Time Complexity**: \( O(n \cdot m) \) (in the worst case).
- **Space Complexity**: \( O(m) \) (for bad character and good suffix tables).

### Optimized Code:
```python
def boyer_moore(text, pattern):
    def bad_character_table(pattern):
        table = {}
        for i in range(len(pattern)):
            table[pattern[i]] = i
        return table

    bad_char = bad_character_table(pattern)
    m, n = len(pattern), len(text)
    s = 0
    while s <= n - m:
        j = m - 1
        while j >= 0 and pattern[j] == text[s + j]:
            j -= 1
        if j < 0:
            print(f"Pattern found at index {s}")
            s += m - bad_char.get(text[s + m], -1) if s + m < n else 1
        else:
            s += max(1, j - bad_char.get(text[s + j], -1))

# Usage
text = "ABAAABCD"
pattern = "ABC"
boyer_moore(text, pattern)  # Output: Pattern found at index 4
```

---

### Final Thoughts on the Remaining Algorithms:
1. **Hashing Algorithm**:
   - Essential for data structures like hash tables, sets, and cryptographic operations.

2. **KMP Algorithm**:
   - Suitable for text pattern matching when repeated patterns are present.
   - Efficient for DNA sequence matching, log analysis, etc.

3. **Boyer-Moore Algorithm**:
   - More efficient than KMP for larger alphabets and longer texts.
   - Commonly used in search tools like `grep`.

Let me know if you’d like to go deeper into any specific algorithm or topic!