class Solution:
    def shortestBeautifulSubstring(self, s: str, k: int) -> str:
        n = len(s)

        for i in range(k, n+1):
            result = ""
            for j in range(0, n - i + 1):
                temp = s[j:j + i]
                ones = 0
                for c in temp:
                    if c == '1':
                        ones += 1
                if ones == k:
                    if result == "" or temp < result:
                        result = temp

            if result != "":
                return result

        return ""

    def shortestBeautifulSubstringV2(self, s: str, k: int) -> str:
        i, j = 0, 0

        n = len(s)
        cnt = 0

        result = ""
        while j < n:
            if s[j] == '1':
                cnt += 1

            while cnt > k or (i <= j and s[i] == '0'): # 缩小窗口,   加一个  i <= j  的条件是为了防止全为0时越界
                if s[i] == '1':
                    cnt -= 1
                i += 1

            if cnt >= k :
                temp = s[i:j+1] # 取到 j
                if result == "" or len(result) > (j- i + 1) or (len(temp) == len(result) and temp < result):
                    result = temp

            j += 1
        return result

if __name__ == '__main__':
    so = Solution()
    s = "100011001"
    k = 3
    print(so.shortestBeautifulSubstring(s, k))

    s = "1011"
    k = 2
    print(so.shortestBeautifulSubstring(s, k))


    s = "100011001"
    k = 3
    print(so.shortestBeautifulSubstringV2(s, k))

    s = "1011"
    k = 2
    print(so.shortestBeautifulSubstringV2(s, k))