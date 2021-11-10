import numpy as np
import os

from datetime import datetime



def getUserInput(_PrintString, _AllowBlank):
    # get user input, check if blank
    while True:
        user_input = input(_PrintString)
        if user_input == '' and _AllowBlank == False:
            print("Please enter a value")
        else:
            return user_input



def doPrintStructure(_Dataset):
    #print struct in a nice format
    for x in _Dataset:
        print(x)

    print("\n")
    print("\n")






def doTrimLines(lines, front_trim, back_trim):
    # trim lines to remove first three lines
    lines = lines[front_trim:len(lines)-back_trim]
    return lines




def doFindMinInList(_Dataset):
    #find the min in a list
    return min(_Dataset)

    
def doFindMinInListOfLists(list_of_lists):
    #find the min in a list of lists
    min_value = []
    for i in range(len(list_of_lists)):
        min_value.append(doFindMinInList(list_of_lists[i]))


    return min(min_value)





def doFindMaxInList(_Dataset):
    #find the max in a list
    return max(_Dataset)


def doFindMaxInListOfLists(list_of_lists):
    #find the max in a list of lists
    max_value = []
    for i in range(len(list_of_lists)):
        max_value.append(doFindMaxInList(list_of_lists[i]))


    return max(max_value)




def doFindMeanInList(_Dataset):
    #find the mean in a list
    return sum(_Dataset)/len(_Dataset)


def doFindStandDevInList(_Dataset):
    #find the standard deviation in a list
    return np.std(_Dataset)





def doClearConsole():
    command = 'clear'
    if os.name in ('nt', 'dos'):  # If Machine is running on Windows, use cls
        command = 'cls'
    os.system(command)
    
    
    
def getCurrentSystemDateTime():
    #now = datetime.now()
    #eturn now.strftime("%H:%M:%S")
    return "yeehaw"




def getDifferenceBetweenValues(_Value1, _Value2):
    return abs(_Value1 - _Value2)



def getPrcntDifferenceBetweenValues(_Value1, _Value2):
    #find the percentage difference between two values, check for divide by zero
    if _Value1 == 0:
        return 0
    else:
        return abs((_Value1 - _Value2)/_Value1)    
    