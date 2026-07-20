class TimeMap:

    def __init__(self):
        self.treeMap = {} 
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        if  key not in self.treeMap:
            self.treeMap[key] = []
        self.treeMap[key].append((timestamp, value))
        
    def get(self, key: str, timestamp: int) -> str:
        ans = ""
        arr = self.treeMap.get(key ,[])
        l,r = 0,len(arr) -1
        
        while l <=r:
            mid = (l+r) // 2
            time, value = arr[mid]
            if time == timestamp:
                return value
            elif time > timestamp:
                r = mid -1
            else:
                ans = value
                l = mid +1 
            
        return ans
