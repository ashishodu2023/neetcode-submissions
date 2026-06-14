class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        if not nums:
            return []

        result = [1] * len(nums)
        for i in range(1, len(nums)):
            result[i] = result[i - 1] * nums[i - 1]

        suffix = 1

        for i in reversed(range(len(nums))):
            result[i] *= suffix
            suffix *= nums[i]

        return result
