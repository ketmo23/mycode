#!/usr/bin/env python3

#total affinity for pokemon type 
affinity_total = 0

#Introduction name and location of character 
print("Hello! Welcome to the world of Pokemon! ")

input()

answer = input("Are you ready to start your journey? \n>")

if answer.lower() == "yes":
    print("Great! Before we begin.. \n")
    name = input("What is your name? \n>")

elif answer.lower() == "no":
    answer = input("Do you wish to quit? \n>")
    if answer.lower() == "yes":
        print("But I thought you wanted to be the best there ever was? ")
        answer = input("Are you sure? \n>")
        if answer.lower() == "yes":
             print("But you must catch them all!! ")
            
             name = input("What is your name young pokemon master? \n")

input()
location = input("Where are you from? \n>")
input()
print(name,"lets determine your starter pokemon! ") 

while true:
    q1_ans = input("Do you wish to have wings and fly away? \na) Yes away we go!, \b) No thanks i'll walk, \nc) You dont need wings to fly. \n>"

            if q1_ans.lower() == "a":
                
                affinity_total = + 3
                break
            
            elif q1_ans.lower() == "b":
                
                affinity_total = + 1
                break
            
            elif q1_ans.lower() == "c":
                
                affinity_total = + 10
                break
            else :
                input()
                print("Please select an answer.")
                input()
                continue





