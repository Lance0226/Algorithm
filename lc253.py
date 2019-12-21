class Solution(object):
    def minMeetingRooms(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        l = []
        
        for i,j in intervals:
            l.append([i,1])
            l.append([j,-1])
            
        l.sort()
        
        #print l
        
        res = 0
        p = 0
        time = -1
        
        for t,k in l:      
            if t != time:
                res = max(res,p)
            p += k
            time = t
            
        return res
