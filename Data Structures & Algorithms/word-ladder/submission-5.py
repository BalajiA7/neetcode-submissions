class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0

        wordList.append(beginWord)
        n = len(wordList)
        adjacentList = defaultdict(list)
        visited = set()

        # Building Adjacent List 
        def wordDiff(s1, s2):
            count = 0
            for i in range(len(s1)):
                if s1[i] != s2[i]:
                    count+=1
            return count

        for i in range(n):
            s1 = wordList[i]
            for j in range(i+1, n):
                s2 = wordList[j]
                if wordDiff(s1, s2) == 1:
                    adjacentList[s1].append(s2)
                    adjacentList[s2].append(s1)
        
        queue = deque([(beginWord,1)])
        visited.add(beginWord)

        while queue:
            word, distance = queue.popleft()
            if word == endWord:
                return distance
              
            for similarWord in adjacentList[word]:
                if similarWord not in visited:
                    visited.add(similarWord)
                    queue.append((similarWord, distance+1))
        
        return 0 

        