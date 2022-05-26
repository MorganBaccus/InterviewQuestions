class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        vals = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
        num, i = 0, 0
        
        if len(s) == 1:
            return vals[s]
        
        while i < (len(s) - 1):
            if vals[s[i+1]] - vals[s[i]] <= 0:
                num += vals[s[i]]
            else:
                num += vals[s[i+1]] - vals[s[i]]
                i += 1
            i += 1
            
            if i == len(s) - 1:
                num += vals[s[i]]
                
        return num
