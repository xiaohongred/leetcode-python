import collections
from typing import List


class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        nei = collections.defaultdict(list)  # pattern: [word1, word2, ...]
        wordList.append(beginWord)
        for word in wordList:
            for j in range(len(word)):
                pattern = word[:j] + "*" + word[j + 1:]
                nei[pattern].append(word)

        visited = set([beginWord])
        q = collections.deque([beginWord])
        res = 1
        while q:
            qLen = len(q)
            for i in range(qLen):
                word = q.popleft()
                if word == endWord:  # 变化成了 endWord, 返回
                    return res
                for j in range(len(word)):  # 对word这个词，找只与其差一个字母的单词
                    pattern = word[:j] + "*" + word[j + 1:]  # pattern 代表哪个字母不同
                    for neiWord in nei[pattern]:  # nei[pattern] 代表这个字母不同的单词有哪些
                        if neiWord not in visited:
                            visited.add(neiWord)
                            q.append(neiWord)
            res += 1

        return 0


if __name__ == '__main__':
    s = Solution()

    beginWord = "hit"
    endWord = "cog"
    wordList = ["hot", "dot", "dog", "lot", "log", "cog"]
    a = s.ladderLength(beginWord, endWord, wordList)
    print(a)
