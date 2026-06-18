class Solution:
    def __init__(self):
        self.hash_map = {}

    def encode(self, strs: List[str]) -> str:
        encoded_str = ""
        for i, val in enumerate(strs):
            encoded_str += val
            self.hash_map[i] = len(val)
        return encoded_str


    def decode(self, s: str) -> List[str]:
        result = []
        curr_idx = 0
        print(s, self.hash_map)
        for index, value in self.hash_map.items():
            if index == 0: 
                result.append(s[curr_idx:value])
                curr_idx = value
            else:
                result.append(s[curr_idx:curr_idx+value])
                curr_idx += value
        return result
            
