import unittest
from service import PaymentService

class TestPaymentService(unittest.TestCase):
    def test_process_payment(self):
        service = PaymentService({"id": "pay_123"})
        self.assertIsNone(service.process_payment(100.0))
    
    def test_refund_with_reason(self):
        service = PaymentService({"id": "pay_456"})
        self.assertIn("quality", service.refund("poor quality"))
