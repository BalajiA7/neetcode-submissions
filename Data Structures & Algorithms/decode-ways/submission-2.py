class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        char = {
            '1', '2', '3', '4', '5', '6', '7', '8', '9',
            '10', '11', '12', '13', '14', '15', '16', '17',
            '18', '19', '20', '21', '22', '23', '24', '25', '26'
        }
        memo = {}

        def decodeNums(idx):
            if idx == n:
                return 1
            
            if idx in memo:
                return memo[idx]
            
            count = 0
            for i in range(idx, min(idx+2, n)):
                val = s[idx:i+1]
                print(val)
                if val in char:
                    count += decodeNums(i+1)
            memo[idx] = count
            return count
        
        return decodeNums(0)
            

        