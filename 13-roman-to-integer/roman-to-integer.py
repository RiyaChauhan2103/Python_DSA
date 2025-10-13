class Solution:
    def romanToInt(self, s: str) -> int:
        roman_to_int={"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
        # total_sum=romanToInt[s[-1]]
        # x={'I':['V','X'],'X':['L','C'],'C':['D','M']}
        # # z=['V','L','D','X','C','M']
        # for i in range(len(s)-2,-1,-1):
        #     # if s[i+1] in z and s[i] in x and s[i+1]!=s[i] :
        #     if s[i] in x and s[i+1] in x[s[i]]:
        #         total_sum-=romanToInt[s[i]]                    
        #     else:
        #         total_sum+=romanToInt[s[i]]
        # return total_sum

        # 2nd solution
        prev=0
        total=0
        for ch in reversed(s):
            v=roman_to_int[ch]
            if v<prev:
                total-=roman_to_int[ch]
            else:
                total+=roman_to_int[ch]
            prev=v
        return total
            