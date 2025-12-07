class Chip:
    def __init__(self, value: int):
        if not isinstance(value, int):
            raise TypeError("Значение фишки должно быть целым числом")
        if value < 0:
            raise ValueError("Значение фишки не может быть отрицательным")
        self.value = value

    def __add__(self, other):
        if isinstance(other, Chip):
            return Chip(self.value + other.value)
        elif isinstance(other, int):
            return Chip(self.value + other)
        return NotImplemented

    def __radd__(self, other):
        if isinstance(other, int):
            return Chip(self.value + other)
        return NotImplemented

    def __repr__(self):
        return f"Фишка: {self.value} "
