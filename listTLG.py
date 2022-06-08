#!/usr/bin/env python3

wordbank= ["four", "spaces"]

#list of students name.
tlgstudents= ["Aaron", "Casey", "Donny", "Emmanuel", "Eric", "Jaelen", "James", "Jay", "John", "Ken", "Maurice", "Mike", "Ryan", "Shamain", "Tuang", "Tyler", "Zhenqian", "Travis"]

#dispay a range of numbers to choose from.
numselection= int(input("Chose a number between 0 and 17. \n"))

#Use the number selected to chose a name from the TlG list.
student_name= tlgstudents[numselection]

#display the information you have selcted.
print(student_name + " always uses " + wordbank[0], wordbank[1] + " to indent.")





