def find(arr,n,x):
    # code here
    return first(arr, 0, n-1, x, n), last(arr,0,n-1,x,n)
    
def first(arr, low, high, x, n) :
    if(high >= low) :
        mid = low + (high - low) // 2
        if( ( mid == 0 or x > arr[mid - 1]) and arr[mid] == x) :
            return mid
        elif(x > arr[mid]) :
            return first(arr, (mid + 1), high, x, n)
        else :
            return first(arr, low, (mid - 1), x, n)
     
    return -1
 
def last(arr, low, high, x, n) :
    if (high >= low) :
        mid = low + (high - low) // 2
        if (( mid == n - 1 or x < arr[mid + 1]) and arr[mid] == x) :
            return mid
        elif (x < arr[mid]) :
            return last(arr, low, (mid - 1), x, n)
        else :
            return last(arr, (mid + 1), high, x, n)
             
    return -1