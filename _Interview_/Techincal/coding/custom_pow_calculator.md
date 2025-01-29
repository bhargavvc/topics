#dont try to understnd logarithms here too complex if u dont knwo about logarthims

#pseudo code
# Here’s the **plain English version** of the power function logic:  

# 1. **Handle Special Cases:**  
#    - If the base is `0` and the exponent is `0` or negative, return an error.  
#    - If the base is `0` with a positive exponent, return `0`.  

# 2. **Handle Negative Exponent:**  
#    - If the exponent is negative, take the **reciprocal** of the base (`1/base`) and make the exponent positive.  

# 3. **Split the Exponent into Two Parts:**  
#    - The **whole number** part (used for simple multiplication).  
#    - The **fractional** part (handled with logarithms and exponentiation).  

# 4. **Compute the Integer Power:**  
#    - Multiply the base by itself as many times as the integer part of the exponent.  

# 5. **Compute the Fractional Power (if needed):**  
#    - Use logarithm and exponentiation to compute the fractional exponent.  

# 6. **Multiply Both Results Together and Return the Final Answer.**




```python
#Manual Power Calculation with Float Support
import math
def power(base, exponent):
    # Handle edge case for base 0
    if base == 0 and exponent <= 0:
        raise ValueError("Base 0 cannot have zero or negative exponent")
    if base == 0:
        return 0

    # # Handle negative exponent
    #why we need to reciporcal of base and exponent here ?
    if exponent < 0:
        base = 1 / base
        exponent = -exponent

    # Separate integer and fractional parts of the exponent
    #int_part is for for loop to handle result cummulative sum
    #but what is need to fraction part
    int_part = int(exponent)
    frac_part = exponent - int_part

    # Calculate the integer power using iterative multiplication
    result = 1
    for _ in range(int_part):
        result *= base
    
    #tell me how this works ..math.exp(frac_part * math.log(base))
    # Calculate the fractional part using math.exp and math.log
    if frac_part != 0:
        result *= math.exp(frac_part * math.log(base))

    return result

# Example usage
print(f"4^-2.5 = {power(4, -2.5)}")   # 4^-2.5 = 0.03125



print(f"2^3 = {power(2, 3)}")         # 2^3 = 8
print(f"2^-3 = {power(2, -3)}")       # 2^-3 = 0.125
print(f"5^0.5 = {power(5, 0.5)}")     # 5^0.5 = sqrt(5) = 2.236...
print(f"9^0.5 = {power(9, 0.5)}")     # 9^0.5 = sqrt(9) = 3
print(f"2^2.5 = {power(2, 2.5)}")     # 2^2.5 = ~5.656

```
# explaination 
Let's break this down step by step for the first three examples: \( 2^3 \), \( 2^{-3} \), and \( 4^{-2.5} \).

---

### **1. Example: \( 2^3 \)**

#### **Step-by-Step Execution**:
1. **Input**: `base = 2`, `exponent = 3`.
2. **Check Base 0**: The base is not 0, so no error is raised.
3. **Separate Exponent**:
   - Integer part: `int_part = int(3) = 3`.
   - Fractional part: `frac_part = 3 - int(3) = 0`.
4. **Calculate Integer Power**:
   - Initialize `result = 1`.
   - Iterative multiplication for `int_part = 3`:
     - Iteration 1: \( result = 1 \times 2 = 2 \).
     - Iteration 2: \( result = 2 \times 2 = 4 \).
     - Iteration 3: \( result = 4 \times 2 = 8 \).
   - Final result after integer power: \( result = 8 \).
5. **Fractional Part**:
   - Since `frac_part = 0`, no further calculation is needed.
6. **Final Result**: Return \( result = 8 \).

#### **Output**:
```
2^3 = 8
```

---

### **2. Example: \( 2^{-3} \)**

#### **Step-by-Step Execution**:
1. **Input**: `base = 2`, `exponent = -3`.
2. **Check Base 0**: The base is not 0, so no error is raised.
3. **Separate Exponent**:
   - Integer part: `int_part = int(-3) = -3`.
   - Fractional part: `frac_part = -3 - int(-3) = 0`.
4. **Handle Negative Exponent**:
   - The `if` block for negative exponents is commented out. However, manually, the calculation assumes:
     - Convert the base: \( base = \frac{1}{2} = 0.5 \).
     - Convert the exponent: \( exponent = -(-3) = 3 \).
5. **Separate Exponent (Revisited)**:
   - Integer part: `int_part = 3`.
   - Fractional part: `frac_part = 0`.
6. **Calculate Integer Power**:
   - Initialize `result = 1`.
   - Iterative multiplication for `int_part = 3`:
     - Iteration 1: \( result = 1 \times 0.5 = 0.5 \).
     - Iteration 2: \( result = 0.5 \times 0.5 = 0.25 \).
     - Iteration 3: \( result = 0.25 \times 0.5 = 0.125 \).
   - Final result after integer power: \( result = 0.125 \).
7. **Fractional Part**:
   - Since `frac_part = 0`, no further calculation is needed.
8. **Final Result**: Return \( result = 0.125 \).

#### **Output**:
```
2^-3 = 0.125
```

---

### **3. Example: \( 4^{-2.5} \)**

