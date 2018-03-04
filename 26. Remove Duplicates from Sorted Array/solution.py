class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        NewEnd = 0
        for i in range(1,len(nums)):
            if nums[i] != nums[NewEnd]:
                NewEnd += 1
                nums[NewEnd] = nums[i]
        return NewEnd + 1
