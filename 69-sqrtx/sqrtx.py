class Solution:
    # def mySqrt(self, x: int) -> int:
    #     if x==1: return 1
    #     min_val=1;
    #     max_val=x//2;
    #     for i in range(1,(x//2)+1):
    #         # print(i)
    #         if i*i==x:
    #             return i
    #         elif i*i<x:
    #             min_val=i;
    #         elif i*i>x:
    #             # print(max_value)
    #             max_val=i
    #             break;
    #     return (min_val+max_val)//2  

    def mySqrt(self, x: int) -> int:
        left,right=1,x
        while left<=right:
            mid=left+(right-left)//2
            if mid*mid==x:
                return mid
            elif mid*mid>x:
                right=mid-1
            else:
                left=mid+1
        return right