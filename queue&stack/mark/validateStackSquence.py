class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        st, j = [], 0
        for x in pushed:
            st.append(x)
            while st and st[-1] == popped[j]:
                st.pop()
                j += 1
        return len(st) == 0

# 题解：模拟出栈过程
# 我的方法：验证序列的性质

# class Solution:
#     def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
#         cnt = {}
#         map_num = {}
#
#         for i in range(0, len(popped)):
#             for j in range(0, len(pushed)):
#                 if popped[i] == pushed[j]:
#                     map_num[popped[i]] = j
#
#         last_zero = -1
#         for num in pushed:
#             cnt[num] = 1
#
#         for i in range(0, len(popped)):
#             if cnt[popped[i]] == 0:
#                 return False
#             pop_num_in_push = map_num[popped[i]]
#             if pop_num_in_push < last_zero:
#                 if last_zero != pop_num_in_push + 1:
#                     for j in pushed[pop_num_in_push + 1:last_zero]:
#                         if cnt[j] != 0:
#                             return False
#                         else:
#                             cnt[popped[i]] = 0
#                             continue
#                 else:
#                     cnt[popped[i]] = 0
#                     continue
#
#             elif pop_num_in_push > last_zero:
#                 last_zero = pop_num_in_push
#                 cnt[popped[i]] = 0
#             else:
#                 return False
#
#         return True