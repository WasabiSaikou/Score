grades = input().split()

total = 0
for i in grades:
    total += int(i)
average = total / len(grades)

print(average)