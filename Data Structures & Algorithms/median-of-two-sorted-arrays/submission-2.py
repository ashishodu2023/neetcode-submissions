class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:

        result = nums1 + nums2
        result.sort()
        n = len(result)
        mid = n // 2

        if n % 2 == 0:
            return (result[mid - 1] + result[mid]) / 2.0
        else:
            return float(result[mid])
