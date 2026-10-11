# Question 4: Longest Consecutive Run of Equal Elements
def longest_run(numbers):
    if len(numbers) == 0:
        return 0

    current = 1
    longest = 1

    for i in range(1, len(numbers)):
        if numbers[i] == numbers[i - 1]:
            current += 1
        else:
            current = 1

        if current > longest:
            longest = current

    return longest


if __name__ == "__main__":
    print(longest_run([1, 1, 2, 2, 2, 3, 3, 1, 1, 1, 1]))  # 4
    print(longest_run([7, 7, 7, 7]))                       # 4
    print(longest_run([]))                                 # 0
