class Solution:
    def maxArea(self, heights: List[int]) -> int:
        if not heights:
            return 0    
        max_area = float('-inf')
        for i in range(len(heights)):
            for j in range(i+1,len(heights)):
                height = min(heights[i],heights[j])
                width = j - i
                area = height * width
                max_area = max(max_area,area)

        return max_area
                
                
        