def bubbleSort(array):
    for i in range(len(array), 0, -1):
        for j in (range(i-1)):
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]

    print array



array = [3,2,1,5,4]
bubbleSort(array)

