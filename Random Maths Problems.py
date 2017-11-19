import random

def first_10_problems(ranges):
    '''10_problems(ranges) -> none
    gives 10 problems, and returns your score'''
    numCorrect = 0
    for x in range(10):
        
        operatorChoices = ['+', '-', '*', '/']

        firstNum = random.randint(1, ranges)
        secondNum = random.randint(1, ranges)

        operator = random.choice(operatorChoices)

        if operator == operatorChoices[0]:
            add = input('What is '+str(firstNum)+' + '+str(secondNum)+'? ')
            total = firstNum + secondNum # answer
            if add.isdigit() is True and int(add) == total:
                print('You are correct! Way to go!\n')
                numCorrect += 1
            else:
                print("I'm sorry, but you are incorrect. The answer is "+\
                      str(total)+'.\n')
                
        elif operator == operatorChoices[1]:

            if firstNum >= secondNum: # first is larger
                difference = input('What is '+str(firstNum)+' - '+str(secondNum)+'? ' )
                total = firstNum - secondNum # answer
            else: 
                difference = input('What is '+str(secondNum)+' - '+str(firstNum)+'? ' )
                total = secondNum - firstNum # answer
            if difference.isdigit() is True and int(difference) == total:
                print('You are correct! Way to go!\n')
                numCorrect += 1
            else: # it is incorrect
                print("I'm sorry, but you are incorrect. The answer is "+\
                      str(total)+'.\n')

        elif operator == operatorChoices[2]:
            product = input('What is '+str(firstNum)+' * '+str(secondNum)+'? ' )
            total = firstNum * secondNum
            if product.isdigit() is True and int(product) == total:
                print('You are correct! Way to go!\n')
                numCorrect += 1
            else:
                print("I'm sorry, but you are incorrect. The answer is "+\
                      str(total)+'.\n')

        elif operator == operatorChoices[3]:
            if firstNum >= secondNum:
                answer = input('What is ' + str(firstNum)\
                             +' / '+str(secondNum)+\
                             '? \n(Express your answer as xRy, where '+\
                             'x is the quotient and y the remainder.) ')
                quotient = firstNum//secondNum # quotient
                remainder = firstNum%secondNum # remainder
            else:
                answer = input('What is ' + str(secondNum)\
                              +' / '+str(firstNum)+\
                              '? \n(Express your answer as xRy, where '+\
                              'x is the quotient and y the remainder.) ')
                quotient = secondNum//firstNum # quotient
                remainder = secondNum%firstNum # remainder
            if answer ==  str(quotient)+'R'+str(remainder):
                print('You are correct! Way to go!\n')
                numCorrect += 1
            else:
                print("I'm sorry, but you are incorrect. The answer is "\
                      +str(quotient)+' Remainder '+str(remainder)+'.\n')
    print('\nYou got '+str(numCorrect)+'0% correct!')

level = input('What level do you want? (Enter \'easy\', \'medium\', or \'hard\') ')
if level.lower() == 'hard':
    ranges = 1000
    first_10_problems(ranges)
elif level.lower() == 'medium':
    ranges = 100
    first_10_problems(ranges)
elif level.lower() == 'easy':
    ranges = 10
    first_10_problems(ranges)
else:
    print("I'm sorry, but we do not have a level called '"+level+"'.")
