import os


file_name = "C:\\Users\\tmrma\\OneDrive\\Desktop\\quiz_questions.txt"

if not os.path.exists(file_name):
    print("Quiz file not found! Make sure 'quiz_questions.txt' exists.")
    exit()

with open(file_name, "r") as file:
    lines = file.readlines()

total_questions = len(lines)
score = 0

print("\n🏏 Welcome to the MS Dhoni Cricket Quiz! 🏏\n")
print("Answer the following questions:\n")

for i, line in enumerate(lines, 1):
    question, correct_answer = line.strip().split(";")
    user_answer = input(f"Q{i}: {question} ").strip()

    if user_answer.lower() == correct_answer.lower():
        print("✅ Correct!\n")
        score += 1
    else:
        print(f"❌ Wrong! The correct answer is: {correct_answer}\n")

print("🏆 Quiz Completed! 🏆")
print(f"Your Score: {score}/{total_questions}")

with open("quiz_results.txt", "w") as result_file:
    result_file.write(f"Total Questions: {total_questions}\n")
    result_file.write(f"Score: {score}\n")

print("\nYour result has been saved to 'quiz_results.txt'.")
