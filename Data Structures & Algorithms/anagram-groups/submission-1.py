from collections import defaultdict
class Solution:

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if not strs:
            return []

        anagram_dict = defaultdict(list)    

        for word in strs:
            key = ''.join(sorted(word))
            anagram_dict[key].append(word)

        return  list(anagram_dict.values())