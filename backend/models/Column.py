class Column:
    def __init__(self, month: str, values: dict):
        self.month = month
        self.values = values

    def __str__(self):
        return f"{self.month} {self.values}"

    def to_json(self):
        result = {"month": self.month}
        result.update(self.values)
        return result
