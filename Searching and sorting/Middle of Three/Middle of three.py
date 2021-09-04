#User function Template for python3

class Solution:
    def middle(self,a,b,c):
        #code here
 # Compare each three number to find
    # middle number. Enter only if a > b
        if a > b :
            if (b > c):
                return b
            elif (a > c) :
                return c
            else :
                return a
        else:
        # Decided a is not greater than b.
            if (a > c) :
                return a
            elif (b > c) :
                return c
            else :
                return b
