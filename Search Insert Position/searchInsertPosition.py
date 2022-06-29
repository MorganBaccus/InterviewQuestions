class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        
        i = 0
        l = len(nums)-1
        
        if nums[0] > target:
            return 0
        elif nums[l] < target:
            return l
        else:
            for num in range(0,l):
                if nums[i] == target:
                    return i
                else:
                    if (nums[i] < target) and (nums[i+1] > target):
                        if target > nums[i]:
                            return i+1
                        else:
                            return i
                i+=1
