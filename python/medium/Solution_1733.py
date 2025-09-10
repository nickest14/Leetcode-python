# 1733. Minimum Number of People to Teach

from typing import List


class Solution:
    def minimumTeachings(
        self, n: int, languages: List[List[int]], friendships: List[List[int]]
    ) -> int:
        users_to_teach: set[int] = set()

        for user1, user2 in friendships:
            user1 -= 1
            user2 -= 1
            can_communicate = False

            for lang in languages[user1]:
                if lang in languages[user2]:
                    can_communicate = True
                    break

            if not can_communicate:
                users_to_teach.add(user1)
                users_to_teach.add(user2)

        ans = len(languages) + 1

        for language in range(1, n + 1):
            count: int = 0
            for user in users_to_teach:
                if language not in languages[user]:
                    count += 1
            ans = min(ans, count)

        return ans


ans = Solution().minimumTeachings(2, [[1], [2], [1, 2]], [[1, 2], [1, 3], [2, 3]])
print(ans)
