List = list
class Solution:
    # def rotate(self, matrix: List[List[int]]) -> None:
    def rotate(self, matrix:list) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        c = int((n-n%2)/2)
        # i 表示当前层数
        for i in range(0,c):
            # j 表示该层元素下标
            for j in range(i,n-i-1):
                temp = matrix[i][j]
                matrix[i][j] = matrix[n-j-1][i]
                matrix[n-j-1][i] = matrix[n-1-i][n-1-j]
                matrix[n-1-i][n-1-j] = matrix[j][n-1-i]
                matrix[j][n-1-i] = temp
        return matrix

if __name__=="__main__":
    my_so = Solution()
    temp = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
    res = my_so.rotate(temp)
    print(str(res))