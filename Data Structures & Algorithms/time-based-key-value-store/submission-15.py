class TimeMap:

    def __init__(self):
        self.timemap = dict()

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.timemap.keys():
            self.timemap[key] = [(value, timestamp)]
        else:
            self.timemap[key].append((value, timestamp))
        

    def get(self, key: str, timestamp: int) -> str:
        
        if key not in self.timemap.keys():
            return("")


        
        lower = 0
        upper = len(self.timemap[key]) - 1
        mid = (lower + upper) // 2

        
        if self.timemap[key][0][1] > timestamp:
            return("")

        if upper == 0:
            return(self.timemap[key][0][0])

        while lower != mid:
            if self.timemap[key][mid][1] <= timestamp and self.timemap[key][mid+1][1] > timestamp:
                return(self.timemap[key][mid][0])
            elif self.timemap[key][mid+1][1] <= timestamp:
                lower = mid
                mid = (lower+upper) // 2
            else:
                upper = mid
                mid = (lower + upper) // 2
        
        if self.timemap[key][upper][1] <= timestamp:
            return(self.timemap[key][upper][0])
        else:
            return(self.timemap[key][lower][0])


