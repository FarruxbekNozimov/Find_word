import random as rd
import os

"""
Plan
1. Questions in file for User
2. Hidden answer of the question
3. Checking the answer
4. Ask play again?  (y/n)
"""
with open('questions.txt') as f:
    question_line = f.read().split('\n')


def play():
    print("Welcome to the game!")
    while True:
        question = rd.choice(question_line).split('-')
        hidden = len(question[1]) * '_'
        while True:
            os.system('cls')
            print(question[0])
            print(f"({len(hidden)} ta harf)  {hidden} ")
            answer = input("Your answer: ").lower()
            for i in range(len(question[1])):
                if answer == question[1][i].lower():
                    hidden = hidden[:i] + answer + hidden[i + 1:]
            if check(hidden, question[1]):
                os.system('cls')
                print(hidden.capitalize())
                break
        print("You find the word!!!")
        if input("Do you want to play again? (y/n) ").lower() == 'n':
            break


def check(ur_answer, real_answer):
    if ur_answer == real_answer:
        return True
    return False


play()
