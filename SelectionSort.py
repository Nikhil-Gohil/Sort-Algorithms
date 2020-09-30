def SelectionSort(myarray):
    for i in range(0, len(myarray)):
        min_index = i
        for j in range(i+1, len(myarray)):
            if myarray[j] < myarray[min_index]:
                min_index = j
        intermediate = myarray[i]
        myarray[i] = myarray[min_index]
        myarray[min_index] = intermediate
    return(myarray)

def main():
    myarray = [12, 2, 36, 45, 1, 8, 198, 64]
    print(SelectionSort(myarray))

if __name__ == "__main__":
    main()