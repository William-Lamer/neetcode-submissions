class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        res = r

        while l <= r:
            k = (l + r) // 2

            totalTime = sum(math.ceil(float(p)/k) for p in piles)
            if totalTime <= h:
                res = k
                r = k - 1
            else:
                l = k + 1
        return res

