def quick_sort(array, low, high):
    if low >= high:
        return

    first , last = low, high
    key = array[first]
    
    while first < last:
        while first < last and array[last] >= key:
            last = last - 1

        array[first] = array[last]
        
        while first < last and array[first] <= key:
            first = first + 1

        array[last] = array[first]

    array[first] = key
    
    quick_sort(array, low, first-1)
    quick_sort(array, first+1, high)

array = [5,4,3,2,1]
quick_sort(array, 0, 4)
print array
