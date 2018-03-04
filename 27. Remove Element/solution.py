class Solution:
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        if not nums:
            return 0
        NewEnd = 0
        for num in nums:
            if num != val:
                nums[NewEnd] = num
                NewEnd += 1
        return NewEnd
