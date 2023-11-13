# class Solution:
#     def judge(self,s:str):
#         n = int((len(s)-len(s)%2)/2)
#         flag = 1
#         for i in range(n):
#             if s[i] == s[len(s)-1-i]:
#                 continue
#             else:
#                 flag = 0
#                 break
#         return flag
#
#     def longestPalindrome(self, s: str) -> str:
#         res = s[0]
#         temp = ""
#         n = len(s)
#         if n <= 1:
#             return s
#         if n == 2:
#             if s[0] == s[1]:
#                 return s
#             else:
#                 return s[0]
#
#         for i in range(n):
#             for foot in range(n-i,1,-1):
#                 if self.judge(s[i:i+foot]) == 1:
#                     temp = s[i:i+foot]
#                     if len(temp) > len(s)/2:
#                         res = temp
#                         return res
#                     if len(temp)>len(res):
#                         res = temp
#         return res

class Solution:
    def longestPalindrome(self, s: str) -> str:
        temp = ""
        res = ""
        for i in range(1,len(s)-1):
            foot = min([i,len(s)-i-1])
            temp = s[i]
            for f in range(1,foot+1):
                if s[i-f] == s[i+f]:
                    temp = s[i-f] + temp + s[i+f]
                else:
                    break
                if len(temp)>len(res):
                    res = temp

        for i in range(1, len(s)):
            foot = min([i, len(s) - i])
            temp = ""
            for f in range(1, foot + 1):
                if s[i - f] == s[i + f-1]:
                    temp = s[i - f] +temp+ s[i + f-1]
                else:
                    break
                if len(temp) > len(res):
                    res = temp
        return res


if __name__=="__main__":
    my_so = Solution()
    temp = "cccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc"
    res = my_so.longestPalindrome(temp)
    print(str(res))