class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        if not s:
            return 0

        result = 0
        seen = dict()
        max_freq = 0
        left = 0

        for right in range(len(s)):
            seen[s[right]] = seen.get(s[right], 0) + 1
            max_freq = max(max_freq, seen[s[right]])

            while (right - left + 1) - max_freq > k:
                seen[s[left]] -= 1
                left += 1
            result = max(result, right - left + 1)

        return result
