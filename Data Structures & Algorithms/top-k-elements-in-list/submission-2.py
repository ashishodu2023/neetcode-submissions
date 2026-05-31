import heapq

class Solution:

    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        if not nums:
            return []
        
        result = []
        heap =[]
        seen = dict()

        for num in nums:
            seen[num] = seen.get(num,0) + 1
        
        for num,freq in seen.items():
            heapq.heappush_max(heap,(freq,num))
        
        for _ in range(k):
            result.append(heapq.heappop_max(heap)[1])
        
        return result

        