Let’s add an **OAuth 2.0** example to the previous **Single Sign-On (SSO)** explanation. OAuth 2.0 is one of the most widely used protocols for implementing SSO and user authentication.

---

### **OAuth 2.0 Example**

**Scenario**: Logging into an application (e.g., a task management app) using your Google account.

---

### **Steps in OAuth Flow**
1. **User Initiates Login**:
   - The user clicks **"Log in with Google"** on the task management app.

2. **Redirect to Authorization Server**:
   - The app redirects the user to the Google Authorization Server.
   - The user is prompted to grant the app permission to access their Google account details (e.g., email, profile).

3. **Authorization Code**:
   - Once the user approves, Google sends an **authorization code** to the app’s backend via a redirect URL.

4. **Token Exchange**:
   - The app exchanges the authorization code for an **access token** by making a server-to-server request to Google's token endpoint.

5. **Access Protected Resources**:
   - Using the access token, the app can retrieve user information (e.g., profile, email) from Google’s APIs.

6. **Grant Access**:
   - The app uses the retrieved user data to log the user in or create an account.

---

### **OAuth Implementation Example**

**Libraries Required**:
Install `requests` and `Flask` for demonstration:
```bash
pip install flask requests
```

---

**Python Implementation**:
```python
from flask import Flask, redirect, request, url_for
import requests

app = Flask(__name__)

# OAuth Configuration
CLIENT_ID = "your-google-client-id"
CLIENT_SECRET = "your-google-client-secret"
REDIRECT_URI = "http://localhost:5000/callback"
AUTHORIZATION_BASE_URL = "https://accounts.google.com/o/oauth2/auth"
TOKEN_URL = "https://oauth2.googleapis.com/token"
USER_INFO_URL = "https://www.googleapis.com/oauth2/v1/userinfo"

@app.route("/")
def home():
    return 'Welcome! <a href="/login">Log in with Google</a>'

@app.route("/login")
def login():
    # Redirect user to Google's OAuth 2.0 authorization page
    auth_url = (
        f"{AUTHORIZATION_BASE_URL}?response_type=code&client_id={CLIENT_ID}"
        f"&redirect_uri={REDIRECT_URI}&scope=email%20profile"
    )
    return redirect(auth_url)

@app.route("/callback")
def callback():
    # Retrieve the authorization code from the query parameters
    code = request.args.get("code")

    # Exchange the authorization code for an access token
    token_response = requests.post(
        TOKEN_URL,
        data={
            "code": code,
            "client_id": CLIENT_ID,
            "client_secret": CLIENT_SECRET,
            "redirect_uri": REDIRECT_URI,
            "grant_type": "authorization_code",
        },
    )
    token_response_data = token_response.json()
    access_token = token_response_data.get("access_token")

    # Use the access token to retrieve user information
    user_info_response = requests.get(
        USER_INFO_URL, headers={"Authorization": f"Bearer {access_token}"}
    )
    user_info = user_info_response.json()

    return f"Hello, {user_info['name']}! Your email is {user_info['email']}."

if __name__ == "__main__":
    app.run(debug=True)
```

---

### **How to Test the Example**
1. **Set up a Google OAuth Client**:
   - Go to [Google Cloud Console](https://console.cloud.google.com/).
   - Create a new project.
   - Enable the **OAuth 2.0 API**.
   - Create credentials for a Web Application.
   - Set the **redirect URI** to `http://localhost:5000/callback`.
   - Copy the `CLIENT_ID` and `CLIENT_SECRET` into the script.

2. **Run the Flask App**:
   ```bash
   python app.py
   ```

3. **Log in with Google**:
   - Visit `http://localhost:5000`.
   - Click on "Log in with Google."
   - Authenticate with your Google account.
   - You’ll be redirected to the callback URL, displaying your name and email.

---

### **Key Components in OAuth Flow**
| **Component**           | **Purpose**                                                |
|--------------------------|-----------------------------------------------------------|
| **Authorization Server** | Verifies user credentials (e.g., Google).                 |
| **Client**               | The app requesting access (e.g., task management app).    |
| **Resource Owner**       | The user granting access.                                 |
| **Access Token**         | Short-lived token for accessing protected resources.      |
| **Refresh Token**        | Optional; used to get a new access token when it expires. |

---

### **Advantages of OAuth for SSO**
1. **User Convenience**:
   - Avoids creating multiple accounts for different applications.
2. **Enhanced Security**:
   - Apps do not store user passwords; they rely on tokens.
3. **Scalable**:
   - Works across multiple platforms and services.

---

Let me know if you need further clarification or additional examples!