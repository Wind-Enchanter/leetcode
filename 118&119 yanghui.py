# class Solution:
#     def getRow(self, rowIndex: int) -> List[int]:
#         res = [[1],[1,1]]
#         if rowIndex == 0 or rowIndex == 1:
#             return res[rowIndex]
#         else:
#             for i in range(2, rowIndex+1):
#                 temp = [1]
#                 for j in range(1, i):
#                     temp.append((res[i-1][j-1]+res[i-1][j]))
#                 temp.append(1)
#                 res.append(temp)
#         return res[rowIndex]
#
# 原办法：计算并存储三角每一行
# 新办法：维护（rowIndex+1）长度的数组，从上一行迭代到最新一行

class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        res = []
        if rowIndex == 0:
            res = [1]
        elif rowIndex == 1:
            res = [1,1]
        else:
            res = [1,1]
            for j in range(2,rowIndex+1):
                for i in range(j-1, 0,-1):
                    res[i] = res[i]+res[i-1]
                res.append(1)
        return res