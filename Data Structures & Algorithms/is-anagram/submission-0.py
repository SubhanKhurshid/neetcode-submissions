class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hashmap = {}
        if (len(s) == len(t)):
            for item in s:
                if item not in hashmap:
                    hashmap[item] = 1
                else:
                    hashmap[item] += 1
            for i in t:
                if i in hashmap and hashmap[i] != 0:
                    hashmap[i] -= 1
                else:
                    return False
            return True
        else:
            return False