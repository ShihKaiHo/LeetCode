class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        table = {}
        for i, element in enumerate(nums):
            if (target - element) in table:
                return [table[target - element], i]
            else:
                table[element] = i
