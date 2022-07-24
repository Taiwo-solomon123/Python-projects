"""
This python program generates random 50 quizes for 35 students.
==> You have a dictionary of the quiz_key and quiz_value
==> All the keys(quiz_keys) and values(quiz_values) would be placed in two different lists and shuffled
==> Then a multichoice question would be presented to each students in different files and the options would contain the main answer with 3 other wrong answers(Shuffle that one too)
==> This would repeat until there are no longer questions to ask.
==> Everytime a student question file has been filled up the state and capital lists would be reshuffled and the program above would repeat till there is no longer any student left.
==> The answer to each student question would be stored in a separate file
"""

import random


def create_quiz(quiz_dictionary, number_of_options, question_format):
    """_summary_
    This function creates a quiz string formed from quiz_dictionary. There are len(quiz_dictionary) number of random questions. This function returns a quiz string and its respective answers. On each call, this function rearranges the questions and its options so the quiz string value generated is different from the last.
    Args:
        quiz_dictionary (_dict_): _Quiz dictionary, where the key is the question and the value is the answer. The quiz questions will be formed from this dictionay_
        number_of_options (_int_): _Number of question choices_
        question_format (_str_): _Format in which questions will be presented to the user. This string is presnted with quiz_question[key]_
    """
    quiz_keys= list(quiz_dictionary.keys())
    random.shuffle(quiz_keys)
    quiz_values= list(quiz_dictionary.values())
    random.shuffle(quiz_values)
    all_questions= []
    all_answers= []
    option_alphabeths= ["A", "B", "C", "D", "E", "F"]
    for i in range(len(quiz_keys)):
        question_number= i+1
        quiz_key= quiz_keys[i]
        quiz_value= quiz_dictionary[quiz_key]
#        quiz_values.remove(quiz_value)
        wrong_options= random.sample(quiz_values, number_of_options-1)
        options= [quiz_value] + wrong_options
        random.shuffle(options)
        
        answer_options= []
        
        for j in range(len(options)):
            option= options[j]
            alphabeth= option_alphabeths[j]
            option_format= f"{alphabeth}    {option}"
            answer_options.append(option_format)
            if option == quiz_dictionary[quiz_key]:
                answer= f"{question_number}. {alphabeth}"
                all_answers.append(answer)
                
        question=f"{question_number}. {question_format} {quiz_key} ?" + "\n"+ "\n".join(answer_options)
        all_questions.append(question)
    
    global quiz_questions
    quiz_questions= "\n\n".join(all_questions)
    global quiz_answers
    quiz_answers= "\n".join(all_answers)
    


def create_student_quiz_file(quiz_dictionary, number_of_students, number_of_options, question_format):
    """_summary_
    This functions uses the create_quiz() function to generate len(number_of_students) number of quiz files with different question and question choices arrangements in the same directory as this python code.
    Args:
        quiz_dictionary (_type_): _description_
        number_of_students (_type_): _description_
        number_of_options (_type_): _description_
        question_format (_type_): _description_
    """
    for i in range(number_of_students):
        create_quiz(quiz_dictionary, number_of_options, question_format)
        student_number= i+1
        student_quiz_file_name= f"capital_quiz{student_number}.txt"
        student_quiz_answer_file_name= f"capital_answer{student_number}.txt"
        with open(student_quiz_file_name, "w") as student_quiz_file:
            student_quiz_file.write(quiz_questions)
        with open(student_quiz_answer_file_name, "w") as student_quiz_answer_file:
            student_quiz_answer_file.write(quiz_answers)


states_and_capitals = {'Alabama': 'Montgomery', 'Alaska': 'Juneau', 'Arizona': 'Phoenix',
'Arkansas': 'Little Rock', 'California': 'Sacramento', 'Colorado': 'Denver', 
'Connecticut': 'Hartford', 'Delaware': 'Dover', 'Florida': 'Tallahassee',
'Georgia': 'Atlanta', 'Hawaii': 'Honolulu', 'Idaho': 'Boise', 'Illinois':
'Springfield', 'Indiana': 'Indianapolis', 'Iowa': 'Des Moines', 'Kansas':
'Topeka', 'Kentucky': 'Frankfort', 'Louisiana': 'Baton Rouge', 'Maine':
'Augusta', 'Maryland': 'Annapolis', 'Massachusetts': 'Boston', 'Michigan':
'Lansing', 'Minnesota': 'Saint Paul', 'Mississippi': 'Jackson', 'Missouri':
'Jefferson City', 'Montana': 'Helena', 'Nebraska': 'Lincoln', 'Nevada':
'Carson City', 'New Hampshire': 'Concord', 'New Jersey': 'Trenton', 'New Mexico': 'Santa Fe', 'New York': 'Albany', 'North Carolina': 'Raleigh',
'North Dakota': 'Bismarck', 'Ohio': 'Columbus', 'Oklahoma': 'Oklahoma City',
'Oregon': 'Salem', 'Pennsylvania': 'Harrisburg', 'Rhode Island': 'Providence',
'South Carolina': 'Columbia', 'South Dakota': 'Pierre', 'Tennessee':
'Nashville', 'Texas': 'Austin', 'Utah': 'Salt Lake City', 'Vermont':
'Montpelier', 'Virginia': 'Richmond', 'Washington': 'Olympia', 'West Virginia': 'Charleston', 'Wisconsin': 'Madison', 'Wyoming': 'Cheyenne'}

def main():
    if __name__=="__main__":
        question_message= "What is the capital of"
        create_student_quiz_file(quiz_dictionary= states_and_capitals, number_of_students= 35, number_of_options= 4, question_format= question_message)
        
main()
