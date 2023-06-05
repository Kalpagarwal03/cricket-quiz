print ("Welcome to my quiz!")
playing = input("do you want to play ? ")

if playing.lower() == "no":
    print("see you soon!")
    quit()

elif playing.lower() == "yes":
    print ("Okay!Leta play a game of cricket! :) ") 
    Score = 0 


answer = input(" What does LBW stand for? ").lower()
if answer.lower() == "leg before wicket":
    print("Correct")
    Score +=1
else:
    print("Incorrect!")

answer = input("What if batsmen hits the ball in air and fielder catches it ? ")
if answer.lower() == "out":
    print("Correct")
    Score +=1
else:
    print("Incorrect!")

answer = input(" What if batsmen hits the ball in air and it goes beyond boundry? ")
if answer.lower() == "six":
    print("Correct")
    Score +=1
else:
    print("Incorrect!")

answer = input(" How many overs are there in one day match? ")
if answer == "50":
    print("Correct")
    Score +=1
else:
    print("Incorrect!")

print("You got "  +  str(Score)  +  " questions correct!" )
print("You got "  +  str((Score / 4) * 100 )  +  "%" )


