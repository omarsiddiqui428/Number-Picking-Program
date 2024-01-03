#number guessing game
#AI player uses binary strategy 

import random

#Functions
def generate_random_number(upper_limit):
    random_number = random.randint(0, upper_limit)
    return random_number

def guess_feedback(guess,random_number):
    if guess == random_number:
        return "correct"
    elif guess > random_number:
        return "too high"
    elif guess < random_number:
        return "too low"

def generate_ai_guess(lower_limit,upper_limit):
    guess = (lower_limit+ upper_limit) // 2
    return guess

def game_winner(ai_guess_count,human_guess_count):
    if ai_guess_count < human_guess_count:
        return "ai"
    if ai_guess_count > human_guess_count:
        return "human"
    elif ai_guess_count == human_guess_count:
        return "tie"

def main():

    human_playing = True
    human_turn_complete = False
    initial_max = 100
    human_guess_count = 0
    ai_guess_count = 0
    ai_turn_complete = False
    ai_playing = True

    print("\nWelcome to the guessing game. Your challenge is to guess the random number from 0-" + str(initial_max) + " in as few guesses as possible.")
    print("Once you guess, the AI will then try to guess the same number. The player that gets the number in the fewest guesses wins!")
    print("The random number has been chosen. You go first.")

    correct_number = generate_random_number(initial_max)

    while human_playing:

        try: #error handling 
            human_guess = int(input("\nEnter your guess: ")) 

        except ValueError:
            print("Your input was not an integer. Please enter a valid integer guess.")
            continue
            
        human_guess_count += 1
        if guess_feedback(human_guess,correct_number) == "correct":
            print("\nYou correctly guessed the number!")
            human_turn_complete = True
            human_playing = False
        if guess_feedback(human_guess, correct_number) == "too high":
            print("your guess was too high")
        if guess_feedback(human_guess, correct_number) == "too low":
            print("your guess was too low")

    if human_turn_complete:
        print("\n\nYour total number of guesses: " + str(human_guess_count))
        print("\nNow it's the AI's turn to guess.\n")
        upper_limit = initial_max
        lower_limit = 0

        while ai_playing:
            ai_guess = generate_ai_guess(lower_limit,upper_limit)
            ai_guess_count += 1
            print("AI guess " + str(ai_guess_count) + ": " + str(ai_guess))
            if guess_feedback(ai_guess, correct_number) == "correct":
                print("\nThe AI correctly guessed the number!")
                ai_turn_complete = True
                ai_playing = False
            if guess_feedback(ai_guess, correct_number) == "too high":
                upper_limit = ai_guess
                print("The AI's guess was too high")
            if guess_feedback(ai_guess, correct_number) == "too low":
                lower_limit = ai_guess
                print("The AI's guess was too low")

    if ai_turn_complete:
        print("\nYour total number of guesses to get the correct number: " + str(human_guess_count))
        print("The AI's total number of guesses to get the correct number: " + str(ai_guess_count))
        if game_winner(ai_guess_count,human_guess_count) == "ai":
            print("\nThe AI wins the guessing game!")
        if game_winner(ai_guess_count,human_guess_count) == "human":
            print("\nYou win the guessing game!")
        if game_winner(ai_guess_count, human_guess_count) == "tie":
            print("\nYou and the AI tie the guessing game!")

    exit("Game over")

if __name__ == "__main__":
    main()
