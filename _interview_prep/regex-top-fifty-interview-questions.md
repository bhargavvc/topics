Here is a list of 50 common interview scenario-based regex questions that a backend developer with 5 years of experience might encounter. Each question includes a brief description of what needs to be matched, followed by the regex pattern in Python using the `re` module.

### Regex Interview Questions with Python Examples

1. **Validate an Email Address**
   - Match a standard email format.
   ```python
   pattern = r"^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$"
   ```

2. **Extract Date from Text**
   - Extract dates formatted as YYYY-MM-DD.
   ```python
   pattern = r"\b\d{4}-\d{2}-\d{2}\b"
   ```

3. **Match a URL**
   - Match HTTP and HTTPS URLs.
   ```python
   pattern = r"https?://[\w.-]+(?:\.[\w.-]+)+[\w\-\._~:/?#\[\]@!$&'()*+,;=]+"
   ```

4. **IP Address Validation**
   - Validate IPv4 addresses.
   ```python
   pattern = r"^(?:[0-9]{1,3}\.){3}[0-9]{1,3}$"
   ```

5. **Password Strength Check**
   - Check for a password that contains at least one lowercase letter, one uppercase letter, one digit, and one special character with a minimum length of 8 characters.
   ```python
   pattern = r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[^a-zA-Z\d]).{8,}$"
   ```

6. **Credit Card Number Validation**
   - Validate credit card numbers (just format, not actual card validation).
   ```python
   pattern = r"^(?:4[0-9]{12}(?:[0-9]{3})?|5[1-5][0-9]{14}|3[47][0-9]{13}|6(?:011|5[0-9]{2})[0-9]{12}|(?:2131|1800|35\d{3})\d{11})$"
   ```

7. **Hexadecimal Color Code**
   - Match hexadecimal color codes.
   ```python
   pattern = r"#[0-9A-Fa-f]{6}\b"
   ```

8. **Username Validation**
   - Validate usernames starting with a letter and consisting of letters, digits, or underscores, 3-16 characters long.
   ```python
   pattern = r"^[a-zA-Z]\w{2,15}$"
   ```

9. **Extracting Tags**
   - Extract all hashtags from a string.
   ```python
   pattern = r"#(\w+)"
   ```

10. **Matching Phone Numbers**
    - Match phone numbers in multiple formats.
    ```python
    pattern = r"\b\d{3}[-.]?\d{3}[-.]?\d{4}\b"
    ```

11. **Matching a Specific Time Format**
    - Match time in HH:MM format.
    ```python
    pattern = r"\b([01]?[0-9]|2[0-3]):[0-5][0-9]\b"
    ```

12. **Postal Code Validation**
    - Match postal codes (U.S. ZIP code format).
    ```python
    pattern = r"\b\d{5}(?:-\d{4})?\b"
    ```

13. **HTML Tag Removal**
    - Remove all HTML tags from a string.
    ```python
    pattern = r"<[^>]*>"
    ```

14. **Finding Duplicate Words**
    - Find consecutive duplicate words in a string.
    ```python
    pattern = r"\b(\w+)\s+\1\b"
    ```

15. **Social Security Number**
    - Match a U.S. Social Security number.
    ```python
    pattern = r"\b\d{3}-\d{2}-\d{4}\b"
    ```

16. **Matching a License Plate**
    - Match standard U.S. license plate formats (e.g., ABC-1234).
    ```python
    pattern = r"\b[A-Z]{3}-\d{4}\b"
    ```

17. **Currency Validation**
    - Match currency amounts in USD format.
    ```python
    pattern = r"\$\d+(?:\.\d{2})?"
    ```

18. **Log Line Extraction**
    - Extract the timestamp and log level from a log line.
    ```python
    pattern = r"^\[(.*?)\] \[(.*?)\]"
    ```

19. **Quoted String Extraction**
    - Extract content inside double quotes.
    ```python
    pattern = r'"(.*?)"'
    ```

20. **IPv6 Address Validation**
    - Validate IPv6 addresses.
    ```python
    pattern = r"\b(?:[0-9a-fA-F]{1,4}:){7}[0-9a-fA-F]{1,4}\b"
    ```

21. **Extract Email Domain**
    - Extract the domain part of an email address.
    ```python
    pattern = r"@(\w+\.\w+)"
    ```

22. **Matching Markdown Links**
    - Extract the text and URL from Markdown-style links.
    ```python
    pattern = r"\[([^\]]+)\]\(([^)]+)\)"
    ```

23. **Multiline Comments**
    - Match multiline comments in code (C-style).
    ```python
    pattern = r"/\*.*?\*/"
    ```

24. **Script Tag Extraction**
    - Extract content inside `<script>` tags.
    ```python
    pattern = r"<script.*?>(.*?)</script>"
    ```

