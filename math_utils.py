def average(numbers):
    """Return the arithmetic mean of a list of numbers."""
    total = 0
    for n in numbers:
        total += n
    return total / len(numbers)


def safe_divide(a, b):
    if b > 0:
        return a / b
    return None
