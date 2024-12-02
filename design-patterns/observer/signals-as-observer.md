
### **Using Django Signals as an Observer Pattern**

Django provides a built-in signals framework that embodies the Observer Pattern principles.

#### **Common Signals in Django**

- **`pre_save` and `post_save`**: Sent before or after a model's `save()` method is called.
- **`pre_delete` and `post_delete`**: Sent before or after a model's `delete()` method is called.
- **`request_started` and `request_finished`**: Sent when a request starts or finishes.

#### **Example: Using Django Signals**

```python
# models.py

from django.db import models
from django.dispatch import receiver
from django.db.models.signals import post_save

class Article(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()

# observers.py

from django.core.mail import send_mail
from .models import Article

@receiver(post_save, sender=Article)
def notify_subscribers(sender, instance, created, **kwargs):
    if created:
        # Logic to notify subscribers
        send_mail(
            subject=f"New Article Published: {instance.title}",
            message=instance.content,
            from_email='no-reply@example.com',
            recipient_list=['user@example.com'],
        )
```

**Explanation:**

- **Signal Receiver**:
  - The `notify_subscribers` function listens for the `post_save` signal of the `Article` model.
  - When a new article is created, it sends an email notification.

---

### **Advantages of Using Django Signals**

- **Decoupling**:
  - Signals allow you to decouple senders and receivers.
  - The sender doesn't need to know which receivers are listening.

- **Reusability**:
  - Signals can be reused across different parts of the application.

- **Maintainability**:
  - Improves code organization by separating signal handling logic.
