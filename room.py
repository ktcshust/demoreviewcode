class Room:
    def __init__(self, room_id, type, price):
        self.room_id = room_id
        self.type = type
        self.price = price
        self.is_available = True

    def set_availability(self, is_available):
        self.is_available = is_available
