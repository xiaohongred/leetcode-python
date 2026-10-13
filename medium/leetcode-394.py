# -*- coding: utf-8 -*-
"""
LeetCode 394. 字符串解码 (Decode String)

题目：
    给定一个经过编码的字符串，返回它解码后的字符串。
    编码规则为: k[encoded_string]，表示其中方括号内部的 encoded_string 正好重复 k 次。
    注意 k 保证为正整数。输入的字符串总是有效的（括号配对、数字合法）。

    示例：
        s = "3[a]2[bc]"       -> "aaabcbc"
        s = "3[a2[c]]"        -> "accaccacc"      （嵌套）
        s = "2[abc]3[cd]ef"   -> "abcabccdcdcdef" （并列 + 尾部残留）
        s = "100[leetcode]"   -> "leetcode" 重复 100 次（k 是多位数）

核心难点：
    括号是**嵌套**的，所以不能简单正则替换，必须利用"栈"这种后进先出（LIFO）的结构，
    让内层的括号先被解开，再拼回外层。

下面给出两种写法：
    解法一 decodeString    ：单栈 + 字符逐个入栈，遇到 ']' 时"回头拆包"（原地展开）
    解法二 decodeStringV2  ：双栈（数字栈 + 字符串栈），边扫描边维护"当前层"的状态（推荐）

时间复杂度：两者都是 O(输出字符串的长度)，因为每个字符最终都会被产生一次；
            （严格说是 O(n + 展开后长度)）
空间复杂度：O(展开后长度)（栈 + 结果字符串）
"""


