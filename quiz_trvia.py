"""Project1 Quiz Program Dan Smestad ITEC 2905-80 Software Dev. Capstone Clara James.
version one
 A quiz program. written for student editing """

#data structue Dicionary to hold data that can be interchanged. May have to rethink the my list names. 

# dictionaries - can use indentation and newlines for readablility for defining a dictionary or list 
question_bank = {   # the main keys are topics for questions 
    "art": 
        {
            "questions": [    # "parallel arrays" - element 0 of one list correlates to element 0 of another list "
                "Who painted the Mona Lisa?",
                "What precious stone is used to make the artist\'s pigment ultramarine?",
                "Anish Kapoor\'s bean-shaped Cloud Gate scuplture is a landmark of which city?"
            ],
            "correct_answers": [
                "Leonardo Da Vinci",
                "Lapiz lazuli",
                "Chicago"
            ]
        },
    "Space": {
        "questions":
["Which planet is closest to the sun?",  
"Which planet spins in the opposite direction to all the others in the solar system?",
"How many moons does Mars have?"],
"correct_answers": ["Mercury" ,"Venus","two"]}}

def main():
    try:     
        total_score = 0   #count the score of coorect answers.
        users_answer = [] #collect the users acutal inputs.
        #question_bank["hockey"] = "what do the letters NHL stand? "#add new pair to existing dictionary.
        print('Welcome to my Triva Quiz program!Topic options are: ')
        
        for k,v in question_bank.items(): # reads the question bank key names and print for user to select one.
            print(k)


        selected_for_topic = input('Please choose a topic, what is your trvia selection? ')# simple instructions to start.
        
        if selected_for_topic in question_bank.keys(): # vaildating that they select one of the choices.                     
        
            print(f'{selected_for_topic} is your choice')# simple instructions to help show users what is happening.
           
            # all the questions = the set of all the questions [ the users input ]
            questions_for_topic = question_bank[selected_for_topic]  # use the variable as key to access 
            print(questions_for_topic)

            # assume index 0 of one list is associated with index 0 of the other list
            # assume index 1 of one list is associated with index 1 of the other list....
            questions = questions_for_topic['questions']  # list of question strings 
            correct_answers = questions_for_topic['correct_answers']  # list of correct answers

            # # counting loop
            # for x in range(len(questions)):
            #     question_text = questions[x]
            #     correct_answer = correct_answers[x]
            #     # print question, ask user, check for right answer....
            #     print(question_text, correct_answer) 

            for question_text, correct_answer in zip(questions, correct_answers):
                print(question_text, correct_answer) 
                # todo ask user question 
                users_answer = input('what is the answer')

                # "Mars"  -> "mars"   # right
                # "MARS"  -> "mars"   # right
                # "mArS"  -> "mars"   # right
                # "Jupiter" -> "jupiter"  # wrong

                # "Mars"  -> "mars"   # correct answer 

                if users_answer.lower() == correct_answer.lower():  
                    print('correct')
                else:
                    print('no')

                

            question_bank_list = list(question_bank.values())

            #creating art question list to loop over, use for loop. Maybe this could be more generic name/
            art_question_list = [question_bank_list[0]["questions"][0], 
            question_bank_list[0]["questions"][1],
            question_bank_list[0]["questions"][2]] 

            #creating art question answer list to loop over, use for loop.Maybe this could be more generic name/
            art_question_answer_list = [question_bank_list[0]["correct_answers"][0], 
            question_bank_list[0]["correct_answers"][1],
            question_bank_list[0]["correct_answers"][2]]

            # for question in art_question_list: #for loop loops through let without len function.
            #     print(question)    #variable question will start at 0 count of list.         
            #     users_answer = input('enter your answer here: ')  #if users_answer in art_question_answer_list:                           
            #     if  users_answer in art_question_answer_list:                
            #         print(f'that was correct, for each correct answer you earn one point,'
            #         ' your next question will load now.') #point of referance to user
            #         total_score += 1   #score total incrementing
            #     else:
            #         print(f'Oops, sorry that was incorrect answer.')
            #         #was working on loop here to give correct answer for each loop but keep getting all three answers.
            
            
            print('End of quiz!')# simple note that quiz has ended. total good byt message follows
            print(f'Your total score on {selected_for_topic} questions is {total_score} out of 3.')
             # extra statement to congratulate user on a well played game, possible to give extra points if all 3 correct.    
            if total_score == 3:
                print('You got all the answers correct!') 
        else: #starting spce triva. Haven't added additional Hockey category questions noteed about.
            print(f'You selected space for your triva quesions.')
            question_bank_list = list(question_bank.values())
                #art_questions = question_bank_list[0]["questions"][0]
                # print(art_questions)
            space_question_list = [question_bank_list[1]["questions"][0], 
            question_bank_list[1]["questions"][1],
            question_bank_list[1]["questions"][2]] 

            space_question_answer_list = [question_bank_list[1]["correct_answers"][0], 
            question_bank_list[1]["correct_answers"][1],
            question_bank_list[1]["correct_answers"][2]]
           
            for question in space_question_list: #for loop loops through let without len function.
                print(question) 
                users_answer = input('enter your answer here: ')  
                    #if users_answer in art_question_answer_list:         
                if users_answer in space_question_answer_list:                                 
                    print(f'that was correct, for each correct answer you earn one point,'
                    'your next question will load now or game will end.') 
                    total_score += 1 # point total socre increments one through loop                    
                else: 
                    print(f'Oops, sorry that was incorrect answer.') #incorrect statement to user.
                    # needed to wotk out giving correct answer here possible.
            print('End of quiz!') #closing note
            print(f'Your total score on {selected_for_topic} questions is {total_score} out of 3.')
            # extra statement to congratulate user on a well played game, possible to give extra points if all 3 correct.
            if total_score == 3:  # TODO what if there are more questions? 
                print('You got all the answers correct!')        
    except Exception as e:     #validation error handling for 
            print(e)  
            print('Opps we didn\'t get the question loaded please pause.')  
            #possible error for service outage.     
       
main() # call main to start /or restart program.

# print(f'Your sletion {selection_for_topic} is not a choice, please try agian, select from the list.')

            # if selection_for_topic not in question_bank.keys():
            #     print(f'Your seletion {selection_for_topic} is not a choice, please try agian, select from the list.')
            #     print('OK, let\'s play Trvia, make a new slection')
            #     restart = main()         #will return to start with list to select.
            # else: 