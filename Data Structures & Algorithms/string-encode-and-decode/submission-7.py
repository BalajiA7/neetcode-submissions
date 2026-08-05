class Solution:

    def encode(self, strs: List[str]) -> str:
        resStr = ""
        for items in strs:
            resStr += str(len(items)) + "#" + items
        print(resStr)
        return resStr

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0

        while i < len(s):
            j = i
            # Get the interger
            while s[j] != "#":
                j+=1
            length = int(s[i:j])
            # move right one step 
            end = j+length+1
            res.append(s[j+1:j+length+1])
            i = j+length+1

        return res

            

