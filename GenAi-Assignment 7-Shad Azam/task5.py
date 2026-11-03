# Task 5: Abstraction (using Abstract base class)

from abc import ABC, abstractmethod

class Payment(ABC):

    @abstractmethod
    def process_payment(self, amount):
        pass

class CreditCardPayment(Payment):
    def process_payment(self, amount):
        print(f"Payment successful via credit Card and amount is : {amount}")

class UPIPayment(Payment):
    def process_payment(self, amount):
        print(f"Payment successful via UPI and amount is : {amount}")


credit_card_payment = CreditCardPayment()
credit_card_payment.process_payment(4000)

upi_payment = UPIPayment()
upi_payment.process_payment(10000)