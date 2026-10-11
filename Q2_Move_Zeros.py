# Question 2: Move All Zeros to the End
# Solution 1: Use a new list
def move_zeros(numbers):
    result = []

    for num in numbers:
        if num != 0:
            result.append(num)

    zero_count = len(numbers) - len(result)
    for _ in range(zero_count):
        result.append(0)

    return result


# Solution 2: Modify the original list in place
def move_zeros_in_place(numbers):
    position = 0

    for i in range(len(numbers)):
        if numbers[i] != 0:
            numbers[position] = numbers[i]
            position += 1

    while position < len(numbers):
        numbers[position] = 0
        position += 1

    return numbers


if __name__ == "__main__":
    numbers = [0, 1, 0, 3, 12, 0, 5]
    print(move_zeros(numbers))  # [1, 3, 12, 5, 0, 0, 0]

    numbers = [0, 1, 0, 3, 12, 0, 5]
    move_zeros_in_place(numbers)
    print(numbers)  # [1, 3, 12, 5, 0, 0, 0]
