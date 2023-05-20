from fastapi import FastAPI, Depends, HTTPException


class PaymentProcessor:
    def process_payment(self, amount: float):
        pass


class CreditCardProcessor(PaymentProcessor):
    def process_payment(self, amount: float):
        return f"Processing credit card payment for {amount} dollars."


class PayPalProcessor(PaymentProcessor):
    def process_payment(self, amount: float):
        return f"Processing PayPal payment for {amount} dollars."


class PaymentProcessorFactory:
    @staticmethod
    def create_processor(processor_type: str) -> PaymentProcessor:
        if processor_type == "credit_card":
            return CreditCardProcessor()
        elif processor_type == "paypal":
            return PayPalProcessor()
        else:
            raise HTTPException(status_code=400, detail="Invalid payment processor type.")


class PaymentService:
    def __init__(self, payment_processor: PaymentProcessor):
        self.payment_processor = payment_processor

    def process_payment(self, amount: float):
        return self.payment_processor.process_payment(amount)


app = FastAPI()


@app.post("/process_payment/{processor_type}")
def process_payment(processor_type: str, amount: float, service: PaymentService = Depends()):
    processor = PaymentProcessorFactory.create_processor(processor_type)
    service = PaymentService(processor)
    return service.process_payment(amount)
