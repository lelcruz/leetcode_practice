class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        i = 0
        while i < len(s):
            for word in wordDict:
                if s[i:i+len(word)] == word:
                    i += len(word)
                    break
            else:
                return False
        return True
        
