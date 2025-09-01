name = input("Enter student name: ")

marks_in_english = int(input("Enter marks in English: "))
marks_in_maths = int(input("Enter marks in Maths: "))
marks_in_science = int(input("Enter marks in Science: "))

# Calculate totals
total_marks = marks_in_english + marks_in_maths + marks_in_science
average_marks = total_marks / 3

# Print Report Card
print("\n===============================")
print(f"      Report Card for {name}")
print("===============================")
print(f"English: {marks_in_english}")
print(f"Maths:   {marks_in_maths}")
print(f"Science: {marks_in_science}")
print("-------------------------------")
print(f"Total Marks:   {total_marks}")
print(f"Average Marks: {average_marks:.2f}")

# Grade
if average_marks >= 75:
    print("Result: Distinction 🏆")
elif average_marks >= 40:
    print("Result: Pass ✅")
else:
    print("Result: Fail ❌")

print("===============================\n")
