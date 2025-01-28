class Solution:
    def equalFrequency(self, word: str) -> bool:
        counter = Counter(word)
        for w in word:
            counter[w] -= 1
            if counter[w] == 0:
                counter.pop(w)
            if len(set(counter.values())) == 1:
                return True
            counter[w] += 1
        return False
        
