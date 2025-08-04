class RoomService:
    def __init__(self):
        self.orders = []

    def order_food(self, room_id, item):
        self.orders.append((room_id, item))
        return f"Ordered {item} to room {room_id}"
