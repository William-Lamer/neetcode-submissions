class Solution:
    def majorityElement(self, nums: list[int]) -> list[int]:
        cand1, cand2, c1, c2 = None, None, 0, 0
        for x in nums:
            if x == cand1:
                c1 += 1
            elif x == cand2:
                c2 += 1
            elif c1 == 0:
                cand1, c1 = x, 1
            elif c2 == 0:
                cand2, c2 = x, 1
            else:
                c1 -= 1
                c2 -= 1
            
        return [c for c in (cand1, cand2) if c is not None and nums.count(c) > len(nums) // 3] 