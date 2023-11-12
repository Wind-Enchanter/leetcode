# # class Solution:
# #     def reverseWords(self, s: str) -> str:
# #         res = ""
# #         for word in s.split(" "):
# #             for i in range(len(word)-1,-1,-1):
# #                 res += word[i]
# #             res += " "
# #         return res.strip(" ")
#
#
# # class Solution:
# #     def reverseWords(self, s: str) -> str:
# #         res = ""
# #         temp = ""
# #         for i in range(len(s)-1,-1,-1):
# #             temp+= s[i]
# #         for word in temp.split(" "):
# #             res = word +" "+ res
# #         return res[0:len(s)]
#
# class Solution:
#     def reverseWords(self, s: str) -> str:
#         words = s.split()
#         reversed_words = [word[::-1] for word in words]
#         return ' '.join(reversed_words)
#
#
# """
# 然后从头到尾遍历原字符串，直到找到空格为止，此时找到了一个单词，并能得到单词的起止位置。随后，根据单词的起止位置，可以将该单词逆序放到新字符串当中。如此循环多次，直到遍历完原字符串，就能得到翻转后的结果。
#
# 作者：LeetCode-Solution
# 链接：https://leetcode.cn/problems/reverse-words-in-a-string-iii/solution/fan-zhuan-zi-fu-chuan-zhong-de-dan-ci-iii-by-lee-2/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
# """

class Solution:
    def reverseWords(self, s: str) -> str:
        s = " " + s + " "
        res = ""
        start = 0
        for i in range(0,len(s)):
            if s[i] == " " and i != 0:
                temp = s[i-1:start:-1]
                res += temp+" "
                start = i
            else:
                continue
        return res[0:len(s)-2]


if __name__ == "__main__":
    my_so = Solution()
    temp = "Let's take LeetCode contest"
    print(my_so.reverseWords(temp))