class Solution:
    def removeElement(self, nums: list, val: int) -> int:
        cnt = 0
        for i in range(0,len(nums)):
            if nums[i] == val:
                nums[i] = -1
            else:
                cnt += 1
        nums.sort(reverse=True)
        return cnt

if __name__=="__main__":
    my_so = Solution()
    temp = [3,2,2,3]
    res = my_so.removeElement(temp,3)
    print(str(res))