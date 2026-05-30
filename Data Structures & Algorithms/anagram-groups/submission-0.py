from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)

        for string in strs:
            frequency=[0]*26

            for ch in string:
                frequency[ord(ch) - ord('a')]+=1
            
            groups[tuple(frequency)].append(string)

        
        return list(groups.values())

        