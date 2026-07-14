class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        if not temperatures:
            return []

        result = [0] * len(temperatures)
        stack = []

        for key, temp in enumerate(temperatures):
            while stack and temp > temperatures[stack[-1]]:
                prev_temp = stack.pop()
                result[prev_temp] = key - prev_temp
            stack.append(key)

        return result
