def find_query(arr,query):
    low=0
    high=len(arr)-1
    while low<=high:
        mid=(low+high)//2
        if arr[mid]==query:
            if arr[mid-1]==arr[mid]:
                high=mid-1
            else:
                return mid
        elif arr[mid]<query:
            high=mid-1
        elif arr[mid]>query:
            low=mid+1
        elif low==high:
            if arr[low]==query:
                return low
        else:
            return "query not found"
        print(arr)
arr=[8,8,6,6,6,6,6,6,3,2,2,2,0,0,0]  
print(find_query(arr,6))