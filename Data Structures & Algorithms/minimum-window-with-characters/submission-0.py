class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not t or not s: 
            return ""

        count_t = Counter(t)
        count_window = defaultdict(int)
        need = len(count_t)
        have = 0

        best_len = float('inf')
        best_left = 0
        left = 0

        for right in range(len(s)):
            c = s[right]
            count_window[c] += 1

            have = (have + 1) if count_t[c] == count_window[c] else have

            while have == need:
                if right - left + 1 < best_len:
                    best_len = right - left + 1
                    best_left = left


                count_window[s[left]] -= 1
                if count_t[s[left]] > count_window[s[left]]:
                    have -= 1
                left += 1

        return "" if best_len == float('inf') else s[best_left:best_left + best_len]