#### **Step-by-Step Execution**:
1. **Input**: `base = 4`, `exponent = -2.5`.
2. **Check Base 0**: The base is not 0, so no error is raised.
3. **Separate Exponent**:
   - Integer part: `int_part = int(-2.5) = -2`.
   - Fractional part: `frac_part = -2.5 - int(-2) = -0.5`.
4. **Handle Negative Exponent**:
   - Convert the base: \( base = \frac{1}{4} = 0.25 \).
   - Convert the exponent: \( exponent = -(-2.5) = 2.5 \).
5. **Separate Exponent (Revisited)**:
   - Integer part: `int_part = 2`.
   - Fractional part: `frac_part = 0.5`.
6. **Calculate Integer Power**:
   - Initialize `result = 1`.
   - Iterative multiplication for `int_part = 2`:
     - Iteration 1: \( result = 1 \times 0.25 = 0.25 \).
     - Iteration 2: \( result = 0.25 \times 0.25 = 0.0625 \).
   - Final result after integer power: \( result = 0.0625 \).
7. **Calculate Fractional Power**:
   - \( result = result \times \exp(\text{frac_part} \times \log(\text{base})) \).
   - Using `math.exp` and `math.log`:
     - \( \exp(0.5 \times \log(0.25)) = \exp(0.5 \times -1.386) \approx \exp(-0.693) \approx 0.5 \).
   - \( result = 0.0625 \times 0.5 = 0.03125 \).
8. **Final Result**: Return \( result = 0.03125 \).

#### **Output**:
```
4^-2.5 = 0.03125
```

---

### **Summary of Results**:
1. \( 2^3 = 8 \)
2. \( 2^{-3} = 0.125 \)
3. \( 4^{-2.5} = 0.03125 \)



######### questions explaination 
Let's go through your questions one by one.

---

### **1. Why do we take the reciprocal of the base when the exponent is negative?**
```python
if exponent < 0:
    base = 1 / base
    exponent = -exponent
```
#### **Reasoning:**
Mathematically, when you have a negative exponent:
\[
a^{-b} = \frac{1}{a^b}
\]
This means:
- Instead of calculating \( a^{-b} \), we calculate \( (1/a)^b \), which avoids dealing directly with negative exponents.
- We **convert** the problem into a positive exponent calculation, making the logic simpler.

#### **Example:**
For \( 4^{-2.5} \):
- Convert `base = 4` → `1 / 4 = 0.25`
- Convert `exponent = -2.5` → `2.5`
- Now, compute \( 0.25^{2.5} \).

---

### **2. Why do we separate the integer and fractional parts of the exponent?**
```python
int_part = int(exponent)
frac_part = exponent - int_part
```
#### **Integer Part (`int_part`)**:
- The integer part helps us perform **iterative multiplication** using a simple loop.

#### **Fractional Part (`frac_part`)**:
- The fractional exponent represents roots or fractional powers, which cannot be handled easily using multiplication loops.
- Instead, we use logarithmic and exponential functions to compute them.

#### **Example:**
For \( 4^{2.5} \):
- Integer part: `int_part = 2`
- Fractional part: `frac_part = 0.5`
- We first calculate \( 4^2 \) using a loop.
- Then, we compute \( 4^{0.5} = \sqrt{4} = 2 \) using logarithmic methods.

---

### **3. How does `math.exp(frac_part * math.log(base))` work?**
```python
if frac_part != 0:
    result *= math.exp(frac_part * math.log(base))
```
This part computes:
\[
a^b = e^{b \cdot \ln(a)}
\]
where:
- \( \ln(a) \) (natural logarithm of `base`) gives the exponent needed to express `base` as a power of \( e \).
- Multiplying by `frac_part` scales it accordingly.
- `math.exp()` raises \( e \) to that power, effectively computing `base ** frac_part`.

#### **Example Calculation for \( 4^{0.5} \)**
- Compute \( \ln(4) \approx 1.386 \)
- Multiply by `frac_part = 0.5`:  
  \( 0.5 \times 1.386 = 0.693 \)
- Compute \( e^{0.693} \approx 2 \), which matches \( \sqrt{4} \).

---

### **Full Walkthrough for \( 4^{-2.5} \)**

#### **Step 1: Handle Negative Exponent**
- `base = 4`, `exponent = -2.5`
- Convert:
  - `base = 1 / 4 = 0.25`
  - `exponent = -(-2.5) = 2.5`

#### **Step 2: Separate Integer and Fractional Parts**
- `int_part = int(2.5) = 2`
- `frac_part = 2.5 - 2 = 0.5`

#### **Step 3: Compute Integer Power (0.25²)**
\[
0.25 \times 0.25 = 0.0625
\]

#### **Step 4: Compute Fractional Power (0.25^{0.5})**
- Compute \( \ln(0.25) \approx -1.386 \)
- Multiply: \( 0.5 \times -1.386 = -0.693 \)
- Compute \( e^{-0.693} \approx 0.5 \)
- Multiply: \( 0.0625 \times 0.5 = 0.03125 \)

#### **Final Result:**
```
4^-2.5 = 0.03125
```

---

### **Summary of Your Questions:**
1. **Reciprocal for negative exponent**: Converts \( a^{-b} \) into \( (1/a)^b \) to make computation easier.
2. **Fractional part**: Used to compute non-integer exponents, which cannot be handled by simple loops.
3. **math.exp(frac_part * math.log(base))**: Uses logarithm and exponentiation to calculate fractional powers.

Would you like a deeper breakdown of any specific part? 😊