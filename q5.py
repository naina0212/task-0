import pandas as pd

df = pd.read_csv("student_performance.csv")

print("First five rows:")
print(df.head())

print("\nNumber of rows and columns:")
print(df.shape)

print("\nColumn names:")
print(df.columns)

print("\nMissing values:")
print(df.isnull().sum())

average_score = df["Final_Score"].mean()
print("\nAverage Final_Score:")
print(average_score)

highest_score_student = df.loc[df["Final_Score"].idxmax()]
print("\nStudent with the highest Final_Score:")
print(highest_score_student)

df["Improvement"] = df["Final_Score"] - df["Previous_Score"]

print("\nDataFrame with Improvement column:")
print(df)

print("\nStudents with Attendance >= 80:")
print(df[df["Attendance"] >= 80])

df = df.sort_values(by="Final_Score", ascending=False)

print("\nDataFrame sorted by Final_Score:")
print(df)

df.to_csv("processed_student_performance.csv", index=False)

print("\nProcessed DataFrame saved as processed_student_performance.csv")