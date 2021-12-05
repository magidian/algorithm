class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        # l, r = 0, len(nums) - 1
        # while l < r:
        #     mid = l + (r-l) // 2
        #     if target == nums[mid]:
        #         return mid
        #     if target < nums[mid]:
        #         r = mid
        #     else:
        #         l = mid
            
        if target not in nums:
            nums.append(target) 
            nums.sort()
        for i in range(len(nums)):
            if nums[i]==target:
                return i