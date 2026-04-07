class Robot:
    def __init__(self, width: int, height: int):
        self.w = width
        self.h = height
        self.pos = 0
        self.perimeter = 2 * (width + height - 2)
        self.moved = False

    def step(self, num: int) -> None:
        self.moved = True
        self.pos = (self.pos + num) % self.perimeter

    def getPos(self) -> list[int]:
        s = self.pos
        if s < self.w:
            return [s, 0]
        elif s < self.w + self.h - 1:
            return [self.w - 1, s - (self.w - 1)]
        elif s < 2 * self.w + self.h - 2:
            return [self.w - 1 - (s - (self.w + self.h - 2)), self.h - 1]
        else:
            return [0, self.h - 1 - (s - (2 * self.w + self.h - 3))]

    def getDir(self) -> str:
        s = self.pos
        # Special case: robot finished a loop and is at (0,0)
        if s == 0 and self.moved:
            return "South"
        
        if 1 <= s < self.w:
            return "East"
        elif self.w <= s < self.w + self.h - 1:
            return "North"
        elif self.w + self.h - 1 <= s < 2 * self.w + self.h - 2:
            return "West"
        else:
            return "South" if self.moved else "East"
