class Solution:

    def encode(self, strs: List[str]) -> str:
        encodedStr = ""
        for word in strs:
            encodedStr += str(len(word)) + "#" + word
        return encodedStr

    def decode(self, s: str) -> List[str]:
        n = len(s)
        res = []
        i = 0

        while i < n:
            j = i
            while s[j] != "#":
                j+=1
            length = int(s[i:j])
            res.append(s[j+1: j+1+length])
            i = j+1+length
        
        return res


