"""Project1 Quiz Program Dan Smestad ITEC 2905-80 Software Dev. Capstone Clara James.
version one
 A quiz program. written for student editing """

#data structue Dicionary to hold data that can be interchanged. May have to rethink the my list names. 

question_bank = {   
"art": 
        {   
        "questions": 
        [
        "Who painted the Mona Lisa?",
        "What precious stone is used to make the artist\'s pigment ultramarine?",
        "Anish Kapoor\'s bean-shaped Cloud Gate scuplture is a landmark of which city?"
        ],
        "correct_answers" : 
        [
        "Leonardo Da Vinci",
        "Lapiz lazuli",
        "Chicago"
        ]
        },
"space": 
        {   
        "questions" :
        [
        "Which planet is closest to the sun?", 
        "Which planet spins in the opposite direction to all the others in the solar system?",
        "How many moons does Mars have?"
        ],
        "correct_answers" : 
        [
        "Mercury",
        "Venus",
        "2"
        ]
        }
}

def main():
    #try:
        #score = 0
        print('Welcome to my Triva Quiz program!Topic options are: ')                         
        for k,v in question_bank.items(): # reads the question bank key names and print for user to select one.
            print(k)
        selected_topic = input('Please choose a trvia selection topic? ')# simple instructions to start.
        get_input(selected_topic)# simple instructions to start.
        questions_for_topic = question_bank[selected_topic] # list of questions.
        quiz_answers = question_bank[selected_topic] # list of correct answers
        score = get_quiz(questions_for_topic, quiz_answers)
        outputs(score)
        #outputs(selected_topic) 
    # except Exception as e:
    #   print('error',e) 
        
def get_input(selected_topic):  
    if selected_topic not in question_bank.keys(): # vaildating that they select one of the choices.                     
        restart()
    else:
        print(f'{selected_topic} is your choice')
        # simple instructions to help show users selection is being used.        
    return selected_topic   

def get_quiz(questions_for_topic, quiz_answers):# argumants needed to setup questions and answers.
    #variables set to use an loop through questions answers. localized function variables. 
    quiz_questions = questions_for_topic['questions']  # list of question strings
    quiz_answers = questions_for_topic['correct_answers']  # list of correct answer
    score = 0  #initalize score for tracking users total score. set to zero at start of quiz.
    for question, correct_answer in zip(quiz_questions, quiz_answers):        
        print(question) 
        #asking user question, to answer the question. 
        users_answer = input('enter your answer here: ') #variable and input function to prompt top user pregroam ready for there input.
        if users_answer.lower()  == correct_answer.lower(): #need to accept any case and validate correct answer.   
            score +=1  #point for correct answer. #TO FIX : validation correct_answer.
            print(f'correct, {score} point added.')#staement that qustio  was answered with correct answer.         
        else:                          # maybe better with score total call to total_scotre().
            print(f'Oops, sorry that was incorrect answer.')
            # To FIX: remove this commentedOUT section once output is working.
    # print('End of quiz!')# simple note that quiz has ended. total good byt message follows
    # print(f'Your total score in Quiz Triva is {score} out of 3.')
    # if score == 3:
    #         print('You got all the answers correct!')
    # extra statement to congratulate user on a well played game, 
    # possible to give extra points if all 3 correct
    print(score)
    return score

    #todo:  fix outputs get understanind of local variable usage here and counter not working.
def outputs(score):  
    
    print('End of quiz!')# simple note that quiz has ended. total good byt message follows
    print(f'Your total score in Quiz Triva is {score} out of 3.')
    if score == 3:
            print('You got all the answers correct! See you next time')
    # extra statement to congratulate user on a well played game, 
    # possible to give extra points if all 3 correct
    return score
    # to fix users incorrect topic is appearing at end of preogram. Also need a break    
def restart():    #requested User input to play again. gets used when topic other than the ones listed is entered by the user.
    retry = input('Your entery was not in the list of Topics. Would you like to select one from the list? Enter y or n: ') 
    if retry.lower() == 'y':
        main()  
    else:
        print('thanks for playing!') #good bye message               

main() # call main to start /or restart program.    

