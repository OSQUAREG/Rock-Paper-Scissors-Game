
import random

# Creating a list of all Possible Options & Dictionary
possibleOptions = ["R", "P", "S"]

optionsDict = {
    "R" : "Rock",
    "P" : "Paper",
    "S" : "Scissors"
}

# Taking User's input
userInput = input("Enter 'R' for  'Rock','P' for 'Paper' or 'S' for 'Scissors'.")

# Making a random choice for the CPU
computerChoice = random.choice(possibleOptions)

#Printing an error and creating a While loop for invalid input
while userInput not in possibleOptions:
    print(f"Your choice ({userInput}) is invalid, please try again.\nEnter 'R' for  'Rock','P' for 'Paper' or 'S' for 'Scissors'.")
    userInput = input("Enter 'R' for  'Rock','P' for 'Paper' or 'S' for 'Scissors'.")
    
    # Printing both User and CPU options
    print(f"\nPlayer ({optionsDict[userInput]}) : CPU ({optionsDict[computerChoice]}).\n")

if userInput == computerChoice:
    print(f"Both Player and CPU selected ({optionsDict[userInput]}). It's a tie!")

elif userInput == "R":
    if computerChoice == "S":
        print("Rock smashes Scissors! You win!")
    else:
        print(f"Paper covers Rock! You lose.")

elif userInput == "P":
    if computerChoice == "R":
        print("Paper covers Rock! You win!")
    else:
        print("Scissors cuts Paper! You lose.")

elif userInput == "S":
    if computerChoice == "P":
        print("Scissors cuts Paper! You win!")
    else:
        print("Rock smashes Scissors! You lose.")

