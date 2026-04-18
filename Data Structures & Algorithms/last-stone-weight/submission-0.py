class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        """

        1. stones --> maxheap
        2. while len(h) > 1
        - x is 2nd pop, y is 1st 
        - if x < y --> heappush(y-x)

        """

        # stones --> maxheap
        h = [-s for s in stones]
        heapq.heapify(h)

        # simulation
        while len(h) > 1:
            y = -heapq.heappop(h)
            x = -heapq.heappop(h)

            if x < y:
                heapq.heappush(h, -(y-x))
        
        return -h[0] if h else 0



