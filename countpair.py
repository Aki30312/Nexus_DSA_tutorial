class Solution:
    def similarPairs(self, words):
        count = 0
        sets = [set(word) for word in words]
        for i in range(len(words)):
            for j in range(i + 1, len(words)):
                if sets[i] == sets[j]:
                    count += 1
                    
        return count
        
