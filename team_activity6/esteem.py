"""
Purpose: Rosenberg self-esteem scale
"""

print("This program is an implementation of the Rosenberg")
print("Self-Esteem Scale. This program will show you ten")
print("statements that you could possibly apply to yourself.")
print("Please rate how much you agree with each of the")
print("statements by responding with one of these four letters:")
print()
print('Measure thingys')
print()

def print_questions():
    """
    Displays and asks the users the questions from the
    Rosenberg Self-Esteem questioneer
    
    Parameters:

    return: 
    """
    questions = ["I feel that I am a person of worth, at least on an equal plane with others",
        "I feel that I have a number of good qualities",
        "All in all, I am inclined to feel that I am a failure",
        "I am able to do things as well as most other people",
        "I feel I do not have much to be proud of",
        "I take a positive attitude toward myself",
        "On the whole, I am satisfied with myself",
        "I wish I could have more respect for myself",
        "I certainly feel useless at times",
        "At times I think I am no good at all"]
    
    answers = []
    
    for i in range(10):
        print(f'{i + 1}. {questions[i]}.')
        answer = input('Enter A, a, D or d: ')
        answers.append(answer)
    compute_total(answers)
    
def compute_total(answer):
    """
    Computes the points based on the answers on
    the Rosenberg questioneer.

    Parameters:
        answers - Takes the answers from the print_questions
        function

    return: The total score from the questioneer.
    """
    points = 0

    for i in range(10):
        if i in [0, 1, 3, 5, 6]:
            if answer[i] == 'D':
                points += 0
            elif answer[i] == 'd':
                points += 1
            elif answer[i] == 'a':
                points += 2
            elif answer[i] == 'A':
                points += 3
        if i in [2, 4, 7, 8, 9]:
            if answer[i] == 'D':
                points += 3
            elif answer[i] == 'd':
                points += 2
            elif answer[i] == 'a':
                points += 1
            elif answer[i] == 'A':
                points += 0
    return points
    
            
def main():
    print_questions()
    score = print_questions()
    print()
    print(f'Your total score is: {score}')
    print('A score less than 15 means that you need to love yourself more')

if __name__ == '__main__':
    main()
