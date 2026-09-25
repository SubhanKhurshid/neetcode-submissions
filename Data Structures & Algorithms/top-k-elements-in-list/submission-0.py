class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = {}
        for i, val in enumerate(nums):
            if val not in hashmap:
                hashmap[val] = 1
            else:
                hashmap[val] += 1

        sorted_map = sorted(hashmap.items(), key=lambda x:x[1], reverse=True)
        my_list = []
        for i, val in enumerate(sorted_map[:k]):
            my_list.append(val[0])

        return my_list
