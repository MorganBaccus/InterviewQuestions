class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        
        if n < 2:
            return 1
        
        p1, p2 = 1, 1
        for i in range(n):
            p1, p2 = p2, p1 + p2
            
        return p1
