class Solution:
    def isPalindrome(self, s: str) -> bool:
        ch=''
        for i in s:
            if i.isalnum():
                ch+=i.lower()
        if ch == ch[::-1]:
            return True
        return False