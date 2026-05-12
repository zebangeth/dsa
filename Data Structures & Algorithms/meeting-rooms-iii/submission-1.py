class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        # stores (available_time, room_number)
        free_rooms = [(0, i) for i in range(n)]
        room_usage = [0] * n
        heapq.heapify(free_rooms)
        meetings.sort()

        for (start, end) in meetings:
            while free_rooms[0][0] < start:
                _, room_number = heapq.heappop(free_rooms)
                heapq.heappush(free_rooms, (start, room_number))

            available_time, room_number = heapq.heappop(free_rooms)
            meeting_end = max(available_time, start) + (end - start)
            heapq.heappush(free_rooms, (meeting_end, room_number))
            room_usage[room_number] += 1
        
        max_room_usage = max(room_usage)
        print(room_usage)
        return room_usage.index(max_room_usage)
