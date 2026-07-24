class Solution:
    def isPalindrome(self, s: str) -> bool:
        s1 = s.lower()
        s2 = re.sub(r'[^a-zA-Z0-9]', '', s1)
        for i in range(0, len(s2)//2):
            if s2[i] is not s2[len(s2) - 1 - i]:
                return False
        

        return True