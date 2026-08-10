class TimeMap:

    def __init__(self):
        self.timeMap = {}
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.timeMap:
            self.timeMap[key] = [(timestamp, value)]
        else:
            self.timeMap[key].append((timestamp, value))
        

    def get(self, key: str, timestamp: int) -> str:
        group = self.timeMap.get(key , [])

        l = 0
        r = len(group) - 1
        res = ""

        while l<=r:
            mid = (l+r) // 2
            t, v = group[mid]

            if t == timestamp:
                return v
            elif t > timestamp:
                r = mid - 1
            else:
                l = mid + 1
                res = v

        return res
