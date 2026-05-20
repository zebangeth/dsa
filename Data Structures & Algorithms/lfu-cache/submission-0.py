class LFUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.min_frq = 0
        self.key2val = {} # {key: val, ...}
        self.key2frq = {} # {key: frq, ...}
        self.frq2key = collections.defaultdict(collections.deque) # {frq: deque(keys), ...}

    def get(self, key: int) -> int:
        if key not in self.key2val:
            return -1
        self.__increase_frq(key)
        return self.key2val[key]

    def put(self, key: int, value: int) -> None:
        if self.cap <= 0:
            return

        if key in self.key2val:
            self.key2val[key] = value
            self.__increase_frq(key)
            return

        if self.cap <= len(self.key2val):
            self.__remove_min_frq_key()

        self.key2val[key] = value
        self.key2frq[key] = 1
        self.frq2key[1].appendleft(key)
        self.min_frq = 1


    def __increase_frq(self, key):
        cur_frq = self.key2frq[key]
        self.key2frq[key] += 1

        self.frq2key[cur_frq].remove(key)
        self.frq2key[cur_frq + 1].appendleft(key)

        if len(self.frq2key[cur_frq]) == 0:
            del self.frq2key[cur_frq]
            if cur_frq == self.min_frq:
                self.min_frq += 1

    def __remove_min_frq_key(self):
        key_q = self.frq2key[self.min_frq]
        del_key = key_q.pop()

        if len(key_q) == 0:
            del self.frq2key[self.min_frq]
            # self.min_frq = min(self.frq2key.keys()) 不用写，因为 min_frq 一定是1
        del self.key2val[del_key]
        del self.key2frq[del_key]