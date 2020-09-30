from Algorithms.SelectionSort import SelectionSort
from Algorithms.BubbleSort import BubbleSort
from Algorithms.InsertionSort import InsertionSort
import numpy as np
import time
import pprint
pp = pprint.PrettyPrinter(indent=4)

def testSelectionSort(myarray):
    start_time = time.time()
    SelectionSort(myarray)
    #pp.pprint(sorted)
    print("SelectionSort took {:.5f} to complete!".format(time.time()-start_time))

def testBubbleSort(myarray):
    start_time = time.time()
    BubbleSort(myarray)
    #pp.pprint(sorted)
    print("BubbleSort took {:.5f} to complete!".format(time.time()-start_time))

def testInsertionSort(myarray):
    start_time = time.time()
    InsertionSort(myarray)
    #pp.pprint(sorted)
    print("InsertionSort took {:.5f} to complete!".format(time.time()-start_time))

def main():
    array = np.random.randint(0, 100000, 20)
    testSelectionSort(array)
    testBubbleSort(array)
    testInsertionSort(array)


if __name__ == "__main__":
    main()
