#https://leetcode.com/problems/longest-palindromic-substring/
for k in range(len(s),0,-1):
            for i in range(0,len(s)):
                #print k
                if i + k <= len(s):
                    j = i+k
                    if s[i:j] == s[i:j][::-1]:
                        return s[i:j]
                    
            
        return ""