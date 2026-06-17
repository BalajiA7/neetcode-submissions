class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if(len(s) != len(t)):
            return False

        char_freq = [0] * 26

        for i in range(len(s)):
            s_idx = ord(s[i]) - ord('a')
            t_idx = ord(t[i]) - ord('a')
            char_freq[s_idx] += 1
            char_freq[t_idx] -= 1

        # for char in s:
        #     idx = ord(char) - ord('a')
        #     char_freq[idx] = char_freq[idx] + 1

        # for char in t:
        #     idx = ord(char) - ord('a')
        #     char_freq[idx] = char_freq[idx] - 1

        for val in char_freq:
            if val != 0:
                return False

        return True        



        