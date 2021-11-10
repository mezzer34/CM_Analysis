import os
from dataclasses import dataclass

import sys
sys.setrecursionlimit(2000)

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

import file_func as file_func
import functions as f
import grapthing as grapth
import dataprocessing as processing

import structs as st       
    
    
    
    
def main():    
    
    #loop and get user options until they quit    
    l_ValidUserOptions = ["1", "2", "9", "q"]
    
    l_MasterModel = st.Model()
    
    while True:
        f.doClearConsole()
        
        
        doPrintCurrentStatus(_CurrentModel=l_MasterModel)
        doPrintUserModeOptions()
        l_OperatingMode_UserSelection = getUserOperatingMode(l_ValidUserOptions)
        
        

        if l_OperatingMode_UserSelection == "1":
            print("Loading existing model...")
            
            l_MasterModel = doOperatingMode_LoadExistingModel()

        elif l_OperatingMode_UserSelection == "2":
            print("Loading from CSV to compare against existing model...")
            
            doOperatingMode_CheckAgainstModel(_ComparrisonDataset=l_MasterModel)

        elif l_OperatingMode_UserSelection == "9":
            print("Loading from CSV and generating reference Model...") 
            
            l_MasterModel = doOperatingMode_LearnDataset()
            
        elif l_OperatingMode_UserSelection == "q":
            print("Exiting")
            print("")
            
            exit()





def doOperatingMode_LoadExistingModel():
    #Let user select which dataset to load
    l_UserFileNameSelection = file_func.doGetFileNameSelectionFromUser(_MaxNumberOfFilesToSelect=1, 
                                                                       _DirectoryPath="./LearnedData/")
    
    
    #Load the model from file
    l_LoadedModel = file_func.doLoadModelFromFile(_FullFilepath=l_UserFileNameSelection[0])
    
    return l_LoadedModel
    




def doOperatingMode_CheckAgainstModel(_ComparrisonDataset):    
    l_Model = processing.doLoadFromCSVAndConvertToModel(_DirectoryPath="./data/")
    
    
    
    # Compare the user loaded models with the master model
    l_DifferentialModels = []
    for l_ModelToCheck in l_Model:
        l_DifferentialModels.append(processing.doCreateComparrisonBetweenTwoModels(_MasterModel=_ComparrisonDataset,
                                                                                    _OtherModel= l_ModelToCheck)) 


    #print the results
    for l_Result in l_DifferentialModels:
        print(l_Result)
        

    x = input("Press enter to continue")



def doOperatingMode_LearnDataset():   
    l_NewModel = processing.doLoadFromCSVAndConvertToModel(_DirectoryPath="./data/")
    
    l_NewModel = l_NewModel[0]
    
    #get new dataset name
    l_NewName = f.getUserInput("Enter new dataset name: ", _AllowBlank=False)
    
    
    #set the name of the model
    l_NewModel.Name = l_NewName



    #save the new model to file
    file_func.doSaveModelToFile(_DataToStore=l_NewModel, 
                                _FullFilepath= "./LearnedData/" + l_NewName)


    
    return l_NewModel










def getUserOperatingMode(valid_options):
    # loop to get user input
    while True:

        User_input = f.getUserInput("Enter selection: ", _AllowBlank=True)

        #check if the user input is valid
        if User_input in valid_options:
            return User_input
        
        else:
            print("Invalid input. Please try again.")



def doPrintCurrentStatus(_CurrentModel):
    
    l_Model = _CurrentModel
    
    
    #if there is data in the current model display it, otherwise display warning    
    if len(l_Model.Name) > 0:
        print("Current model:   " + _CurrentModel.Name)
        print("Model date:      " + _CurrentModel.OriginDate)
        
    else:
        print("No model loaded")
    
    
    print("Waiting for user input")
    print("\n")


def doPrintUserModeOptions():
    print("Select operating mode")
    print("1 - Load existing model")
    print("2 - Load data from file and check against model")
    print("9 - Load data from file to learn model")
    print("q - Quit")
    print("")






if __name__ == "__main__":
    main()
