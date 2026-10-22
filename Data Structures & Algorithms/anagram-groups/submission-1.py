class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}
        for s in strs:
            group = tuple(sorted(s))
            groups[group] = groups.get(group, []) + [s]
        return list(groups.values())