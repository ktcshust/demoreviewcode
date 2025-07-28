class DatabaseModel:
    def __init__(self, data: dict):
        self.id = data.get("id")
        self.created_at = data.get("created_at")

    def save(self):
        """Lưu object vào database"""
        print(f"Saving object {self.id} to DB...")

    def validate(self):
        """Kiểm tra tính hợp lệ của dữ liệu"""
        if not self.id:
            raise ValueError("Missing ID")
