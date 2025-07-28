from core import DatabaseModel

class PaymentService(DatabaseModel):
    def process_payment(self, amount: float):
        """Xử lý thanh toán"""
        self.validate()
        print(f"Processing payment ${amount} for {self.id}")

    def refund(self, reason: str):
        """Hoàn tiền"""
        print(f"Refunding {self.id} due to: {reason}")
