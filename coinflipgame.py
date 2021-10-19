def determine_coin_face():
    coin_value = random.randint(0,1)
    if (coin_value == 0):
        return "heads"
    else:
        return "tails"

def flip_coin(guess, coin_value):
    converted_guess = convert_guess(guess)
    if (converted_guess == coin_value):
        return print(f"Congrats {converted_guess.upper()} is correct! \nYOU WIN!!!")
    else:
        return print(f"Sorry its {coin_value.upper()}\n")

def quit_game_or_play_again(inputs):
    if (inputs == "q" or inputs == "Quit"):
        return False 
    elif (inputs.lower() == "y" or inputs.lower() == "yes"):
        return True

def validate_string(guess):
    if (guess == "heads" or guess == "h" or guess == "tails" or guess == "t"):
        return True

def convert_guess(guess):
    if (guess == "h" or guess == "heads"):
        return "heads"
    else:
        return "tails"

def coin_flip_game():
    print("Welcome to Heads or tails!\n To play type HEADS,h or TAILS,t\n to QUIT type q or quit")
    # Generate Heads or tails
    coin_value = determine_coin_face()
    while True:
        # Check to see if players want to quit.
        guess = input("Heads or Tails: ")
        guess = guess.lower()
        # validate String,
        valid = False
        valid = validate_string(guess)

        if (valid == True and guess != "quit" and guess!="q"):
            flip_coin(guess, coin_value)   
            # play game again?
            inputs = input("If YES type y or yes \nIf NO type q or quit: \n\n")
            reply = quit_game_or_play_again(inputs)
            if (reply == True):
                coin_flip_game()
            else:
                print("Have a Great Day")
                return 
        elif (guess == "quit" or guess =="q"):
            print("Goodbye Quitter!")
            return False

coin_flip_game()