class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # # with kadane Algorithm
          
        # # Initialize current_subarray_sum and max_subarray_sum
        current_sum = max_sum = nums[0]

        # # Iterate from the second element onward
        for num in nums[1:]:
            # Decide whether to:
            # 1️ .Start a new subarray from current element (num)
            # 2️ Or extend the previous subarray by adding current element
            current_sum = max(num, current_sum + num)

            # Update the global maximum sum found so far
            max_sum = max(max_sum, current_sum)

            # Return the largest sum of any contiguous subarray
        return max_sum
        # alternate solution
        # max_sub_arr=nums[0]
        # currSum=0
        # for n in nums:
        #     if currSum<0:
        #         currSum=0
        #     currSum+=n
        #     max_sub_arr=max(currSum,max_sub_arr)
        # return max_sub_arr
       
