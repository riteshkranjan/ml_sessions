
import datetime

def sort_system(a):
    startTime = datetime.datetime.now()
    a.sort()
    return datetime.datetime.now() - startTime

def swap(a,i,j):
    t = a[i]
    a[i] = a[j]
    a[j] = t
    
def q_sort_list(a):
    startTime = datetime.datetime.now()
    q_sort(a,0,len(a)-1)
    return datetime.datetime.now() - startTime

def q_sort(a,L,R):
    if R<=L:
        return
    last = L
    for i in range(L+1,R+1):
        if a[i] < a[L]:
            swap(a,i,++last)
    swap(a,L,last)
    q_sort(a,L,last-1)
    q_sort(a,last+1,R)

RUN = 32 
def insertionSort(arr, left, right):  
    for i in range(left + 1, right+1):  
        temp = arr[i]  
        j = i - 1 
        while arr[j] > temp and j >= left:  
            arr[j+1] = arr[j]  
            j -= 1
        arr[j+1] = temp  
        
def merge(arr, l, m, r): 
    len1, len2 =  m - l + 1, r - m  
    left, right = [], []  
    for i in range(0, len1):  
        left.append(arr[l + i])  
    for i in range(0, len2):  
        right.append(arr[m + 1 + i])  
    i, j, k = 0, 0, l 
    while i < len1 and j < len2:  
        if left[i] <= right[j]:  
            arr[k] = left[i]  
            i += 1 
        else: 
            arr[k] = right[j]  
            j += 1 
        k += 1
    while i < len1:  
        arr[k] = left[i]  
        k += 1 
        i += 1
    while j < len2:  
        arr[k] = right[j]  
        k += 1
        j += 1
        
def timSort(arr, n):  
    startTime = datetime.datetime.now()
    for i in range(0, n, RUN):  
        insertionSort(arr, i, min((i+31), (n-1)))  
    size = RUN 
    while size < n:  
        for left in range(0, n, 2*size):  
            mid = left + size - 1 
            right = min((left + 2*size - 1), (n-1))  
            merge(arr, left, mid, right)  
        size = 2*size 
    return datetime.datetime.now() - startTime

if __name__ == "__main__":
    import random
    size = int(input("enter sample size : "))
    a = [random.randint(1,10000) for x in range(size)]

    test_list1 = a.copy()
    time_to_run1 = sort_system(test_list1)

    test_list2 = a.copy()
    time_to_run2 = q_sort_list(test_list2)

    test_list3 = a.copy()
    time_to_run3 = timSort(test_list3, len(test_list3))

    if test_list1 == test_list2: 
        print("The lists are identical") 
    else : 
        print("The lists are not identical") 
    print("time to run system sort is {} while my quick sort is {}".format(time_to_run1,time_to_run2))
    if time_to_run2 > time_to_run1:
        print("system sort is faster by {}".format(time_to_run2-time_to_run1))
    else:
        print("system sort is slower by {}".format(time_to_run1-time_to_run2))


    if test_list1 == test_list3: 
        print("The lists are identical") 
    else : 
        print("The lists are not identical") 
    print("time to run system sort is {} while my tim sort is {}".format(time_to_run1,time_to_run3))
    if time_to_run3 > time_to_run1:
        print("system sort is faster by {}".format(time_to_run3-time_to_run1))
    else:
        print("system sort is slower by {}".format(time_to_run1-time_to_run3))

