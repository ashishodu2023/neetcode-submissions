class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:

        if not nums:
            return [[]]

        result = []
        subset = []

        def dfs(index):
            result.append(subset.copy())
            for i in range(index, len(nums)):
                subset.append(nums[i])

                dfs(i + 1)
                subset.pop()

        dfs(0)
        return result
