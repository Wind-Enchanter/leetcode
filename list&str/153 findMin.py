class Solution:
    def findMin(self, nums: List[int]) -> int:
        i = int(len(nums)/2)
        res = 0
        if len(nums) == 1:
            res = nums[0]
        elif len(nums) == 2:
            if nums[1] < nums[0]:
                res = nums[1]
            else:
                res = nums[0]
        elif nums[i-1] > nums[i]:
            res = nums[i]
        elif nums[i-1] < nums[i]:
            if nums[i+1] > nums[i]:
                if nums[i] < nums[len(nums)-1]:
                    nums = nums[0:i]
                    res = self.findMin(nums)
                else:
                    nums = nums[i+1:len(nums)]
                    res = self.findMin(nums)
            else:
                res = nums[i+1]
        return res