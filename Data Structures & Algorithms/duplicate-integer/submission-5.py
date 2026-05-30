from collections import Counter
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        
        if not nums:
            return False 
        
        count = Counter(nums)

        for element,frequency in count.most_common():
            if frequency>1:
                return True
        
        return False
        