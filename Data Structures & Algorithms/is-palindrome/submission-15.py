class Solution:
    def isPalindrome(self, s: str) -> bool:

        if not s:
            return True 
        
        cleaned_str = "".join([char.lower() for char in s if char.isalnum()])
        

        left = 0 
        right = len(cleaned_str) -1
        
        while left<right:
            if cleaned_str[left]!=cleaned_str[right]:
                return False 
            left+=1
            right-=1

        return True
        