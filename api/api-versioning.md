**API Versioning** with  **ShopEase Example**, which provides an e-commerce API that returns product information. We’ll imagine the company evolving its API over time, adding new fields, changing response formats, and deprecating old behavior. Using this single real-world-style scenario, we’ll walk through each versioning approach—one by one—and explain in detail how it would work, what the URLs look like, what clients see, the pros and cons, and why a company might choose or avoid that method.

---

# ShopEase API Evolution

**Initial Situation:**  
ShopEase starts with a simple API that returns products. Initially, the API returns just a product’s `id` and `name`:

- **Initial Endpoint (no versioning yet):**  
  `https://api.shopease.com/products`  
  **Response (JSON):**
  ```json
  [
    { "id": 1, "name": "Laptop" },
    { "id": 2, "name": "Headphones" }
  ]
  ```

**The Problem:**  
As time goes on, ShopEase wants to add more fields (like `description`, `price`, `stock`), change response formats, and possibly remove old fields that are no longer needed. They need a strategy to manage these changes so that existing clients aren’t suddenly broken. This is where API versioning comes into play.

---

## 1. URI Versioning

**Concept:**  
URI versioning involves embedding the version number directly into the identifier for the resource. In practice, this often means placing a version segment right in the URL path.

**What It Looks Like:**  
First version might have been:  
`https://api.shopease.com/v1/products`

When ShopEase updates the product resource in a breaking way (e.g., changing `name` to `title`), they introduce a new version:  
`https://api.shopease.com/v2/products`

**Example Evolution:**
- **v1:** Returns `id`, `name`.  
  `https://api.shopease.com/v1/products`  
  ```json
  [
    { "id": 1, "name": "Laptop" },
    { "id": 2, "name": "Headphones" }
  ]
  ```
  
- **v2:** Returns `id`, `title`, `price`.  
  `https://api.shopease.com/v2/products`  
  ```json
  [
    { "id": 1, "title": "Laptop", "price": 999.99 },
    { "id": 2, "title": "Headphones", "price": 199.99 }
  ]
  ```

**Advantages:**
- **Clarity:** Version is immediately visible in the URL. Easy for developers to see which version they’re using.
- **Routing Simplicity:** The server can route `v1` and `v2` to different internal code paths easily.

**Challenges:**
- **URL Clutter:** With many versions, you get many endpoints: `/v3/products`, `/v4/products`, etc.
- **Client Disruption:** If a client’s integrated with `v1` and you remove it later, they must update their endpoints.

**Real-World Equivalent:**
- **Twitter API:** Uses version numbers in the URL (e.g., `/1.1/`).
- **GitHub API:** Has endpoints like `/v3/`.

---

## 2. Path Versioning (a Subset of URI Versioning)

**Concept:**  
Path versioning is essentially the same as URI versioning, but specifically refers to placing the version number as a path segment. Since URI versioning can sometimes mean versioning in other URI components (query parameters, etc.), path versioning is the most direct and common form of URI versioning.

**What It Looks Like:**
`https://api.shopease.com/api/v2/products`

The `v2` is a path segment after `/api/`. This is essentially the same as the above example but often discussed as a straightforward approach under URI versioning.

**Advantages & Challenges:**  
Identical to URI versioning since path versioning is the most typical way URI versioning is done.

---

## 3. Query Parameter Versioning

**Concept:**  
Instead of changing the path, keep the URL the same but add a query parameter for versioning.

**What It Looks Like:**  
`https://api.shopease.com/products?version=2`

**v1 Response:**  
`https://api.shopease.com/products?version=1`  
```json
[
  { "id": 1, "name": "Laptop" }
]
```

**v2 Response:**  
`https://api.shopease.com/products?version=2`  
```json
[
  { "id": 1, "title": "Laptop", "price": 999.99 }
]
```

**Advantages:**
- **Clean Base URL:** The main endpoint (`/products`) stays the same, only the parameter differs.
- **Easy Switching:** Clients can switch versions just by changing a query parameter, no need to change the entire endpoint.

