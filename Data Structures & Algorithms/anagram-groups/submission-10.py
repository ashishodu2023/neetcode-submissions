class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        if not strs:
            return [[""]]

        if len(strs) == 1:
            return [[strs[0]]]

        seen = dict()

        for word in strs:
            key = "".join(sorted(word))

            if key not in seen:
                seen[key] = []

            seen[key].append(word)

        return [group for group in seen.values()]
