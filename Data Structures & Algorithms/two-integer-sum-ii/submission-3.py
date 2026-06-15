class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        if not numbers:
            return []

        left = 0
        right = len(numbers) - 1

        while left < right:
            num1 = numbers[left]
            num2 = numbers[right]

            value = num1 + num2

            if value == target:
                return [left + 1, right + 1]

            elif value < target:
                left += 1
            elif value > target:
                right -= 1
