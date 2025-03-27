class Solution:
    def isValid(self, s: str) -> bool:
        table = {')': '(', ']':'[', '}':'{'}
        stack = []
        

        for bracket in s:
            if bracket in table.values():
                stack.append(bracket)
            elif bracket in table:
                if not stack or stack[-1] != table[bracket]:
                    return False
                stack.pop()
        return not stack
            
        
