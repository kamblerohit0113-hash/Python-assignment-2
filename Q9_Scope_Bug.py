# Question 9: Predict and Correct a Scope Bug
score = 50


def update():
    global score
    print(score)
    score = score + 10


if __name__ == "__main__":
    update()
    print(score)
    # Output:
    # 50
    # 60
