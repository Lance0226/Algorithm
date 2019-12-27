#test
class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        if not height:
            return 0
        
        dict = {}
        dp = {}
        l = []
        
        for i,h in enumerate(height):
            dict[i] = 0
            dp[i] = h
            l.append([h,i])
        
        l = sorted(l)[::-1]
        
        left,right = l[0][1],l[0][1]
        li,ri = 0,0
        
        while left > 0:
            #print left
            while li < len(l)-1:
                li += 1
                if l[li][1] < left:
                    #print l[li][1],left
                    for m in range(l[li][1]+1,left):
                        dict[m] = l[li][0] - dp[m] 
                    print ""
                    left = l[li][1]
                    break
                    
            
        while right < len(l)-1:
            while ri < len(l):
                ri += 1
                if l[ri][1] > right:
                    for n in range(right+1,l[ri][1]):
                        dict[n] = l[ri][0] - dp[n] 
                    right = l[ri][1]
                    break
            
        return sum(dict.values())
            
             
            
        
        
        