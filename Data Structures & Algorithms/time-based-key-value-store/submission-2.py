class TimeMap:

    def __init__(self):
        self.treeMap = {} 
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        if  key not in self.treeMap:
            self.treeMap[key] = []
        self.treeMap[key].append((timestamp, value))
        
    def get(self, key: str, timestamp: int) -> str:
        arr = self.treeMap.get(key)
        if arr:
            for i in range(len(arr)-1, -1, -1):
                time, value = arr[i]
                if time <= timestamp:
                    return value
            
        return ""
