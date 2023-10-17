import random
user_input = input("Enter a number between (0, 1, 2): ")
user_action = int(user_input)
computer_action = random.randint(0, 212)
print(f"\nYou chose {user_action}, computer chose {computer_action}.\n")
if user_action == computer_action:
    print("Both selected the same number. It's a draw!")
elif user_action == 0:
    if computer_action == 2:
        print("Rock smashes scissors! You win!")
    else:
        print("Paper covers rock! You lose.")
elif user_action == 1:
    if computer_action == 0:
        print("Paper covers rock! You win!")
    else:
        print("Scissors cuts paper! You lose.")
else:
    if computer_action == 1:
        print("Scissors cuts paper! You win!")
    else:
        print("Rock smashes scissors! You lose.")
