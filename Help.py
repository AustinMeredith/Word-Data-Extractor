import os

class Help:    #Help class declaration
        print("You are now in the help menu, please type help for more information")
        def HelpDisplay(self,HelpList):
            if(HelpList=="help"):    #if the input is just help, display following message
                print("This is a Python-docx based program that will allow the user to specify a .docx formatted file, parse that file, and save the parsed XML information to a specific location. Invalid entries will result in error. If you need help with a specific command, please type help followed by the command name, i.e. help input.")
            elif("help" in HelpList):    #if it contains help and another word
                if(len(HelpList.split())==2):    #then it outputs a message depending on that other word
                    if("outname" in HelpList):    #if the second word contains outname, display following message
                        print("This command will then allow the user to specify the name for the saved XML file. Typing outname will result in the program prompting the user to type in a specific, valid file name that the XML will be saved as.")
                    elif("outloc" in HelpList):    #if the second word contains outloc, display following message
                        print("This command will then allow the user to specify the location in which the XML will be saved. Typing outloc will result in the program prompting the user to type in a specific, valid folder location in their system for the XML to be saved within.")
                    elif("input" in HelpList):    #if the second word contains input, display following message
                        print("This command will then allow the user to specify the .docx file to be parsed. Typing input will result in the program prompting the user to enter a specific, valid filepath to the .docx file to be parsed.")
                    elif("parse" in HelpList):    #if the second word contains parse, display following message
                        print("This command will then parse the specified .docx file. Typing parse will result in the program running through its parse script, parsing the .docx file into its XML equivalent.")
                    elif("exit" in HelpList):    #if the second word contains exit, display following message
                        print("This command will then return the user to a previous menu, or stop the program.")
                    else:    #if the second word is not one of the valid help commands, print following error
                        print("Invalid command")
                else:    #if the first word is not a valid command, print following error
                    print("Invalid command")
            elif(HelpList=="exit"):    #if the user inputs exit, exits program
                exit()
            else:    #if user input is not help, exit, or other commands, print following error
                print("Invalid command")
                


H=Help()    #Class variable with function loop
for i in range(5):
    HelpList=input("User Input: ")
    H.HelpDisplay(HelpList)
    print("-------- \nYou are in the help menu \n--------")