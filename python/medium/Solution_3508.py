# 3508. Implement Router

from typing import List
from collections import deque, defaultdict
import bisect


class Router:
    def __init__(self, memoryLimit: int):
        self.capacity: int = memoryLimit
        self.packet_queue: deque = deque()
        self.dest_to_timestamps: dict[int, deque] = defaultdict(deque)
        self.seen_packets: set[tuple[int, int, int]] = set()

    def addPacket(self, source: int, destination: int, timestamp: int) -> bool:
        if (source, destination, timestamp) in self.seen_packets:
            return False

        self.packet_queue.append((source, destination, timestamp))
        self.dest_to_timestamps[destination].append(timestamp)
        self.seen_packets.add((source, destination, timestamp))

        if len(self.packet_queue) > self.capacity:
            evicte_packet = self.packet_queue.popleft()
            evicted_dest = evicte_packet[1]
            self.dest_to_timestamps[
                evicted_dest
            ].popleft()
            self.seen_packets.discard(evicte_packet)

        return True

    def forwardPacket(self) -> List[int]:
        if not self.packet_queue:
            return []

        source, destination, timestamp = self.packet_queue.popleft()
        self.dest_to_timestamps[destination].popleft()
        self.seen_packets.discard((source, destination, timestamp))

        return [source, destination, timestamp]

    def getCount(self, destination: int, startTime: int, endTime: int) -> int:
        left = bisect.bisect_left(self.dest_to_timestamps[destination], startTime)
        right = bisect.bisect_right(self.dest_to_timestamps[destination], endTime)
        return right - left


router = Router(3)
print(router.addPacket(1, 4, 90))
print(router.addPacket(2, 5, 90))
print(router.addPacket(1, 4, 90))
print(router.addPacket(3, 5, 95))
print(router.addPacket(4, 5, 105))
print(router.forwardPacket())
print(router.addPacket(5, 2, 110))
print(router.getCount(5, 100, 110))
