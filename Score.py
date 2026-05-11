grades = list(map(int, input().split()))
fail = 0
for grade in grades:
    if grade < 60:
        fail += 1
print(fail)


total = 0

for i in grades:
    total += int(i)
average = total / len(grades)

print(average)