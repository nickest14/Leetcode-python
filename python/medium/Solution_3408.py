# 3408. Design Task Manager

from typing import List
import heapq


class Manager:
    def __init__(self, userId, taskId, priority):
        self.userId = userId
        self.taskId = taskId
        self.priority = priority

    def __lt__(self, other) -> bool:
        if self.priority == other.priority:
            return self.taskId > other.taskId  # higher taskId wins
        return self.priority > other.priority  # higher priority wins


class TaskManager:
    def __init__(self, tasks: List[List[int]]) -> None:
        self.heap: list[Manager] = []
        self.record: dict[int, Manager] = {}
        for userId, taskId, priority in tasks:
            m = Manager(userId, taskId, priority)
            heapq.heappush(self.heap, m)
            self.record[taskId] = m

    def add(self, userId, taskId, priority) -> None:
        m = Manager(userId, taskId, priority)
        heapq.heappush(self.heap, m)
        self.record[taskId] = m

    def edit(self, taskId, newPriority) -> None:
        if taskId not in self.record:
            return
        old = self.record[taskId]
        updated = Manager(old.userId, taskId, newPriority)
        heapq.heappush(self.heap, updated)
        self.record[taskId] = updated

    def rmv(self, taskId) -> None:
        if taskId in self.record:
            del self.record[taskId]  # lazy delete

    def execTop(self) -> int:
        while self.heap:
            top = heapq.heappop(self.heap)
            latest = self.record.get(top.taskId)
            if latest is None:
                continue
            if latest.priority != top.priority or latest.userId != top.userId:
                continue
            del self.record[top.taskId]
            return top.userId
        return -1


task_manager = TaskManager([[1, 101, 10], [2, 102, 20], [3, 103, 15]])
task_manager.add(4, 104, 5)
task_manager.edit(102, 8)
print(task_manager.execTop())
task_manager.rmv(101)
task_manager.add(5, 105, 15)
print(task_manager.execTop())
