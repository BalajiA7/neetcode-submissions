class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        parent = [i for i in range(n)]
        weight = [1] * n
        self.components = n
        print("Before")
        print(parent)
        print(weight)

        def find(x):
            if x == parent[x]:
                return x
            parent[x] = find(parent[x])
            return parent[x] 
        
        def union(u,v):
            parentU = find(u)
            parentV = find(v)

            if parentU == parentV:
                return
            
            if weight[parentU] > weight[parentV]:
                weight[parentU] += weight[parentV]
                parent[parentV] = parentU
            else:
                weight[parentV] += weight[parentU]
                parent[parentU] = parentV
            
            self.components -=1
        
        for u, v in edges:
            union(u,v)
        
        print("After")
        print(parent)
        print(weight)
        return self.components