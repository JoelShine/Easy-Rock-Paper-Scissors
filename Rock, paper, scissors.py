import random
from playsound import playsound

computer_choices = ['rock', 'paper', 'scissors']

print("Welcome to rock, paper and scissors")
print("")

while True:
    random.shuffle(computer_choices)
    one_choice = random.choice(computer_choices)

    print("Your choice - ")
    human_choice = input()

    if one_choice == "rock" and human_choice == "rock":
        print("Computer's choice - "+one_choice)
        print("")
        print("!! Game Draw !!")

    elif one_choice == "rock" and human_choice == "paper":
        print("Computer's choice - "+one_choice)
        print("")
        print("!! You Win !!")
        playsound("win.mp3")

    elif one_choice == "rock" and human_choice == "scissors":
        print("Computer's choice - "+one_choice)
        print("")
        print("!! Jarvis Wins !!")
        playsound("lose.mp3")

    elif one_choice == "paper" and human_choice == "rock":
        print("Computer's choice - "+one_choice)
        print("")
        print("!! Jarvis Wins !!")
        playsound("lose.mp3")

    elif one_choice == "paper" and human_choice == "paper":
        print("Computer's choice - "+one_choice)
        print("")
        print("!! Game Draw !!")

    elif one_choice == "paper" and human_choice == "scissors":
        print("Computer's choice - "+one_choice)
        print("")
        print("!! You Win !!")
        playsound("win.mp3")

    elif one_choice == "scissors" and human_choice == "rock":
        print("Computer's choice - "+one_choice)
        print("")
        print("!! You Win !!")
        playsound("win.mp3")

    elif one_choice == "scissors" and human_choice == "paper":
        print("Computer's choice - "+one_choice)
        print("")
        print("!! Jarvis Wins !!")
        playsound("lose.mp3")

    elif one_choice == "scissors" and human_choice == "scissors":
        print("Computer's choice - "+one_choice)
        print("")
        print("!! Game Draw !!")

    elif 'quit' in human_choice or 'break' in human_choice or 'close' in human_choice or 'exit' in human_choice:
        print("")
        print("Thank You for playing !!!")
        break

