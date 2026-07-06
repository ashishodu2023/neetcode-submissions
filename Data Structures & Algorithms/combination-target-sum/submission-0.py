class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        if not nums:
            return [[]]

        if len(nums)==1 and nums[0]<target:
            return []
        
        result =[]
        subset = []


        def dfs(index,total):
            
            if total==target:    
                result.append(subset.copy())
            if total>target:
                return 
            
            for i in range(index,len(nums)):
                subset.append(nums[i])
                dfs(i, total + nums[i])   # Reuse same number

                subset.pop()

        dfs(0,0)
        return result

