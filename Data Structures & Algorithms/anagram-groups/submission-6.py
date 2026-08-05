class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        seen = set()
        group = defaultdict(list)

        for i in range(len(strs)):
            freq = [0] * 26
            for s in strs[i]:
                freq[ord(s) - ord('a')] +=1

            key = tuple(freq)
            group[key].append(strs[i])
        
        return list(group.values())
            
            # if strs[i] not in seen:
            #     res = []
            #     res.append(strs[i])
            #     seen.add(strs[i])
            #     mapA = {}
            #     for s in strs[i]:
            #         mapA[s] = mapA.get(s, 0) + 1

            #     for j in range(i+1, len(strs)):
            #         # check anagram
            #         mapB = {}
            #         for s in strs[j]:
            #             mapB[s] = mapB.get(s, 0) + 1
                    
            #         if mapA == mapB:
            #             seen.add(strs[j])
            #             res.append(strs[j])

            #     group.append(res)

        