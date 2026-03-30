class Solution:
    def isPalindrome(self, s: str) -> bool:
        l = 0
        r = len(s) -1 
        def check_alpha_num(c):
            if c>= 'A' and c <= 'Z':
                return True
            if c>= 'a' and c<= 'z':
                return True
            if c>= '0' and c<='9':
                return True
            return False
        while l < r:
            if not check_alpha_num(s[l]):
                l+=1
                continue
            if not check_alpha_num(s[r]):
                r -= 1
                continue
            if s[l].lower() == s[r].lower():
                l+=1
                r-=1 
                continue
            else:
                print(l)
                print(r)
                return False 
        return True  
        