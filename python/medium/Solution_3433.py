# 3433. Count Mentions Per User

from typing import List


class Solution:
    def countMentions(self, numberOfUsers: int, events: List[List[str]]) -> List[int]:
        ans: list[int] = [0] * numberOfUsers
        online_time: list[int] = [0] * numberOfUsers
        events.sort(key=lambda x: (int(x[1]), x[0] == "MESSAGE"))
        for msg, time, mentions in events:
            t: int = int(time)
            if msg == "MESSAGE":
                if mentions == "ALL":
                    for i in range(numberOfUsers):
                        ans[i] += 1
                elif mentions == "HERE":
                    for i in range(numberOfUsers):
                        if t >= online_time[i]:
                            ans[i] += 1
                else:
                    for p in mentions.replace("id", "").split():
                        ans[int(p)] += 1
            else:
                online_time[int(mentions)] = t + 60
        return ans


ans = Solution().countMentions(
    2, [["MESSAGE", "10", "id1 id0"], ["OFFLINE", "11", "0"], ["MESSAGE", "71", "HERE"]]
)

print(ans)
