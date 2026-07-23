class TimeMap:

    def __init__(self):
        self.hashMap = {}
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.hashMap:
            self.hashMap[key].append((timestamp, value))
        else:
            self.hashMap[key] = [(timestamp, value)]
        
    def get(self, key: str, timestamp: int) -> str:
        values = self.hashMap.get(key,[])
        l=0
        r=len(values)-1
        minValue = ""

        while l<=r:
            mid = (l+r) // 2
            if values[mid][0] == timestamp:
                return values[mid][1]
            elif values[mid][0] > timestamp:
                r = mid-1
            else:
                minValue = values[mid][1]
                l = mid+1
        
        return minValue



        
