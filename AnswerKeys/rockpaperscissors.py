import random

tie_text = "It's a tie!"
computer_text = "Too bad, the computer wins."
user_text = "Congratulations, you win!"

tie = True
while tie:
    computer = random.randint(1, 3)
    if computer == 1:
        computer_chooses = "rock"
    elif computer == 2:
        computer_chooses = "paper"
    else:
        computer_chooses = "scissors"

    user_chooses = input("Please select rock, paper, scissors? ")


    if user_chooses == computer_chooses:
        print(tie_text)
    else:
        tie = False

if user_chooses == 'rock' and computer_chooses == 'paper':
    result = computer_text
elif user_chooses == 'rock' and computer_chooses == 'scissors':
    result = user_text
elif user_chooses == 'paper' and computer_chooses == 'rock':
    result = user_text
elif user_chooses == 'paper' and computer_chooses == 'scissors':
    result = computer_text
elif user_chooses == 'scissors' and computer_chooses == 'rock':
    result = computer_text
elif user_chooses == 'scissors' and computer_chooses == 'paper':
    result = user_text
else:
    result = "An unexpected error occured.  Please try again."

# Cover Re-ask for entry in case of tie in class

print('The computer chose', computer_chooses)
print(result)
