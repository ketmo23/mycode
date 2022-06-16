#!/usr/bin/env python3

#total affinity for pokemon type 
affinity_total = 0

#Introduction name and location of character 
print("Hello! Welcome to the world of Pokemon! ")

input()

answer = input("Are you ready to start your journey? \n>")

if answer.lower() == "yes":
        print()
        print("Great! Before we begin.. \n")
        name = input("What is your name? \n>")

elif answer.lower() == "no":
        answer = input("Do you wish to quit? \n>")
        if answer.lower() == "yes":
            print("But I thought you wanted to be the best there ever was? ")
            answer = input("Are you sure? \n>")
            if answer.lower() == "yes":
                print("But you must catch them all!! ")
                input()
                name = input("What is your name young pokemon master? \n>")

print()
location = input("Where are you from? \n>")
print()
print(name,"from", location, "lets determine your starter pokemon! \n") 
print()

#questions to determine pokemon
while True:
    
    q1_ans = input("Do you wish to have wings and fly away? \na) I prefer the sea. \nb) No thanks I'll walk. \nc) Yes, away we go! \nd) You dont need wings to fly. \n>")

    if q1_ans.lower() == "a":
      affinity_total = + 1
      break    
    
    elif q1_ans.lower() == "b":
      affinity_total = + 3
      break
            
    elif q1_ans.lower() == "c":
      affinity_total = + 5
      break
   
    elif q1_ans.lower() == "d":
      affinity_total = + 10
      break  

    else:
      print()
      print("Please select an answer.")
      print()
      continue

while True:
    q2_ans = input("Of the following, which is your ideal vacation destination? \na) Vermilion City \nb) Cerulean City \nc) Cinnabar City \nd) Pallet Town \n>")
    if q2_ans.lower() == "a":
      affinity_total = + 1
      break
    elif q2_ans.lower() == "b":
      affinity_total = + 3
      break
    elif q2_ans.lower() == "c":
      affinity_total = + 5
      break
    elif q2_ans.lower() == "d":
      affinity_total = + 10
      break
    else:
      print()
      print("Please select an answer.")
      print()
      continue


while True:

    q3_ans = input("What's one thing you won't forget before you leave home? \na) My Pokedex. \nb) PokePuffins. \nc) My Pokemons! \nd) The power of friendship. \n>")
    if q3_ans.lower() == "a":
      affinity_total = + 1
      break
    elif q3_ans.lower() == "b":
      affinity_total = + 3
      break

    elif q3_ans.lower() == "c":
      affinity_total = + 5
      break

    elif q3_ans.lower() == "d":
      affinity_total = + 5
      break
    
    else:
      print()
      print("Please select an answer.")
      print()
      continue


while True:
    q4_ans = input("Which Pokemon trainer do you relate to the most? \na) Gary \nb) May \nc) Red \nd) Ash \n>")
    if q4_ans.lower() == "a":
      affinity_total = + 1
      break

    elif q4_ans.lower() == "b":
      affinity_total = + 3
      break

    elif q4_ans.lower() == "c":
      affinity_total = + 5
      break
    elif q4_ans.lower() == "d":
      affinity_total = + 10
      break  
   
    else:
      print()
      print("Please select an answer.")
      print()
      continue


while True:

    q5_ans = input("In your group of friends, you are the ... \na) friendly one. \nb) tough one. \nc) shy one. \nd)adventurous one. \n>")

    if q5_ans.lower() == "a":
      affinity_total = + 3
      break

    elif q5_ans.lower() == "b":
      affinity_total = + 1
      break

    elif q5_ans.lower() == "c":
      affinity_total = + 5
      break

    elif q5_ans.lower() == "d":
      affinity_total = + 10
      break
    
    else:
      print()
      print("Please select an answer.")
      print()
      continue


while True:
    q6_ans = input("Why would you battle other Pokemon? \na) For the experince. \nb) To defend myself. \nc) To be the strongest. \nd) To become the Pokemon Master! \n>")

    if q6_ans.lower() == "a":
      affinity_total = + 3
      break

    elif q6_ans.lower() == "b":
      affinity_total = + 1
      break

    elif q6_ans.lower() == "c":
      affinity_total = + 5
      break
    
    elif q6_ans.lower() == "d":
      affinity_total = + 10
      break

    else:
      print()
      print("Please select an answer.")
      print()
      continue

print()
print("caluculating... \n>")
print()
input()

print()
print("caluculating... \n>")
print()
input()

print("Complete!.. \n>")
input()

#Possiblities from results 
if affinity_total in range(1,8): 
    print("You are",name,"from",location,", who left home to become the next Pokemon Master! \n>")
    input()
    print("Congratulations!! Your starter is Squirtl!")
#Display pokedex data for Squirlt.

elif affinity_total in range(9,16):
    print("You are",name,"from",location,", who left home to become the next Pokemon Master! \n>")
    input()
    print("Congratulations!! Your starter is Bulbasaur!")
#Display pokedex data for Bulbasur.


elif affinity_total in range (17,30):
    print("You are",name,"from",location,", who left home to become the next Pokemon Master! \n>")
    input()
    print("Congratulations!! Your starter is Charmander!")
#Display pokedex data for Charmander.
    

elif affinity_total in range (31,50):
    print("You are",name,"from",location,", who left home to become the next Pokemon Master! \n>")
    input()
    print("Congratulations!! Pikachu has chosen you!")
#Display pokedex data for Pikachu.



#ref of points total
print()
print(affinity_total)

