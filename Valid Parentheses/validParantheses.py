class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        
        paraCount = 0
        curlyCount = 0
        squareCount = 0
        
        for i in s:
            if i == '(':
                paraCount = 1 + paraCount
            elif i == '{':
                curlyCount = 1 + curlyCount
            elif i == '[':
                squareCount = 1 + squareCount
            elif i == ')':
                paraCount = paraCount - 1
            elif i == '}':
                curlyCount = curlyCount - 1
            elif i == ']':
                squareCount = squareCount - 1
            else:
                i = i+1
                
        if (paraCount == 0) and (curlyCount == 0) and (squareCount == 0):
            return True
        else:
            return False
