class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heapq.heapify_max(stones)

        while len(stones) > 1:
            heaviest = heapq.heappop_max(stones)
            second = heapq.heappop_max(stones)
            if heaviest != second:
                heapq.heappush_max(stones, heaviest - second)

        return stones[0] if stones else 0