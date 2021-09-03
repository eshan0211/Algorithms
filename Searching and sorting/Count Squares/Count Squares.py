class Solution:
    def countSquares(self, N):
        # code here 
        if N == 0 or N == 1:
            return 0
        
        x = int(math.sqrt(N))
        
        if (x**2 == N) :
            return x - 1
        else : 
            return x
        