
### **Thread-Safe Singleton Implementation**

In multithreaded applications, the Singleton implementation needs to be thread-safe to prevent multiple instances from being created.

#### **Thread-Safe Singleton Metaclass**

```python
import threading

class ThreadSafeSingletonMeta(type):
    """
    Thread-safe implementation of Singleton.
    """
    _instance_lock = threading.Lock()
    _instance = None

    def __call__(cls, *args, **kwargs):
        with cls._instance_lock:
            if cls._instance is None:
                cls._instance = super().__call__(*args, **kwargs)
        return cls._instance
```

**Explanation:**

- **Locking Mechanism**: Uses `threading.Lock()` to ensure that only one thread can create an instance at a time.
- **Thread Safety**: Prevents race conditions where multiple threads might create separate instances.

#### **Using the Thread-Safe Singleton**

```python
class ConfigManager(metaclass=ThreadSafeSingletonMeta):
    def __init__(self):
        self.settings = {}

    def get_setting(self, key):
        return self.settings.get(key, None)

    def set_setting(self, key, value):
        self.settings[key] = value
```
