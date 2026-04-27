class TimeMap:

    def __init__(self):
        self.key_map = collections.defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.key_map[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.key_map:
            return ""
        return self._get_most_recent(self.key_map[key], timestamp)
    
    def _get_most_recent(self, lst, timestamp):
        # for i in range(len(lst) - 1, -1, -1):
        #     if lst[i][0] <= timestamp:
        #         return lst[i][1]
        # return ""

        start, end = 0, len(lst) - 1
        while start + 1 < end:
            mid = (start + end) // 2
            if lst[mid][0] == timestamp:
                return lst[mid][1]
            elif lst[mid][0] < timestamp:
                start = mid
            else:
                end = mid

        if lst[end][0] <= timestamp:
            return lst[end][1]
        if lst[start][0] <= timestamp:
            return lst[start][1]
        return ""