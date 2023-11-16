# class Solution:
#     def myAtoi(self, str: str) -> int:
#         str = str.strip()                      # 删除首尾空格
#         if not str: return 0                   # 字符串为空则直接返回
#         res, i, sign = 0, 1, 1
#         int_max, int_min, bndry = 2 ** 31 - 1, -2 ** 31, 2 ** 31 // 10
#         if str[0] == '-': sign = -1            # 保存负号
#         elif str[0] != '+': i = 0              # 若无符号位，则需从 i = 0 开始数字拼接
#         for c in str[i:]:
#             if not '0' <= c <= '9' : break     # 遇到非数字的字符则跳出
#             if res > bndry or res == bndry and c > '7': return int_max if sign == 1 else int_min # 数字越界处理
#             res = 10 * res + ord(c) - ord('0') # 数字拼接
#         return sign * res
#
#

# 方法1：删除空格、判断符号、计算数字
# 方法2：有限状态机
# 方法3：（我的）判断符号、计算数字（有点臃肿，但时间复杂度也是On）（但是转换数字有待修改）

INT_MAX = 2 ** 31 - 1
INT_MIN = -2 ** 31


class Automaton:
    def __init__(self):
        self.state = 'start'
        self.sign = 1
        self.ans = 0
        self.table = {
            'start': ['start', 'signed', 'in_number', 'end'],
            'signed': ['end', 'end', 'in_number', 'end'],
            'in_number': ['end', 'end', 'in_number', 'end'],
            'end': ['end', 'end', 'end', 'end'],
        }

    def get_col(self, c):
        if c.isspace():
            return 0
        if c == '+' or c == '-':
            return 1
        if c.isdigit():
            return 2
        return 3

    def get(self, c):
        self.state = self.table[self.state][self.get_col(c)]
        if self.state == 'in_number':
            self.ans = self.ans * 10 + int(c)
            self.ans = min(self.ans, INT_MAX) if self.sign == 1 else min(self.ans, -INT_MIN)
        elif self.state == 'signed':
            self.sign = 1 if c == '+' else -1


class Solution:
    def myAtoi(self, str: str) -> int:
        automaton = Automaton()
        for c in str:
            automaton.get(c)
        return automaton.sign * automaton.ans



# class Solution:
#     def myAtoi(self, s: str) -> int:
#         max_n = pow(2, 31) - 1
#         min_n = -max_n - 1
#
#         num_list = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
#         cal_list = ["+", "-"]
#         nos = [".", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t",
#                "u", "v", "w", "x", "y", "z"]
#         num = ""
#         cal, cnt = "", 0
#         flag, temp = 0, 0
#         for i in range(0, len(s)):
#             if s[i] in num_list:
#                 if flag == 0:
#                     temp = i
#                     flag = 1
#                 num += s[i]
#                 if i == len(s) - 1 or s[i + 1] in num_list:
#                     continue
#                 else:
#                     break
#         if len(num) == 0:
#             return 0
#
#         for i in range(0, temp):
#             if s[i] in nos:
#                 return 0
#             if s[i] in cal_list:
#                 cal += s[i]
#                 if s[i] == "-":
#                     cnt += 1
#                 if i == len(s) - 1 or s[i + 1] in cal_list:
#                     continue
#                 else:
#                     break
#
#         mul = 1
#         if temp >= 1:
#             if s[temp - 1] in cal_list:
#                 if s[temp - 1] == "-":
#                     mul = -1
#             elif len(cal) == 0:
#                 mul = 1
#             else:
#                 return 0
#
#         if len(cal) > 1:
#             return 0
#
#         res = mul * int(num)
#
#         if res > max_n:
#             return max_n
#         if res < min_n:
#             return min_n
#
#         return res


if __name__ == "__main__":
    my_so = Solution()
    temp = "  0000000000012345678"
    print(my_so.myAtoi(temp))
