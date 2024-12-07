
### 3. **Packaging Principles - Coupling**

#### **3.1 Acyclic Dependencies Principle (ADP)**
*Avoid cyclic dependencies between packages.*

- **Why?** Cycles create tight coupling and make the system harder to understand.
- **Solution:** Use dependency injection or abstractions to break cycles.

---

#### **3.2 Stable Dependencies Principle (SDP)**
*Depend on more stable components.*

- **Why?** Stable components change less often, reducing the risk of breaking dependent components.

---

#### **3.3 Stable Abstractions Principle (SAP)**
*Stable components should be abstract to allow for flexibility.*

- **Why?** Abstraction allows extending functionality without modifying stable components.
