class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False

        anagram_dict = dict()

        for char1 in s:
            anagram_dict[char1] = anagram_dict.get(char1, 0) + 1

        for char2 in t:
            if char2 not in anagram_dict or anagram_dict[char2] == 0:
                return False
            anagram_dict[char2] -= 1

        return True
