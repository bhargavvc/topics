
### 2. **Packaging Principles - Cohesion**

#### **2.1 Release Reuse Equivalency Principle (REP)**
*Group reusable components together.*

- **Why?** Releasing and reusing components together ensures consistency.
- **Example:** Grouping authentication and user management in one package makes sense because they are reused together.

---

#### **2.2 Common Closure Principle (CCP)**
*Classes that change together should stay together.*

- **Why?** If classes are related in functionality, putting them in the same package reduces the impact of changes.
- **Example:** Grouping all payment-related classes in a single package ensures cohesive updates.

---

#### **2.3 Common Reuse Principle (CRP)**
*Classes that are reused together should stay together.*

- **Why?** Reduces unnecessary dependencies.
- **Example:** Grouping UI-related classes in a single package ensures consistent styling and behavior.

---
