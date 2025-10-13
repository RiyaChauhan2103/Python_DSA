class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # if not strs:
        #     return ""
        # ans=""
        # strs=sorted(strs)
        # first=strs[0]
        # last=strs[-1]
        # for i in range(min(len(first),len(last))):
        #     if first[i]!=last[i]:
        #         return ans
        #     ans+=first[i]
        # return ans
        if not strs:
            return ""
        prefix = strs[0]
        for s in strs[1:]:
            # shrink prefix until s starts with it
            while not s.startswith(prefix):
                prefix = prefix[:-1]
                if not prefix:
                    return ""
        return prefix