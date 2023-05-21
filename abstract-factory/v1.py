from fastapi import FastAPI
from abc import ABC, abstractmethod


# Abstract Factory
class PaymentProcessorFactory(ABC):
    @abstractmethod
    def create_payment_processor(self):
        pass


# Concrete Factories
class CreditCardProcessorFactory(PaymentProcessorFactory):
    def create_payment_processor(self):
        return CreditCardProcessor()


class PayPalProcessorFactory(PaymentProcessorFactory):
    def create_payment_processor(self):
        return PayPalProcessor()


# Abstract Product
class PaymentProcessor(ABC):
    @abstractmethod
    def process_payment(self, amount: float):
        pass


# Concrete Products
class CreditCardProcessor(PaymentProcessor):
    def process_payment(self, amount: float):
        return f"Processing credit card payment for {amount} dollars."


class PayPalProcessor(PaymentProcessor):
    def process_payment(self, amount: float):
        return f"Processing PayPal payment for {amount} dollars."


# Client
class PaymentService:
    def __init__(self, processor_factory: PaymentProcessorFactory):
        self.processor_factory = processor_factory

    def process_payment(self, amount: float):
        processor = self.processor_factory.create_payment_processor()
        return processor.process_payment(amount)


app = FastAPI()
credit_card_factory = CreditCardProcessorFactory()
paypal_factory = PayPalProcessorFactory()


@app.post("/process_payment/{processor_type}")
def process_payment(processor_type: str, amount: float):
    if processor_type == "credit_card":
        service = PaymentService(credit_card_factory)
    elif processor_type == "paypal":
        service = PaymentService(paypal_factory)
    else:
        raise ValueError("Invalid processor type")

    return service.process_payment(amount)
