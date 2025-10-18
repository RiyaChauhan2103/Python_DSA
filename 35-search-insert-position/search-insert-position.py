class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        # for i in range(len(nums)):
        #     if nums[i]==target:
        #         return i
        #     elif nums[i]>target:
        #         return i
         
        # return len(nums)
        if target> nums[-1]:
            return len(nums)
        if target < nums[0]:
            return 0
        low ,high = 0, len(nums) - 1
        while low <= high:
            mid = (low + high) // 2
            if nums[mid] == target: 
                return mid
            if nums[mid] < target: 
                low = mid + 1
                if low < len(nums) and nums[low]>target:
                    return low
            else: 
                high = mid - 1

