# 929. Unique Email Addresses

from typing import List


class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        ans: set[str] = set()
        for email in emails:
            local_name, domain_name = email.split('@')
            local_name = local_name.split('+')[0].replace('.', '')
            email = f'{local_name}@{domain_name}'
            ans.add(email)

        return len(ans)


ans = Solution().numUniqueEmails([
    "test.email+alex@leetcode.com",
    "test.e.mail+bob.cathy@leetcode.com",
    "testemail+david@lee.tcode.com"])
print(ans)
