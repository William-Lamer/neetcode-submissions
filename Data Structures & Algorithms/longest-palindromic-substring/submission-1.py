class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = ""
        resLen = 0


        for i in range(len(s)):
            l, r = i, i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                substring = s[l:r+1]
                if len(substring) > resLen:
                    res = substring
                    resLen = len(substring)
                l -= 1
                r += 1

        for i in range(len(s)):
            l, r = i, i + 1
            while l >=0 and r < len(s) and s[l] == s[r]:
                substring = s[l:r+1]
                if len(substring) > resLen:
                    res = substring
                    resLen = len(substring)
                l -= 1
                r += 1
        

        return res

