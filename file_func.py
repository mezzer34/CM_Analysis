import os
import structs as st

import pickle

from dataclasses import dataclass


import functions as f


#Return the file names as selected by the user
def doGetFileNameSelectionFromUser(_MaxNumberOfFilesToSelect, _DirectoryPath):
    l_Directory_FileList = doReturnDirectoryFileList(_DirectoryPath)



    #generate a list of numbers for the files
    l_FileNumberList = []
    for num in range(len(l_Directory_FileList)):
        l_FileNumberList.append(str(num))
        
    #add a quit option to the file list
    l_FileNumberList.append("q")
    
    f.doClearConsole()
    doPrintFileList(_FileList=l_Directory_FileList)
    

    l_UserFileNumberList = getListOfFileNumbersFromUser(_MaxNumberOfFilesToLoad=_MaxNumberOfFilesToSelect,
                                                        _ValidFileNumbersList = l_FileNumberList)

    #generate a list of file names based on user input
    l_FileNameList = []
    for i in l_UserFileNumberList:
        l_FileNameList.append(l_Directory_FileList[i])
    
    return l_FileNameList






#get all files in directory
def doReturnDirectoryFileList(_DirectoryPath):
    l_FileList = []
    for r, d, f in os.walk(_DirectoryPath):
        for file in f:
            l_FileList.append(os.path.join(r, file))
    return l_FileList





def doPrintFileList(_FileList):
    # print file list on seperate lines
    for num in range(len(_FileList)):   
        # print line number
        print(str(num) + ": " + _FileList[num])
        
    print("q - Quit")
    
    
    
    
    
def doLoadDataFromSelectedFile(_FileToLoad):
    l_OpenedFile = open(_FileToLoad, "r")
    l_LoadedData = l_OpenedFile.readlines()
    return l_LoadedData
        


def getListOfFileNumbersFromUser(_MaxNumberOfFilesToLoad, _ValidFileNumbersList):
    l_UserSelectedFileNumbers = []

    #loop to get all user inputs
    while (len(l_UserSelectedFileNumbers) < _MaxNumberOfFilesToLoad):
        l_NewUserInput = f.getUserInput("Enter file number: ", _AllowBlank=False)

        if l_NewUserInput == "" and len(l_UserSelectedFileNumbers) > 0:
            print("All files selected")  
            break
        
        #quit clause
        elif l_NewUserInput == "q":
            break
        
        
        #Check if user input is in the list of valid files
        elif l_NewUserInput in _ValidFileNumbersList:
            l_UserSelectedFileNumbers.append(int(l_NewUserInput))
            print("File " + l_NewUserInput + " selected")
        
        
        else:
            print("Invalid file number")


    return l_UserSelectedFileNumbers


def doSaveModelToFile(_DataToStore, _FullFilepath):
    #encode data to file
    pickle.dump(_DataToStore, open(_FullFilepath, "wb"))
        
        
        
def doLoadModelFromFile(_FullFilepath):
    #load data from file
    with open(file=_FullFilepath, mode="rb") as f:
        return pickle.load(f)


