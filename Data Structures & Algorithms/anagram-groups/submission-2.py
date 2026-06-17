class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = []
        anagram_group = {}

        for curr_str in strs:
            key = tuple(sorted(curr_str))
            # if key present append/create    
            if key in anagram_group:
                anagram_group[key].append(curr_str)
            else:
                anagram_group[key] = [curr_str]
        
        for curr_group in anagram_group.values():
            result.append(curr_group)
        
        return result


