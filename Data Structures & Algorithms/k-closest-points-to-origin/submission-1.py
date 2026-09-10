class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        maxHeap = []

        for x, y in points:
            distance = (x**2) + (y**2)
            heapq.heappush_max(maxHeap, (distance, x, y))

            if len(maxHeap) > k:
                heapq.heappop_max(maxHeap)
        
        res = []
        for i in range(len(maxHeap)):
            _, x, y = heapq.heappop(maxHeap)
            res.append([x,y])

        return res
            

