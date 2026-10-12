class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        prices = [float("infinity")] * n
        prices[src] = 0

        for i in range(k+1):
            dist = prices.copy()
            for u, v, c in flights:
                if dist[u] != float("infinity") and prices[u] + c < dist[v]:
                    dist[v] = prices[u] + c
            prices = dist
        
        return prices[dst] if prices[dst] != float("infinity") else -1

        