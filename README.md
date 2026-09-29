# 📊 Student Performance Analysis

## 📌 Project Overview

Student Performance Analysis is a Python-based data analytics project developed to analyze academic performance and identify meaningful patterns in student data.

The project analyzes factors such as attendance, study hours, subject scores, assignment performance, gender, and final scores using exploratory data analysis and data visualization techniques.

The analysis transforms raw student data into meaningful insights that can help understand overall academic performance and identify students who may require additional academic attention.

---

## 🎯 Objectives

- Analyze student academic performance.
- Examine the relationship between attendance and final scores.
- Analyze the relationship between study hours and academic performance.
- Compare performance across different subjects.
- Analyze gender-wise performance.
- Study the distribution of final scores.
- Identify relationships between important variables using correlation analysis.
- Create meaningful data visualizations.
- Identify students who may require additional academic attention.
- Generate data-driven recommendations.

---

## 🛠️ Technologies Used

| Technology | Purpose |
|---|---|
| Python | Programming and data analysis |
| Pandas | Data manipulation and analysis |
| Matplotlib | Data visualization |
| Seaborn | Statistical visualization |
| Jupyter Notebook | Interactive data analysis |
| VS Code | Development environment |
| CSV | Dataset storage |
| GitHub | Version control |

---

## 📂 Dataset

The project uses a dataset containing **100 student records**.

### Dataset Features

| Feature | Description |
|---|---|
| Student_ID | Unique student identifier |
| Gender | Student gender |
| Age | Student age |
| Attendance | Attendance percentage |
| Study_Hours | Daily study hours |
| Math_Score | Mathematics score |
| Science_Score | Science score |
| English_Score | English score |
| Assignment_Score | Assignment score |
| Final_Score | Calculated final score |

The Final Score is calculated using the average of Mathematics, Science, English, and Assignment scores.

---

## 🔍 Analysis Performed

The project performs the following analysis:

### 1. Data Inspection

- Dataset shape
- Data types
- Missing value detection
- Duplicate detection
- Statistical summary

### 2. Performance Analysis

Students are categorized into:

- **Excellent** — 80 and above
- **Good** — 60–79
- **Average** — 40–59
- **Needs Improvement** — Below 40

### 3. Attendance Analysis

The project examines the relationship between attendance and final academic performance.

### 4. Study Hours Analysis

The project analyzes the relationship between daily study hours and final scores.

### 5. Subject Analysis

Average performance is compared across:

- Mathematics
- Science
- English
- Assignment

### 6. Gender-wise Analysis

Average final scores are compared between male and female students.

### 7. Correlation Analysis

Correlation analysis is performed between:

- Attendance
- Study Hours
- Mathematics
- Science
- English
- Assignment
- Final Score

---

## 📈 Visualizations

The project contains the following visualizations:

- Performance Categories
- Attendance vs Final Score
- Study Hours vs Final Score
- Subject Comparison
- Final Score Distribution
- Gender-wise Performance
- Correlation Heatmap
- Subject Average Comparison
- Attendance Distribution
- Study Hours Distribution

All generated charts are stored in the `charts` folder.

---

## 📊 Key Findings

The analysis provides several observations about the student dataset:

- Most students fall within the Good performance category.
- A smaller proportion of students achieve Excellent performance.
- Attendance and study hours can be examined in relation to final academic performance.
- Subject-wise analysis highlights differences in average scores.
- The final score distribution shows how student performance is spread across different score ranges.
- Correlation analysis helps identify relationships between academic and behavioral variables.
- Students with lower final scores can be identified for further academic monitoring.

---

## 📁 Project Structure

```text
STUDENT+PERFORMANCE
│
├── charts
│   ├── performance_categories.png
│   ├── attendance_vs_final_score.png
│   ├── study_hours_vs_final_score.png
│   ├── subject_comparison.png
│   ├── final_score_distribution.png
│   ├── gender_performance.png
│   ├── correlation_heatmap.png
│   ├── subject_average_comparison.png
│   ├── attendance_distribution.png
│   └── study_hours_distribution.png
│
├── dataset
│   └── student_performance.csv
│
├── notebooks
│   └── student_performance_analysis.ipynb
│
├── reports
│   └── student_performance_analysis_report.md
│
├── create_dataset.py
│
└── README.md