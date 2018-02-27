class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if len(strs) == 0:
            return ""
        LCP = strs[0]
        del strs[0]
        for string in strs:
            temp = ""
            if len(LCP) <= len(string):
                for i, char in enumerate(LCP):
                    if char == string[i]:
                        temp += char
                    else:
                        break
            else:
                for i, char in enumerate(string):
                    if char == LCP[i]:
                        temp += char
                    else:
                        break
            LCP = temp
        return LCP
