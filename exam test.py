import json

with open('k.json', 'r') as f:
    data = json.load(f)

answer = {}
info = {
    'Name: ': input(data["student_name"]),
    'Surname: ': input(data["student_surname"])
}
answer['Info'] = info

for question_num, question_data in data["exam_content"].items():
    print(f"Question {question_num}: {question_data['question']}")
    print("Options:")
    for option, value in question_data.items():
        if option not in ['question', 'correct_answer']:
            print(f"{option}) {value}")
    user_answer = input("Answers (a, b, c, d): ")
    while user_answer not in ['a', 'b', 'c', 'd']:
        user_answer = input("Invalid input. Please choose a valid option (a, b, c, d): ")
    print(f"You selected: {user_answer}\n")

    question_key = f"{question_num}. {question_data['question']}"
    answer[question_key] = user_answer

with open('t.json', 'w') as f:
    json.dump(answer, f, indent=4)














