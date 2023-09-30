import random
import time
from colorama import Fore, Style

# Define color codes for formatting
CORRECT_COLOR = Fore.GREEN
WRONG_COLOR = Fore.RED
RESET_COLOR = Style.RESET_ALL

class Question:
    def __init__(self, question, options, correct_answer, difficulty):
        self.question = question
        self.options = options
        self.correct_answer = correct_answer
        self.difficulty = difficulty

class MillionaireGame:
    def __init__(self):
        self.all_questions = []  # Store all available questions
        self.questions = []  # Questions for the current game
        self.current_question_index = 0
        self.score = 0
        self.lifelines = {
            "50/50": self.fifty_fifty,
            "Ask the Audience": self.ask_the_audience,
            "Phone a Friend": self.phone_a_friend
        }
        self.load_questions()  # Load questions at the beginning
        self.timer_seconds = 20

    def load_questions(self):
        # Add more questions here
        questions = [
            Question("What is the capital of France?", ["A. London", "B. Paris", "C. Berlin", "D. Madrid"], "B", "Easy"),
            Question("Which planet is known as the Red Planet?", ["A. Venus", "B. Earth", "C. Mars", "D. Jupiter"], "C", "Easy"),
            Question("What is the chemical symbol for gold?", ["A. Go", "B. Gd", "C. Au", "D. Ag"], "C", "Medium"),
            Question("What is the smallest unit of matter?", ["A. Atom", "B. Cell", "C. Molecule", "D. Electron"], "A", "Medium"),
            Question("Who wrote the play 'Romeo and Juliet'?", ["A. Charles Dickens", "B. William Shakespeare", "C. Leo Tolstoy", "D. Jane Austen"], "B", "Hard"),
            Question("What is the largest mammal in the world?", ["A. Elephant", "B. Rhinoceros", "C. Blue Whale", "D. Giraffe"], "C", "Hard"),
            Question("What is the capital of Japan?", ["A. Beijing", "B. Tokyo", "C. Seoul", "D. Bangkok"], "B", "Easy"),
            # Add more questions here
        ]
        self.all_questions.extend(questions)

    def choose_random_questions(self, num_questions):
        if num_questions <= len(self.all_questions):
            self.questions = random.sample(self.all_questions, num_questions)
        else:
            print("Not enough questions available.")

    def add_question(self, question):
        self.questions.append(question)

    def shuffle_questions(self):
        random.shuffle(self.questions)

    def reset_timer(self):
        pass  # No need for timer with colorama

    def times_up(self):
        print("\nTime's up! You didn't answer in time.")
        self.end_game()

    def start_game(self):
        self.shuffle_questions()
        print("Welcome to Who Wants to Be a Millionaire!")
        while self.current_question_index < len(self.questions):
            self.display_question()
            user_input = input("Enter your answer or lifeline name (quit to exit): ").strip().upper()
            if user_input == "QUIT":
                break
            elif user_input in self.lifelines:
                self.use_lifeline(user_input)
            else:
                self.check_answer(user_input)
        self.end_game()

    def display_question(self):
        question = self.questions[self.current_question_index]
        print(f"\nQuestion ({question.difficulty}): {question.question}")
        for option in question.options:
            print(option)

    def check_answer(self, user_answer):
        question = self.questions[self.current_question_index]
        if user_answer == question.correct_answer:
            print(CORRECT_COLOR + "Correct!" + RESET_COLOR)
            self.score += 100000  # Increase the score by the winning amount
            self.current_question_index += 1
        else:
            print(WRONG_COLOR + f"Wrong! The correct answer is {question.correct_answer}." + RESET_COLOR)
            self.end_game()

    def use_lifeline(self, lifeline_name):
        if lifeline_name in self.lifelines:
            lifeline_function = self.lifelines[lifeline_name]
            lifeline_function()
        else:
            print("Invalid lifeline!")

    def fifty_fifty(self):
        question = self.questions[self.current_question_index]
        options_to_keep = [question.correct_answer]
        options_to_remove = random.sample(set(question.options) - {question.correct_answer}, 2)
        options_to_keep.extend(options_to_remove)
        random.shuffle(options_to_keep)
        print(f"50/50 Lifeline: {', '.join(options_to_keep)}")

    def ask_the_audience(self):
        print("Ask the Audience Lifeline: The audience believes...")
        # Simulate audience responses by generating random percentages for each option
        question = self.questions[self.current_question_index]
        audience_responses = {}

        # Generate random percentages for each option
        total_percentage = 100
        correct_answer_percentage = random.randint(1, total_percentage)
        remaining_percentage = total_percentage - correct_answer_percentage

        audience_responses[question.correct_answer] = correct_answer_percentage

        # Distribute the remaining percentage among incorrect options
        incorrect_options = set(question.options) - {question.correct_answer}
        for option in incorrect_options:
            random_percentage = random.randint(1, remaining_percentage)
            audience_responses[option] = random_percentage
            remaining_percentage -= random_percentage

        # Print the audience responses
        for option, percentage in audience_responses.items():
            print(f"{option}: {percentage}%")

    def phone_a_friend(self):
        print("Phone a Friend Lifeline: Your friend suggests...")
        # Simulate a friend's response by randomly selecting an option
        question = self.questions[self.current_question_index]
        options = question.options
        suggested_option = random.choice(options)
        print(f"Your friend suggests: {suggested_option}")

    def end_game(self):
        print(f"\nGame Over! Your final score is: ${self.score}")
        if self.current_question_index == len(self.questions):
            print("Congratulations! You've won one million dollars!")
        else:
            print("You did not win the game.")

if __name__ == "__main__":
    # Create questions
    questions = [
        Question("What is the capital of France?", ["A. London", "B. Paris", "C. Berlin", "D. Madrid"], "B",
                 "Easy"),
        Question("Which planet is known as the Red Planet?", ["A. Venus", "B. Earth", "C. Mars", "D. Jupiter"],
                 "C", "Easy"),
        Question("What is the chemical symbol for gold?", ["A. Go", "B. Gd", "C. Au", "D. Ag"], "C", "Medium"),
        Question("What is the smallest unit of matter?", ["A. Atom", "B. Cell", "C. Molecule", "D. Electron"],
                 "A", "Medium"),
        Question("Who wrote the play 'Romeo and Juliet'?",
                 ["A. Charles Dickens", "B. William Shakespeare", "C. Leo Tolstoy", "D. Jane Austen"], "B",
                 "Hard"),
        Question("What is the largest mammal in the world?",
                 ["A. Elephant", "B. Rhinoceros", "C. Blue Whale", "D. Giraffe"], "C", "Hard"),
        Question("What is the capital of Japan?", ["A. Beijing", "B. Tokyo", "C. Seoul", "D. Bangkok"], "B",
                 "Easy"),
    ]
    game = MillionaireGame()
    for question in questions:
        game.add_question(question)

    while True:
        num_questions = int(input("Enter the number of questions for this game (1-5): "))
        if 1 <= num_questions <= 5:
            game.choose_random_questions(num_questions)
            game.start_game()
            play_again = input("Play again? (yes/no): ").strip().lower()
            if play_again != "yes":
                break
        else:
            print("Please enter a number between 1 and 5.")
