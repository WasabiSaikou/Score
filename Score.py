grades = list(map(int, input().split()))
fail = 0
max = 0
min = 100
for grade in grades:
    if grade < 60:
        fail += 1
    if grade > max:
        max = grade
    if grade < min:
        min = grade
print("不及格人數:", fail)
print(f"max: {max}, min: {min}")