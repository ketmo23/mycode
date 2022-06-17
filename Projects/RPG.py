#!/usr/bin/env python3

def showInstructions():
  #print a main menu and the commands
  print('''
RPG Game
========
Commands:
  go [direction]
  get [item]

''')

def showStatus():
  #print the player's current status
  print('---------------------------')
  print('You are in the ' + currentRoom)
  #print the current inventory
  print('Inventory : ' + str(inventory))
  #print an item if there is one
  if "item" in rooms[currentRoom]:
    print('You see a ' + rooms[currentRoom]['item'])
  print("---------------------------")

#an inventory, which is initially empty
inventory = []

#a dictionary linking a room to other rooms
## A dictionary linking a room to other rooms
rooms = {

            'Hall' : {
                  'south' : 'Kitchen',
                  'east'  : 'Dining Room',
                  'item'  : 'key'
                },

            'Kitchen' : {
                  'north' : 'Hall',
                  'item'  : 'monster',
                },
            'Dining Room' : {
                  'west' : 'Hall',
                  'south': 'Garden',
                  'item' : 'potion',
                  'north' : 'Pantry',
                },
            'Garden' : {
                  'north' : 'Dining Room',
                  'south' : 'Cave',
               },
            'Pantry' : {
                  'south' : 'Dining Room',
                  'item' : 'cookie',
                 },
              'Cave' : {
                  'north' : 'Garden',
                  'south' : 'Swamp',
                  'item'  : 'old troll',
                  },
              'Swamp': {
                  'north' : 'Cave',
                  'item'  : 'rust nugget', # get Gold Nugget --> get gold nugget

            },
         }

#start the player in the Hall
currentRoom = 'Hall'

showInstructions()

#loop forever
while True:

  showStatus()

  #get the player's next 'move'
  #.split() breaks it up into an list array
  #eg typing 'go east' would give the list:
  #['go','east']
  move = ''
  while move == '':
    move = input('>')

  # split allows an items to have a space on them
  # get golden key is returned ["get", "golden key"]
  move = move.lower().split(" ", 1)
  #if they type 'go' first
  if move[0] == 'go':
    #check that they are allowed wherever they want to go
    if move[1] in rooms[currentRoom]:
      #set the current room to the new room
      currentRoom = rooms[currentRoom][move[1]]
    #there is no door (link) to the new room
    else:
        print('You can\'t go that way!')

  #if they type 'get' first
  if move[0] == 'get' :
    #if the room contains an item, and the item is the one they want to get
    if "item" in rooms[currentRoom] and move[1] in rooms[currentRoom]['item']:
      #add the item to their inventory
      inventory += [move[1]]
      #display a helpful message
      print(move[1] + ' got!')
      #delete the item from the room
      del rooms[currentRoom]['item']
    #otherwise, if the item isn't there to get
    else:
      #tell them they can't get it
      print('Can\'t get ' + move[1] + '!')

  ## Define how a player can win
  if currentRoom == 'Garden' and 'key' in inventory and 'potion' in inventory:
    print('You escaped the house with the ultra rare key and magic potion... YOU WIN!')
    break
 ## SECRET WIN CONDITION 
  if currentRoom == 'Cave' and 'rust nugget' in inventory and 'old troll' in inventory:
     print("You have found the Troll who's been lost for ages.")
     print()
     print("He sees your rusty nugget and tells you it's actually an  ancient relic...")
     print()
     print("The Golden Nugget of Awe!")
     print()
     print("You and the Troll  quickly escape the cave beneath the house and quickly!")
     print()
     print("sell your Nugget and enjoy your new found riches till the end of time.....Excellent Victory!!")
     break

  ## If a player enters a room with a monster
  elif 'item' in rooms[currentRoom] and 'monster' in rooms[currentRoom]['item']:
    print('A monster has got you... GAME OVER!')
    break
