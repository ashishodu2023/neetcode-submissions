class Solution:
    
    def longestConsecutive(self, nums: List[int]) -> int:

        if not nums:
            return 0 
        
        if len(nums)==0:
            return 0

        nums_set = set(nums)
        longest = 0
        for number in nums_set:
            if (number - 1) not in nums_set:
                count=1
                num = number
                while num+1 in nums_set:
                    num+=1
                    count+=1
                longest = max(longest,count)

        return longest 