**Challenges:**
- **Caching Complexity:** Different query params can affect how caches treat these requests.  
- **Less Visible:** Developers might not notice the version parameter as easily as seeing `v1` in the path.
- **Tooling Support:** Some tooling and documentation generators might prefer version in the path for clarity.

**Real-World Equivalent:**
- **YouTube Data API:** Uses parameters like `v=` to indicate version.

---

## 4. Subdomain Versioning

**Concept:**  
Put the version number in the subdomain, so each version is essentially a separate host.

**What It Looks Like:**
- **v1:** `https://v1.api.shopease.com/products`  
- **v2:** `https://v2.api.shopease.com/products`

**Advantages:**
- **Clear Isolation:** Each version lives under its own subdomain, which can have its own infrastructure, codebase, or even server.
- **Complete Independence:** v1 and v2 can run on different stacks or versions of runtime if needed.

**Challenges:**
- **DNS & Ops Complexity:** Requires managing multiple DNS entries.  
- **More Complex Setup:** Clients must change the entire host to upgrade versions.

**Real-World Equivalent:**
- Historically, some APIs or services isolate completely different versions or environments this way (e.g., `sandbox.api.example.com` vs `api.example.com` for different stages). Versioning by subdomain is less common but still a possible approach.

---

## 5. Header Versioning

**Concept:**  
The client specifies the version it wants via a special HTTP header. The URL doesn’t change at all; the version info is in the request header.

**What It Looks Like:**
- **URL:** `https://api.shopease.com/products`
- **Header:** `Accept: application/vnd.shopease.v2+json`

**Server Behavior:**
If the client sends:
```http
GET /products HTTP/1.1
Host: api.shopease.com
Accept: application/vnd.shopease.v1+json
```
They get the v1 response:
```json
[
  { "id": 1, "name": "Laptop" }
]
```

If they send:
```http
GET /products HTTP/1.1
Host: api.shopease.com
Accept: application/vnd.shopease.v2+json
```
They get v2:
```json
[
  { "id": 1, "title": "Laptop", "price": 999.99 }
]
```

**Advantages:**
- **Clean URLs:** No clutter in the URL at all.
- **Flexible Negotiation:** You can easily add more parameters in headers for content-type, language, etc.
  
**Challenges:**
- **Less Visibility:** Clients need to remember to set the header. The version isn’t visible in the URL, making it less intuitive at a glance.
- **Tooling Overhead:** Some developers find it harder to test or debug since you must remember custom headers.

**Real-World Equivalent:**
- **GitHub API:** Allows specifying API versions in the `Accept` header.

---

## 6. Content Negotiation

**Concept:**  
Content negotiation uses the `Accept` header to select not just format, but also the version. Similar to header versioning, but more standardized around the idea of negotiating response type (including version) rather than using custom headers.

**What It Looks Like:**
- `GET https://api.shopease.com/products`
- `Accept: application/json; version=2`

**Server Behavior:**
- Checks the `Accept` header’s `version` parameter and returns the appropriate response for that version.

**Advantages:**
- **Combines Version & Format:** You can say `Accept: application/json; version=2` or `Accept: application/xml; version=1`.
- **Standards-Based:** Aligns well with the idea of content negotiation already built into HTTP.

**Challenges:**
- **Complexity for Clients:** Clients must be configured to send these headers.  
- **Less Obvious Versioning Mechanism:** It’s not as straightforward as changing a URL segment.

**Real-World Equivalent:**
- **Facebook Graph API:** Allows specifying different fields and versions through headers and parameters that negotiate what you get.

---

## 7. Timestamp Versioning

**Concept:**  
Each API version is associated with a release date (timestamp). Clients specify which date’s version they want.

**What It Looks Like:**
- `https://api.shopease.com/products?version=2024-01-15`
  
On `2024-01-15`, ShopEase released a new API version that now includes `title` and `price`. If the client uses `version=2024-01-15`, they get that snapshot.

