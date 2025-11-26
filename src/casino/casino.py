
class Chip:
    def __init__(self, value: int):
        self.value = value

    def __add__(self, other):
        if isinstance(other, Chip):
            return Chip(self.value + other.value)
        elif isinstance(other, int):
            return Chip(self.value + other)

    def __repr__(self):
        return f"Фишка: {self.value} "
