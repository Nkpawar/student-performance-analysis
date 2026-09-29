import pandas as pd
import random

# Make the results repeatable
random.seed(42)

data = []

# Create data for 100 students
for i in range(1, 101):

    age = random.randint(18, 22)
    gender = random.choice(["Male", "Female"])

    attendance = random.randint(60, 100)
    study_hours = random.randint(1, 8)

    math = random.randint(40, 100)
    science = random.randint(40, 100)
    english = random.randint(40, 100)
    assignment = random.randint(40, 100)

    # Calculate final score
    final_score = round(
        (math + science + english + assignment) / 4
    )

    data.append([
        f"ST{i:03}",
        gender,
        age,
        attendance,
        study_hours,
        math,
        science,
        english,
        assignment,
        final_score
    ])

# Column names
columns = [
    "Student_ID",
    "Gender",
    "Age",
    "Attendance",
    "Study_Hours",
    "Math_Score",
    "Science_Score",
    "English_Score",
    "Assignment_Score",
    "Final_Score"
]

# Create DataFrame
df = pd.DataFrame(data, columns=columns)

# Save dataset
df.to_csv("dataset/student_performance.csv", index=False)

print("Dataset created successfully!")
print()
print(df.head())