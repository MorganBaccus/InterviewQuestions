class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        
        left = 0
        right = len(nums)-1
        mid = (left + right) / 2
        
        while left <= right:
            mid = (left + right) / 2
            if nums[mid] == target:
                return mid
            elif target > nums[mid]:
                left = mid
            else:
                right = mid
