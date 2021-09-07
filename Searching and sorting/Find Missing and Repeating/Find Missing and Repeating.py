class Solution:
    def findTwoElement( self,arr, n): 
        # code here
        for i in range(n):
            if arr[abs(arr[i])-1]>0:
                arr[abs(arr[i])-1] = -arr[abs(arr[i])-1]
            else:
                repeating = abs(arr[i])
                
        for i in range(n):
            if arr[i] > 0:
                missing = i+1
                
        return repeating, missing
