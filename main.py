# Number Picking Program

#TODO- handle incorrect inputs 

#Imports
import random
from random import choice

#Variables

#Functions
def generate_random_number(upper_limit):
    random_number = random.randint(0, upper_limit)
    return random_number

def generate_random_ai_guess(upper_limit,guessed_list):
    random_guess = choice([i for i in range(0, upper_limit) if i not in guessed_list])
    return random_guess

def check_guess(guess,random_number,turn): #should return #don't have side effects here
    if turn == "ai":
        if guess == random_number:
            return "correct"
        else:
            return "incorrect"
    if turn == "human":
        if guess == random_number:
            return "correct"
        else:
            return "incorrect"

def check_turn(turn):
    if turn % 2 == 0:
        return "ai"
    else:
        return "human"

def main():
    #TODO- question, why did my program not work when the variables were before the functions?
    playing = True
    complete = False
    guessed_list = []
    current_turn = 0
    upper_limit = 100

    print("\nWelcome to the guessing game. Your challenge is to guess the random number (from 0-" + str(upper_limit) + ") before the AI does.")
    print("The random number has been chosen. You get first guess.")
    correct_number = generate_random_number(upper_limit)

    while playing:
        current_turn = current_turn + 1
        if check_turn(current_turn) == "ai":
            ai_guess = generate_random_ai_guess(upper_limit,guessed_list)
            guessed_list.append(ai_guess)
            if check_guess(ai_guess,correct_number,check_turn(current_turn)) == "correct":
                print("\nAi turn- the Ai correctly guessed the number " + str(correct_number) + ". You lost :(")
                playing = False
                complete = True
            else:
                print("\nAi turn- the Ai guessed " + str(ai_guess) + " which was incorrect")
                #should go back to beginning of loop

        if check_turn(current_turn) == "human":
            human_guess = input("\nYour turn- enter your guess here: ")
            if check_guess(human_guess, correct_number, check_turn(current_turn)) == "correct":
                print("You correctly guessed the number " + str(correct_number) + "! You won!")
                playing = False
                complete = True
            else:
                print("Your guess was incorrect, the number is not " + str(human_guess))

    if complete:
        exit("Game over")

if __name__ == "__main__":
    main()
