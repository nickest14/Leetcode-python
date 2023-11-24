# 1396. Design Underground System


class UndergroundSystem:

    def __init__(self):
        self.check_in_map = {}  # id -> (station_name, time)
        self.total_map = {}  # (start, end) -> [total_time, count]

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.check_in_map[id] = (stationName, t)

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        start_station, start_time = self.check_in_map.get(id)
        route = (start_station, stationName)
        if route not in self.total_map.keys():
            self.total_map[route] = [0, 0]
        self.total_map[route][0] += t - start_time
        self.total_map[route][1] += 1

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        time, count = self.total_map[(startStation, endStation)]
        return time / count


obj = UndergroundSystem()
obj.checkIn(1, "A", 10)
obj.checkOut(1, "B", 50)
param_3 = obj.getAverageTime("A", "B")
