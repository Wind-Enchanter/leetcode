# class Solution:
#     def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
#         temp_max = [0]
#         i = 0
#         while i < len(nums):
#             if nums[i] == 1:
#                 j = i
#                 cnt = 0
#                 while j<=len(nums)-1 and nums[j] == 1:
#                     j += 1
#                     cnt += 1
#                 temp_max.append(cnt)
#                 i = j+1
#             else:
#                 i += 1
#                 continue
#         return max(temp_max)
#
"""
我的方法:
是i指针指向每段连续的第一个1，j往后遍历，同时计数，并存到计数数组中，直到遍历到0，然后把i指针移到j指针所指位置，继续向后遍历
得到所有连续1的长度数组，取最大
时间：O(n^2)  空间：O(n)

官方题解：
一次遍历，判断i指针指向元素是否为1，为一则计数，不为一则计算当前计数器是否大于max，并把计数清零
"""


class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_temp = 0
        cnt = 0
        for i in range(0,len(nums)):
            if nums[i] == 1:
                cnt += 1
            else:
                max_temp = max([max_temp,cnt])
                cnt = 0
        return max([max_temp,cnt])