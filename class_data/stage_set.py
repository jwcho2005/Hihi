from .classes.stage import *
from .grimer import *
from .minion import *
from .mooneater import *
from .spawn_blocks import *

class Setted_Stage(Stage):
    def __init__(self, game, name, level, start_point, center, background, sound):
        Stage.__init__(self, game, name, level, start_point, center, background, sound)
    
    def update(self):
        super().update()
        if self.game.message == None and self.end_check:
            self.game.lobby.start()
            for i in self.ground:
                i.delete()
            if self.end_point:
                self.end_point.delete()
            self.game.stage = None
            self.game.animation = None
            b = self.game.enemies.copy()
            for i in b:
                i.delete()
            b = self.game.impacts.copy()
            for i in b:
                i.delete()
            b = self.game.bullets.copy()
            for i in b:
                i.delete()
    
    def minion_spawn_block(self, image, num, location, size = (50, 50)):
        self.spawn_block(spawn_minion(self.game, {'통상' : Animation([Scene(image, size)], None)}, num, location=self.start_point + location))
    
    def bigheadsquid_spawn_block(self, image, num, location, size = (50, 50)):
        self.spawn_block(spawn_bigheadsquid(self.game, {'통상' : Animation([Scene(image, size)], None)}, num, location=self.start_point + location))

    def grimer_spawn_block(self, image, num, location, size = (50, 50)):
        self.spawn_block(spawn_grimer(self.game, {'통상' : Animation([Scene(image, size)], None)}, num, location=self.start_point + location))

    def mooneater_spawn(self, location):
        self.boss = mooneater(self.game, location=self.start_point + location)