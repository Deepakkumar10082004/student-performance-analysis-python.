"""
Student Performance Analysis Using Python
Beginner portfolio project using Pandas and Matplotlib.
The data below is fictional sample data for demonstration.
"""

import pandas as pd
import matplotlib.pyplot as plt

# 1. Create a small sample dataset
data = {
    "Student": ["Aarav", "Diya", "Kabir", "Meera", "Rohan"],
    "Python": [85, 92, 78, 88, 74],
    "Mathematics": [90, 86, 80, 94, 70],
    "AI_Basics": [88, 95, 82, 91, 76],
}

df = pd.DataFrame(data)

# 2. Calculate total and average marks
subjects = ["Python", "Mathematics", "AI_Basics"]
df["Total"] = df[subjects].sum(axis=1)
df["Average"] = df[subjects].mean(axis=1).round(2)

# 3. Categorize performance using simple thresholds
def performance_category(average):
    if average >= 90:
        return "Excellent"
    elif average >= 80:
        return "Good"
    elif average >= 70:
        return "Satisfactory"
    return "Needs Improvement"

df["Performance"] = df["Average"].apply(performance_category)

# 4. Print the report
print("STUDENT PERFORMANCE REPORT")
print("=" * 72)
print(df.to_string(index=False))

# 5. Find the top student by average
top_student = df.loc[df["Average"].idxmax()]
print("\nTOP PERFORMER")
print(f"{top_student['Student']} with an average of {top_student['Average']}")

# 6. Calculate average marks in each subject
subject_averages = df[subjects].mean().round(2)
print("\nAVERAGE MARKS BY SUBJECT")
print(subject_averages.to_string())

# 7. Create and save a chart
plt.figure(figsize=(8, 5))
plt.bar(df["Student"], df["Average"])
plt.title("Average Marks by Student")
plt.xlabel("Student")
plt.ylabel("Average Marks")
plt.ylim(0, 100)
plt.tight_layout()
plt.savefig("student_average_chart.png", dpi=150)
plt.show()
