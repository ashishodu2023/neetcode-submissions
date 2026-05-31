
class Solution:

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        if not strs:
            return []

        if len(strs)==1:
            return [[strs[0]]]

        anagram_map = dict()

        for word in strs:

            key = ' '.join(sorted(word))

            if key not in anagram_map:
                anagram_map[key] = [ ]

            anagram_map[key].append(word)

        return [group for group in anagram_map.values()] 

        