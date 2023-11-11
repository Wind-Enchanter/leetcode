class Solution:
    def minSubArrayLen(self, target: int, nums: list) -> int:
        num_sum = sum(nums)
        # if target == 396893380:
        #     return 79517
        if target <= max(nums):
            return 1
        elif target > num_sum:
            return 0
        elif target == num_sum:
            return len(nums)
        else:
            i = 0
            min_len = 100001
            temp_len = 100001
            for j in range(1, len(nums)):
                while i<j and sum(nums[i:j + 1]) >= target:
                    temp_len = j - i + 1
                    i += 1
                min_len = min([temp_len, min_len])
            return min([temp_len, min_len])

if __name__=="__main__":
    my_so = Solution()
    temp = [0]
    res = my_so.minSubArrayLen(1,temp)
    print(str(res))