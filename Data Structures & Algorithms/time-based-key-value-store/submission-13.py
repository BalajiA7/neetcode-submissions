class TimeMap:

    def __init__(self):
        self.hashMap = defaultdict(dict)

    def set(self, key: str, value: str, timestamp: int) -> None:
        if timestamp in self.hashMap[key]:
            self.hashMap[key][timestamp] = value
        else:
            self.hashMap[key][timestamp] = value
        # print(self.hashMap)
        

    def get(self, key: str, timestamp: int) -> str:
        if key in self.hashMap:
            if timestamp in self.hashMap[key]:
                # you have an key as well as timestamp
                return self.hashMap[key][timestamp]
            else:
                # you have an key but timestamp is not present
                # print("Key" , self.hashMap[key], timestamp)
                prevTimestamp = None
                for k, v in self.hashMap[key].items():
                    print(k, v)
                    if k <= timestamp:
                        prevTimestamp = k
                    else:
                        break
                return self.hashMap[key][prevTimestamp] if prevTimestamp != None else ""

        return ""
        
