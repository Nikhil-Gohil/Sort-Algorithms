def BubbleSort(myarray):
    for i in range(0, len(myarray)):
        for j in range(0, len(myarray) - i - 1):
            if myarray[j] > myarray[j + 1]:
                myarray[j], myarray[j + 1] = myarray[j + 1], myarray[j]
    return myarray


def BubbleSortRecursive(myarray):
    for i, num in enumerate(myarray):
        try:
            if myarray[i + 1] < num:
                myarray[i] = myarray[i + 1]
                myarray[i + 1] = num
                BubbleSortRecursive(myarray)
        except IndexError:
            pass
    return myarray
