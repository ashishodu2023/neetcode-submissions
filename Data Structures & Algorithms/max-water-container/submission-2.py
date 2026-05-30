#Two pointer approach
class Solution:
    
    def maxArea(self, heights: List[int]) -> int:
        if not heights:
            return 0 

        max_area = 0
        left = 0 
        right = len(heights) -1 

        while left<right:
            height = min(heights[left],heights[right])
            width = (right - left)
            current_area = height * width

            max_area = max(current_area,max_area)
            if heights[left]<heights[right]:
                left+=1
            else:
                right -=1

        return max_area

        
        