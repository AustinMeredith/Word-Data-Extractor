import os

class Help:    #Help class declaration
        def HelpDisplay(self):
            if(HelpDisplay=="help"):    #if the input string is just help, display following message
                print("This is a Python-docx based program that will allow the user to specify a .docx formatted file, parse that file, and save the parsed XML information to a specific location. The follwing are help commands; help, help input, help parse, help outname, help outloc, and help exit")
            elif("help" in HelpDisplay):    #if it contains help and another string
                if(len(HelpDisplay.split())==2):    #then it outputs a message depending on that other string
                    if("outname" in HelpDisplay):    #if the second string is outname, display following message
                        print("This command will then allow the user to specify the name for the saved XML file. Typing outname will result in the program prompting the user to type in a specific, valid file name that the XML will be saved as.")
                    elif("outloc" in HelpDisplay):    #if the second string is outloc, display following message
                        print("This command will then allow the user to specify the location in which the XML will be saved. Typing outloc will result in the program prompting the user to type in a specific, valid folder location in their system for the XML to be saved within.")
                    elif("input" in HelpDisplay):    #if the second string is input, display following message
                        print("This command will then allow the user to specify the .docx file to be parsed. Typing input will result in the program prompting the user to enter a specific, valid filepath to the .docx file to be parsed.")
                    elif("parse" in HelpDisplay):    #if the second string is parse, display following message
                        print("This command will then parse the specified .docx file. Typing parse will result in the program running through its parse script, parsing the .docx file into its XML equivalent.")
                    elif("exit" in HelpDisplay):    #if the second string is exit, display following message
                        print("This command will then return the user to a previous menu, or stop the program.")
                    else:    #if the second string is not one of the valid second string options, print following error
                        print("Invalid command")
                else:    #if the first string is not a valid command, print following error
                    print("Invalid command")
            elif(HelpDisplay=="exit"):    #if the user inputs exit, exits program
                exit()
            else:    #if user input is not help, exit, or other commands, print following error
                print("Invalid command")
                


H=Help()    #Class variable with function loop to run
for i in range(10):
    HelpDisplay=input()
    H.HelpDisplay()
