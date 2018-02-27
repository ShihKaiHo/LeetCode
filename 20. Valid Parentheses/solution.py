class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        for element in s:
            if element == ")":
                if stack == []:
                    return False
                elif stack[-1] == "(":
                    stack.pop()
                else:
                    return False
            elif element == "}":
                if stack == []:
                    return False
                elif stack[-1] == "{":
                    stack.pop()
                else:
                    return False
            elif element == "]":
                if stack == []:
                    return False
                elif stack[-1] == "[":
                    stack.pop()
                else:
                    return False
            else:
                stack.append(element)
        if stack == []:
            return True
        else:
            return False
