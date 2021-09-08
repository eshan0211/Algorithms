class Solution:
    def majorityElement(self, A, N):
        #Your code here
        m = {}
        for i in range(N):
            if A[i] in m:
                m[A[i]] += 1
            else:
                m[A[i]] = 1
        count = 0
        for key in m:
            if m[key] > N / 2:
                count = 1
                return key
                break
        if(count == 0):
            print("No Majority element")
