
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hm = {}

        for word in strs:
            count = [0]*26
            for letter in word:
                count[ord("a")-ord(letter)]+=1
            key = tuple(count)
            if key in hm:
                hm[key].append(word)
            else:
                hm[key] = [word]        


        return list(hm.values())
        

