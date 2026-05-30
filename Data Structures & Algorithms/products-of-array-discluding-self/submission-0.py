class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        if not nums:
            return []

        result = [1]*len(nums)

        left_sum = 1
        right_sum = 1

        for i in range(len(nums)):
            result[i] = left_sum
            left_sum= left_sum*nums[i]

        for j in range(len(nums)-1,-1,-1):
            result[j] *= right_sum
            right_sum *= nums[j]

        return result


        