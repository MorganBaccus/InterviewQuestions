class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """

        LCP = ''
        ind = 0
        
        while ind < len(min(strs)):
            letter_set = set()
            for i in strs:
                letter_set.add(i[ind])
            if len(letter_set) == 1:
                LCP += letter_set.pop()
                ind += 1
            else:
                break

        return LCP
