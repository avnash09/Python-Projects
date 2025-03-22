from Question_Class import Question

question_prompts = [
    "1.  What is the capital of France? \n\t- A) Berlin\n\t- B) Madrid\n\t- C) Paris\n\t- D) Rome\n\n",
    "2.  Which planet is known as the Red Planet? \n\t- A) Earth\n\t- B) Mars\n\t- C) Jupiter\n\t- D) Venus\n\n",
    "3.  Who wrote the play \"Romeo and Juliet\"? \n\t- A) William Shakespeare\n\t- B) Charles Dickens\n\t- C) Mark Twain\n\t- D) Jane Austen\n\n",
    "4.  What is the largest ocean on Earth? \n\t- A) Atlantic Ocean\n\t- B) Indian Ocean\n\t- C) Arctic Ocean\n\t- D) Pacific Ocean\n\n",
    "5.  Which element has the chemical symbol 'O'? \n\t- A) Gold\n\t- B) Oxygen\n\t- C) Silver\n\t- D) Iron\n\n",
    "6.  Who was the first President of the United States? \n\t- A) Thomas Jefferson\n\t- B) Abraham Lincoln\n\t- C) George Washington\n\t- D) John Adams\n\n",
    "7.  What is the smallest prime number? \n\t- A) 1\n\t- B) 2\n\t- C) 3\n\t- D) 5\n\n",
    "8.  Which country is known as the Land of the Rising Sun? \n\t- A) China\n\t- B) Japan\n\t- C) South Korea\n\t- D) Thailand\n\n",
    "9.  What is the main ingredient in guacamole? \n\t- A) Tomato\n\t- B) Avocado\n\t- C) Onion\n\t- D) Pepper\n\n",
    "10.  Which is the longest river in the world? \n\t- A) Amazon River\n\t- B) Nile River\n\t- C) Yangtze River\n\t- D) Mississippi River\n\n"
]

# Replace   with a space
#question_prompts = [q.replace("\s", " ") for q in question_prompts]

#print(question_prompts[1])

questions = [
    Question(question_prompts[0], "c"),
    Question(question_prompts[1], "b"),
    Question(question_prompts[2], "a"),
    Question(question_prompts[3], "d"),
    Question(question_prompts[4], "b"),
    Question(question_prompts[5], "c"),
    Question(question_prompts[6], "b"),
    Question(question_prompts[7], "b"),
    Question(question_prompts[8], "b"),
    Question(question_prompts[9], "b")
]

def mcq_test(questions):
    is_true = True
    score = 0
    while is_true:
        for question in questions:
            answer = input(question.prompt)
            if answer.lower() == question.answer:
                score += 1
        print(f"You got {score} / {len(questions)} correct.")
        response = input("Do you want to continue? (y/n): ")
        if response.lower() == "n":
            is_true = False
        score = 0

mcq_test(questions)