class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        i = len(s)-1
        length = 0
        
        for c in range(i,0,-1):
            if s[c] == ' ':
                if length == 0:
                    i = i - 1
                else:
                    return length
            else:
                length+=1
        return length
