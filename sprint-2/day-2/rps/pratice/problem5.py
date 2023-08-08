# Write a Python program that simulates a Rock Paper Scissors game between a player and the computer. Take user input for their choice, generate a random computer choice, and determine the winner based on the rules.


import random 

print("Welcome to Rock Paper Sissors Game \n \n ")

userName = (input("Enter Your Name:---- ").strip());

print('\n')

rounds = int(input("How many Round you Want to play?  "))

options = ['Rock','Paper','Scissors']

computerScore = 0;

userScore = 0;

tieMatches = 0;

PlayGame = True


while PlayGame:
    print("----------------------")
    userChoise  = input("Enter Your Move:-  ")
    print('\n')
    computerChoise = options[random.randint(0,2)]
    print(f"Your Choose -- {userChoise} \n");
    print(f"Computer Choose -- {computerChoise}");
    print('\n')
    if userChoise=="Rock" and computerChoise=="Paper":
        computerScore+=1;
        print("---Computer Won---")
    elif userChoise=="Rock" and computerChoise=="Scissors":
        userScore+=1;
        print(f"---{userName} Won---")
    elif userChoise=="Rock" and computerChoise=="Rock":
        tieMatches+=1;
        print(f"---Match Tie---")
    elif userChoise=="Paper" and computerChoise=="Paper":
        tieMatches+=1;
        print(f"---Match Tie---")
    elif userChoise=="Paper" and computerChoise=="Rock":
        userScore+=1;
        print(f"---{userName} Won---")
    elif userChoise=="Paper" and computerChoise=="Scissors":
        computerScore+=1;
        print("---Computer Won---")
    elif userChoise=="Scissors" and computerChoise=="Paper":
        userScore+=1;
        print(f"---{userName} Won---")
    elif userChoise=="Scissors" and computerChoise=="Rock":
        computerScore+=1;
        print("---Computer Won---")
    elif userChoise=="Scissors" and computerChoise=="Scissors":
        tieMatches+=1;
        print(f"---Match Tie---")
    
    print('\n')
    print("-----TotalScore------")
    print(f"{userName}--- {userScore}")
    print(f"Computer---- {computerScore}")
    print(f"Tiematches --- {tieMatches} \n")
    rounds-=1;
    if(rounds==0):
        quitGame = input("Do you Want to quit game : 'Y' or 'N'   ").strip()
        if(quitGame=="y" or quitGame=='Y'):
             PlayGame=False
        elif (quitGame=="n" or quitGame=='N'):
            rounds = int(input("How many Round you Want to play?  "))
    

print('\n')

if userScore==computerScore:
    print("You Played Well!! But Match is Tie!! ")
    print("But Still you can play and win the match")

elif userScore>computerScore:
    print(f"Congratulation {userName} You Won the Match!!")
else:
    print(f"Sorry! {userName} You Lost the Match!!")
    print("But Still you can play and win the match")