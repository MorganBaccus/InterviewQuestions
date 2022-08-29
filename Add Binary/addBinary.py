class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        
        carry = total = 0
        result = ""        
        a = list(a)
        b = list(b)
        
        while a or b or carry == 1:
            if a:
                total += int(a.pop())
            if b:
                total += int(b.pop())
            result += str((total + carry) % 2)
            carry = (total + carry) // 2 
            total = 0
        
        return result[::-1]
