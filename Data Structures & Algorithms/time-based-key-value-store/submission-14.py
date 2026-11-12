class TimeMap:

    def __init__(self):
        self.hashMap = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.hashMap:
            self.hashMap[key].append((timestamp, value))
        else:
            self.hashMap[key] = [(timestamp, value)]      

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.hashMap:
            return ""

        group = self.hashMap.get(key, [])
        l = 0
        r = len(group) - 1
        res = ""

        while l <= r:
            mid = (l+r) // 2
            time, value = group[mid]
            if time == timestamp:
                return value
            elif time > timestamp:
                r = mid-1
            else:
                res = value
                l = mid + 1
        
        return res
        
