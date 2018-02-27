class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        ans = ((x>0) - (x<0))*int(str(abs(x))[::-1])
        return ans if ans.bit_length() < 32 else 0
