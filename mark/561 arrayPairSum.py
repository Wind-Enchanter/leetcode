class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums = sorted(nums)
        return sum(nums[0:len(nums)-1:2])

# 第一次和标答一样，而且速度内存都占优