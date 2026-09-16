class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # count the freq of tasks
        taskFreq = {}
        for task in tasks:
            taskFreq[task] = taskFreq.get(task, 0) + 1
        
        # putting elements in to max-heap for retreival
        heap = [-f for f in taskFreq.values()]
        heapq.heapify(heap)

        # calculating least interval
        time = 0
        queue = deque()
        while heap or queue:
            time+=1

            if queue and queue[0][0] == time:
                timeStamp, freq = queue.popleft() 
                heapq.heappush(heap, freq)
            
            if heap:
                freq = 1 + heapq.heappop(heap)
                if freq:
                    queue.append([time+n+1, freq])

        return time



        