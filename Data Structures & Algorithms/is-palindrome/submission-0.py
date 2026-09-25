import re
class Solution:
    def isPalindrome(self, s: str) -> bool:
        m = re.sub(r'[^a-zA-Z0-9]', '', s)
        for i in range(len(m)):
            if (m[i].lower()!=m[len(m)-i-1].lower()):
                return False
        return True
        