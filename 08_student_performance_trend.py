# Assignment 8: Student Performance Trend Analysis
# Store examination marks, calculate average, and compare successive exams.

n = int(input("Enter number of examinations: "))

if n <= 0:
    print("Enter at least one examination.")
else:
    marks = []

    for i in range(n):
        mark = int(input(f"Enter marks for exam {i + 1} (0-100): "))
        if mark < 0 or mark > 100:
            print("Marks must be between 0 and 100.")
            raise SystemExit
        marks.append(mark)

    print("Marks:", marks)
    print("Total Marks:", sum(marks))
    print("Average Marks:", round(sum(marks) / n, 2))

    for i in range(1, n):
        if marks[i] > marks[i - 1]:
            print(f"Exam {i + 1}: Improved")
        elif marks[i] < marks[i - 1]:
            print(f"Exam {i + 1}: Declined")
        else:
            print(f"Exam {i + 1}: No Change")
