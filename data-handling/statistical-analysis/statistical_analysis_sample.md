Let’s take **real-world examples** and apply the concepts and functions. I'll illustrate how each function can solve practical problems step-by-step, diving deeply into their workings.

---

## 1. **Linear Regression Using Statsmodels**
### Real-World Example: Predicting House Prices
Suppose you’re a real estate agent, and you want to predict house prices (`y`) based on the size of the house in square feet (`x`). You have historical data for houses that includes:
- Size of the house in square feet (`x`).
- Price of the house (`y`).

#### Data Example:
```python
import numpy as np
import statsmodels.api as sm

# Historical data (size in square feet and price in thousands of dollars)
x = np.array([800, 1000, 1200, 1500, 1800])  # House sizes
y = np.array([200, 250, 300, 350, 400])  # Prices in thousands of dollars
```

### Code Explanation:
```python
def linear_regression_using_statsmodels(x, y):
    """
    Performs a linear regression analysis using Statsmodels to predict house prices.
    """
    X = sm.add_constant(x)  # Adds a column of 1s to calculate the intercept (b).
    model = sm.OLS(y, X).fit()  # Fits the regression model using OLS.
    print("Statsmodels Linear Regression Results:")
    return model.summary()  # Returns detailed regression results.
```

### Applying the Code:
```python
summary = linear_regression_using_statsmodels(x, y)
print(summary)
```

#### What Happens Internally:
1. **Adds a Constant**:
   Converts `x` into a matrix to include the intercept:
   ```
   X = [
       [1, 800],
       [1, 1000],
       [1, 1200],
       [1, 1500],
       [1, 1800]
   ]
   ```

2. **Fits the Line**:
   The regression model solves:
   \[
   y = mx + b
   \]
   For the above data, it finds:
   - \( m \) (slope): The price increase per square foot.
   - \( b \) (intercept): Base price when the size is 0.

3. **Interprets Results**:
   - **Coefficients**: Show how size affects price.
   - **R-squared**: Indicates how well the model fits (closer to 1 is better).
   - **P-value**: Checks if the relationship is statistically significant.

#### Real Insight:
If the slope \( m = 0.2 \), it means the price increases by $200 for every additional square foot.

---

## 2. **T-test Using Scipy**

### Real-World Example: Testing Medication Effectiveness
You want to test if a new medication improves blood pressure compared to a placebo. You have data for two groups:
- Group 1 (Medication): Blood pressure reductions after taking the medication.
- Group 2 (Placebo): Blood pressure reductions after taking a placebo.

#### Data Example:
```python
import numpy as np
from scipy import stats

group1 = np.random.normal(-10, 5, 100)  # Blood pressure reductions (mean=-10).
group2 = np.random.normal(-5, 5, 100)  # Placebo reductions (mean=-5).
```

### Code Explanation:
```python
def t_test_using_scipy(group1, group2):
    """
    Performs a two-sample t-test to compare the effectiveness of medication vs placebo.
    """
    t_stat, p_value = stats.ttest_ind(group1, group2)  # T-test for independent samples.
    return t_stat, p_value  # Returns the t-statistic and p-value.
```

### Applying the Code:
```python
t_stat, p_value = t_test_using_scipy(group1, group2)
print(f"T-statistic = {t_stat}, P-value = {p_value}")
```

#### What Happens Internally:
1. **Calculates Mean Difference**:
   Compares the mean reduction in blood pressure:
   \[
   \text{Mean Reduction (Group 1)} = -10, \, \text{Mean Reduction (Group 2)} = -5
   \]

2. **Tests Null Hypothesis**:
   Null Hypothesis (\( H_0 \)): The means are equal (medication has no effect).
   Alternative Hypothesis (\( H_A \)): The means are different (medication is effective).

3. **Computes T-statistic**:
   Measures how different the group means are, relative to variability:
   \[
   t = \frac{\text{Mean Difference}}{\text{Standard Error}}
   \]

4. **P-value**:
   If \( \text{P-value} < 0.05 \), reject \( H_0 \): The medication significantly reduces blood pressure.

---

## 3. **Correlation Using Pingouin**

### Real-World Example: Studying Correlation Between Study Time and Exam Scores
You’re a teacher analyzing whether more study hours lead to better exam scores.

#### Data Example:
```python
import pandas as pd
import pingouin as pg

study_time = [1, 2, 3, 4, 5, 6, 7]  # Hours of study.
exam_scores = [50, 55, 60, 65, 70, 80, 90]  # Exam scores.
data = pd.DataFrame({'study_time': study_time, 'exam_scores': exam_scores})
```

### Code Explanation:
```python
def correlation_using_pingouin(data):
    """
    Computes the correlation between study time and exam scores using Pingouin.
    """
    correlation = pg.corr(data['study_time'], data['exam_scores'])  # Computes correlation and p-value.
    return correlation
```

### Applying the Code:
```python
correlation = correlation_using_pingouin(data)
print(f"Correlation Coefficient (r): {correlation['r'].values[0]}")
print(f"P-value: {correlation['p-val'].values[0]}")
```

#### What Happens Internally:
1. **Computes Correlation Coefficient (\( r \))**:
   Measures the strength of the relationship:
   \[
   r = \frac{\text{Covariance of Study Time and Scores}}{\text{Product of Standard Deviations}}
   \]
   For this data, \( r = 0.95 \), meaning a strong positive correlation.

2. **Tests Statistical Significance**:
   - Null Hypothesis (\( H_0 \)): No correlation (\( r = 0 \)).
   - Alternative Hypothesis (\( H_A \)): There is correlation (\( r \neq 0 \)).

3. **Interprets Results**:
   - If \( \text{P-value} < 0.05 \), reject \( H_0 \): The correlation is statistically significant.
   - For \( r = 0.95 \), it’s clear more study hours lead to higher scores.

---

### Summary
1. **Linear Regression**:
   Use it to **predict** one variable (e.g., house prices) based on another (e.g., house size).
2. **T-test**:
   Use it to **compare** two groups (e.g., medication vs placebo) and see if their means differ significantly.
3. **Correlation**:
   Use it to **analyze relationships** (e.g., study time and exam scores) and see if they’re linked.

Would you like additional clarification on any part?