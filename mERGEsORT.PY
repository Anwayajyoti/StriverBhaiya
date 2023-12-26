def merge(arr, left, mid, right):
    # Create copies of the subarrays
    L = arr[left:mid+1]
    R = arr[mid+1:right+1]
    # Initialize pointers for the subarrays and the original array
    i = j = 0
    k = left
    # Loop until one of the subarrays is exhausted
    while i < len(L) and j < len(R):
        # Compare the current elements of the subarrays and copy the smaller one to the original array
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1
    # Copy the remaining elements of the non-empty subarray to the original array
    while i < len(L):
        arr[k] = L[i]
        i += 1
        k += 1
    while j < len(R):
        arr[k] = R[j]
        j += 1
        k += 1
        
def merge_sort(arr, left, right):
    if left < right:
        mid = (left + right) // 2
        merge_sort(arr, left, mid)
        merge_sort(arr, mid + 1, right)
        merge(arr, left, mid, right)


arr = [5, 3, 8, 2, 6, 1, 4, 7]
print("Original array:", arr)
merge_sort(arr, 0, len(arr) - 1)
print("Sorted array:", arr)
