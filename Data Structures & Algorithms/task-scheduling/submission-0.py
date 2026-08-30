class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        hm = {}
        for task in tasks:
            hm[task] = hm.get(task, 0) + 1
        
        heap = [-cnt for cnt in hm.values()]
        heapq.heapify(heap)

        queue = deque()
        # queue format is [-cnt, time]
        
        time = 0
        while heap or queue:
            time+=1
            
            if heap:
                cnt = 1+ heapq.heappop(heap)
                if cnt:
                    queue.append([cnt, time + n])
            
            if queue and queue[0][1] == time:
                heapq.heappush(heap, queue.popleft()[0])
            
        return time