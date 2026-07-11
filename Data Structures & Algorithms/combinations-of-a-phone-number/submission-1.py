class Solution:
    def letterCombinations(self, digits: str) -> List[str]:

        if not digits:
            return []

        digit_map = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }

        result =[]
        subset =[]

        def dfs(index):

            if index == len(digits):
                result.append("".join(subset))
                return 
            
            letters = digit_map[digits[index]]

            for char in letters:
                subset.append(char)
                dfs(index +1)
                subset.pop()


        dfs(0)
        return result   


        