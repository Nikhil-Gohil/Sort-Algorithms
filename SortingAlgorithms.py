from SelectionSort import SelectionSort
from BubbleSort import BubbleSort
import numpy as np
import time
def testSelectionSort(myarray):
    start_time = time.time()
    SelectionSort(myarray)
    print("SelectionSort took {:.5f} to complete!".format(time.time()-start_time))

def testBubbleSort(myarray):
    start_time = time.time()
    BubbleSort(myarray)
    print("BubbleSort took {:.5f} to complete!".format(time.time()-start_time))

def main():
    array = np.random.randint(-100000, 100000, 10000)
    testSelectionSort(array)
    testBubbleSort(array)

if __name__ == "__main__":
    main()