class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        dict_close = {
            ")" : "(",
            "]" : "[",
            "}" : "{"
        }

        for char in s:
            if char in dict_close:
                if stack and stack[-1] == dict_close[char]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(char)
        if not stack:
            return True
        else:
            return False