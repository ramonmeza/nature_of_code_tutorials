from dataclasses import dataclass
from random import choice

from pygame.color import Color

from lessons.lesson import Lesson

@dataclass
class Walker:

    x: int
    y: int

    def walk(self) -> None:
       self.x += choice([-1, 1])
       self.y += choice([-1, 1])


class RandomWalker(Lesson):

    walker: Walker

    def __init__(self) -> None:
        super().__init__()
        self.walker = Walker(int(self.get_width() / 2), int(self.get_height() / 2))
        self.fill(Color(255, 255, 255))

    def tick(self) -> None:
        self.walker.walk()

    def _render(self) -> None:
        self.set_at([int(self.walker.x), int(self.walker.y)], Color(0, 0, 0))
