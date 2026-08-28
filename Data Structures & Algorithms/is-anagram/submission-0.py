class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        ##return sorted(s) == sorted(t)

        freqS = {}
        freqT = {}

        if len(s) != len(t): return False

        for letter in s:
            if letter in freqS:
                freqS[letter] += 1
            else:
                freqS[letter] = 1
        for letter in t:
            if letter in freqT:
                freqT[letter] += 1
            else:
                freqT[letter] = 1
        return freqS == freqT
        