**Advantages:**
- **Historical Clarity:** It’s clear when each version was released. Clients can say, “we’re using the API as it was on January 15, 2024.”
- **Good for Auditing & Compliance:** Regulated industries can track exactly what the API looked like at any point in time.

**Challenges:**
- **Less Intuitive:** Clients must remember dates instead of simple version numbers.  
- **Version Sprawl:** If you release frequently, you end up with many date-based versions.

**Real-World Equivalent:**
- **Stripe & Google Cloud APIs:** They often use date-based versions (like `/2020-08-27/`) to indicate when a specific version’s features were locked in.

---

## 8. Semantic Versioning

**Concept:**  
Use semantic versioning (`MAJOR.MINOR.PATCH`) to communicate what kind of changes happened:

- Major: Breaking changes
- Minor: Backward-compatible new features
- Patch: Backward-compatible bug fixes

**What It Looks Like:**
`https://api.shopease.com/v1.2.0/products`

If ShopEase introduces a breaking change (rename `name` to `title`), they move to `v2.0.0`. If they add a field that doesn’t break anything, that’s `v1.1.0`. A minor fix with no break is `v1.0.1`.

**Advantages:**
- **Clear Indication of Change Type:** Clients know if an update is just a fix or a breaking change.
- **Predictable Evolution:** Follows a well-known pattern widely understood in software development.

**Challenges:**
- **More Complex Version Numbers:** Clients must pay attention to three numbers instead of just one.
- **Still Need a Location for Version:** You still have to put these numbers somewhere—in the URL, headers, or another method.

**Real-World Equivalent:**
- **Node.js & Many Libraries:** Strictly follow semantic versioning so developers know what to expect.
- **Stripe API:** Incorporates semantic versions in their SDKs and sometimes in their API headers.

---

## Summary of Each Strategy with Our ShopEase Example

| Strategy                 | Example Endpoint/Headers                              | Visibility of Version | Advantages                                 | Challenges                                      |
|--------------------------|---------------------------------------------------------|-----------------------|---------------------------------------------|-------------------------------------------------|
| URI Versioning           | `https://api.shopease.com/v2/products`                 | High (in URL)         | Easy routing, immediate clarity             | URL clutter, must maintain multiple base paths   |
| Path Versioning          | `https://api.shopease.com/api/v2/products`             | High (in URL)         | Modular grouping, simple concept            | Similar to URI versioning challenges             |
| Query Parameter Versioning | `https://api.shopease.com/products?version=2`       | Medium (in params)    | Clean base URL, easy switching              | Harder caching, less obvious to spot version     |
| Subdomain Versioning     | `https://v2.api.shopease.com/products`                 | High (in host)        | Strong isolation, independent infra          | DNS management overhead, more ops complexity     |
| Header Versioning        | `Accept: application/vnd.shopease.v2+json`             | Low (in headers)      | Clean URLs, flexible                       | Hidden from quick inspection, requires header setup |
| Content Negotiation      | `Accept: application/json; version=2`                  | Low (in headers)      | Fine-grained control (version & format)     | Complexity for clients, less intuitive to humans |
| Timestamp Versioning     | `https://api.shopease.com/products?version=2024-01-15` | Medium (in params)    | Historical clarity, auditing                | Potential confusion, too many dates to track     |
| Semantic Versioning       | `https://api.shopease.com/v1.2.0/products`            | High (in URL)         | Communicates nature of changes              | More complex version numbers, still need a location |

---

## Final Thoughts

- **No One-Size-Fits-All:** The right versioning strategy depends on your organization’s needs—how often you change the API, how many clients you have, how sensitive they are to breakage, and what tooling they use.
- **Combining Approaches:** Some companies combine approaches. For example, they might use semantic versioning numbers in the URL path, or use timestamp versioning as query parameters.
- **Clarity and Communication:** The most important aspect is that your versioning strategy is well-documented and communicated clearly to clients.
