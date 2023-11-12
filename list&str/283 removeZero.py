class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        slow, fast = 0, 0
        next_0 = []
        while fast < len(nums):
            if nums[fast] == 0:
                next_0.append(fast)
                fast += 1
            elif fast < len(nums) and nums[fast] != 0:
                if len(next_0) >= 1:
                    slow = next_0[0]
                    temp = nums[slow]
                    nums[slow] = nums[fast]
                    nums[fast] = temp
                    next_0.append(fast)
                    try:
                        next_0 = next_0[1:len(next_0)]
                    except IndexError:
                        next_0 = []
                fast += 1