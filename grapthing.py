

def doPlotData(data_List):
    
    fig = plt.figure()
    
    for individual_data in data_List:

        #cast the data to a numpy array
        Time = individual_data[0]
        Data = individual_data[1]
        Data1 = individual_data[2]
        Data2 = individual_data[3]

        
        #find max and mins
        X_max = max(Time)
        X_min = min(Time)

        
        
        #create list from data
        plot_data = [Data, Data1, Data2]



        Y_max = doFindMaxInListOfLists(list_of_lists=plot_data)
        Y_min = doFindMinInListOfLists(list_of_lists=plot_data)


        #add an allowance onto the max and min
        Y_range_Upper = Y_max + (Y_max * 0.1)
        Y_range_Lower = Y_min - (Y_min * 0.1)


        


        #sns.displot(plot_data, palette="tab10")
        


        #plot the max and mins for the three vibration datasets
      #  plt.axhline(y=Y_max, color='r', linestyle='-')
       # plt.axhline(y=Y_min, color='r', linestyle='-')

        

        
       # plt.ylim(bottom=Y_range_Lower, top=Y_range_Upper)
       # plt.xlim(left=X_min, right=X_max)

    
    
    plt.show()





def doLineplot(data):    
    sns.lineplot(data=data, palette="tab10")
    
    
def doScatterplot(data):
    sns.scatterplot(data=data, palette="tab10")
    