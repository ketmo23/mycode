#!/usr/bin/env python3

#Intro
print("Hello! Welcome to the world of Pokemon! ")

input()

answer = input("Are you ready to start your journey? \n")

if answer.lower() == "yes":
    print("Great! Before we begin.. \n")
    name = input("What is your name? \n")
    print(name,"lets determine your starter pokemon! ")

elif answer.lower() == "no":
    answer = input("Do you wish to quit? \n")
    if answer.lower() == "yes":
        print("But I thought you wanted to be the best there ever was? ")
        answer = input("Are you sure? \n")
        if answer.lower() == "yes":
             print("But you must catch them all!! ")
             input()
             name = input("What is your name young pokemon master? \n")

input()
year = int(input("choose a year between 1996-2004 \n"))

#while year 
#gen1 
#gen2
#gen3
