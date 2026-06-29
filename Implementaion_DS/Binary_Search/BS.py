


def BS(arr, size, key):
    start = 0
    end = size - 1
    
    while start <= end:
        
        # Claculating mid 
        mid = start + (end - start) // 2  # Floor division to avoid float index
        # Check if mid is key
        if arr[mid] == key:
            return mid
        elif arr[mid] < key:
            start = mid + 1
        else:
            end = mid - 1
    return -1



# Driver code
if __name__ == "__main__":
    arr = [2, 3, 4, 10, 40, 50]
    size = len(arr)
    key = 10
    
    result = BS(arr, size, key)
    if result != -1:
        print("Element is present at index", str(result))
    else:
        print("Element is not present in array")