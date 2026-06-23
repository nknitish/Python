
#Operator Overloading means giving special meaning to operators (+, -, *, ==, etc.) when they are used with objects of your own classes.

class Number:
    def __init__(self, n):
        self.n = n

    def __add__(self, other):
        return self.n + other.n


a = Number(10)
b = Number(20)

print(a + b)



"""

| Operator   | Magic Method     |
| ---------- | ---------------- |
| `+`        | `__add__()`      |
| `-`        | `__sub__()`      |
| `*`        | `__mul__()`      |
| `/`        | `__truediv__()`  |
| `//`       | `__floordiv__()` |
| `%`        | `__mod__()`      |
| `**`       | `__pow__()`      |
| `==`       | `__eq__()`       |
| `!=`       | `__ne__()`       |
| `<`        | `__lt__()`       |
| `>`        | `__gt__()`       |
| `<=`       | `__le__()`       |
| `>=`       | `__ge__()`       |
| `str(obj)` | `__str__()`      |
| `len(obj)` | `__len__()`      |


"""
