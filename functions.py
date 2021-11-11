#import numpy as np
import os


def getUserInput(_PrintString: str, _AllowBlank: bool):
    # get user input, check if blank
    while True:
        user_input = input(_PrintString)
        if user_input == '' and _AllowBlank == False:
            print("Please enter a value")
        else:
            return user_input




def doTrimLines(lines: list[str], front_trim: int, back_trim: int):
    # trim lines to remove first three lines
    lines = lines[front_trim:len(lines)-back_trim]
    return lines




def doFindMinInList(_Dataset: list[float]):
    #find the min in a list
    return min(_Dataset)

    
def doFindMinInListOfLists(_ListOfDataset: list[list[float]]):
    #find the min in a list of lists
    l_MinValueSubset = list[float]()
    for i in range(len(_ListOfDataset)):
        l_MinValueSubset.append(doFindMinInList(_ListOfDataset[i]))


    return min(l_MinValueSubset)





def doFindMaxInList(_Dataset: list[float]):
    #find the max in a list
    return max(_Dataset)


def doFindMaxInListOfLists(_ListOfDataset: list[list[float]]):
    #find the max in a list of lists
    l_MaxValueSublist = list[float]()
    for i in range(len(_ListOfDataset)):
        l_MaxValueSublist.append(doFindMaxInList(_ListOfDataset[i]))


    return max(l_MaxValueSublist)




def doFindMeanInList(_Dataset: list[float]):
    #find the mean in a list
    return sum(_Dataset)/len(_Dataset)


def doFindStandDevInList(_Dataset: list[float]):
    #find the standard deviation in a list
    #return np.std(a=_Dataset,
    #              ddof=1)
    return 0




def doClearConsole():
    command = 'clear'
    if os.name in ('nt', 'dos'):  # If Machine is running on Windows, use cls
        command = 'cls'
    os.system(command)
    
    
    
def getCurrentSystemDateTime():
    #now = datetime.now()
    #eturn now.strftime("%H:%M:%S")
    return "yeehaw"




def getDifferenceBetweenValues(_Value1: float, _Value2: float):
    return abs(_Value1 - _Value2)



def getPrcntDifferenceBetweenValues(_Value1: float, _Value2: float):
    #find the percentage difference between two values, check for divide by zero
    if _Value1 == 0:
        return 0
    else:
        return abs((_Value1 - _Value2)/_Value1)    
    
    
    
def doGetNumberOfFixedLength(_Number: float, _Digits_BeforeDecimal: int, _Digits_AfterDecimal: int):
    
    #round the number down if needed
    l_RoundedNumber = round(_Number, _Digits_AfterDecimal)
    
    #get number as a string
    l_StringNumber = str(l_RoundedNumber)
    
    
    #Pad zeros to the left of the decimal point
    l_StringNumber = l_StringNumber.rjust(_Digits_BeforeDecimal + _Digits_AfterDecimal + 1, '0')
    
    #Pad zeros to the right of the decimal point
    l_StringNumber = l_StringNumber.ljust(_Digits_BeforeDecimal + _Digits_AfterDecimal + 1, '0')
    
    
    return l_StringNumber
    
    