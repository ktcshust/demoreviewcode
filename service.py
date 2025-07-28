from core import DatabaseModel

class PaymentService(DatabaseModel):
    def process_payment(self, amount: float, currency: str = "USD"):
        """Xử lý thanh toán"""
        self.validate()
        print(f"Processing {amount} {currency} for {self.id}")

    def refund(self, reason: str):
        """Hoàn tiền"""
        print(f"Refunding {self.id} due to: {reason}")
    def _log_transaction(self):
        """Ghi log bảo mật (new method)"""
        print(f"[SECURITY] Payment {self.id} processed")
