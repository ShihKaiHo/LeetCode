class Solution:
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        str_x = str(x)
        str_len = len(str_x)
        half_str_len = len(str_x)//2
        for i, char in enumerate(str_x):
            if i >= half_str_len:
                break
            if char != str_x[str_len-i-1]:
                return False
        return True
