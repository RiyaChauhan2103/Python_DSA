class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # Loop backwards
        for i in range(len(nums) - 1, -1, -1):
            if nums[i] == val:
                nums.pop(i)   # remove the element if it's equal to val

        # print for debugging (optional)
        print(nums)

        # return the count of remaining elements
        return len(nums)

