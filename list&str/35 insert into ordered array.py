class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if target > nums[len(nums) - 1]:
            return len(nums)
        if target <= nums[0]:
            return 0
        if target == nums[len(nums) - 1]:
            return len(nums) - 1
        else:
            for i in range(1, len(nums)):
                if target == nums[i]:
                    return i
                if nums[i - 1] < target < nums[i]:
                    return i

# 暴力遍历 Java
# class Solution {
#     public int searchInsert(int[] nums, int target) {
#         for(int i=0;i<nums.length;i++){
#             if(nums[i]>=target) return i;
#         }
#         return nums.length;
#     }
# }



# 二分法
# class Solution:
#     def searchInsert(self, nums: List[int], target: int) -> int:
#         if len(nums) < 1: return 0
#         left = 0
#         right = len(nums) - 1  # 这里使用闭区间
#         while(left <= right):
#             mid = left + (right - left) // 2
#             if nums[mid] == target:
#                 return mid
#             elif nums[mid] > target:
#                 right = mid - 1
#             else:
#                 left = mid + 1
#         return right + 1