class Solution(object):
    def sumSubarrayMins(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        self.res = 0
    
        def dfs(k):
            #print k
            _i,_j = 0,len(A)-1
            for i in range(k-1,-1,-1):
                #print i,k,A[i],A[k]
                if A[i] <= A[k]:
                    _i = i+1
                    break
            
            for j in range(k+1,len(A)):
                #print j
                if A[j] < A[k]:
                    _j = j-1
                    break
            self.res += ((_j - k+1)*(k - _i+1)*A[k]) 
            self.res %= (10**9+7)

        
        for t in range(len(A)):
            dfs(t)
            
        return self.res 
        
