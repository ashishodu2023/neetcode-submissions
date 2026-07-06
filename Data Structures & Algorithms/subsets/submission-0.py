class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return [[]]

        result = []
        subset = []

        def dfs(index):
            if index == len(nums):
                result.append(subset.copy())
                return 
            
            #Take
            subset.append(nums[index])
            dfs(index+1)

            #Backtrack
            subset.pop()

            #Skip
            dfs(index+1)

        dfs(0)
        return result
