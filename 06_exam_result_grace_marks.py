# Assignment 6: Examination Result and Grace Marks
# Illustrative policy: marks from 32 to 34 are raised to 35.
# Each subject is out of 100.

marks = []
for i in range(1, 4):
    mark = int(input(f"Enter marks in subject {i}: "))
    if mark < 0 or mark > 100:
        print("Marks must be between 0 and 100.")
        raise SystemExit
    marks.append(mark)

for i in range(len(marks)):
    if 32 <= marks[i] < 35:
        marks[i] = 35

total = sum(marks)
average = total / len(marks)

print("Final Marks:", marks)
print("Total Marks:", total)
print("Average Marks:", round(average, 2))

if all(mark >= 35 for mark in marks):
    print("Result: PASS")
else:
    print("Result: FAIL")
