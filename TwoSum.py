class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
       hashSet = {}
       for i, num in enumerate(nums):
           if target - num in hashSet:
               return hashSet[target-num], i
           else:
                hashSet[num] = i