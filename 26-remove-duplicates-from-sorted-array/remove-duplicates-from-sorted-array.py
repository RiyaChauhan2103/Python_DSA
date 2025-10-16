class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        idx=0
        seen=set()
        for i in range(len(nums)):
            if nums[i] not in seen:
                seen.add(nums[i])
                nums[idx]=nums[i]
                idx+=1
        return idx