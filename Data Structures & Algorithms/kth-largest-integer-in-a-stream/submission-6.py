"""

k-sized minheap

init
- insert all vals into blank minheap
- pop when len(h) > k

add
- insert into minheap
- pop when len(h) > k
- return peek of minheap

"""

class KthLargest:

    # O(nlogK)
    def __init__(self, k: int, nums: List[int]):
        self.h = []
        heapq.heapify(self.h)
        self.k = k

        # insert all vals into blank minheap
        for n in nums:
            heapq.heappush(self.h, n)
        
            while len(self.h) > self.k:
                heapq.heappop(self.h) # keeps minheap k-sized

    # O(logK)
    def add(self, val: int) -> int:
        # insert val
        heapq.heappush(self.h, val)

        # keep it k-sized
        while len(self.h) > self.k:
            heapq.heappop(self.h)
        
        # return kth elem
        return self.h[0]






