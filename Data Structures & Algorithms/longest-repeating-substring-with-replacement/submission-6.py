class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        if not s:
            return 0 

        longest = 0 
        seen = dict()
        left = 0 
        result = 0 

        for right in range(len(s)):
            seen[s[right]] = seen.get(s[right],0) + 1
            longest = max(longest,seen[s[right]])

            while(right - left +1) - longest>k:
                seen[s[left]]-=1
                left+=1
            
            result = max(result, right - left +1)

        return result 


        