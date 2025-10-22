class Solution:
    def addBinary(self, a: str, b: str) -> str:
        x=int(a,2) #3
        y=int(b,2) #1
        ans=x+y

        res = ''  # binary result
        while ans > 0:
            res = str(ans % 2) + res
            ans //= 2
        return str(ans) if res=='' else res