class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        """ 

        insert (-dist, x, y) into k-sized maxheap
        return points left in maxheap

        """

        # create k-sized maxheap
        h = []
        heapq.heapify(h)

        # insert points into k-sized maxheap w/ dist
        for x, y in points:
            # calculate dist
            dist = math.sqrt((x**2) + (y**2))
            heapq.heappush(h, (-dist, x, y))

            while len(h) > k:
                heapq.heappop(h)

        # return points left in heap
        return [[x, y] for dist, x, y in h]

        

