from collections import deque


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:

        if not temperatures:
            return []

        stack = deque()
        result = [0] * len(temperatures)

        for index, temp in enumerate(temperatures):
            while stack and temp >temperatures[stack[-1]]:
                prev_temp = stack.pop()
                result[prev_temp] = index - prev_temp

            stack.append(index)

        return result
