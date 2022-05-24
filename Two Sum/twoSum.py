class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        i = 0
        j = 1
        
        for i in range(len(nums)):
            for j in range(len(nums)):
                if (target == nums[i]+nums[j]):
                    return [i,j]
                
        return [-1,-1]
