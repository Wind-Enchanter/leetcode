class Solution:
    def spiralOrder(self, matrix: list) -> list:
        res = []
        while matrix:
            # 削头（第一层）
            res += matrix.pop(0)
            # 将剩下的逆时针转九十度，等待下次被削
            unzipped = zip(*matrix)
            un_list = list(unzipped)
            matrix = un_list[::-1]
        return res

# 我的方法：递归，注意每次的返回条件，以及注意矩阵的选择区域方式
# 好方法：每次输出第一层，然后逆时针旋转，再输出第一层

# class Solution:
#     def spiralOrder(self, matrix: list) ->list:
#         res = []
#         try:
#             m, n = len(matrix), len(matrix[0])
#         except IndexError:
#             return []
#         if m == 0 or n == 0:
#             return []
#         if m == 1:
#             return matrix[0]
#         if n == 1:
#             for num in matrix:
#                 res += num
#             return res
#         last = n - 1
#         for i in range(0, n):
#             res.append(matrix[0][i])
#         for i in range(1, m - 1):
#             res.append(matrix[i][last])
#         for i in range(n - 1, -1, -1):
#             res.append(matrix[m - 1][i])
#         for i in range(m - 2, 0, -1):
#             res.append(matrix[i][0])
#         next = []
#         for nums in matrix[1:m-1]:
#             next.append(nums[1:n-1])
#         res = res + self.spiralOrder(next)
#
#         return res
#

if __name__ == "__main__":
   my_so = Solution()
   temp = [[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15],[16,17,18,19,20],[21,22,23,24,25]]
   print(my_so.spiralOrder(temp))
#

