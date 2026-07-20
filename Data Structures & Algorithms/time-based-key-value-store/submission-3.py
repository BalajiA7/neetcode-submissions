class TimeMap:

    def __init__(self):
        self.treeMap = {} 
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        if  key not in self.treeMap:
            self.treeMap[key] = []
        self.treeMap[key].append((timestamp, value))
        
    def get(self, key: str, timestamp: int) -> str:
        arr = self.treeMap.get(key)
        if not arr:
            return ""
        
        ans = ""
        l = 0
        r = len(arr) -1
        
        while l <=r:
            mid = (l+r) // 2
            if arr[mid][0] == timestamp:
                return arr[mid][1]
            elif arr[mid][0] > timestamp:
                r = mid -1
            else:
                ans = arr[mid][1]
                l = mid +1 
            
        return ans
