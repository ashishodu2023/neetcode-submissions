class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return [[]]

        result = []
        path = []

        def dfs(index):

            result.append(path.copy())

            for i in range(index,len(nums)):
                path.append(nums[i])

                dfs(i+1)
                path.pop()

        dfs(0)
        return result 
                
            
        