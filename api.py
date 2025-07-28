from service import PaymentService

def handle_payment_request(payload: dict):
    """Xử lý request thanh toán từ client"""
    payment = PaymentService(payload)
    payment.process_payment(payload["amount"])
    return {"status": "success", "transaction_id": payment.id}
