class Solution:
    def longestCommonPrefix(self, strs: list) -> str:
        test = ""
        res = ""
        flag = 0
        for k in range(len(strs[0])):
            test = strs[0][0:k+1]
            flag = 1
            for j in range(1,len(strs)):
                if strs[j][0:k+1] == test:
                    continue
                else:
                    flag = 0
                    break
            if flag == 1:
                res = test
        return res


if __name__=="__main__":
    my_so = Solution()
    temp = ["flower","flow","flight"]
    res = my_so.longestCommonPrefix(temp)
    print(str(res))