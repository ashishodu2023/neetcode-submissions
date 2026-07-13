class Solution:
    def isPalindrome(self, s: str) -> bool:
        if not s:
            return False 
        
        clean_text = ''.join([char.lower() for char in s if char.isalnum()])

        left = 0 
        right = len(clean_text) - 1

        while left<right:
            if clean_text[left]!=clean_text[right]:
                return False 
            
            left+=1
            right-=1

        return True 
        