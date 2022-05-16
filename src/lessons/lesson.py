from abc import abstractmethod
import json5
import pygame as pyg

from pathlib import Path
from typing import Dict, List

from settings import Settings


class Lesson(pyg.Surface):

    # methods
    def __init__(self) -> None:
        # get settings
        display_settings: Dict = Settings.load(Path('data/settings.json5'), 'display')
        
        # subclass init
        pyg.Surface.__init__(self, size=(display_settings['width'], display_settings['height']))

    def update(self, dt: float) -> None:
        self.tick()
        self._render()

    @abstractmethod
    def tick(self) -> None:
        pass

    @abstractmethod
    def _render(self) -> None:
        pass
