from __future__ import annotations


class Distance:
    def __init__(self, km: float) -> None:
        self.km = km

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    def __add__(self, other: Distance | int | float) -> Distance:
        if isinstance(other, Distance):
            value = other.km
        elif isinstance(other, (int, float)):
            value = other
        else:
            return NotImplemented
        return Distance(self.km + value)

    def __iadd__(self, other: Distance | int | float) -> Distance:
        if isinstance(other, Distance):
            value = other.km
        elif isinstance(other, (int, float)):
            value = other
        else:
            return NotImplemented
        self.km += value
        return self

    def __mul__(self, other: int | float) -> Distance:
        if isinstance(other, (int, float)):
            value = other
        else:
            return NotImplemented
        return Distance(self.km * value)

    def __truediv__(self, other: int | float) -> Distance:
        if isinstance(other, (int, float)):
            value = other
        else:
            return NotImplemented
        result = round(self.km / value, 2)
        return Distance(result)

    def __lt__(self, other: Distance | int | float) -> bool:
        if isinstance(other, Distance):
            value = other.km
        elif isinstance(other, (int, float)):
            value = other
        else:
            return NotImplemented
        return self.km < value

    def __gt__(self, other: Distance | int | float) -> bool:
        if isinstance(other, Distance):
            value = other.km
        elif isinstance(other, (int, float)):
            value = other
        else:
            return NotImplemented
        return self.km > value

    def __eq__(self, other: object) -> bool:
        # Для __eq__ тип other зазвичай 'object' за стандартом Python
        if isinstance(other, Distance):
            value = other.km
        elif isinstance(other, (int, float)):
            value = other
        else:
            return NotImplemented
        return self.km == value

    def __le__(self, other: Distance | int | float) -> bool:
        if isinstance(other, Distance):
            value = other.km
        elif isinstance(other, (int, float)):
            value = other
        else:
            return NotImplemented
        return self.km <= value

    def __ge__(self, other: Distance | int | float) -> bool:
        if isinstance(other, Distance):
            value = other.km
        elif isinstance(other, (int, float)):
            value = other
        else:
            return NotImplemented
        return self.km >= value
