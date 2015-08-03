def insertSort(array):
    for i in range(1, len(array)):
        key = array[i]
        j = i
        while (j >0 and key < array[j-1]):
            array[j] = array[j-1]
            j = j - 1

        array[j] = key

    print array


a = [13,4,5,5,6,7,8,3]
insertSort(a)
