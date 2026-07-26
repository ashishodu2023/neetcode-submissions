class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        if not s:
            return 0

        longest = 0
        seen = dict()
        left = 0
        maxfreq = 0

        for right, char in enumerate(s):
            seen[char] = seen.get(char, 0) + 1
            maxfreq = max(maxfreq, seen[char])

            while (right - left + 1) - maxfreq > k:
                seen[s[left]] -= 1
                left += 1
            longest = max(longest, right - left +1)

        return longest
