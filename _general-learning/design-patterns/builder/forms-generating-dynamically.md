
### **Example: Building Forms Dynamically**

In Django, forms are used for user input and can vary widely in fields and validation. Using the builder pattern can help construct forms dynamically based on conditions.

1. **Create a Form Builder (`DynamicFormBuilder`):**

   ```python
   # form_builder.py

   from django import forms

   class DynamicFormBuilder:
       def __init__(self):
           self.fields = {}

       def add_char_field(self, name, label, max_length=100, required=True):
           self.fields[name] = forms.CharField(label=label, max_length=max_length, required=required)
           return self

       def add_email_field(self, name, label, required=True):
           self.fields[name] = forms.EmailField(label=label, required=required)
           return self

       def add_choice_field(self, name, label, choices, required=True):
           self.fields[name] = forms.ChoiceField(label=label, choices=choices, required=required)
           return self

       def build(self):
           return type('DynamicForm', (forms.Form,), self.fields)
   ```

   **Explanation:**

   - The builder collects field definitions.
   - The `build` method dynamically creates a `Form` class with the specified fields.

2. **Using the Builder in a View:**

   ```python
   # views.py

   from django.shortcuts import render
   from .form_builder import DynamicFormBuilder

   def dynamic_form_view(request):
       builder = DynamicFormBuilder()

       # Always include name and email fields
       builder.add_char_field('name', 'Your Name')
       builder.add_email_field('email', 'Your Email')

       # Conditionally add fields
       if request.user.is_authenticated:
           builder.add_choice_field('contact_method', 'Preferred Contact Method', choices=[('email', 'Email'), ('phone', 'Phone')])
       else:
           builder.add_char_field('message', 'Your Message', required=False)

       DynamicForm = builder.build()
       form = DynamicForm(request.POST or None)

       if request.method == 'POST' and form.is_valid():
           # Process form data
           pass

       return render(request, 'dynamic_form.html', {'form': form})
   ```

   **Explanation:**

   - The form fields are added based on conditions (e.g., whether the user is authenticated).
   - The builder pattern simplifies the dynamic creation of forms.
   - The form is rendered and processed as usual.
