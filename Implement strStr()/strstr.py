class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """ 
            
        lenNeedle = len(needle)
        
        if lenNeedle == 0:
            return 0
        elif lenNeedle >= 1:
            for i in range(len(haystack)):
                if haystack[i]==needle[0] and haystack[i:i+lenNeedle] == needle:
                    return i
        else: 
            return -1
