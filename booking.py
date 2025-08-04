class Booking:
    def __init__(self, customer, room, start_date, end_date):
        self.customer = customer
        self.room = room
        self.start_date = start_date
        self.end_date = end_date
        self.status = 'pending'

    def confirm(self):
        self.status = 'confirmed'
        self.room.set_availability(False)

    def cancel(self):
        self.status = 'cancelled'
        self.room.set_availability(True)
