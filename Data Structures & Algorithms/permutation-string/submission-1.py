class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        if len(s1) > len(s2):
            return False

        seen = dict()
        window = dict()
        left = 0 

        # S1 Frequnecy
        for char1 in s1:
            seen[char1] = seen.get(char1, 0) + 1

        # Window Frequency
        for i in range(len(s1)):
            window[s2[i]] = window.get(s2[i], 0) + 1

        if seen == window:
            return True

        # Sliding window

        for right in range(len(s1), len(s2)):
            # Add new character
            window[s2[right]] = window.get(s2[right], 0) + 1

            # Remove old character
            window[s2[left]] -= 1

            if window[s2[left]] == 0:
                del window[s2[left]]

            left += 1

            if seen == window:
                return True

        return False
