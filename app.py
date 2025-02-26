def add(a, b):
    """Ajoute deux nombres."""
    return a + b


def multiply(x, y):
    return x * y


def divide(x, y):
    if y != 0:
        return x / y
    else:
        return None  # Retourner None ou une valeur appropriée si y == 0


def greet(name):
    """Greet function."""
    if name == "":
        return "Hello, World!"
    else:
        return "Hello, " + name
