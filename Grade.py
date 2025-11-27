import sys
if len(sys.argv) != 6:
    print("Usage: python student_grade.py <n1> <n2> <n3> <n4> <n5>")
    sys.exit()
n1 = float(sys.argv[1])
n2 = float(sys.argv[2])
n3 = float(sys.argv[3])
n4 = float(sys.argv[4])
n5 = float(sys.argv[5])
average = (n1 + n2 + n3 + n4 + n5) / 5
if average >= 90:
    grade = "A"
elif average >= 75:
    grade = "B"
elif average >= 60:
    grade = "C"
elif average >= 35:
    grade = "D"
else:
    grade = "Fail"
print("\n----- Student Result -----")
print("Average Marks:", average)
print("Grade:", grade)
