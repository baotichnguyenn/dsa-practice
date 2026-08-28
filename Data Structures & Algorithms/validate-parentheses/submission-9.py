class Solution:
    def isValid(self, s: str) -> bool:
        matching_close_and_open = {
            "[": "]",
            "{": "}",
            "(": ")"
        }

        opening_stack =[]
        for char in s:
            if char in matching_close_and_open.keys():
                opening_stack.append(char)
            if char in matching_close_and_open.values():
                if len(opening_stack) ==0:
                    return False
                if char != matching_close_and_open[opening_stack.pop()]:
                    return False
        if len(opening_stack) != 0:
            return False
        else:
            return True
            

           

            
        