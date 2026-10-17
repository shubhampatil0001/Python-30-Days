# welcome to the Python Quiz Game!
# we have used conditional statements, loops, and functions in this game dictionary to store questions, options, and answers. The game will ask the user a series of questions and keep track of their score.

questions = [
    {
        "question": "Which language are we learning?",
        "options": ["1. Java", "2. Python", "3. C++"],
        "answer": "2"
    },
    {
        "question": "Which keyword creates a function?",
        "options": ["1. func", "2. define", "3. def"],
        "answer": "3"
    },
    {
        "question": "Which data type stores True or False?",
        "options": ["1. bool", "2. str", "3. list"],
        "answer": "1"
    },
    {
        "question": "Which keyword creates a class?",
        "options": ["1. object", "2. class", "3. new"],
        "answer": "2"
    },
    {
        "question": "Which mode appends data to a file?",
        "options": ['1. "r"', '2. "w"', '3. "a"'],
        "answer": "3"
    }
]



def play_quiz():
    score = 0

    for item in questions:
        print("\n" + item["question"])

        for option in item["options"]:
            print(option)

        answer = input("Your answer (1/2/3): ")

        if answer == item["answer"]:
            print("Correct! 🎉")
            score += 1
            
        elif answer not in ["1", "2", "3"]:
            print("Invalid input! Please enter 1, 2, or 3.")
                
        else:
            print("Incorrect!")

    print("\nQuiz completed!")
    print("Your score:", score, "/", len(questions))



play_quiz()
