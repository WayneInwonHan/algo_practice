class Solution:
    def isValid(self, parentheses):
        stack, bracket = [], {"(": ")", "{": "}", "[": "]"}
        for parenthese in parentheses:
            if parenthese in bracket:
                stack.append(parenthese)
            elif len(stack) == 0 or bracket[stack.pop()] != parenthese:
                return False
        return len(stack) == 0