class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        temp_stack = []
        res = [0] * len(temperatures)

        for i, temperature in enumerate(temperatures):

            while temp_stack and temperature > temperatures[temp_stack[-1]]:
                date_index = temp_stack.pop()
                days = i - date_index
                res[date_index] = days

            temp_stack.append(i)

        return res