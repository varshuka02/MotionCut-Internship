# my inputs - quiz questions
quiz_questions = [
  {
    "question": "What is the capital of France?",
    "options": ["A. Paris", "B. London", "C. Berlin", "D. Madrid"],
    "answer": "A"
  },
  {
    "question": "What is the largest planet in our solar system?",
    "options": ["A. Earth", "B. Mars", "C. Jupiter", "D. Saturn"],
    "answer": "C"
  },
  {
    "question": "Who wrote 'Romeo and Juliet'?",
    "options": ["A. Mark Twain", "B. William Shakespeare", "C. Charles Dickens", "D. Jane Austen"],
    "answer": "B"
  },
  {
    "question": "What is the name of the world's longest river?",
    "options": ["A. Nile", "B. Amazon", "C. Yangtze", "D. Mississippi"],
    "answer": "A"
  },
  {
    "question": "What is the most populous country in the world?",
    "options": ["A. India", "B. China", "C. United States", "D. Indonesia"],
    "answer": "B"
  },
  {
    "question": "Which invention revolutionized communication in the 19th century?",
    "options": ["A. Steam Engine", "B. Telephone", "C. Automobile", "D. Airplane"],
    "answer": "B"
  },
  {
    "question": "What is the national currency of India?",
    "options": ["A. Euro", "B. US Dollar", "C. Yuan", "D. Rupee"],
    "answer": "D"
  },
  {
    "question": "Which is the tallest mountain peak located entirely within India?",
    "options": ["A. Mount Everest", "B. K2", "C. Kangchenjunga", "D. Kanchenjunga South"],
    "answer": "C"
  },
  {
    "question": "What is the most widely spoken language in India?",
    "options": ["A. Hindi", "B. English", "C. Tamil", "D. Bengali"],
    "answer": "A"
  },
  {
    "question": "What is the name of India's most famous monument?",
    "options": ["A. Taj Mahal", "B. Red Fort", "C. Qutub Minar", "D. Gateway of India"],
    "answer": "A"
  },
]

def get_validated_input():
  valid_answers = ["A", "B", "C", "D"]
  while True:
    answer = input("Your answer (A, B, C, or D): ").strip().upper()
    if answer in valid_answers:
      return answer
    else:
      print("Invalid input. Please enter A, B, C, or D.")


def display_question(question_data):
  print(question_data["question"])
  for option in question_data["options"]:
    print(option)
  answer = get_validated_input()
  return answer

def check_answer(user_answer, correct_answer):
  return user_answer == correct_answer

def run_quiz():
  score = 0 
  for question_data in quiz_questions:
    user_answer = display_question(question_data)
    if check_answer(user_answer, question_data["answer"]):
      print("Correct!")
      score += 1 
    else:
      print(f"Incorrect! The correct answer was {question_data['answer']}.")
    print()  

  print(f"Quiz Over! Your final score is {score}/{len(quiz_questions)}")

if __name__ == "__main__":
  run_quiz()


