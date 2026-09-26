class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        my_map = {}
        if len(s) == len(t):
            for item in s:
                if item not in my_map:
                    my_map[item] = 1
                else:
                    my_map[item] += 1
            for item in t:
                if item in my_map and my_map[item] != 0:
                    my_map[item] -= 1
                else:
                    return False
            return True
        else:
            return False