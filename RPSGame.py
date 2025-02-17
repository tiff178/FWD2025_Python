# Rock, Paper, Scissors (RPG) Game 
import random 
options = ["Rock", "Paper", "Scissors"]

userChoice = input("Choose Rock, Paper, or Scissors: ")
computerChoice = random.choice(options)

print("You chose:", userChoice)
print("Computer chose:", computerChoice)

if userChoice == computerChoice:
    print("It's a tie!")

elif userChoice == "Rock" and computerChoice == "Scissors":
    print("You win!")

elif userChoice == "Paper" and computerChoice == "Rock":
    print("You win!")

elif userChoice == "Scissors" and computerChoice == "Paper":
    print("You win!")
    
else: 
    print("Computer wins!")