class MyCalendarThree:

    def __init__(self):
        self.delta = {}

    def book(self, start: int, end: int) -> int:
        # marcações da linha de varredura
        self.delta[start] = self.delta.get(start, 0) + 1
        self.delta[end] = self.delta.get(end, 0) - 1

        active = 0
        max_active = 0

        # varre em ordem de chaves
        for x in sorted(self.delta):
            active += self.delta[x]
            max_active = max(max_active, active)

        return max_active
