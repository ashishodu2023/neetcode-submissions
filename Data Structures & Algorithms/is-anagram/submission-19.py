class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        seen = dict()

        for char1 in s:
            seen[char1] = seen.get(char1, 0) + 1

        for char2 in t:
            if char2 not in seen or seen[char2] == 0:
                return False
            seen[char2]-=1

        return True
