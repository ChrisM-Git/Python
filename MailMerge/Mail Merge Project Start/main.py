#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp
import os

path = "./Input/Names/invited_names.txt"
names = open(path,"r")
nameslist = []

for name in names:
    nameslist.append(name.strip())

letterpath = "./Input/Letters/starting_letter.txt"

with open(letterpath) as letters:
    lettercontent = letters.read()
    for names in nameslist:
        newletter = lettercontent.replace("[name]",names)
        with open(f"./Output/ReadyToSend/Letter for {names}.txt","w") as completed_letter:
            completed_letter.write(newletter)

        

