class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        if len(s1) > len(s2):
            return False

        seen = dict()
        window = dict()

        # Count characters in s1
        for char in s1:
            seen[char] = seen.get(char, 0) + 1

        # Build first window
        for i in range(len(s1)):
            char = s2[i]
            window[char] = window.get(char, 0) + 1

        if window == seen:
            return True

        left = 0
        # Slide the window
        for right in range(len(s1), len(s2)):
            # Add new character
            char = s2[right]
            window[char] = window.get(char, 0) + 1

            # Remove old character
            old = s2[left]
            window[old] -= 1

            if window[old] == 0:
                del window[old]
            left += 1

            if window == seen:
                return True

        return False
