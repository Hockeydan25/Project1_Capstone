"""Project1 Quiz Program Dan Smestad ITEC 2905-80 Software Dev. Capstone Clara James.

 A Triva quiz program for student editing :

 1.	Write a more descriptive docstring at the start of the program. The docstring should describe the purpose and features of the program.
2.	Create data structure(s) to store the questions and answers. Your data structure should make it easy to add a new topic+questions, and to add/remove questions for an existing topic. Your program should not require the same number of questions for any topic. Data structure should be structured in a way that makes it easy for the program to access the data.
3.	Reduce repeated code.
4.	Use functions to group code into logical blocks.
5.	Enable user to enter answer in any case and program should decide it is correct. For example, if the answer is 'Chicago', then 'chicago', 'cHicAgo' and 'CHICAGO' are all correct.
6.	Improve the user interface when the user selects the quiz topic. It's not clear what the user should enter here, topic = input('Would you like art, or space questions? ') If the user doesn't enter the exact string 'art' or the exact string 'space' then they must restart the program to try again. Include validation to ensure the user chooses a valid topic. Remember that the program should work if there are more available topics, and the user should be able to choose between all available topics.
7.	Ensure the message that is printed if user gets all the answers correct is always printed even if questions are added or removed. If another question was added, and the user answers all correctly, would the message on line 37 or line 70 be printed?
8.	Comment code. You should not need to comment every line, but add comments to help explain the more complex parts of the program.
9.	Pay attention to code quality and style. Descriptive variable and function names, write efficient, logical, readable code.
 """

#data structure, Dicionary to hold data retieved and used to run program. readability with { [ , spacing. 
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

        print('Welcome to my Triva Quiz program!Topic options are: ')                         
        for k,v in question_bank.items(): # reads the question bank key names and print for user to select one.
            print(k)        
        selected_topic= get_input()# simple instructions to start.
        questions_for_topic = question_bank[selected_topic] # variable to hold list of questions from dictionary question_bank.
        quiz_answers = question_bank[selected_topic] # variable to hold list of correct answers from dictinary question_bank.
        score = get_quiz(questions_for_topic, quiz_answers)
        outputs(score, selected_topic) 
        
def get_input():  
    while True:
        selected_topic = input('Please choose a trvia selection topic? ')
        # simple instructions to start, user selects a triva topic.
        # vaildating that they select one of the choices. will keep in While loop until uset types topic in list.        
        if selected_topic not in question_bank.keys():                      
            print('that was not in our choices') 
        else:
            print(f'{selected_topic} is your choice')
            # simple instructions to help show users selection is being used.        
            return selected_topic   

def get_quiz(questions_for_topic, quiz_answers):# argumants needed to setup questions and answers.
    #variables set to use an loop through questions answers. localized function variables. 
    quiz_questions = questions_for_topic['questions']  # variables list of question strings.
    quiz_answers = questions_for_topic['correct_answers']  # variables list of correct answer.
    score = 0  #initalize score for tracking users total score. set to zero at start of quiz.
    for question, correct_answer in zip(quiz_questions, quiz_answers):        
        print(question) 
        #asking user question, to answer the question. 
        users_answer = input('enter your answer here: ') #variable and input function to prompt top user pregroam ready for there input.
        if users_answer.lower()  == correct_answer.lower(): #need to accept any case and validate correct answer.   
            score +=1  #point for correct answer.
            print(f'correct, current points earned = {score}.')#staement that qustion  was answered with correct answer.         
        else:      #message that answer is incorrect, points earned given too.
            print(f'Oops, sorry that was incorrect answer, current points earned = {score}.')
            # could have a retry here to give user another try or add a hint to user to get correct anwser.
    return score # returns score to main and outputs will use.

    #outputs dispplays end messaging to user with score and goodbye.
def outputs(score, selected_topic):      
    print('End of quiz!')# simple note that quiz has ended. total good byt message follows
    print(f'Your total score today in Quiz Triva is {score} out of 3.')
    if score == 3:
            print(f'You got all the Quiz Triva answers on {selected_topic} Triva correct! See you next time!')
    # extra statement to congratulate user on a well played game, 
    # possible to give extra points if all 3 correct
    return score, selected_topic
             
main() # call main to start /or restart program.    