class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        n = len(words)
        adjList = {c:set() for word in words for c in word}

        for i in range(n-1):
            w1 = words[i]
            w2 = words[i+1]
            length = min(len(w1), len(w2))

            if len(w1) > len(w2) and w1[:length] == w2[:length]:
                return ""
            
            for j in range(length):
                if w1[j] != w2[j]:
                    adjList[w1[j]].add(w2[j])
                    break
        print(adjList)
        visited = {}
        # true -> cycle
        # false -> already processed

        res = []
        def dfs(c):
            if c in visited:
                return visited[c]
            
            visited[c] = True
            for neiC in adjList[c]:
                if dfs(neiC):
                    return True
            visited[c] = False

            res.append(c)
        
        for c in adjList:
            if dfs(c):
                return ""
        
        res.reverse()
        return "".join(res)