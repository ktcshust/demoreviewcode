class Room:
    def __init__(self, room_id, type, price):
        self.room_id = room_id
        self.type = type
        self.price = price
        self.is_available = True
        self.reviews = []

    def set_availability(self, is_available):
        self.is_available = is_available

    def add_review(self, customer, rating, comment):
        self.reviews.append({
            "customer": customer.name,
            "rating": rating,
            "comment": comment
        })
        return f"Review added by {customer.name}"
