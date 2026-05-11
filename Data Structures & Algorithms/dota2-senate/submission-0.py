class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        qr, qd = collections.deque(), collections.deque()
        for i, p in enumerate(senate):
            if p == 'R':
                qr.append(i)
            else:
                qd.append(i)
        
        while qr and qd:
            if qr[0] < qd[0]:
                qd.popleft()
                qr.append(len(senate) + qr.popleft())
            else:
                qr.popleft()
                qd.append(len(senate) + qd.popleft())
        return "Radiant" if qr else "Dire"