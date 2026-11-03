from abc import ABC, abstractmethod


class Payment(ABC):
    @abstractmethod
    def process_payment(self, amount):
        pass


class CreditCardPayment(Payment):
    def process_payment(self, amount):
        print(f"Payment Successful via credit card and amout is : {amount}")
        print("-" * 30)


class UPIPayment(Payment):
    def process_payment(self, amount):
        print(f"Payment Successful via UPI and amout is : {amount}")
        print("-" * 30)


creditcard_payment = CreditCardPayment()
creditcard_payment.process_payment(2500)

upi_payment = UPIPayment()
upi_payment.process_payment(1200)
