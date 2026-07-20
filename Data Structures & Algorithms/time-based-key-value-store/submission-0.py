class TimeMap:

    def __init__(self):
        self.timestamps = [0] * (10 ** 7 + 1) 
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        if  self.timestamps[timestamp]:
            self.timestamps[timestamp][key] = value
        else:
            pair = {}
            pair[key]= value
            self.timestamps[timestamp] = pair
        

    def get(self, key: str, timestamp: int) -> str:
        index = timestamp
        while index>=0:
            if  self.timestamps[index] and key in self.timestamps[index]:
                return self.timestamps[index][key]
            index-=1
        return ""
