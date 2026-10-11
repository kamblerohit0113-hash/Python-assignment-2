# Question 1: Second Largest Distinct Element
def second_largest(numbers):
    largest = None
    second = None

    for num in numbers:
        if largest is None or num > largest:
            second = largest
            largest = num
        elif num != largest and (second is None or num > second):
            second = num

    if second is None:
        return "No second-largest distinct value"
    return second


if __name__ == "__main__":
    print(second_largest([12, 35, 1, 10, 34, 35]))  # 34
    print(second_largest([5, 5, 5, 4]))             # 4
    print(second_largest([10, 10, 10]))             # No second-largest distinct value
    print(second_largest([-5, -2, -10, -1]))        # -2
