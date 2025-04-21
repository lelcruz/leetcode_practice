class Solution:
    def romanToInt(self, s: str) -> int:
        integer = 0
        translate = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000}
        roman = len(s)
        

        for char in range(roman - 1) :
            if translate[s[char]] < translate[s[char + 1]]:
                integer -= translate[s[char]]
            else:
                integer += translate[s[char]]
        integer += translate[s[-1]]
            
        return integer
                
                    
