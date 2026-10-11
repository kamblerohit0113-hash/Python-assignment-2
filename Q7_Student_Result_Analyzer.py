# Question 7: Student Result Analyzer
def analyze_marks(*args):
    if len(args) == 0:
        return {
            "Total": 0,
            "Average": 0,
            "Highest": None,
            "Passing count": 0
        }

    total = 0
    highest = args[0]
    passing_count = 0

    for mark in args:
        total += mark

        if mark > highest:
            highest = mark

        if mark >= 40:
            passing_count += 1

    average = total / len(args)

    return {
        "Total": total,
        "Average": average,
        "Highest": highest,
        "Passing count": passing_count
    }


if __name__ == "__main__":
    result = analyze_marks(35, 72, 80, 45, 90, 30)
    for key, value in result.items():
        print(f"{key}: {value}")

    print("Empty input:", analyze_marks())
