class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        """

        alw do maxfreq task to avoid idle time

        time = 1
        h = [-2] 
        q = []

        """

        # add freqs to heap
        freq_map = defaultdict(int)
        for c in tasks:
            freq_map[c] += 1
        h = [-f for f in freq_map.values()]
        heapq.heapify(h)

        # maxheap w/ time-based queue
        time = 0
        q = deque()

        while h or q:
            # pull from q
            if q and q[0][1] == time:
                heapq.heappush(h, q.popleft()[0])

            # idle time
            if not h:
                time += 1
            
            # pop max val from heap
            else:
                val = heapq.heappop(h)
                time += 1
                if abs(val+1) > 0:
                    q.append((val+1, time+n)) # (val, expiration_time)
        
        return time




