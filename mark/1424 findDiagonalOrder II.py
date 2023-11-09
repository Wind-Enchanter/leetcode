# class Solution:
#     def findDiagonalOrder(self, nums: List[List[int]]) -> List[int]:
#         res = []
#         flag = 0
#         temp_sum = 0
#         m = len(nums)
#
#         n = 0
#         for small in nums:
#             if len(small) > n:
#                 n = len(small)
#
#         if m==1:
#             return nums[0]
#         if n == 1:
#             for small in nums:
#                 res += small
#             return res
#
#         while temp_sum <= m+n-2:
#             for i in range(temp_sum,-1,-1):
#                 try:
#                     res.append(nums[i][temp_sum-i])
#                 except IndexError:
#                     continue
#             temp_sum += 1
#         return res
#

# 单看坐标
# [
#   [(0,0),(0,1),(0,2),(0,3),(0,4)]
#   [(1,0),(1,1)]
#   [(2,0)]
#   [(3,0),(3,1),(3,2)]
#   [(4,0),(4,1),(4,2),(4,3),(4,4)]
# ]
# 转化为和
# [
#   [0,1,2,3,4]
#   [1,2]
#   [2]
#   [3,4,5]
#   [4,5,6,7,8]
# ]
# 按和来分组，注意加到组里的顺序
# [[0][1,1][2,2,2][3,3][4,4,4][5,5][6][7][8]]

from typing import List
import collections


class Solution:
  def findDiagonalOrder(self, nums: List[List[int]]) -> List[int]:
    n = len(nums)
    matrix = collections.defaultdict(list)
    for i in range(n):
      for j in range(len(nums[i])):
        # 因为是左上往右下遍历，后遍历的对象插入到前面
        matrix[i+j].insert(0, nums[i][j])
    res = []
    for val in matrix.values():
      res += val
    return res
