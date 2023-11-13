# 直接模拟
class Solution:
    def findDiagonalOrder(self, mat: list) -> list:
        res = []
        flag = 0
        temp_sum = 0
        m,n = len(mat),len(mat[0])
        if m==1:
            return mat[0]
        if n == 1:
            for small in mat:
                res += small
            return res
        while temp_sum <= m+n-2:
            if flag == 1:
                for i in range(0,temp_sum+1):
                    try:
                        res.append(mat[i][temp_sum-i])
                    except IndexError:
                        continue
                    flag = 0
            else:
                for i in range(temp_sum,-1,-1):
                    try:
                        res.append(mat[i][temp_sum-i])
                    except IndexError:
                        continue
                    flag = 1
            temp_sum += 1
        return res

if __name__=="__main__":
    my_so = Solution()
    temp = []
    res = my_so.findDiagonalOrder(temp)
    print(str(res))
