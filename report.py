class ReportGenerator:
    def __init__(self):
        pass

    def generate_booking_report(self, bookings):
        return [b.status for b in bookings]
