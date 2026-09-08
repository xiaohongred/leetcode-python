class Solution:
    def toLowerCase(self, s: str) -> str:
        res = ""
        for c in s:
            if (c >= 'A' and c <= 'Z' ) or (c >= 'a' and c <= 'z'):
                res += chr((ord(c)|32))
            else:
                res += c
        return res



# 用位运算的技巧就行了。。。

# 大写变小写、小写变大写 : 字符 ^= 32;

# 大写变小写、小写变小写 : 字符 |= 32;

# 小写变大写、大写变大写 : 字符 &= -33;


if __name__ == "__main__":
    solution = Solution()
    s = "Hello"
    result = solution.toLowerCase(s)
    print(result)  # Output: "hello"

    s = "here"
    result = solution.toLowerCase(s)
    print(result)  # Output: "here"

    s = "LOVELY"
    result = solution.toLowerCase(s)
    print(result)  # Output: "lovely"