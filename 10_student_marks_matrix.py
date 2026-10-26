# Assignment 10: Student Marks Matrix Analysis
# Use a nested list to calculate each student's total and average.

students = [
    [80, 75, 90],
    [65, 70, 85],
    [90, 95, 88]
]

for i in range(len(students)):
    total = sum(students[i])
    average = total / len(students[i])

    print("\nStudent", i + 1)
    print("Marks:", students[i])
    print("Total:", total)
    print("Average:", round(average, 2))

    if average >= 75:
        print("Performance: Good")
    else:
        print("Performance: Needs Improvement")
