from random import choices, randint
from typing import List

from pygame.color import Color

from lessons.lesson import Lesson
from utils import clamp


class Walker:

    x: int
    y: int
    _max_x: int
    _max_y: int

    def __init__(self, x: int, y: int, max_x: int, max_y: int) -> None:
        self.x = x
        self.y = y
        self._max_x = max_x
        self._max_y = max_y

    def walk(self, weights: List[float] = [0.5, 0.5]) -> None:
        next_x = self.x + choices([-1, 1], weights, k=1)[0]
        next_y = self.y + choices([-1, 1], weights, k=1)[0]
        self.x = clamp(next_x, 0, self._max_x)
        self.y = clamp(next_y, 0, self._max_y)


class RandomWalker(Lesson):

    walker: Walker

    def __init__(self) -> None:
        super().__init__()
        self.walker = Walker(
            int(self.get_width() / 2),
            int(self.get_height() / 2),
            self.get_width(),
            self.get_height())
        
        self.fill(Color(255, 255, 255))

    def tick(self) -> None:
        self.walker.walk([0.47, 0.53])

    def _render(self) -> None:
        walk_color: Color = Color(randint(0, 255), randint(0, 255), randint(0, 255))
        self.set_at([self.walker.x, self.walker.y], walk_color)
