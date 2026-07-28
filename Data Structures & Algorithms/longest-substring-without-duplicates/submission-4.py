class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = {} #char -> index
        longest_substring = 0
        l, r = 0, 0

        for r in range(len(s)):
            
            # check if the next char is a duplicate
            if s[r] in seen:
                # Duplicate, advance left until past the occurent of the char
                l = max(seen[s[r]] + 1, l)
            
            seen[s[r]] = r

            longest_substring = max(longest_substring, r - l + 1)
            

        return longest_substring

