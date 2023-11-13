class Solution:
    def longestPalindrome(self, s: str) -> int:
        alpha_dict = {}
        res = 0
        max_odd = 0
        all_odd = 0
        for i in range(len(s)):
            try:
                alpha_dict[s[i]] += 1
            except KeyError:
                alpha_dict[s[i]] = 1

        for i in alpha_dict:
            if alpha_dict[i] % 2 == 0:
                res += alpha_dict[i]
            if alpha_dict[i] % 2 == 1 and alpha_dict[i] > max_odd:
                max_odd = alpha_dict[i]
        for i in alpha_dict:
            if alpha_dict[i] % 2 == 1 and alpha_dict[i] > 1:
                all_odd += alpha_dict[i] - 1
        if max_odd > 1:
            all_odd = all_odd - (max_odd - 1)
        return res + all_odd + max_odd

if __name__=="__main__":
    my_so = Solution()
    temp = "civil"
    res = my_so.longestPalindrome(temp)
    print(str(res))


# class Solution:
#     def longestPalindrome(self, s: str) -> int:
#         # k神解答
#
#         # 统计字符次数
#         dic = {}
#         for i in s:
#             if i not in dic:
#                 dic[i] = 1
#             else:
#                 dic[i] += 1
#         res = 0
#         odd = 0
#         # 统计构造回文串的最大长度
#         for i in dic.values():
#             # 【i%2】d的目的是，区分奇数和偶数
#             # 符合题目要求中的回文组合中，总结起来就是【偶数都要，奇数只计算1次】
#             # 如果i是奇数，【i%2】就会得1，那【i-rem】就会变成偶数
#             # 如果i是偶数，【i%2】就会得0，那【i-rem】就还是偶数
#             # 按照我们需要【把偶数都要】的结论来说，res里面就计算了【所有字母偶数个的数量】
#             # 注意，奇数的偶数个，也是算在这里面的，比如说3算了2进去，5算了4进去
#             rem = i % 2
#             res += i - rem
#             # 再按照我们需要【把奇数只算1次】的结论来说，
#             # 当取余数rem为1时，说明i是奇数，要算1次奇数，那就给最后的结果中补偿一个1
#             # 注意，这条语句会重复执行，但odd始终都为1且不管有几个奇数，odd都只算进去一次
#             if rem == 1: odd = 1
#         # 最后返回res和odd的和就是答案
#         return res + odd