class Solution:
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        ans = 0
        last_word = len(s) - 1
        for i, char in enumerate(s):
            if char == "I":
                if i != last_word:
                    if (s[i+1] == "V") or (s[i+1] == "X"):
                        ans -= 1
                    else:
                        ans += 1
                else:
                    ans += 1
            elif char == "X":
                if i != last_word:
                    if (s[i+1] == "L") or (s[i+1] == "C"):
                        ans -= 10
                    else:
                        ans += 10
                else:
                    ans += 10
            elif char == "C":
                if i != last_word:
                    if (s[i+1] == "D") or (s[i+1] == "M"):
                        ans -= 100
                    else:
                        ans += 100
                else:
                    ans += 100
            elif char == "V":
                ans += 5
            elif char == "L":
                ans += 50
            elif char == "D":
                ans += 500
            elif char == "M":
                ans += 1000
        return ans