class Solution:
    def decodeString(self, s: str) -> str:
        """
        解法一：单栈法（原地展开）

        思路一句话：
            把字符一个一个压进栈；一旦碰到 ']'，就说明"一对括号里的活干完了"，
            于是从栈顶往回倒着弹出，直到找到 '[' —— 弹出的这一串就是本层要重复的内容；
            再继续往前弹数字，得到重复次数 k；把展开后的结果整体压回栈顶。
            由于最内层的 ']' 最先被处理，天然满足嵌套的从内向外顺序。

        注意一个关键设计：
            stack 里存的既可能是单个字符（还没被展开的字母），
            也可能是一整段已经展开好的字符串（subStr * int(k) 的结果），
            最后统一用 "".join(stack) 拼起来，所以两种元素可以共存。
        """
        stack = []  # 既存字符，也存"已展开的片段"

        for i in range(len(s)):
            # 只要不是右括号，就先原样入栈：字母、数字、'[' 都直接压进去
            if s[i] != "]":
                stack.append(s[i])
            else:
                # ===== 遇到 ']'：开始"拆包"这一层括号 =====

                # 1) 倒着弹出本层括号内的内容，直到遇到 '['
                #    因为栈是后进先出，正着 pop 出来的是逆序，
                #    所以用 subStr = stack.pop() + subStr 把它"头插"回正序
                subStr = ""
                while stack[-1] != "[":
                    subStr = stack.pop() + subStr

                # 2) 弹掉这个 '[' 本身（左括号只是分隔标记，不需要保留）
                stack.pop()

                # 3) 继续往前弹数字，拼出重复次数 k
                #    题目保证 k 是正整数，但仍要写 `stack and ...` 防止越界（如 "a]" 这种边界）
                #    同样因为倒着 pop，数字也要"头插"才能保持原来的顺序（处理 100、12 这类多位数）
                k = ""
                while stack and stack[-1].isdigit():
                    k = stack.pop() + k

                # 4) 把展开后的整段字符串压回栈，作为上一层（外层）的一部分继续参与运算
                stack.append(subStr * int(k))

        # 扫描结束后，栈里剩下的全是"已展开的片段"，拼起来就是答案
        return "".join(stack)

    def decodeStringV2(self, s: str) -> str:
        """
        解法二：双栈法（推荐，逻辑更清晰）

        思路一句话：
            维护两个"当前层"的变量：cur_num（正在读的重复次数）和 cur_str（当前层已拼好的字符串）。
            遇到 '[' 表示要进入更深的一层：把当前的 cur_num / cur_str 入栈保存，然后清零重新开始；
            遇到 ']' 表示当前层结束：弹出上一层的次数和前缀，把本层结果重复后接回上一层。

            这里栈保存的是"外层的上下文现场"，所以叫双栈法（数字栈 + 字符串栈）。
            相比解法一，它不需要"回头倒着扫"，是严格单向的一次遍历，更好理解也更好写。

        ──────────────────────────────────────────────────────────────
        【核心难点】cur_str = prev_str + cur_str * repeat 到底在干什么？

        拆成三步看：
            ① cur_str * repeat  →  把「本层括号里的内容」重复 k 次
            ② prev_str + ...    →  接在「进入本层之前已积累的内容」后面
            ③ 写回 cur_str      →  因为 ']' 之后作用域回到上一层，
                                   cur_str 的语义始终是"当前层累加器"，
                                   归约后当前层就是外层，所以直接写回它，继续接后面的字符

        prev_str 有两个身份（本质是同一个东西，代码里不需要区分）：

            身份 A：嵌套时，它是"外层没拼完的左半截"
                3[a2[c]] 中，内层 2[c] 解开得到 "cc"，但它前面还有外层攒下的 "a"，
                归约后必须拼成 "a" + "cc" = "acc"，再被外层 3[...] 重复。
                少了 prev_str，这个 "a" 就丢了。

            身份 B：并列时，它是"上一个已经解完的兄弟段"
                2[abc]3[cd] 中，解 3[cd] 时 prev_str = "abcabc"（前一段的成果），
                归约后是 "abcabc" + "cd"*3 = "abcabccdcdcd"。

            统一说法：prev_str = 进入这对括号之前的「全部已有成果」。

        ──────────────────────────────────────────────────────────────
        【执行轨迹一】s = "3[a2[c]]"   （嵌套场景）

            读到    动作                          cur_num  cur_str      num_stack  str_stack
            ------  ---------------------------  -------  -----------  ---------  ----------
            '3'     累加数字                      3        ""           []         []
            '['     进层：压栈 + 清零              0        ""           [3]        [""]
            'a'     追加字母                      0        "a"          [3]        [""]
            '2'     累加数字                      2        "a"          [3]        [""]
            '['     再进一层：压栈 + 清零           0        ""           [3, 2]     ["", "a"]
            'c'     追加字母                      0        "c"          [3, 2]     ["", "a"]
            ']'     归约 repeat=2, prev_str="a"            "acc"        [3]        [""]
                    → "a" + "c" * 2
            ']'     归约 repeat=3, prev_str=""             "accaccacc"  []         []
                    → "" + "acc" * 3

            最终 cur_str = "accaccacc"

        【执行轨迹二】s = "2[abc]3[cd]ef"   （并列 + 括号外尾巴）

            读到        动作                                    cur_str
            ----------  --------------------------------------  --------------
            "2[abc]"    归约 → "" + "abc" * 2                   "abcabc"
            "3["        压栈 str_stack=["abcabc"]，清零           ""
            "cd"        追加字母                                 "cd"
            "]"         归约 → "abcabc" + "cd" * 3               "abcabccdcdcd"
            "ef"        追加字母（括号外的尾巴，不属于任何一层）    "abcabccdcdcdef"

        ──────────────────────────────────────────────────────────────
        【对照递归写法】双栈只是把递归里的"局部变量"手动存起来，本质完全一样：

            def dfs(s, i):
                res = ""
                while s[i] != ']':
                    if s[i].isdigit():
                        k = 解析数字
                    elif s[i] == '[':
                        inner, i = dfs(s, i + 1)   # 拿到内层结果
                        res += inner * k           # ← 这里的 res 就是 prev_str
                    else:
                        res += s[i]
                    i += 1
                return res, i + 1

            num_stack 存的是递归里的 k，str_stack 存的是递归里的 res。
        """
        num_stack = []  # num_stack[i] 保存第 i 层的重复次数 k
        str_stack = []  # str_stack[i] 保存第 i 层开始之前，外层已经拼好的字符串（前缀）

        cur_num = 0     # 当前正在解析的重复次数（支持多位数：逐位 cur_num = cur_num * 10 + 数字）
        cur_str = ""    # 当前层已经拼好的字符串

        for c in s:
            if c.isdigit():
                # 数字：可能是多位数，用"进位"的方式累加
                # 例如 "100["：读到 '1' -> 1，读到 '0' -> 10，读到 '0' -> 100
                cur_num = cur_num * 10 + int(c)

            elif c == '[':
                # 左括号：进入新的一层
                # 先把"当前层的现场"保存到栈里：
                #   - cur_num 是这一对新括号对应的重复次数
                #   - cur_str 是进入括号前已经拼好的前缀（外层的内容）
                # 然后把两个"当前层变量"清零，开始处理括号内部
                num_stack.append(cur_num)
                str_stack.append(cur_str)
                cur_num = 0
                cur_str = ""

            elif c != ']':
                # 普通字母：直接追加到当前层的字符串
                cur_str += c

            else:
                # ===== 右括号：本层收工，做一次"归约"，把成果交还给上一层 =====

                # repeat  ：本层括号前的重复次数（就是进层时压进 num_stack 的那个 cur_num）
                # prev_str：进层时压进 str_stack 的那个 cur_str，
                #           即"进入本层之前的全部已有成果"（详见上面 docstring 的身份 A / B）
                repeat = num_stack.pop()
                prev_str = str_stack.pop()

                # 这一行是整个算法的核心，拆成三步理解：
                #   ① cur_str * repeat  → 本层括号内的内容重复 repeat 次
                #   ② prev_str + ...    → 接到"上一层的现场"后面
                #                          （嵌套时是外层的左半截，并列时是前面已解完的
                #                            兄弟段，两者在代码里不区分，都是同一个 cur_str）
                #   ③ 赋值回 cur_str    → ']' 之后作用域回到上一层，而 cur_str 的语义
                #                          始终是"当前层累加器"，所以直接写回它，
                #                          继续接住后面的字符（如 "2[abc]3[cd]ef" 的 "ef"）
                #
                # 记忆口诀：遇 ']' = 收工回上一层 —— 本层成果复制 repeat 份，
                #           接回上一层现场，交还给上一层继续干。
                cur_str = prev_str + cur_str * repeat

        # 全部扫描完，cur_str 就是最外层的结果
        return cur_str


if __name__ == '__main__':
    solu = Solution()

    # 用例 1：并列的两个括号，没有嵌套
    s = "3[a]2[bc]"
    a = solu.decodeString(s)
    print(a)  # aaabcbc

    # 用例 2：嵌套括号，内层 2[c] -> cc，外层 3[a + cc] -> accaccacc
    s = "3[a2[c]]"
    a = solu.decodeStringV2(s)
    print(a)  # accaccacc

    # 用例 3：并列括号 + 括号外的尾巴
    s = "2[abc]3[cd]ef"
    a = solu.decodeStringV2(s)
    print(a)  # abcabccdcdcdef
