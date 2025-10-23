from datetime import datetime

print("=== Student Grading System ===")

# Clear file at start
with open("class_scores.txt", "w", encoding="utf-8") as f:
    pass

total_score = 0
student_count = 0
scores = []
students = []

while True:
    name = input("Enter student name: ").strip().title()
    score = int(input("Enter test score (0–100): "))
    age = int(input("Enter age: "))

    # 🧩 Determine Grade + Comment
    if score >= 90:
        grade = "A+"
        comment = "Excellent"
    elif 80 <= score < 90:
        grade = "A"
        comment = "Very Good"
    elif 70 <= score < 80:
        grade = "B"
        comment = "Good"
    elif 60 <= score < 70:
        grade = "C"
        comment = "Needs Improvement"
    else:
        grade = "F"
        comment = "Failed"

    # 🧠 Feedback based on age
    if age < 18 and score > 50:
        feedback = "Great potential, keep it up!"
    elif age >= 18 and score < 50:
        feedback = "You can still improve, never too late!"
    else:
        feedback = "Keep learning!"

    # 🧮 Track totals and lists
    total_score += score
    student_count += 1
    scores.append(score)
    students.append(name)

    # 💾 Save record
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    summary = f"[{timestamp}] Name: {name} | Score: {score} | Grade: {grade} | Comment: {comment} | Feedback: {feedback}\n"
    with open("class_scores.txt", "a", encoding="utf-8") as f:
        f.write(summary)

    print(f"\n{name} scored {score} ({grade} – {comment})")
    print(f"Feedback: {feedback}\n")

    another = input("Add another student? (y/n): ").lower()
    if another != "y":
        break

# 🧾 After loop: show class summary
average = round(total_score / student_count, 2)
if average >= 85:
    overall = "Excellent"
elif average >= 70:
    overall = "Good"
else:
    overall = "Needs improvement"

highest_score = max(scores)
lowest_score = min(scores)
top_index = scores.index(highest_score)
top_performing = students[top_index]

print("\n--- CLASS SUMMARY ---")
print(f"Total students: {student_count}")
print(f"Average score: {average}")
print(f"Overall performance: {overall}")
print(f"Highest Score: {highest_score}")
print(f"Lowest Score: {lowest_score}")
print(f"Top Performing Student: {top_performing}")

# 🧾 Save class summary
with open("class_scores.txt", "a", encoding="utf-8") as f:
    f.write(
        f"Class average: {average} | Overall: {overall} | "
        f"Highest: {highest_score} | Lowest: {lowest_score} | Top Student: {top_performing}\n"
    )

print("Saved to class_scores.txt ✅")
