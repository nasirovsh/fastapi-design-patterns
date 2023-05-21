from fastapi import FastAPI


# Adaptee (Existing Component)
class LegacyPaymentProcessor:
    def process_payment(self, amount):
        # Process payment using the legacy system
        return f"Payment processed by the legacy system for amount: {amount}"


# Target Interface
class PaymentProcessor:
    def process_payment(self, amount):
        pass


# Adapter
class LegacyPaymentAdapter(PaymentProcessor):
    def __init__(self, legacy_processor):
        self.legacy_processor = legacy_processor

    def process_payment(self, amount):
        # Convert the interface of the legacy processor to the target interface
        return self.legacy_processor.process_payment(amount)


app = FastAPI()
legacy_processor = LegacyPaymentProcessor()
adapter = LegacyPaymentAdapter(legacy_processor)


@app.post("/process_payment")
def process_payment(amount: float):
    result = adapter.process_payment(amount)
    return result
