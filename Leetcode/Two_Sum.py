# 作者：Alex
# 2024/10/15 16:39
class Solution:
    @staticmethod
    def twosum(self, nums, target) -> list:
        hashmap = {}
        for i, num in enumerate(nums):
            value = target - num
            if value in hashmap: return[hashmap[value],i]
            else:
                hashmap[num] = i
