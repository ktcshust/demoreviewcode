class DiscountManager:
    def __init__(self):
        self.codes = {
            'SUMMER10': 0.10,
            'VIP20': 0.20,
            'WELCOME5': 0.05
        }

    def get_discount(self, code):
        return self.codes.get(code.upper(), 0.0)
