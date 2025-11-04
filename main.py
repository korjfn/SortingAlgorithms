def selection_sort(myarray):
    n = len(myarray)
    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            if myarray[j] < myarray[min_index]:
                min_index = j
        myarray[i], myarray[min_index] = myarray[min_index], myarray[i] 

def insertion_sort(myarray):
    n = len(myarray)
    for i in range(1, n):
        insertindex = i
        currentvalue = myarray[i]
        for j in range(i - 1, -1, -1):
            if myarray[j] > currentvalue:
                myarray[j + 1] = myarray[j]
                insertindex = j
            else:
                break
        myarray[insertindex] = currentvalue

def partition(array,low,high):
    pivot = array[high]
    i = low -1
    for j in range(low,high):
        if array [j] <= pivot:
            i += 1
            array[i], array[j] = array[j], array[i]
    array [i+1], array[high] = array [high], array[i+1]
    return i + 1

def quicksort_sort(array,low = 0, high = None):
    if high is None:
        high = len(array) -1

    if low < high:
        pivot_index = partition(array,low,high)
        quicksort_sort(array, low, pivot_index -1)
        quicksort_sort(array, pivot_index +1, high)

def merge(left,right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])

    return result


def mergesort_sort(arr):
    if len(arr) <= 1:
        return arr
    
    mid = len(arr) // 2
    lefthalf = arr[:mid]
    righthalf = arr[mid:]
    sortedleft = mergesort_sort(lefthalf)
    sortedright = mergesort_sort(righthalf)
    return merge(sortedleft,sortedright)

def bubblesort_sort(myarray):
    n = len(myarray)
    for i in range(n -1):
        for j in range(n -i -1):
            if myarray[j] > myarray[j+1]:
                myarray[j], myarray[j+1] = myarray[j+1], myarray[j]



n = int(input("how many elements are in the array? "))

myarray = []
print("input the elements in order: ")
for i in range(n):
    element = int(input())
    myarray.append(element)

print("Which sorting algorithm should I use: ( 1 for Selection sort, 2 for Insertion sort, 3 for QuickSort, 4 For mergesort, 5 for bubble sort,):")
c = int(input())

if c == 1:
    selection_sort(myarray)
    print("Sorted array using Selection sort:")
elif c == 2:
    insertion_sort(myarray)
    print("Sorted array using Insertion sort:")
elif c == 3:
    quicksort_sort(myarray)
    print("Sorted array using Quick sort:")
elif c == 4:
    mergesort_sort(myarray)
    print("Sorted array using Merge sort:")
    myarray = mergesort_sort(myarray)
elif c == 5:
    bubblesort_sort(myarray)
    print("Sorted array using Bubble sort:")


print(myarray)