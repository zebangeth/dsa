class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = [(position[i], speed[i]) for i in range(len(position))]
        cars.sort(reverse=True)

        travel_times = [(target - cars[i][0]) / cars[i][1] for i in range(len(cars))]

        groups = 0
        fleets = []
        for time in travel_times:
            if not fleets or time > fleets[-1]:
                fleets.append(time)
                groups += 1
        return groups
