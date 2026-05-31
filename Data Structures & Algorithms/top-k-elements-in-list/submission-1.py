import heapq

class Solution:

    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        if not nums:
            return []

        seen = {}
        result = []
        heap =[]

        for num in nums:
            seen[num] = seen.get(num,0) + 1
        
        for num,freq in seen.items():
             heapq.heappush(heap, (-freq, num))

        for _ in range(k):
            result.append(heapq.heappop(heap)[1])

        return result


