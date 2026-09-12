class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        substring = set()
        longest = 0

        for r in range(len(s)):
            if s[r] in substring:
                while s[r] in substring:
                    substring.remove(s[l])
                    l += 1
                    
            substring.add(s[r])
            longest = max(longest, len(substring))

        return longest

