
import random
import requests

# Fetching quiz data from GitHub
url = "https://raw.githubusercontent.com/mehmetmeral/quiz_questions/main/questions.json"
response = requests.get(url)

if response.status_code == 200:
    quiz_data = response.json()
else:
    print("Failed to fetch questions from GitHub.")
    quiz_data = []

# Ensure the JSON data is a list
if isinstance(quiz_data, list):
    # Adjusting the tuple structure to match the correct keys
    quiz_questions = [(item["question"], item["correct"], *item["incorrect"]) for item in quiz_data]
else:
    print("Error: JSON data is not a list.")
    quiz_questions = []

def shuffle_and_ask_question(question_tuple):
    question, correct_answer, *wrong_answers = question_tuple
    options = [correct_answer] + wrong_answers
    random.shuffle(options)  # Shuffle the options

    # Display the question and options
    print(f"Question: {question}")
    for idx, option in enumerate(options, start=1):
        print(f"{idx}. {option}")

    # Get user input for the answer
    user_answer = input("Choose your answer (1-4): ")

    # Check if the selected answer is correct
    if options[int(user_answer) - 1] == correct_answer:
        return True
    else:
        return False

def play_game(player_name):
    print(f"\n{player_name}'s turn!")
    correct_answers = 0
    random.shuffle(quiz_questions)  # Shuffle questions
    selected_questions = quiz_questions[:5]  # Select the first 5 questions

    # Loop through the selected questions
    for question_tuple in selected_questions:
        if shuffle_and_ask_question(question_tuple):
            correct_answers += 1  # Increment score for correct answer
    
    return correct_answers

def main():
    mode = input("Choose game mode (1 for Single Player, 2 for Two Player): ")

    if mode == '1':
        print("\nSingle Player Mode")
        player_name = input("Enter your name: ")
        score = play_game(player_name)
        print(f"\n{player_name}, you got {score} out of 5 correct!")

    elif mode == '2':
        print("\nTwo Player Mode")
        player1 = input("Enter Player 1 name: ")
        player2 = input("Enter Player 2 name: ")

        player1_score = play_game(player1)
        player2_score = play_game(player2)

        if player1_score > player2_score:
            print(f"{player1} wins with {player1_score} correct answers!")
        elif player1_score < player2_score:
            print(f"{player2} wins with {player2_score} correct answers!")
        else:
            print(f"It's a tie! Both players got {player1_score} correct answers.")

    else:
        print("Invalid mode! Please choose either 1 for Single Player or 2 for Two Player.")

if __name__ == "__main__":
    main()

import random
import requests

# Fetch quiz data from GitHub
URL = "https://raw.githubusercontent.com/mehmetmeral/quiz_questions/main/questions.json"
response = requests.get(URL)

if response.status_code == 200:
    quiz_data = response.json()
else:
    print("Failed to fetch questions from GitHub.")
    quiz_data = []

# Convert JSON to tuples
if isinstance(quiz_data, list):
    quiz_questions = [
        (item["question"], item["correct"], *item["incorrect"])
        for item in quiz_data
    ]
else:
    print("Error: JSON data is not a list.")
    quiz_questions = []


def ask_question(question_tuple):
    question, correct_answer, *wrong_answers = question_tuple
    options = [correct_answer] + wrong_answers
    random.shuffle(options)

    print("\n" + question)
    for i, option in enumerate(options, start=1):
        print(f"{i}. {option}")

    choice = input("Your answer (1-4): ")

    return options[int(choice) - 1] == correct_answer


def play_game(player_name):
    print(f"\n{player_name}'s turn")
    score = 0

    random.shuffle(quiz_questions)
    for question in quiz_questions[:5]:
        if ask_question(question):
            score += 1

    return score


def main():
    mode = input("Choose mode (1 = Single Player, 2 = Two Players): ")

    if mode == "1":
        name = input("Enter your name: ")
        score = play_game(name)
        print(f"\n{name}, you scored {score}/5")

    elif mode == "2":
        p1 = input("Player 1 name: ")
        p2 = input("Player 2 name: ")

        score1 = play_game(p1)
        score2 = play_game(p2)

        print(f"\n{p1}: {score1}/5")
        print(f"{p2}: {score2}/5")

        if score1 > score2:
            print(f"{p1} wins!")
        elif score2 > score1:
            print(f"{p2} wins!")
        else:
            print("It's a tie!")

    else:
        print("Invalid mode")


if __name__ == "__main__":
    main()

