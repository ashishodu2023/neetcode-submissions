class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:

        nums.sort()

        if not nums:
            return [[]]

        result = []
        subset = []

        def dfs(index):

            result.append(subset.copy())

            for i in range(index, len(nums)):
                if i > index and nums[i - 1] == nums[i]:
                    continue

                subset.append(nums[i])
                dfs(i + 1)
                subset.pop()

        dfs(0)

        return result
