
### **Extending the Example with Asynchronous Notifications**

In real-world applications, you might want to send notifications asynchronously to avoid blocking the main thread.

#### **Using Celery for Asynchronous Tasks**

```python
# tasks.py

from celery import shared_task
from django.core.mail import send_mail

@shared_task
def send_notification(email, subject, message):
    send_mail(
        subject=subject,
        message=message,
        from_email='no-reply@example.com',
        recipient_list=[email],
    )
```

#### **Updating the Observer to Use Celery**

```python
# concrete_observers.py

from .tasks import send_notification

class EmailSubscriber(Observer):
    def __init__(self, email):
        self.email = email

    def update(self, article):
        # Asynchronously send an email
        send_notification.delay(
            email=self.email,
            subject=f"New article: {article.title}",
            message=article.content
        )
```

**Explanation:**

- **Asynchronous Task**:
  - `send_notification` is a Celery task that sends an email.
  - Using `delay()` schedules the task to be executed asynchronously.
