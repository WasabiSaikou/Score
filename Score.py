grades = list(map(int, input().split()))
fail = 0
max = 0
min = 100
total = 0
for grade in grades:
    if grade < 60:
        fail += 1

    total += grade

    if grade > max:
        max = grade
    if grade < min:
        min = grade
average = total / len(grades)

print(average)
print(f"不及格人數:{fail}")
print(f"最大值:{max}")
print(f"最小值:{min}")
print(f"平均值:{average}")
