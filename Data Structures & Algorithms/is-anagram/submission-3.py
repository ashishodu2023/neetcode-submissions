class Solution:
    
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s)!=len(t):
            return False 
        char_seen ={}

        for ch in s:
            char_seen[ch]= char_seen.get(ch,0)+1

        for ch in t:
            if ch not in char_seen or char_seen[ch]==0:
                return False
            
            char_seen[ch]-=1
        
        return True