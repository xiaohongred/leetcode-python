from collections import defaultdict
from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)  # mapping charCount to List of Anagrams
        for s in strs:
            count = [0] * 26  # a ...z
            for c in s:
                count[ord(c) - ord('a')] += 1

            res[tuple(count)].append(s)
        result = []
        for v in res:
            result.append(res[v])
        return result


if __name__ == '__main__':
    strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
    s = Solution()
    a = s.groupAnagrams(strs)
    print(a)
