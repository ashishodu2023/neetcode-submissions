class Solution:
    def isPalindrome(self, s: str) -> bool:

        if not s:
            return True

        clean_strs = "".join([char.lower() for char in s if char.isalnum()])

        left = 0
        right = len(clean_strs) -1
        while left <=right:
            if clean_strs[left] != clean_strs[right]:
                return False

            left += 1
            right -= 1

        return True
