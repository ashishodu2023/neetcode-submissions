class Solution:

    def hasDuplicate(self, nums: List[int]) -> bool:
        
        if not nums:
            return False 
        
        seen = {}

        for i,num in enumerate(nums):
            if num in seen:
                return True
            seen[num] =i

        return False
        


