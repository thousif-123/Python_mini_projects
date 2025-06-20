class Quiz:
    def __init__(self):
        rules='''Welcome to the quiz game!
        Rules : 
        1. In this game you will be given some questions, and every question have
        4 options(a,b,c,d).
        2. You have to choose correct option.
        3. If you choose correct option, you will get 1 point for each correct answer.
        4. Initially your score is 0.and next it will be increase for your correct answer.
        Best of Luck.'''
        print(rules)
        
    def problems(self):
        choose=input('Do you want start the Quiz (y/n) :').capitalize()
        if(choose=='Y'):
                questions=[{'question':'what is the capital of france',
                            'options':["A. Berlin", "B. Paris", "C. Rome", "D. Madrid"],
                            'answer':'B'},
                                {
                                    "question": "Which language is used to build Android apps?",
                                    "options": ["A. Java", "B. Python", "C. C++", "D. Swift"],
                                    "answer": "A"
                                },
                                {
                                    "question": "Who developed Python?",
                                    "options": ["A. Elon Musk", "B. Bill Gates", "C. Guido van Rossum", "D. Linus Torvalds"],
                                    "answer": "C"
                                },
                                {
                                     "question":"What is the correct syntax?",
                                     "options":["A. sql all from customers;","B. sql * from customers;","C. sql from customers;","D. sql * customers;"],
                                     "answer": "B"
                                }
                                ]
                score=0
                for q in questions:
                    print(f"\n"+q["question"])
                    for option in q["options"]:
                        print(option)
                    
                    user_answer = input("Enter your answer (A/B/C/D): ").strip().upper()

                    if(user_answer==q['answer']):
                        score+=1
                        print("correct")
                    else:
                        print(f"wrong, the correct answer is :{q['answer']}")
                print('quiz completed')
                print(f"Your final score is :{score}/{len(questions)}")
        
        else:
             print("Exit")
            

obj=Quiz()
obj.problems()

