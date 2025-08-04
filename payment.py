class PaymentProcessor:
    def process_payment(self, amount, method):
        if method == 'credit_card':
            return self._process_credit_card(amount)
        elif method == 'paypal':
            return self._process_paypal(amount)
        elif method == 'crypto':
            return self._process_crypto(amount)

    def _process_credit_card(self, amount):
        return f"Charged {amount} via credit card."

    def _process_paypal(self, amount):
        return f"Charged {amount} via PayPal."

    def _process_crypto(self, amount):
        return f"Charged {amount} via Crypto."

