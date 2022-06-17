#!/usr/bin/env python3


"""Let's Determine Your Pokemon Starter"""

import urllib.request
from PIL import Image
import time
import playsound
import winsound

# Sound effects upon selecting choices
winsound.PlaySound("C:\\Users\\etmo2\\Downloads\\open.wav", winsound.SND_ASYNC | winsound.SND_ALIAS)

# Total affinity points to determine Pokémon Starter.
affinity_total = 0

# Question pool
Questions = {"q1": "Do you wish to have wings and fly away? \na) I prefer the sea. \nb) No thanks I'll walk. \nc)"
                   " Yes, away we go! \nd) You don't need wings to fly. \n>",
             "q2": "Of the following, which is your ideal vacation destination? \na) Vermilion City \nb)"
                   " Cerulean City \nc) Cinnabar City \nd) Pallet Town \n>",
             "q3": "What's one thing you won't forget before you leave home? \na) My Pokédex. \nb)"
                   " PokePuffins. \nc) My Pokemon! \nd) The power of friendship. \n>",
             "q4": "Which Pokemon trainer do you relate to the most? \na) Gary \nb) May \nc) Red \nd) Ash \n>",
             "q5": "In your group of friends, you are the ... \na) friendly one. \nb) tough one. \nc)"
                   " shy one. \nd) adventurous one. \n>",
             "q6": "Why would you battle other Pokemon? \na) For the experience. \nb) To defend myself. \nc)"
                   " To be the strongest. \nd) To become the Pokemon Master! \n>"}

# Introduction, name, and location of character.
print("Hello! Welcome to the world of Pokémon!")
print()
time.sleep(1.9)

while True:
    answer = input("Are you ready to start your journey? \n>")

    if answer.lower() == "yes":
        print()
        print("Great! Before we begin.. \n")
        break
    elif answer.lower() == "no":
        answer = input("Do you wish to quit? \n>")
        if answer.lower() == "yes":
            print("But I thought you wanted to be the best there ever was? ")
            answer = input("Are you sure? \n>")
            if answer.lower() == "yes":
                print("Sorry, but you gotta catch them all!! Please try again.")
                input()
            else:
                print()
                print("Please try again.")
                print()
                continue
time.sleep(1.2)

while True:
    name = input("What is your name young pokemon master? \n>")
    if name.lower() != "":
        break
    else:
        continue
print()

while True:
    location = input("Where are you from? \n>")
    if location.lower() != "":
        break
    else:
        continue

print()
print(name, "from", location, "let's determine your starter pokemon! \n")
print()

# Questions with assigned values for each answer.
while True:

    q1_ans = input(Questions["q1"])
    if q1_ans.lower() == "a":
        affinity_total += 1
        break

    elif q1_ans.lower() == "b":
        affinity_total += 3
        break

    elif q1_ans.lower() == "c":
        affinity_total += 5
        break

    elif q1_ans.lower() == "d":
        affinity_total += 10
        break

    else:
        print()
        print("Please select an answer.")
        print()
        continue

playsound.playsound("C:\\Users\\etmo2\\Downloads\\Lvl.mp3")

while True:
    q2_ans = input(Questions["q2"])
    if q2_ans.lower() == "a":
        affinity_total += 1
        break
    elif q2_ans.lower() == "b":
        affinity_total += 3
        break
    elif q2_ans.lower() == "c":
        affinity_total += 5
        break
    elif q2_ans.lower() == "d":
        affinity_total += 10
        break
    else:
        print()
        print("Please select an answer.")
        print()
        continue

playsound.playsound("C:\\Users\\etmo2\\Downloads\\Lvl.mp3")

while True:

    q3_ans = input(Questions["q3"])
    if q3_ans.lower() == "a":
        affinity_total += 1
        break
    elif q3_ans.lower() == "b":
        affinity_total += 3
        break

    elif q3_ans.lower() == "c":
        affinity_total += 5
        break

    elif q3_ans.lower() == "d":
        affinity_total += 10
        break

    else:
        print()
        print("Please select an answer.")
        print()
        continue

playsound.playsound("C:\\Users\\etmo2\\Downloads\\Lvl.mp3")

while True:
    q4_ans = input(Questions["q4"])
    if q4_ans.lower() == "a":
        affinity_total += 1
        break

    elif q4_ans.lower() == "b":
        affinity_total += 3
        break

    elif q4_ans.lower() == "c":
        affinity_total += 5
        break
    elif q4_ans.lower() == "d":
        affinity_total += 10
        break

    else:
        print()
        print("Please select an answer.")
        print()
        continue

