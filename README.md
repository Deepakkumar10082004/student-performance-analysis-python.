# Student Performance Analysis Using Python

A beginner-friendly data analysis project using Python, Pandas, and Matplotlib.

## Features
- Calculates each student's total and average marks
- Assigns a simple performance category
- Identifies the student with the highest average
- Calculates average marks for each subject
- Creates a bar chart of student averages

## Requirements
- Python 3.9+
- pandas
- matplotlib

Install dependencies:
```bash
pip install pandas matplotlib
```

Run:
```bash
python student_performance_analysis.py
```

## Dataset
The program uses fictional sample marks created inside the script. They are for demonstration only and are not real student records.

## Performance categories
- Excellent: average >= 90
- Good: average >= 80 and < 90
- Satisfactory: average >= 70 and < 80
- Needs Improvement: average < 70

These are example thresholds selected for this project, not official grading rules.

## Possible improvements
- Read data from a CSV file
- Add more students and subjects
- Validate marks are between 0 and 100
- Add subject-wise charts and a simple user interface
