class Solution:
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        min = 0
        max = len(nums) - 1
        if target > nums[max]:
            return max + 1
        if target == nums[max]:
            return max
        if target <= nums[min]:
            return min
        while 1:
            if (max - min) <= 1:
                return min + 1
            if target == nums[(max + min)//2]:
                return (max + min)//2
            if target > nums[(max + min)//2]:
                min = (max + min)//2
            else:
                max = (max + min)//2
