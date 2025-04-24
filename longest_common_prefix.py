class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        common_prefix = ""
        for i in range(len(strs[0])):
            for word in strs:
                if word[i] != strs[0][i]:
                    return common_prefix
            common_prefix += strs[0][i]

        return common_prefix
            
