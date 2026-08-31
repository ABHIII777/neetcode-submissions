class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        braces = {")": "(", "}": "{", "]": "["}

        for char in s:
            if char in braces.values():
                stack.append(char)

            elif char in braces.keys():
                if not stack or braces[char] != stack.pop():
                    return False

        return not stack
