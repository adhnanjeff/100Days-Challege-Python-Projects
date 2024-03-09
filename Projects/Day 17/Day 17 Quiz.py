from data import question_data

print("""
                    ___                       ___     
      ___          /__/\        ___          /  /\    
     /  /\         \  \:\      /  /\        /  /::|   
    /  /::\         \  \:\    /  /:/       /  /:/:|   
   /  /:/\:\    ___  \  \:\  /__/::\      /  /:/|:|__ 
  /  /:/~/::\  /__/\  \__\:\ \__\/\:\__  /__/:/ |:| /|
 /__/:/ /:/\:\ \  \:\ /  /:/    \  \:\/\ \__\/  |:|/:/
 \  \:\/:/__\/  \  \:\  /:/      \__\::/     |  |:/:/ 
  \  \::/        \  \:\/:/       /__/:/      |  |::/  
   \__\/          \  \::/        \__\/       |  |:/   
                   \__\/                     |__|/   
  """)

class Question:
    def __init__(self, question, answer):
        self.question = question
        self.answer = answer

class QuizBrain:
    def __init__(self, question_bank):
        self.question_bank = question_bank
        self.current_question_index = 0
        self.score = 0

    def next_question(self):
        current_question = self.question_bank[self.current_question_index]
        self.current_question_index += 1
        user_ans = input(f"Q.{self.current_question_index}: {current_question.question} (True/False): ")
        self.check_answer(user_ans, current_question.answer)

    def still_has_questions(self):
        return self.current_question_index < len(self.question_bank)
    
    def check_answer(self, uans, cans):
        if uans.lower() == cans.lower():
            self.score += 1
            print(f"You got it right, it's {cans}")
        else:
            print(f"Oops, you messed it up, the right answer is {cans}")

        print(f"Your current score is {self.score}/{self.current_question_index}")
        print("\n")

question_bank = []

for question_data_item in question_data:
    question_text = question_data_item["question"]
    question_answer = question_data_item["correct_answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()

print("You've completed the quiz")
print(f"Your final score is {quiz.score}/{quiz.current_question_index}")
