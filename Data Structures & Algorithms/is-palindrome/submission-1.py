class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        if not s:
            return False 
        clean = re.sub(r"[^\w]", "", s).lower()

        return clean==clean[::-1]