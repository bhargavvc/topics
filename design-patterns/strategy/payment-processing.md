
### **Example 2: Payment Processing in an E-Commerce Application**

**Scenario:**

An e-commerce platform needs to support multiple payment methods:

- **Credit Card**
- **PayPal**
- **Bitcoin**

Each payment method has a different processing algorithm.

**Challenges:**

- **Support Multiple Payment Methods:** Customers may prefer different payment options.
- **Easily Add New Methods:** Ability to add new payment methods in the future.
- **Maintain Clean Codebase:** Avoid cluttering the checkout process with numerous conditional statements.

**Applying the Strategy Pattern:**

1. **Define the Strategy Interface:**

   ```python
   # payment_strategy.py
   from abc import ABC, abstractmethod

   class PaymentStrategy(ABC):
       @abstractmethod
       def pay(self, amount):
           pass
   ```

2. **Implement Concrete Strategies:**

   ```python
   # credit_card_payment.py
   class CreditCardPayment(PaymentStrategy):
       def __init__(self, card_number, expiration_date, cvv):
           self.card_number = card_number
           self.expiration_date = expiration_date
           self.cvv = cvv

       def pay(self, amount):
           print(f"Processing credit card payment of ${amount:.2f}")
   ```

   ```python
   # paypal_payment.py
   class PayPalPayment(PaymentStrategy):
       def __init__(self, email):
           self.email = email

       def pay(self, amount):
           print(f"Processing PayPal payment of ${amount:.2f} for {self.email}")
   ```

   ```python
   # bitcoin_payment.py
   class BitcoinPayment(PaymentStrategy):
       def __init__(self, wallet_address):
           self.wallet_address = wallet_address

       def pay(self, amount):
           print(f"Processing Bitcoin payment of ${amount:.2f} to wallet {self.wallet_address}")
   ```

3. **Create the Order Class (Context):**

   ```python
   # order.py
   class Order:
       def __init__(self, amount, payment_strategy: PaymentStrategy):
           self.amount = amount
           self.payment_strategy = payment_strategy

       def process_order(self):
           # Additional order processing logic can go here
           self.payment_strategy.pay(self.amount)
   ```

4. **Process Orders with Different Payment Methods:**

   ```python
   # main.py
   if __name__ == "__main__":
       # Order paid with Credit Card
       credit_card_payment = CreditCardPayment("4111111111111111", "12/24", "123")
       order1 = Order(amount=100.0, payment_strategy=credit_card_payment)
       order1.process_order()

       # Order paid with PayPal
       paypal_payment = PayPalPayment("user@example.com")
       order2 = Order(amount=200.0, payment_strategy=paypal_payment)
       order2.process_order()

       # Order paid with Bitcoin
       bitcoin_payment = BitcoinPayment("1BoatSLRHtKNngkdXEeobR76b53LETtpyT")
       order3 = Order(amount=300.0, payment_strategy=bitcoin_payment)
       order3.process_order()
   ```

**Output:**

```
Processing credit card payment of $100.00
Processing PayPal payment of $200.00 for user@example.com
Processing Bitcoin payment of $300.00 to wallet 1BoatSLRHtKNngkdXEeobR76b53LETtpyT
```

**Explanation:**

- **Separation of Concerns:** Payment processing logic is separated from order processing.
- **Extensibility:** New payment methods can be added by implementing the `PaymentStrategy` interface.
- **Runtime Flexibility:** The payment method can be selected at runtime based on user input.
