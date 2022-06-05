while True:
    import random
    user_options = input("Enter a choice of uppercase:\n 'R' for rock\n 'P' for paper\n 'S' for scissors\n")
    possible_options = ["R","P","S"]
    computer_action = random.choice(possible_options)
    if user_options == computer_action:
        print("Player:CPU selected %s. It is a tie!" %user_options)
    elif user_options == "R":
        if computer_action == "S":
            print("Rock smashes scissors! You win!")
        else:
            print("Paper covers rock! you lose!")
    elif user_options == "P":
        if computer_action == "R":
            print("Paper covers rock! You win!")
        else:
            print("Scissors cuts paper! you lose!")
    elif user_options == "S":
        if computer_action == "P":
            print("Scissors cuts paper! You win!")
        else:
            print("Rock smashes scissors! you lose!")
    else:
        print("Invalid input, enter your choice again")
    play_again = input("Play again? (y/n): ")
    if play_again.lower() != "y":
        break
