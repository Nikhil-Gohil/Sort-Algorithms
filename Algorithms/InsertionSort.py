def InsertionSort(myarray):
    size = len(myarray)
    for i in range(1, size):
        current_element = myarray[i]
        for j in range(0, i-1):
            if current_element < myarray[j]:
                myarray.insert(j, current_element)
                del myarray[i]
                break
    return(myarray)        