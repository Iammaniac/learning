#the problem is that i have an array of numbers sorted in the ascneding or descending order and i want to find the position of some particular number in the array using binary search algorithm
#first find out if array is ascending or descending
def asc_des(arr):
    if len(arr) == 0:
        return "empty"
    elif len(arr) > 1:
        if arr[0] > arr[1]:
            return "descending"
        else:
            return "ascending"
    else:
        return "array has single element"

def locate_number_desc(array,num):
    low = 0
    high = len(array) - 1
    while low <= high:
        mid = (high + low) // 2
        if array[mid] == num:
            return mid
        elif array[mid] > num:
            low = mid + 1
        elif array[mid] < num:
            high = mid - 1
    return "number not found"

def locate_number_asc(array,num):
    low = 0
    high = len(array) - 1
    while low <= high:
        mid = (high + low) // 2
        if array[mid] == num:
            return mid
        elif array[mid] > num:
            high = mid - 1
        elif array[mid] < num:
            low = mid + 1
    return "number not found"
    
arr=[]
if asc_des(arr)=="descending":
    locate=int(input("enter which number to locate"))
    print(locate_number_desc(arr,locate))
elif asc_des(arr)=="ascending":
    locate=int(input("enter which number to locate"))
    print(locate_number_asc(arr,locate))
elif len(arr)==1:
    print(asc_des(arr))
else:
    print("array is empty")
    print("riddhima is ok")

