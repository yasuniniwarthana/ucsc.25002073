# Get student name
student_name = input("Enter student's name: ")

# Get marks for 3 subjects
mark1 = float(input("Enter mark for subject 1: "))
mark2 = float(input("Enter mark for subject 2: "))
mark3 = float(input("Enter mark for subject 3: "))

# Calculate average
average = (mark1 + mark2 + mark3) / 3

# Display result
print(f"\nStudent: {student_name}")
print(f"Average: {average:.2f}")

if average >= 40:
    print("Result: Pass")
else:
    print("Result: Fail")