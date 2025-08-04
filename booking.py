from .discount import DiscountManager

class Booking:
    def __init__(self, customer, room, start_date, end_date):
        self.customer = customer
        self.room = room
        self.start_date = start_date
        self.end_date = end_date
        self.status = 'pending'
        self.discount_code = None
        self.final_price = room.price


    def confirm(self):
        self.status = 'confirmed'
        self.room.set_availability(False)

    def cancel(self):
        self.status = 'cancelled'
        self.room.set_availability(True)

    def apply_discount(self, code):
        self.discount_code = code
        discount = DiscountManager().get_discount(code)
        self.final_price = self.room.price * (1 - discount)
        return self.final_price
