from typing import List


class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        unique = set()
        for e in emails:
            local, domain = e.split("@")
            local = local.split("+")[0]

            local = local.replace(".", "")

            unique.add((local, domain))
        return len(unique)


if __name__ == '__main__':
    emails = ["test.email+alex@leetcode.com", "test.e.mail+bob.cathy@leetcode.com", "testemail+david@lee.tcode.com"]
    s = Solution()
    a = s.numUniqueEmails(emails)
    print(a)
