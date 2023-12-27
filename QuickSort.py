arr=[10,15,1,2,9,16,11]

def quicksort(arr):  
    if len(arr) < 2:  
        return arr  
    pivot = arr[0]  
    left = [x for x in arr[1:] if x < pivot]  
    right = [x for x in arr[1:] if x >= pivot]  
    return quicksort(left) + [pivot] + quicksort(right)  

print(quicksort(arr))