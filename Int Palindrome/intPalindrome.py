class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        
        xs = str(x)
        xr = xs[::-1]
        
        if xr == xs:
            return True
        else:
            return False
