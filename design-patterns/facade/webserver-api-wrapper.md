
### **Additional Example: Web Service API Wrapper**

**Scenario**:

An application needs to interact with an external web service API that has multiple endpoints and requires specific request formats.

**Challenge**:

- Handling authentication tokens.
- Formatting requests and parsing responses.
- Managing retries and error handling.

**Solution Using the Facade Pattern**:

- Create an `ApiFacade` class that provides simple methods for the required operations.
- The facade handles authentication, request formatting, and response parsing.

**Implementation**:

```python
# api_facade.py
import requests

class ApiFacade:
    def __init__(self, api_key):
        self.api_key = api_key
        self.base_url = "https://api.example.com"

    def _make_request(self, endpoint, params):
        headers = {'Authorization': f'Bearer {self.api_key}'}
        response = requests.get(f"{self.base_url}/{endpoint}", headers=headers, params=params)
        if response.status_code == 200:
            return response.json()
        else:
            # Handle errors, retries, etc.
            response.raise_for_status()

    def get_user_info(self, user_id):
        return self._make_request(f"users/{user_id}", {})

    def get_user_posts(self, user_id):
        return self._make_request(f"users/{user_id}/posts", {})

    def search_posts(self, query):
        return self._make_request("posts/search", {'q': query})
```

**Usage**:

```python
# client.py
from api_facade import ApiFacade

def main():
    api = ApiFacade(api_key="your_api_key_here")

    user_info = api.get_user_info(user_id=123)
    print("User Info:", user_info)

    user_posts = api.get_user_posts(user_id=123)
    print("User Posts:", user_posts)

    search_results = api.search_posts(query="facade pattern")
    print("Search Results:", search_results)

if __name__ == "__main__":
    main()
```

**Explanation**:

- The `ApiFacade` class simplifies interaction with the web service API.
- Clients use high-level methods without worrying about authentication and request details.
- The facade handles error checking and can implement retries or fallback mechanisms.

---