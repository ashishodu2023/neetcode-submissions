class Solution:
    def partition(self, s: str) -> List[List[str]]:
        if not s:
            return [[]]

        result = []
        subset = []

        def ispalindrome(left, right):

            while left < right:
                if s[left] != s[right]:
                    return False

                left += 1
                right -= 1
            return True

        def dfs(index):
            if index == len(s):
                result.append(subset.copy())
                return

            for i in range(index, len(s)):
                if ispalindrome(index, i):
                    subset.append(s[index : i + 1])
                    dfs(i + 1)
                    subset.pop()

        dfs(0)

        return result
