class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = sorted([(position[i], speed[i]) for i in range(len(position))], key=lambda x:-x[0])
        print(cars)

        result = []
        for car in cars:
            pos, speed = car[0], car[1]
            time_to_target = (target - pos) / speed
            if not result or time_to_target > result[-1]:
                result.append(time_to_target)
                continue

        return len(result)