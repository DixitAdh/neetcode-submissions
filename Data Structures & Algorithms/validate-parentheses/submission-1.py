class Solution:
        
    def isValid(self, s: str) -> bool:
        stack = []
        mapping = {')': '(', '}': '{', ']':'['}
        for b in s:
            if not mapping.get(b):
                stack.append(b)
            else:
                if stack and mapping.get(b) == stack[-1]:
                    stack.pop()
                else:
                    return False
        return False if len(stack) > 0 else True