def BubbleSort(myarray):
    for i in range(0, len(myarray)):
       for j in range(0, len(myarray)-i-1):
        if  myarray[j] > myarray[j+1]:
            myarray[j], myarray[j+1] = myarray[j+1], myarray[j]
    return(myarray)