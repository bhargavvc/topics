
### **Real-World Example: Database ORM (Object-Relational Mapping)**

In web development, interacting with databases can be complex due to SQL queries and data management. ORMs provide a simplified interface to interact with databases using object-oriented paradigms.

**How the Facade Pattern Applies**:

- **Facade**: The ORM library (e.g., SQLAlchemy in Python, Django ORM).
- **Subsystems**:
  - SQL query execution.
  - Connection pooling.
  - Transaction management.
- **Client**: The application code that performs database operations.

**Example with SQLAlchemy**:

```python
# Using SQLAlchemy ORM to interact with a database
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import User  # Assuming User is a mapped class

engine = create_engine('sqlite:///app.db')
Session = sessionmaker(bind=engine)
session = Session()

# Facade provides simple methods to interact with the database
new_user = User(name="Alice", email="alice@example.com")
session.add(new_user)
session.commit()

# Querying users
users = session.query(User).filter_by(name="Alice").all()
```

**Explanation**:

- The ORM provides a simplified interface to perform CRUD operations.
- The complexities of SQL queries, connection management, and transactions are hidden.
- The client code remains clean and focused on business logic.
