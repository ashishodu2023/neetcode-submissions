class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return []

        if len(nums) == 1:
            return [[nums[0]]]

        result = []
        subset = []
        visited = set()

        def dfs():

            if len(subset) == len(nums):
                result.append(subset.copy())
                return

            for num in nums:
                if num in visited:
                    continue

                visited.add(num)
                subset.append(num)

                dfs()

                subset.pop()
                visited.remove(num)

        dfs()
        return result
