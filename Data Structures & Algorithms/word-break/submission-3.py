class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(wordDict)
        memo = {len(s): True}

        def backtrack(idx): 
            if idx in memo:
                return memo[idx]
            
            for i in range(n):
                length = len(wordDict[i])
                if s[idx: idx+length] == wordDict[i] and backtrack(idx+length):
                    memo[idx] = True
                    return True
            
            memo[idx] = False
            return memo[idx]
        
        return backtrack(0)