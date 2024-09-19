import random
from datetime import datetime


def game():

    gameover = False

    # Basic counter for number of games won
    gamecount = 0
    wincount = 0

    

    print("Welcome to the Number Guessing Game!")

# Select a Difficulty and assign the number of tries based on that difficulty    
    print("Please select the difficulty level. \n 1. EASY (10 chances) \n 2. MEDIUM (5 chances) \n 3. HARD (3 chances)")

    locked_in = False

    while locked_in == False:
        difficulty = input("Enter your choice (EASY, MEDIUM, HARD): ")

        if difficulty.upper() == "EASY":
            max_tries = 10
            locked_in = True

        elif difficulty.upper() == "MEDIUM":
            max_tries = 5
            locked_in = True
        
        elif difficulty.upper() == "HARD":
                max_tries = 3
                locked_in = True

        else:
                print("I don't understand.")  
            
    print(f"You've selected {difficulty}. Remember to type HINT for help. \n")

# Select a Winning number and record when the game starts
    correct = random.randint(1,100)
    
    start = datetime.now()

    guess = input("Guess a number between 1 and 100: ")

    tries = 0

# Hint system (Basically guarantees you to win in if the number is 50 lol)
    if correct < 50:
        hint = "The number is less than 50"
    elif correct > 50:
        hint = "The number is more than 50"
    else:
        hint = "The number is between 25 and 50" 

# Game loop starts now
    while gameover == False and tries <= max_tries:      

        if guess.lower() == 'hint':
            print(hint)
            guess = input("\nGuess a number between 1 and 100: ")

        elif guess.lower() != 'hint':

            try:
                int(guess) * 1

            except:
                print("This is not a number. Please try again.")
                guess = input("\nGuess a number between 1 and 100: ")

            if int(guess) > correct:
                print("You've guessed too high! Please try again")
                tries += 1
                guess = input("\nGuess a number between 1 and 100: ")

            elif int(guess) < correct:
                print("You've guessed too low! Please try again!")
                tries += 1
                guess = input("\nGuess a number between 1 and 100: ")

            # Win Condition
            else:
                    # Stats
                    score = tries
                    wincount += 1
                    end = datetime.now()

                    # Measures time
                    difference = end - start
                    seconds = difference.total_seconds()

                    # Keeps track of high score
                    if gamecount == 0:
                            lowest_score = score
                            gamecount += 1
                    else:
                            lowest_score = min(lowest_score, score)
                            gamecount += 1

                    print(f"\nCongratulations! You win!\nThe correct number was {correct}!")

                    if lowest_score <= score:
                        print(f"You guessed in {score + 1} out of {max_tries} tries! A personal best!")
                        
                    else:
                            print(f"You guessed in {score + 1} out of {max_tries} tries!")
                    print(f"\nGame completed in {seconds} seconds.")
                    print(f"You've won {wincount} out of {gamecount} games!")
                    gameover = True

        # Gameover
        if tries >= max_tries:
                print(f"\nSorry, that was incorrect. The number was {correct}.  \nGame over! :(")
                print(f"You've won {wincount} out of {gamecount} games!")
                gameover = True

        
    # Post game settings. Check to see if they want to play again or leave game.
    while gameover == True:

        restart = input("\nWould you like to play again? (Y/N) \n")

        if restart.lower() == 'y':
            gamecount += 1
            return game()

        elif restart.lower() == 'n':
            quit()

        else: 
            print("I don't understand. Please try again.")
            restart = input("Would you like to play again? (Y/N) \n")

game()