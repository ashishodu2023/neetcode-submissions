from collections import defaultdict
class Solution:
    
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        if not nums:
            return []

        seen = defaultdict(int)
        result = []

        for num in nums:
            seen[num] = seen.get(num,0)+1

        for key, value in sorted(seen.items(), key=lambda x:x[1],reverse=True):
            result.append(key)

            if len(result)==k:
                return result
            

        