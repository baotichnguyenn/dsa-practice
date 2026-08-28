class Solution:
    def isValid(self, s: str) -> bool:
        matching_close_and_open = {
            "[": "]",
            "{": "}",
            "(": ")"
        }

        opening_stack =[]
        for char in s:
            if char in matching_close_and_open:
                opening_stack.append(char)
            else:
                if len(opening_stack) ==0:
                    return False
                if char != matching_close_and_open[opening_stack.pop()]:
                    return False
        if opening_stack:
            return False
        else:
            return True
            

           

            
        