from collections import deque


class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:

        if not position or not speed:
            return 0

        stack = deque()

        cars = sorted(zip(position, speed), reverse=True)

        for pos, spd in cars:
            time = (target - pos) / spd

            stack.append(time)

            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()

        return len(stack)
