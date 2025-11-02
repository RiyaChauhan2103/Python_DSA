class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        n=len(nums)
        res=[0]*n
        left=0
        right=n-1
        k=n-1
        while left<=right:
            if abs(nums[left])>abs(nums[right]):
                res[k]=nums[left]*nums[left]
                left+=1
                k-=1
            else:
                res[k]=nums[right]*nums[right]
                right-=1
                k-=1
        return res

            


            

            
