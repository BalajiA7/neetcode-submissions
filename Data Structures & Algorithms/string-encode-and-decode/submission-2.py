class Solution:

    def encode(self, strs: List[str]) -> str:
        if len(strs) == 0: return "Array is Empty"
        encoded_str = strs[0]
        for i in range(0, len(strs)-1):
            encoded_str = encoded_str + "¢" + strs[i+1]
        return encoded_str


    def decode(self, s: str) -> List[str]:
        if s == "Array is Empty": return []
        return s.split("¢")
