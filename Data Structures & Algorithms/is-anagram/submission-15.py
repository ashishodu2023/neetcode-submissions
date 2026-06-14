class Solution:

    def isAnagram(self, s: str, t: str) -> bool:

        if len(s)!=len(t):
            return False 
        
        char_dict = dict()

        for char1 in s:
            char_dict[char1] = char_dict.get(char1,0) + 1

        for char2 in t:
            if char2 not in char_dict or char_dict[char2]==0:
                return False 
            char_dict[char2]-=1
        
        return True 
            