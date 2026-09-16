class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # count the freq of tasks
        taskFreq = {}
        for task in tasks:
            taskFreq[task] = taskFreq.get(task, 0) + 1
        
        # putting elements in to max-heap for retreival
        heap = []
        for t, f in taskFreq.items():
            heapq.heappush(heap, [-f, t])
        
        # calculating least interval
        time = 0
        queue = deque()
        while heap or queue:
            time+=1
            if queue and queue[0][0] == time:
                timeStamp, task = queue.popleft() 
                heapq.heappush(heap, task)
            
            if heap:
                freq, task = heapq.heappop(heap)
                freq = -freq
                if freq-1 > 0:
                    queue.append([time+n+1, [-(freq-1), task]])

        return time



        