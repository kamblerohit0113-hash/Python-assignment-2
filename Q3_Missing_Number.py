# Question 3: Find the Missing Number
def find_missing(numbers, n):
    expected_sum = n * (n + 1) // 2
    actual_sum = 0

    for num in numbers:
        actual_sum += num

    return expected_sum - actual_sum


# Optional alternative using XOR
def find_missing_xor(numbers, n):
    result = 0

    for i in range(1, n + 1):
        result ^= i

    for num in numbers:
        result ^= num

    return result


if __name__ == "__main__":
    numbers = [1, 2, 4, 6, 3, 7, 8]
    print(find_missing(numbers, 8))       # 5
    print(find_missing([2, 3, 4, 5], 5)) # 1
    print(find_missing_xor(numbers, 8))   # 5
