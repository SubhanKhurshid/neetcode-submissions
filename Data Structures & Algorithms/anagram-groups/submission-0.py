class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = {}
        for i, val in enumerate(strs):
            key = tuple(sorted(val))
            if key not in hashmap:
                hashmap[key] = []
                hashmap[key].append(val)
            else:
                hashmap[key].append(val)
        return list(hashmap.values())


    