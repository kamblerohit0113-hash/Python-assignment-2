# Question 8: Recursive Palindrome Checker
def is_palindrome(text, left, right):
    if left >= right:
        return True

    if text[left] != text[right]:
        return False

    return is_palindrome(text, left + 1, right - 1)


if __name__ == "__main__":
    text = "racecar"
    print(is_palindrome(text, 0, len(text) - 1))  # True

    text = "python"
    print(is_palindrome(text, 0, len(text) - 1))  # False
