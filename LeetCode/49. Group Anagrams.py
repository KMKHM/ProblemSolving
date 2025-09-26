class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        for s in strs:
            ch = "".join(sorted(s))
            res[ch].append(s)
        return list(res.values())