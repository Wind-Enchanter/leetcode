# class Solution:
#     def merge(self, intervals: List[List[int]]) -> List[List[int]]:
#         intervals.sort(key=lambda x: x[0])
#
#         merged = []
#         for interval in intervals:
#             # 如果列表为空，或者当前区间与上一区间不重合，直接添加
#             if not merged or merged[-1][1] < interval[0]:
#                 merged.append(interval)
#             else:
#                 # 否则的话，我们就可以与上一区间进行合并
#                 merged[-1][1] = max(merged[-1][1], interval[1])
#
#         return merged
# 将列表中的区间按照左端点升序排序。然后我们将第一个区间加入 merged 数组中，并按顺序依次考虑之后的每个区间：
# 如果当前区间的左端点在数组 merged 中最后一个区间的右端点之后，那么它们不会重合，我们可以直接将这个区间加入数组 merged 的末尾；
# 否则，它们重合，我们需要用当前区间的右端点更新数组 merged 中最后一个区间的右端点，将其置为二者的较大值。


class Solution:
    # def no_repeat(self, intervals: list[list[int]], new_interval: list[int]) -> list[list[int]]:
    def no_repeat(self, intervals: list, new_interval: list) -> list:
        output = []
        l_new = new_interval[0]
        r_new = new_interval[1]
        # 目标区间只有一个，添加或合并
        if len(intervals) == 1:
            res = []
            l_1 = intervals[0][0]
            r_1 = intervals[0][1]
            if r_1 < l_new:
                res.append(intervals[0])
                res.append(new_interval)
                return res
            elif r_new < l_1:
                res.append(new_interval)
                res.append(intervals[0])
                return res
            else:
                temp = []
                temp.append(min([l_1, l_new, r_1, r_new]))
                temp.append(max([l_1, l_new, r_1, r_new]))
                res.append(temp)
            return res
        # 多个目标区间，添加或合并区间
        else:
            # 左添加
            if r_new < intervals[0][0]:
                intervals.append([])
                for i in range(0, len(intervals)-1):
                    intervals[len(intervals) - i -1] = intervals[len(intervals) - 2 - i]
                intervals[0] = new_interval
                return intervals
            # 右添加
            if l_new > intervals[len(intervals) - 1][1]:
                intervals.append(new_interval)
                return intervals
            else:
                # 中间添加
                for i in range(0, len(intervals) - 1):
                    if r_new < intervals[i + 1][0] and l_new > intervals[i][1]:
                        for i in range(0, i+1):
                            output.append(intervals[i])
                        output.append(new_interval)
                        for i in range(i+1, len(intervals)):
                            output.append(intervals[i])
                        return output
                # 合并
                l_in = 0
                r_in = len(intervals) - 1
                if l_new <= intervals[0][0]:
                    l_in = 0
                if r_new >= intervals[len(intervals) - 1][1]:
                    r_in = len(intervals) - 1
                # 标记左合并点
                for i in range(1, len(intervals)):
                    if intervals[i-1][1] < l_new <= intervals[i][1]:
                        l_in = i
                # 标记右合并点
                for i in range(l_in, len(intervals)-1):
                    if intervals[i][0] <= r_new < intervals[i+1][0]:
                        r_in = i
                # 落在某区间里面或者给某区间单侧加长或者包含某区间
                if l_in == r_in:
                    intervals[l_in][0] = min([intervals[l_in][0], l_new])
                    intervals[r_in][1] = max([intervals[r_in][1], r_new])
                    return intervals
                # l_in != r_in ，涉及多个区间
                else:
                    for i in range(0, l_in):
                        output.append(intervals[i])
                    l_temp = min([intervals[l_in][0], l_new])
                    r_temp = max([intervals[r_in][1], r_new])
                    output.append([l_temp, r_temp])
                    for i in range(r_in + 1, len(intervals)):
                        output.append(intervals[i])
                    return output

    # def merge(self, intervals: list[list[int]]) -> list[list[int]]:
    def merge(self, intervals: list) -> list:
        temp = [intervals[0]]
        if len(intervals) > 1:
            for i in range(1, len(intervals)):
                temp = self.no_repeat(temp, intervals[i])
        return temp

# if __name__=="__main__":
#     my_so = Solution()
#     temp = [[2,3],[2,2],[3,3],[1,3],[5,7],[2,2],[4,6]]
#     res = my_so.merge(temp)
#     print(str(res))