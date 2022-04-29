#This File was committed by Austin Meredith
import os

class Help:    #Help class declaration




        def HelpDisplay(self):
                helpExit= False
                while helpExit!=True:
                    
                    HelpDisplay=input(">>>")
                    if(HelpDisplay=="help"):    #if the input is just help, display following message
                        print("This is a Python-docx based program that will allow the user to specify a .docx formatted file, parse that file, and save the parsed XML information to a specific location. The follwing are help commands; help, help input, help parse, help outname, help outloc, and help exit")
                    elif("help" in HelpDisplay):    #if it contains help and another word
                        if(len(HelpDisplay.split())==2):    #then it outputs a message depending on that other word
                            if("outname" in HelpDisplay):    #if the second word contains outname, display following message
                                print("This command will then allow the user to specify the name for the saved XML file. Typing outname will result in the program prompting the user to type in a specific, valid file name that the XML will be saved as.")
                            elif("outloc" in HelpDisplay):    #if the second word contains outloc, display following message
                                print("This command will then allow the user to specify the location in which the XML will be saved. Typing outloc will result in the program prompting the user to type in a specific, valid folder location in their system for the XML to be saved within.")
                            elif("input" in HelpDisplay):    #if the second word contains input, display following message
                                print("This command will then allow the user to specify the .docx file to be parsed. Typing input will result in the program prompting the user to enter a specific, valid filepath to the .docx file to be parsed.")
                            elif("parse" in HelpDisplay):    #if the second word contains parse, display following message
                                print("This command will then parse the specified .docx file. Typing parse will result in the program prompting you for details about procedures in the .docx file to be parsed and then running through its parse script, parsing the .docx file into its XML equivalent.")
                            elif("exit" in HelpDisplay):    #if the second word contains exit, display following message
                                print("This command will then return the user to a previous menu, or stop the program.")
                            elif("view" in HelpDisplay):    #if the second word contains exit, display following message
                                print("This command will print the entire word document as a 4-dimenstional array.")
                            elif("patterns" in HelpDisplay):    #if the second word contains exit, display following message
                                print("This command allows the user to enter the patterns used for procedure parsing. See the \"Difficulty Extracting Procedures\" section of the User Guide.")
                            else:    #if the second word is not one of the valid help commands, print following error
                                print("Invalid command")
                        else:    #if the first word is not a valid command, print following error
                            print("Invalid command")
                    elif(HelpDisplay=="exit"):    #if the user inputs exit, exits program
                         helpExit=True
                    else:    #if user input is not help, exit, or other commands, print following error
                        print("Invalid command")
                


