# Question 6: Merge Two Sorted Lists Without Sorting
def merge_sorted(a, b):
    result = []
    i = 0
    j = 0

    while i < len(a) and j < len(b):
        if a[i] <= b[j]:
            result.append(a[i])
            i += 1
        else:
            result.append(b[j])
            j += 1

    while i < len(a):
        result.append(a[i])
        i += 1

    while j < len(b):
        result.append(b[j])
        j += 1

    return result


if __name__ == "__main__":
    a = [1, 4, 7, 10]
    b = [2, 3, 8, 11, 15]
    print(merge_sorted(a, b))
    # [1, 2, 3, 4, 7, 8, 10, 11, 15]
