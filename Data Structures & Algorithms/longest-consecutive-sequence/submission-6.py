class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        if not nums:
            return 0
        
        num_set = set(nums)
        max_length = 0 

        for num in num_set:
            if num -1 not in num_set:
                count = 1

                while num + count in num_set:
                    count+=1
                max_length = max(max_length, count)

        return max_length

        