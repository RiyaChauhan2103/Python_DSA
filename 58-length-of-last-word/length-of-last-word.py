class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        """count=0
        for i in range(len(s)):         
            if s[i]==" "  and i!=len(s)-1 :
                count=0    
            else:
                count+=1
            print(count ,"and" ,s[i])
        return count"""
        count=0
        for i in range(len(s)-1,-1,-1):
            if s[i]==" " and count==0:
                continue
            elif s[i]==" " and count>0:
                return count
            else:
                count+=1
        return count