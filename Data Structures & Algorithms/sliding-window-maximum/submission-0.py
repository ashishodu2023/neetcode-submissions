from collections import deque


class Solution:
    def maxSlidingWindow(self, nums, k):

        q = deque()
        result = []
        left = 0

        for right in range(len(nums)):
            # Remove indices outside window
            while q and q[0] < left:
                q.popleft()

            # Remove smaller elements
            while q and nums[q[-1]] < nums[right]:
                q.pop()

            q.append(right)

            # Window reached size k
            if right - left + 1 == k:
                result.append(nums[q[0]])
                left += 1

        return result
