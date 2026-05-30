class Solution:
    
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        if not nums:
            return []

        seen = {}

        for key, value in enumerate(nums):
            compliment = target - value 
            if compliment in seen:
                return [seen[compliment],key]
            
            seen[value]=key
        