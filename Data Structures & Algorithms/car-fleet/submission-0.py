class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        out = 1
        cars = []
        for i in range(len(position)):
            # (position, time to destination)
            distance = target - position[i]
            time = distance / speed[i]
            cars.append((position[i], time))
        cars.sort(reverse=True)
        
        curr_time = cars[0][1]
        while cars:
            if curr_time >= cars[0][1]:
                cars.pop(0)
            # curr_time < cars[0][1]
            else:
                out += 1
                curr_time = cars[0][1]
                cars.pop(0)

        return out