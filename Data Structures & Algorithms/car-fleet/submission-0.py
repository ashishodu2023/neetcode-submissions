class Solution:

    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        
        if not position or not speed:
            return 0 
        
        tuple_car = sorted(zip(position,speed),reverse=True)

        count_fleet = 0 
        max_time = 0 

        for pos,spd in tuple_car:
            time = (target - pos) / spd

            if time>max_time:
                count_fleet+=1
                max_time = time

        return count_fleet
        