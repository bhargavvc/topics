
### **Example 1: Door Mechanisms in a Building**

**Scenario:**

Imagine a building with various types of doors:

- **Safe Door**: Requires a password to lock/unlock.
- **Sliding Door**: Slides open and may not lock.
- **Revolving Door**: Rotates and may have a keycard access.

Each door has different mechanisms for locking and opening, but they all share common characteristics like dimensions or materials.

**Challenges:**

- **Avoid Code Duplication**: Similar locking mechanisms shouldn't be redefined for each door type.
- **Enhance Flexibility**: Ability to add new locking/opening mechanisms without altering existing code.
- **Promote Reusability**: Share behaviors among different doors when applicable.

**Applying the Strategy Pattern:**

1. **Define Strategy Interfaces:**

   - **LockBehavior**: Interface for locking mechanisms.
     ```python
     from abc import ABC, abstractmethod

     class LockBehavior(ABC):
         @abstractmethod
         def lock(self):
             pass

         @abstractmethod
         def unlock(self):
             pass
     ```

   - **OpenBehavior**: Interface for opening mechanisms.
     ```python
     from abc import ABC, abstractmethod

     class OpenBehavior(ABC):
         @abstractmethod
         def open(self):
             pass

         @abstractmethod
         def close(self):
             pass
     ```

2. **Implement Concrete Strategies:**

   - **Locking Mechanisms:**

     ```python
     # Password Lock
     class PasswordLock(LockBehavior):
         def lock(self):
             print("Locking with a password.")

         def unlock(self):
             print("Unlocking with a password.")

     # Keycard Lock
     class KeycardLock(LockBehavior):
         def lock(self):
             print("Locking with a keycard.")

         def unlock(self):
             print("Unlocking with a keycard.")

     # No Lock
     class NoLock(LockBehavior):
         def lock(self):
             print("This door does not lock.")

         def unlock(self):
             print("This door does not unlock.")
     ```

   - **Opening Mechanisms:**

     ```python
     # Standard Open
     class StandardOpen(OpenBehavior):
         def open(self):
             print("Opening the door normally.")

         def close(self):
             print("Closing the door normally.")

     # Sliding Open
     class SlidingOpen(OpenBehavior):
         def open(self):
             print("Sliding the door open.")

         def close(self):
             print("Sliding the door closed.")

     # Revolving Open
     class RevolvingOpen(OpenBehavior):
         def open(self):
             print("Revolving the door open.")

         def close(self):
             print("Revolving the door closed.")
     ```

3. **Create the Door Class (Context):**

   ```python
   class Door:
       def __init__(self, lock_behavior: LockBehavior, open_behavior: OpenBehavior):
           self.lock_behavior = lock_behavior
           self.open_behavior = open_behavior

       def perform_lock(self):
           self.lock_behavior.lock()

       def perform_unlock(self):
           self.lock_behavior.unlock()

       def perform_open(self):
           self.open_behavior.open()

       def perform_close(self):
           self.open_behavior.close()

       # Methods to change behaviors at runtime
       def set_lock_behavior(self, lock_behavior: LockBehavior):
           self.lock_behavior = lock_behavior

       def set_open_behavior(self, open_behavior: OpenBehavior):
           self.open_behavior = open_behavior
   ```

4. **Instantiate Doors with Specific Behaviors:**

   ```python
   # Safe Door with Password Lock and Standard Open
   safe_door = Door(lock_behavior=PasswordLock(), open_behavior=StandardOpen())
   safe_door.perform_lock()
   safe_door.perform_open()
   safe_door.perform_close()
   safe_door.perform_unlock()

   # Sliding Door with No Lock and Sliding Open
   sliding_door = Door(lock_behavior=NoLock(), open_behavior=SlidingOpen())
   sliding_door.perform_lock()
   sliding_door.perform_open()
   sliding_door.perform_close()
   sliding_door.perform_unlock()

   # Revolving Door with Keycard Lock and Revolving Open
   revolving_door = Door(lock_behavior=KeycardLock(), open_behavior=RevolvingOpen())
   revolving_door.perform_lock()
   revolving_door.perform_open()
   revolving_door.perform_close()
   revolving_door.perform_unlock()
   ```

**Output:**

```
Locking with a password.
Opening the door normally.
Closing the door normally.
Unlocking with a password.

This door does not lock.
Sliding the door open.
Sliding the door closed.
This door does not unlock.

Locking with a keycard.
Revolving the door open.
Revolving the door closed.
Unlocking with a keycard.
```

**Explanation:**

- **Flexibility:** We can mix and match different locking and opening behaviors without modifying the `Door` class.
- **Runtime Changes:** Behaviors can be changed at runtime using `set_lock_behavior` or `set_open_behavior`.
- **Extensibility:** New behaviors can be added by implementing the respective interfaces without altering existing code.
