class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        char = {
            '1', '2', '3', '4', '5', '6', '7', '8', '9',
            '10', '11', '12', '13', '14', '15', '16', '17',
            '18', '19', '20', '21', '22', '23', '24', '25', '26'
        }
        # memo = {}
        dp = [0] * (n+1)
        next1 = 1
        next2 = 0

        for i in range(n-1, -1, -1):
            count = 0
            for j in range(i, min(i+2, n)):
                val = s[i:j+1]
                if val in char:
                    if i == j:
                        count += next1
                    else:
                        count += next2

            next2 = next1
            next1 = count

        return next1

        # def decodeNums(idx):
        #     if idx == n:
        #         return 1
            
        #     if idx in memo:
        #         return memo[idx]
            
        #     count = 0
        #     for i in range(idx, min(idx+2, n)):
        #         val = s[idx:i+1]
        #         print(val)
        #         if val in char:
        #             count += decodeNums(i+1)

        #     memo[idx] = count
        #     return count
        
        # return decodeNums(0)
            

        