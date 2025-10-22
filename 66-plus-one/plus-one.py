class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        # carry=1
        for i in range(len(digits)-1,-1,-1):
            digits[i]=(digits[i]+1)%10;
            if i==0 and digits[i]==0:
                digits.insert(0,1)
            elif digits[i]!=0:
                return digits
        return digits
            

