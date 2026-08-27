class Solution:

    def lexGreaterPermutation(self, s: str, target: str) -> str:
        count = [0] * 26

        for c in s:
            index = ord(c) - ord('a')
            count[index] += 1

        curr = ""

        result = ""

        def solve(curr: str, count: list[int], target: str, i: int, greater: bool):
            nonlocal result
            if i == len(target):
                if greater:
                    result = curr
                    return True
                else:
                    return False
            
            for idx in range(0, 26):
                c = chr(ord('a') + idx)
                if count[idx] == 0:
                    continue
                if greater == False and c < target[i]:
                    continue
                curr += c
                count[idx] -= 1
                isGreater = greater or c > target[i]
                if solve(curr, count, target, i+1, isGreater):
                    return True
                curr = curr[:-1]
                count[idx] += 1
            return False




        solve(curr, count, target, 0, False)
        return result

    def lexGreaterPermutationWithExplain(self, s: str, target: str) -> str:
        # 1. 统计 s 中每个字符的出现次数
        count = [0] * 26
        for c in s:
            index = ord(c) - ord('a')
            count[index] += 1
        
        curr = ""     # 当前构建的字符串
        result = ""   # 最终答案
        
        # 2. DFS 递归函数
        def solve(curr: str, count: list[int], target: str, i: int, greater: bool):
            nonlocal result
            
            # 2.1 已经构建了 len(target) 个字符（完整排列）
            if i == len(target):
                if greater:           # 必须比 target 大
                    result = curr
                    return True
                else:                 # 等于 target，不满足
                    return False
            
            # 2.2 尝试所有可能的下一个字符（a-z，按字典序）
            for idx in range(0, 26):
                c = chr(ord('a') + idx)
                
                # 这个字符用完了
                if count[idx] == 0:
                    continue
                
                # 剪枝：如果当前和 target 相等，不能选比 target[i] 小的字符
                if not greater and c < target[i]:
                    continue
                
                # 选择这个字符
                curr += c
                count[idx] -= 1
                
                # 更新 greater 状态
                isGreater = greater or (c > target[i])
                
                # 递归到下一层
                if solve(curr, count, target, i + 1, isGreater):
                    return True  # 找到答案，立即返回
                
                # 回溯：撤销选择
                curr = curr[:-1]
                count[idx] += 1
            
            return False  # 没有找到
        
        # 3. 开始搜索
        solve(curr, count, target, 0, False)
        return result

if __name__ == '__main__':
    so = Solution()
    s = "abc"
    target = "bba"
    print(so.lexGreaterPermutation(s, target))

    s = "leet"
    target = "code"
    print(so.lexGreaterPermutation(s, target))

    s = "baba"
    target = "bbaa"
    print(so.lexGreaterPermutation(s, target))



s = "abc", target = "abc"

# # 递归过程：
# solve(curr="", i=0, greater=False)
#   ├─ idx=0 ('a'): 选择 'a'
#   │  isGreater = False or ('a' > 'a') = False
#   │  solve(curr="a", i=1, greater=False)
#   │    ├─ idx=0 ('a'): count=0, 跳过
#   │    ├─ idx=1 ('b'): 选择 'b'
#   │    │  isGreater = False or ('b' > 'b') = False
#   │    │  solve(curr="ab", i=2, greater=False)
#   │    │    ├─ idx=0 ('a'): count=0, 跳过
#   │    │    ├─ idx=1 ('b'): count=0, 跳过
#   │    │    ├─ idx=2 ('c'): 选择 'c'
#   │    │    │  isGreater = False or ('c' > 'c') = False
#   │    │    │  solve(curr="abc", i=3, greater=False)
#   │    │    │    ├─ i==len(target): greater=False → 返回 False
#   │    │    │    └─ 回溯
#   │    │    └─ 回溯
#   │    └─ 回溯
#   │    ├─ idx=2 ('c'): 选择 'c'
#   │    │  isGreater = False or ('c' > 'b') = True
#   │    │  solve(curr="ac", i=2, greater=True)
#   │    │    ├─ idx=0 ('a'): count=0, 跳过
#   │    │    ├─ idx=1 ('b'): 选择 'b'
#   │    │    │  isGreater = True or ('b' > 'c') = True
#   │    │    │  solve(curr="acb", i=3, greater=True)
#   │    │    │    ├─ i==len(target): greater=True → result="acb", 返回 True
#   │    │    │    └─ 向上返回 True
#   │    │    └─ 返回 True
#   │    └─ 返回 True
#   └─ 返回 True

# 最终 result = "acb"



# 核心要点：

# 有序尝试：按字典序从小到大

# 状态维护：用 greater 标记是否已经比 target 大

# 剪枝优化：在不大于 target 时，跳过小于 target[i] 的字符

# 找到即返回：第一个找到的就是最小的大于 target 的排列

# 模板
# def backtrack(path, choices, ...):
#     if 到达终点:
#         if 满足条件:
#             记录答案
#             return True
#         return False
    
#     for 每个选择 in 按顺序排列的选择:
#         if 选择不合法:
#             continue
#         if 剪枝条件:
#             continue
        
#         做选择
#         if backtrack(...):  # 递归
#             return True
#         撤销选择
    
#     return False