class ReportGenerator:
    def __init__(self):
        pass

    def generate_booking_report(self, bookings):
        return [b.status for b in bookings]

    def generate_room_reviews(self, rooms):
        return {
            room.room_id: room.reviews
            for room in rooms if room.reviews
        }
