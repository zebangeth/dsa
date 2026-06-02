class LFUCache:

    def __init__(self, capacity: int):
        self.key_to_frq = {} # {key: frq, ...}
        self.frq_to_keys_to_val = collections.defaultdict(collections.OrderedDict)
        # {frq: {key: val, ...}, ...}
        self.cap = capacity
        self.size = 0
        self.min_frq = 0

    def get(self, key: int) -> int:
        if key not in self.key_to_frq:
            return -1

        self.__increase_frq(key)
        frq = self.key_to_frq[key]
        return self.frq_to_keys_to_val[frq][key]

    def put(self, key: int, value: int) -> None:
        # if key exists, update value
        if key in self.key_to_frq:
            self.__increase_frq(key)
            frq = self.key_to_frq[key]
            self.frq_to_keys_to_val[frq][key] = value
            return

        # if cap is full, pop the LRU item in the LFU group
        if len(self.key_to_frq) == self.cap:
            lfu_group = self.frq_to_keys_to_val[self.min_frq]
            popped_key, popped_val = lfu_group.popitem(last=False)
            self.key_to_frq.pop(popped_key)

        # add KV pair and KF pair (frq = 1)
        self.key_to_frq[key] = 1
        self.frq_to_keys_to_val[1][key] = value
        self.min_frq = 1

    def __increase_frq(self, key):
        frq = self.key_to_frq[key]
        self.key_to_frq[key] += 1

        val = self.frq_to_keys_to_val[frq].pop(key)
        self.frq_to_keys_to_val[frq + 1][key] = val

        if self.min_frq == frq and len(self.frq_to_keys_to_val[frq]) == 0:
            # 当前 key 的 frq 不一定是 min_freq, 所以要先判断 self.min_frq == frq
            self.min_frq += 1