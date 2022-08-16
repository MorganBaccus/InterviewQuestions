class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        
        l, r = 0, x
        while l < r:
            m = l + (r - l) // 2
            if m ** 2 == x:
                return m
            elif m ** 2 > x:
                r = m
            else:
                l = m + 1
        return l - 1 if l ** 2 != x else l