25. **ISBN Validation**
    - Validate ISBN-10 and ISBN-13.
    ```python
    pattern = r"(?:ISBN(?:-13)?:? )?(?=[0-9X]{10}\b|(?=(?:[0-9]+[- ]){3})[- 0-9X]{13}\b)(97[89][- ]?)?[0-9]{1,5}[- ]?[0-9]+[- ]?[0-9]+[- ]?[0-9X]\b"
    ```

26. **Word Boundary Match**
    - Match words starting with "pre".
    ```python
    pattern = r"\bpre\w*"
    ```

27. **Identifying SQL Injection**
    - Detect naive SQL injection attempts.
    ```python
    pattern = r"(?:\b(or|and)\b\s+(?:\d{1,10}\s*=\s*\d{1,10}))|(?:\b(or|and)\b\s+'[^']+')"
    ```

28. **Code Comment Removal**
    - Remove single line comments from code (C-style `//` comments).
    ```python
    pattern = r"//.*?$"
    ```

29. **Vehicle Identification Number (VIN)**
    - Match a standard 17-character VIN.
    ```python
    pattern = r"\b[A-HJ-NPR-Z0-9]{17}\b"
    ```

30. **Matching Roman Numerals**
    - Match valid Roman numerals up to 3999.
    ```python
    pattern = r"\bM{0,3}(CM|CD|D?C{0,3})(XC|XL|L?X{0,3})(IX|IV|V?I{0,3})\b"
    ```

31. **Extracting SQL Table Names**
    - Extract table names from SQL `SELECT` queries.
    ```python
    pattern = r"FROM\s+(\w+)"
    ```

32. **File Path Extraction**
    - Extract file paths from strings.
    ```python
    pattern = r"/[^/\s]+/[^/\s]+"
    ```

33. **CSV Parsing**
    - Match fields in a CSV (handling commas within quotes).
    ```python
    pattern = r'(?!\s*$)\s*(?:"([^"]*?"|[^",]*))(?:,|$)'
    ```

34. **Matching Scientific Notation**
    - Match numbers expressed in scientific notation.
    ```python
    pattern = r"\b\d+(\.\d+)?[eE][-+]?\d+\b"
    ```

35. **Latex Tag Removal**
    - Remove LaTeX formatting commands.
    ```python
    pattern = r"\\[\w\s]+(?:{.*?})?"
    ```

36. **Matching Nested Brackets**
    - Match nested brackets up to one level of nesting.
    ```python
    pattern = r"\[(?:[^\[\]]+|\[.*?\])\]"
    ```

37. **Identifying Redundant Spaces**
    - Match multiple consecutive spaces.
    ```python
    pattern = r"\s{2,}"
    ```

38. **Matching Leading Zeros**
    - Find numbers with leading zeros.
    ```python
    pattern = r"\b0+\d+\b"
    ```

39. **Extracting Function Calls**
    - Extract function calls and their arguments from code.
    ```python
    pattern = r"\b(\w+)\(([^)]*)\)"
    ```

40. **Validating Date (MM/DD/YYYY)**
    - Validate dates in MM/DD/YYYY format.
    ```python
    pattern = r"(0[1-9]|1[012])/(0[1-9

]|[12][0-9]|3[01])/[0-9]{4}"
    ```

41. **Matching MAC Addresses**
    - Validate MAC addresses.
    ```python
    pattern = r"\b(?:[A-Fa-f0-9]{2}[:-]){5}[A-Fa-f0-9]{2}\b"
    ```

42. **Python Decorator Extraction**
    - Extract decorators from Python code.
    ```python
    pattern = r"@[\w\.]+"
    ```

43. **Matching Floating-Point Numbers**
    - Match floating-point numbers including those in scientific notation.
    ```python
    pattern = r"\b-?\d+(\.\d+)?([eE][-+]?\d+)?\b"
    ```

44. **Identifying Proper Nouns**
    - Match capitalized words that aren't at the start of a sentence.
    ```python
    pattern = r"\B[A-Z]\w*"
    ```

45. **Matching Twitter Handles**
    - Extract Twitter usernames from text.
    ```python
    pattern = r"@\w+"
    ```

46. **Matching Email Threads**
    - Match "Re:" or "Fwd:" in email subjects.
    ```python
    pattern = r"\b(?:Re|Fwd):\s*"
    ```

47. **Matching CamelCase Words**
    - Match words in CamelCase format.
    ```python
    pattern = r"\b[A-Z][a-z]+[A-Z][a-zA-Z]*"
    ```

48. **Extracting Year from Text**
    - Extract four-digit years.
    ```python
    pattern = r"\b[1-2][0-9]{3}\b"
    ```

49. **Identifying Non-ASCII Characters**
    - Match characters outside the ASCII range.
    ```python
    pattern = r"[^\x00-\x7F]+"
    ```

50. **Matching Nested Parentheses**
    - Match content within nested parentheses.
    ```python
    pattern = r"\(([^()]|(?R))*\)"
    ```

These regex patterns are intended to serve as a starting point for further customization and refinement based on specific requirements and contexts you may face during interviews or actual development tasks.