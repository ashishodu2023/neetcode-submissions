from collections import deque 

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:

        if not heights:
            return 0 
        
        stack = deque()
        max_area = 0 

        for index,height in enumerate(heights + [0]):

            start = index 

            while stack and stack[-1][1]> height:

                i, h = stack.pop()
                max_area = max(max_area, h * (index - i))
                start = i 
            
            stack.append((start,height))

        return max_area
