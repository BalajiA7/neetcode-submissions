class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_group = defaultdict(list)

        for curr_str in strs:
            key = tuple(sorted(curr_str))
            anagram_group[key].append(curr_str)
        
        return list(anagram_group.values())

