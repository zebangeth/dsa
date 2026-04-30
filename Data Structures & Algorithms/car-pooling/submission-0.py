class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        events = []
        for (num_passenger, fr, to) in trips:
            events.append((fr, num_passenger))
            events.append((to - 0.1, -num_passenger))
        
        passenger = 0
        for event in sorted(events):
            passenger += event[1]
            if passenger > capacity:
                return False

        return True