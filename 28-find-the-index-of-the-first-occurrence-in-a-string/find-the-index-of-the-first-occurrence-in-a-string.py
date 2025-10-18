class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        j=0
        # idx=0
        if needle not in haystack:
            return -1
        return haystack.index(needle)