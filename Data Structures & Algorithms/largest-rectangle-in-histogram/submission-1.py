from collections import deque

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:

        stack = deque()
        max_area = 0

        for index, height in enumerate(heights):

            start = index

            while stack and stack[-1][1] > height:

                i, h = stack.pop()

                area = h * (index - i)

                max_area = max(max_area, area)

                start = i

            stack.append((start, height))

        for index, height in stack:

            area = height * (len(heights) - index)

            max_area = max(max_area, area)

        return max_area