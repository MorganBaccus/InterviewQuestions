class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        
        i = len(digits) - 1
        
        if digits[i] != 9:
            digits[i] = digits[i] + 1
        elif len(digits) == 1:
            digits.insert(0,1)
            digits[1] = 0
        else:
            digits[i-1] = digits[i-1] + 1
            digits[i] = 0
        
        return digits
