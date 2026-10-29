class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(wordDict)
        m = len(s)
        # memo = {len(s): True}
        dp = [False] * (m + 1)
        dp[m] = True

        for idx in range(m-1, -1, -1):
            for word in wordDict:
                length = len(word)
                if s[idx: idx+length] == word and dp[idx+length]:
                    dp[idx] = True

        # def backtrack(idx): 
        #     if idx in memo:
        #         return memo[idx]
            
        #     for i in range(n):
        #         length = len(wordDict[i])
        #         if s[idx: idx+length] == wordDict[i] and backtrack(idx+length):
        #             memo[idx] = True
        #             return True
            
        #     memo[idx] = False
        #     return memo[idx]
        return dp[0]