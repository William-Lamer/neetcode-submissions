class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        count_s1 = Counter(s1)
        length = len(s1)
        count_window = defaultdict(int)
        left = 0

        for right in range(len(s2)):
            count_window[s2[right]] += 1

            if count_window == count_s1:
                return True

            if right - length + 1 >= left:
                count_window[s2[left]] -= 1
                if count_window[s2[left]] == 0:
                    del count_window[s2[left]]
                left += 1


        return False
            