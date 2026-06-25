class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:

        if not nums:
            return False 
        
        n = len(nums)
        ans =nums

        for i in range(len(ans)):
            ans.append(nums[i])

        return ans



        