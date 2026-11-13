# 1. Create a tuple to store fixed student details
student_profile = ("Aarav", "Grade 6", "Section A", 6)

# Access tuple elements using indexing and slicing
print("Student Name:", student_profile[0])
print("Class Details:", student_profile[1:3])
print("-" * 40)

# 2. Create sets to store unique school subjects
monday_subjects = {"Math", "Science", "English", "Computer", "Art"}
tuesday_subjects = {"Math", "History", "English", "Sports", "Music"}

print("Initial Monday Subjects:", monday_subjects)
print("Initial Tuesday Subjects:", tuesday_subjects)
print("-" * 40)

# 3. Modify sets using add() and discard()
monday_subjects.add("Geography")
tuesday_subjects.discard("Sports")

print("Updated Monday Subjects:", monday_subjects)
print("Updated Tuesday Subjects:", tuesday_subjects)
print("-" * 40)

# 4. Compare subject sets using set operations
# Union: All unique subjects across both days
all_subjects = monday_subjects.union(tuesday_subjects)
print("All Subjects (Union):", all_subjects)

# Intersection: Subjects common to both days
common_subjects = monday_subjects.intersection(tuesday_subjects)
print("Common Subjects (Intersection):", common_subjects)

# Difference: Subjects only on Monday
only_monday = monday_subjects.difference(tuesday_subjects)
print("Only Monday Subjects (Difference):", only_monday)

# Symmetric Difference: Subjects taken on either day, but not both
unique_per_day = monday_subjects.symmetric_difference(tuesday_subjects)
print("Non-overlapping Subjects (Symmetric Difference):", unique_per_day)