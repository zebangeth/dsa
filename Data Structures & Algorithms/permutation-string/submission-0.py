class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if not s1: 
            return True
        if len(s2) < len(s1):
            return False

        match = collections.Counter(s1)
        window = collections.Counter(s2[:len(s1)])
        
        for r in range(len(s1), len(s2)):
            if window == match:
                return True
            
            window[s2[r]] += 1

            l = r - len(s1)
            window[s2[l]] -= 1
            if window[s2[l]] == 0:
                window.pop(s2[l])
        
        return window == match