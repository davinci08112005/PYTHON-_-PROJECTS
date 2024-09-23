import random 

print ("********welcome to rock paper scissor game *********")
print (" ********test your skill ******")
print("***get ready ****")

options = ("rock","paper" , "scissors")
user_score = 0 
computer_score = 0
 
while True : 
     user_choice  = input("enter a choice (rock or paper or scissors): ").lower()
     if user_choice not in options:
        print("invalid choice. please enter a valid choice :\n ")
     else:
        computer_choice = random.choice(options)
        print(f"your choice : {user_choice}")
        print(f"computer choice : { computer_choice}")
        if user_choice==computer_choice :
           print("its a tie ")
        elif( user_choice == "rock" and computer_choice == "scissors"):
           print("you win")
           user_score +=1
        elif( user_choice == "scissors" and computer_choice == "paper"):
           print("you win")
           user_score +=1
        elif( user_choice == "paper" and computer_choice == "rock"):
           print("you win")
           user_score +=1         
        else:
           print("you lose")
           computer_score += 1 
        print("user_score :",user_score) 
        print("computer_score : ", computer_score)

        play_again = input("\n do you want to play again ? (yes/no): ").lower()
        if play_again != 'yes': 
           break

print("\final score are : ")
print("user_score :",user_score) 
print("computer_score : ", computer_score)

print("*** THANKS FOR PLAYING ***")
       
