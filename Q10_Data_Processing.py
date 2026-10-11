# Question 10: Integrated Data Processing Challenge
def process_numbers(numbers):
    total = 0
    count = 0
    largest = None

    for num in numbers:
        if num >= 0 and num % 2 == 0:
            square = num * num
            total += square
            count += 1

            if largest is None or square > largest:
                largest = square

    return total, count, largest


# Optional functional approach using filter(), map(), and reduce()
from functools import reduce


def process_numbers_functional(numbers):
    even_numbers = filter(lambda x: x >= 0 and x % 2 == 0, numbers)
    squares = list(map(lambda x: x * x, even_numbers))

    total = reduce(lambda a, b: a + b, squares, 0)
    count = len(squares)
    largest = None

    if count > 0:
        largest = reduce(lambda a, b: a if a > b else b, squares)

    return total, count, largest


if __name__ == "__main__":
    numbers = [-2, 1, 2, 3, 4, 6, -8]
    total, count, largest = process_numbers(numbers)
    print("Total:", total)
    print("Count:", count)
    print("Largest squared value:", largest)

    print("No qualifying numbers:", process_numbers([-3, -5, 1, 3]))
    print("Functional result:", process_numbers_functional(numbers))
