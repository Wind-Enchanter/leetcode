class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        i = 0
        while i < len(nums):
            l_sum = 0
            r_sum = 0
            l_i = 0
            r_i = i + 1
            while l_i < i:
                l_sum += nums[l_i]
                l_i += 1

            while r_i < len(nums):
                r_sum += nums[r_i]
                r_i += 1

            if l_sum == r_sum:
                return i
            else:
                i += 1

        return -1

# class Solution:
#     def pivotIndex(self, nums: List[int]) -> int:
#         all = sum(nums)
#         left = 0
#         for i in range(len(nums)):
#             if left * 2 + nums[i] == all:
#                 return i
#             else:
#                 left += nums[i]
#         return -1
# 先计算总和，然后遍历计算left总和，如果left总和×2加当前值等于总和，就返回当前值