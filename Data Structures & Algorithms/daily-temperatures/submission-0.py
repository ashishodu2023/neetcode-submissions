from collections import deque


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:

        if not temperatures:
            return []

        stack = deque()
        result = [0] * len(temperatures)

        for index,temp in enumerate(temperatures):

            while stack and temp > temperatures[stack[-1]]:

                previous_temperature = stack.pop()

                result[previous_temperature] = index - previous_temperature
        
            stack.append(index)

        return result
