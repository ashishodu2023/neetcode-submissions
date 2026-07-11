class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:

        candidates.sort()

        if not candidates:
            return [[]]

        if len(candidates) == 1 and candidates[0] < target:
            return []
            
        result = []
        subset = []

        def dfs(index, total):

            if total == target:
                result.append(subset.copy())
                return

            if total > target:
                return

            for i in range(index, len(candidates)):
                if i > index and candidates[i - 1] == candidates[i]:
                    continue

                subset.append(candidates[i])

                dfs(i + 1, total + candidates[i])

                subset.pop()

        dfs(0, 0)
        return result
