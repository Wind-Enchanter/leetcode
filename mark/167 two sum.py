
# class Solution:
#     # 找到中间位置，然后双指针一个向前找，一个从前往后找（注意边界和numbers长度为2的情况）
#     # 尝试了二分查找，递归找中间位置，不太会处理递归返回值
#     # 尝试了双指针一个从mid向前找，一个向后找，但是不太会处理 左+中 和 右+中 的情况
#     def middle(self, numbers: List[int], target: int) -> int:
#         for i in range(0, len(numbers)):
#             if target <= 2 * numbers[i]:
#                 return i
#
#     def twoSum(self, numbers: List[int], target: int) -> List[int]:
#         res = [0, 0]
#         n = len(numbers)
#
#         if n == 2:
#             if sum(numbers) == target:
#                 return [1, 2]
#             else:
#                 return [0, 0]
#
#         mid = self.middle(numbers, target)
#         for i in range(mid, -1, -1):
#             for j in range(0, mid):
#                 if numbers[i] + numbers[j] == target:
#                     res[0] = i + 1
#                     res[1] = j + 1
#                     return sorted(res)
#             for j in range(mid + 1, len(numbers)):
#                 if numbers[i] + numbers[j] == target:
#                     res[0] = i + 1
#                     res[1] = j + 1
#                     return sorted(res)
#
#         return res
#
#
# if __name__=="__main__":
#     my_so = Solution()
#     # temp = [-1,0]
#     # temp = [1,2,3,4,4,9,56,90]
#     temp = [3, 24, 50, 79, 88, 150, 345]
#     res = my_so.twoSum(temp,-2)
#     print(str(res))