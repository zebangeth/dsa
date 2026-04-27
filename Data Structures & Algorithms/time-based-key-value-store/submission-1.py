class TimeMap:

    def __init__(self):
        self.key_map = collections.defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.key_map[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        return self._get_most_recent(self.key_map[key], timestamp)
    
    def _get_most_recent(self, lst, timestamp):
        for i in range(len(lst) - 1, -1, -1):
            if lst[i][0] <= timestamp:
                return lst[i][1]
        return ""
