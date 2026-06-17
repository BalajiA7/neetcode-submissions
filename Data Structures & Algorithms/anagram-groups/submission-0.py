class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        list = []
        is_processed = set()

        for i in range(len(strs)):
            a = strs[i]
            sub_list = [a]

            if a in is_processed:
                continue

            # string a freq character
            freq_a = [0] * 26
            for char in a:
                pos = ord(char) - ord('a')
                freq_a[pos] += 1
           
            for j in range(i+1, len(strs)):
                b = strs[j]
                if(len(a) != len(b)):
                    continue
                # string b freq character
                freq_b = freq_a.copy()
                for char in b:
                    pos = ord(char) - ord('a')
                    freq_b[pos] -= 1
                #check is an and b are anagram\
                is_anagram = True
                for val in freq_b:
                    if val != 0:
                        is_anagram = False
                # if anagram
                if is_anagram:
                    sub_list.append(b)
                    is_processed.add(b)
            # finally push that sublist to final list        
            list.append(sub_list)

        return list
        


