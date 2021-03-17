import random

MAX = 100
MIN = 1


def game():
    play = "y"
    bestscore = 0
    while play == "y" or play == "yes":
        print("play  ", play)
        print("---------------------------------------------------------------")
        print("              Number Guessing Game")
        print("---------------------------------------------------------------")
        random_num = random.randrange(MIN, MAX)
        attempts = 1

        if bestscore != 0:
            print("The best score is: {}".format(bestscore))

        guess = guess_number(0)

        while guess != random_num:
            if guess > MAX or guess < MIN:
                print("Your guess was out of range. Try again")
                guess = guess_number(guess)
            elif guess > random_num:
                print("It's Lower")
                attempts += 1
                guess = guess_number(guess)
            elif guess < random_num:
                print("It's Higher")
                attempts += 1
                guess = guess_number(guess)
        print("You Won and Game Over")
        print("It took you {} attempts!   ".format(attempts))

        if attempts < bestscore:
            bestscore = attempts
        elif bestscore == 0:
            bestscore = attempts
        print("The best score is: ", bestscore)
        play = input(
            "Would you like to play again?   [Y]es or [N]o?  ").lower()

    print("Thank you for playing the Number Guessing Game!")


def guess_number(num):
    while True:
        try:
            num = int(
                input("Pick a number between {} and {}!   ".format(MIN, MAX)))
            break
        except ValueError:
            print("That wasn't a number between {} and {}.   ".format(MIN, MAX))
            continue
    return num


game()
