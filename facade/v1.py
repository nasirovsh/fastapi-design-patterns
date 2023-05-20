from fastapi import FastAPI


# Subsystems
class OrderService:
    def create_order(self, order_data):
        # Create order logic
        return {"message": "Order created successfully"}


class PaymentService:
    def process_payment(self, payment_data):
        # Process payment logic
        return {"message": "Payment processed successfully"}


class ShippingService:
    def ship_order(self, order_data):
        # Ship order logic
        return {"message": "Order shipped successfully"}


# Facade
class OnlineStoreFacade:
    def __init__(self):
        self.order_service = OrderService()
        self.payment_service = PaymentService()
        self.shipping_service = ShippingService()

    def place_order(self, order_data, payment_data):
        order_result = self.order_service.create_order(order_data)
        payment_result = self.payment_service.process_payment(payment_data)
        shipping_result = self.shipping_service.ship_order(order_data)

        return {
            "order_result": order_result,
            "payment_result": payment_result,
            "shipping_result": shipping_result
        }


app = FastAPI()
store_facade = OnlineStoreFacade()


@app.post("/place_order")
def place_order(order_data: dict, payment_data: dict):
    result = store_facade.place_order(order_data, payment_data)
    return result
