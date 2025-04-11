class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        max_length = 0
        char_map = {}
        left = 0

        for right in range(n):
            if s[right] not in char_map or char_map[s[right]] < left:
                char_map[s[right]] = right
                max_length = max(max_length, right - left + 1)
            else:
                left = char_map[s[right]] + 1
                char_map[s[right]] = right
        return max_length
        
