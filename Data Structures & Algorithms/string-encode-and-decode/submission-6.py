class Solution:
    def encode(self, strs: List[str]) -> str:
        encoded_str = ""
        for val in strs:
            encoded_str += str(len(val)) + "#" + val
        return encoded_str


    def decode(self, s: str) -> List[str]:
        result = []
        curr_idx = 0
        while(curr_idx < len(s)):
            # size = int(s[curr_idx])
            num = ""
            while(s[curr_idx] != "#"):
                num += s[curr_idx]
                curr_idx += 1

            start_idx = curr_idx + 1
            end_idx = start_idx + int(num)
            result.append(s[start_idx:end_idx])
            curr_idx = end_idx
        return result
            
