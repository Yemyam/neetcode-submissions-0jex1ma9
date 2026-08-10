class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mapping = {")": "(", "]": "[", "}": "{"}
        if len(s) == 1:
            return False
        for char in s:
            if char in "({[":
                stack.append(char)
            elif char in ")]}":
                if len(stack) == 0:
                    return False
                elif mapping[char] == stack[-1]:
                    stack.pop()
                else:
                    return False
            else:
                return False

        if len(stack) > 0:
            return False

        return True
                