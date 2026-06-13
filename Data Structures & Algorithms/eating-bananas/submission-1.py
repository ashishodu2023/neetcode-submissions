class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        if not piles:
            return 0

        left = 1
        right = max(piles)

        while left < right:
            mid = (left + right) // 2

            hours = sum((pile + mid - 1) // mid for pile in piles)

            if hours <= h:
                right = mid
            if hours > h:
                left = mid + 1

        return left
