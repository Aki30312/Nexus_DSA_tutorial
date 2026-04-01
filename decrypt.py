class Solution:
    def freqAlphabets(self, s: str) -> str:
        mapping = {str(i): chr(96+i) for i in range(1, 27)}
        
        result = ""
        i = 0
        
        while i < len(s):
            if i+2 < len(s) and s[i+2] == '#':
                result += mapping[s[i:i+2]]
                i += 3
            else:
                result += mapping[s[i]]
                i += 1
                
        return result
    