playsound.playsound("C:\\Users\\etmo2\\Downloads\\Lvl.mp3")

while True:

    q5_ans = input(Questions["q5"])

    if q5_ans.lower() == "a":
        affinity_total += 1
        break

    elif q5_ans.lower() == "b":
        affinity_total += 3
        break

    elif q5_ans.lower() == "c":
        affinity_total += 5
        break

    elif q5_ans.lower() == "d":
        affinity_total += 10
        break

    else:
        print()
        print("Please select an answer.")
        print()
        continue

playsound.playsound("C:\\Users\\etmo2\\Downloads\\Lvl.mp3")

while True:
    q6_ans = input(Questions["q6"])

    if q6_ans.lower() == "a":
        affinity_total += 1
        break

    elif q6_ans.lower() == "b":
        affinity_total += 3
        break

    elif q6_ans.lower() == "c":
        affinity_total += 5
        break

    elif q6_ans.lower() == "d":
        affinity_total += 10
        break

    else:
        print()
        print("Please select an answer.")
        print()
        continue

playsound.playsound("C:\\Users\\etmo2\\Downloads\\Lvl.mp3")

winsound.PlaySound(None, winsound.SND_ASYNC)

print()
winsound.PlaySound("C:\\Users\\etmo2\\Downloads\\Evo.wav", winsound.SND_ASYNC | winsound.SND_ALIAS)
print("calculating... \n>")
time.sleep(1.9)

print()
print("calculating... \n>")
time.sleep(1.7)

print("Complete!.. \n>")
time.sleep(1.5)

# Results possibilities
if affinity_total in range(1, 10):
    # Display user results
    print("Congratulations", name, "!!")
    print()
    time.sleep(1.5)
    print("Your starter pokemon is...")
    print()
    time.sleep(2.1)
    print("Squirtle!")
    # Retrieve Pokémon image from website
    urllib.request.urlretrieve('https://assets.pokemon.com/assets/cms2/img/pokedex/full/007.png', "Srt.png")
    img = Image.open("srt.png")
    img.show()
    winsound.PlaySound(None, winsound.SND_ASYNC)
    # Pokémon sound for Squirtle
    playsound.playsound("C:\\Users\\etmo2\\Downloads\\srtV.mp3")

elif affinity_total in range(10, 25):
    # Display user results
    print("Congratulations", name, "!!")
    print()
    time.sleep(1.5)
    print("Your starter pokemon is...")
    print()
    time.sleep(1.9)
    print("Bulbasaur!")
    # Retrieve Pokémon image from website
    urllib.request.urlretrieve('https://assets.pokemon.com/assets/cms2/img/pokedex/full/001.png', "Bul.png")
    img = Image.open("Bul.png")
    img.show()
    winsound.PlaySound(None, winsound.SND_ASYNC)
    # Pokémon sound for Bulbasaur
    playsound.playsound("C:\\Users\\etmo2\\Downloads\\bulV.mp3")

elif affinity_total in range(25, 46):
    # Display user results
    print("Congratulations", name, "!")
    print()
    time.sleep(1.5)
    print("Your starter pokemon is...")
    print()
    time.sleep(2.0)
    print("Charmander!")
    # retrieve Pokémon image from website
    urllib.request.urlretrieve('https://assets.pokemon.com/assets/cms2/img/pokedex/full/004.png', "Cha.png")
    img = Image.open("Cha.png")
    img.show()
    winsound.PlaySound(None, winsound.SND_ASYNC)
    # Pokémon sound for Charmander
    playsound.playsound("C:\\Users\\etmo2\\Downloads\\chaV.mp3")


elif affinity_total in range(46, 61):
    # Display user results
    print("Congratulations", name, "!!")
    print()
    time.sleep(1.5)
    print("It looks like...")
    print()
    time.sleep(2.0)
    print("Pikachu has chosen you!")
    # retrieve Pokémon image from website
    urllib.request.urlretrieve('https://assets.pokemon.com/assets/cms2/img/pokedex/full/025.png', "Pka.png")
    img = Image.open("Pka.png")
    img.show()
    winsound.PlaySound(None, winsound.SND_ASYNC)
    # Pokémon sound for Pikachu
    playsound.playsound("C:\\Users\\etmo2\\Downloads\\pkaV.mp3")

# ref of points total
print()
print("Total affinity points", affinity_total)
print("Done")

