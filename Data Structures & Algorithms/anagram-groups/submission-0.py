class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anag = {}
        for s in strs:
            if "".join(sorted(s)) in anag:
                anag["".join(sorted(s))].append(s)
            else:
                anag["".join(sorted(s))] = [s]
        
        return [anag[i] for i in anag]