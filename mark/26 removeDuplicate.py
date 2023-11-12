# class Solution:
#     def removeDuplicates(self, nums: List[int]) -> int:
#         info = {}
#         res = 0
#         keys = []
#         for i in range(0, len(nums)):
#             try:
#                 info[nums[i]] += 1
#             except KeyError:
#                 info[nums[i]] = 1
#
#         for k, x in info.items():
#             keys.append(k)
#
#         for i in range(0, len(keys)):
#             nums[i] = keys[i]
#
#         return len(keys)
# 方法1：存储计数字典，返回不重复的key数量n，并覆盖原列表前n项
# 方法2：双指针，一个指向待插入位置，另一个指向下一个不重复的数（双指针一个循环就可以，注意写法）

# class Solution:
#     def removeDuplicates(self, nums: List[int]) -> int:
#         cnt = 0
#         if len(nums) == 1:
#             return 1
#         if len(nums) == 2:
#             if nums[0] == nums[1]:
#                 return 1
#             else:
#                 return 2
#         i,j = 0, 0
#         while i < len(nums):
#             while j < len(nums) and nums[j]==nums[i-1]:
#                 j += 1
#             if i < len(nums) and j < len(nums):
#                 nums[i] = nums[j]
#             i += 1
#             if nums[i-1] == nums[len(nums)-1]:
#                 break
#         return i

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0

        n = len(nums)
        fast = slow = 1
        while fast < n:
            if nums[fast] != nums[fast - 1]:
                nums[slow] = nums[fast]
                slow += 1
            fast += 1

        return slow
