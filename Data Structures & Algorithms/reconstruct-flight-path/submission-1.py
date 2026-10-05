class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        adjList = defaultdict(list)
        tickets.sort(reverse=True)

        for u,v in tickets:
            adjList[u].append(v)
        
        res = []
        def dfs(airport):
            while adjList[airport]:
                poppedAiport = adjList[airport].pop()
                dfs(poppedAiport)
            res.append(airport)
        
        dfs("JFK")
        return res[::-1]


        
        
        