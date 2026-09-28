class Solution:
    def findRedundantConnection(self, edges: list[list[int]]) -> list[int]:
        n = len(edges) + 1
        parent = [i for i in range(n)]
        weight = [1] * n

        def find(x):
            if x == parent[x]:
                return x
            parent[x] = find(parent[x])
            return parent[x]
        
        def union(u,v):
            parentU = find(u)
            parentV = find(v)

            if parentU == parentV:
                return [u,v]
            
            if weight[parentU] > weight[parentV]:
                weight[parentU] += weight[parentV]
                parent[parentV] = parentU
            else:
                weight[parentV] += weight[parentU]
                parent[parentU] = parentV
            
            return [-1, -1]
        
        for u, v in edges:
            a,b = union(u,v)
            if a != -1 and b != -1:
                return [a,b]
             


        