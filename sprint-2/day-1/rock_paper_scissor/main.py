import random

options=["Rock","Paper","Scissors"]

move=True

personCount=0

systemCount=0

TieCount=0


while move:
    computer=random.choice(options)
    userMove=input("Enter your Move :- ")

    if userMove not in options:
        print("Enter valid Move ")
    else:
         if userMove==computer:
                print(f"Computer choice:- {computer}")
                print("Game Tie")
                TieCount+=1
                
         elif userMove=="Rock" and computer=="Scissors ":
               print(f"Computer choice:- {computer}")
               print("You won")
               personCount+=1


         elif userMove=="Paper" and computer=="Rock":
               print(f"Computer choice:- {computer}")
               print("You won")
               personCount+=1      
              


         elif userMove=="Scissors " and computer=="Paper":
               print(f"Computer choice:- {computer}")
               print("You won")
               personCount+=1  


         else:
             print(f"Computer choice:- {computer}")
             print("You Loose")
             systemCount+=1 



         print(f"UserMove-Points:- {personCount} Computer-Points:- {systemCount} Game-Ties:-{TieCount}") 


         exit=input("Do you want to Quit Enter (Y/N) :- ") 


         if(exit=="Y" or exit=="y" ) :
              move=False