from .obstacles import *
from .gimic_block import *
from .animation import *
from .variable import *
from .decoration import *
from .message import *
import time

class Stage():
    def __init__(self, game, name, level, start_point, center, background, sound, background_follow = True):
        self.name = name
        self.game = game
        self.ground = []
        self.start_point = start_point
        self.start_time = 0
        self.center = center
        self.background_follow = background_follow
        self.background = background.image_r
        self.rect = background.rect
        self.rect.center = self.center
        self.sound = sound.sound
        self.sound.set_volume(sound.volume)
        self.level = level
        self.defo_center = vec(0, 0)
        self.end_point = None
        self.end_check = False
        self.end_time = 0
        self.message_time = 0
        self.clear_check = False
        self.deco_update()
    
    def start(self):
        self.sound.play(-1)
        self.game.player = self.game.player
        self.game.player.none_damage = False
        self.game.player.rect.center = self.start_point
        self.game.eyesight.mode = 'x추적'
        self.game.eyesight.rect.center = self.start_point
        self.background_update()
        self.deco_update()
        self.start_time = time.time()
        self.game.message = message(self.game, self.name, 1, size = 100)
    
    def clear(self):
        self.clear_check = True
        if self.game.level < self.level:
            self.game.level = self.level
        self.end()
    
    def end(self):
        self.sound.stop()
        self.game.player.none_damage = True
        self.end_time = time.time()
        b = self.game.enemies.copy()
        for i in b:
            i.delete()
        b = self.game.bullets.copy()
        for i in b:
            i.delete()
        b = self.game.impacts.copy()
        for i in b:
            i.delete()
        if self.game.message == None and not self.end_check:
            if self.clear_check:
                if self.end_time - self.start_time < 300:
                    self.game.player.gold += 300 - int(self.end_time - self.start_time)
                self.game.player.gold += (1 + self.level * 0.2) * 100
                self.game.message = message(self.game, 'Clear', 3, size = 100, color = YELLOW)
            else:
                self.game.message = message(self.game, 'Fail', 3, size = 100, color = PURPLE)
                if self.game.player.gold > self.level * 20:
                    self.game.player.gold -= self.level * 20
                else:
                    self.game.player.gold = 0
            self.end_check = True

    def update(self):
        self.background_update()
        self.deco_update()
        if self.end_point and pg.sprite.collide_mask(self.end_point, self.game.player) and not self.end_check:
            self.clear()
        
        if self.game.player.die_check():
            self.end()

    def background_update(self):
        if self.background_follow:
            self.rect.center = vec(int(0.97 * self.game.eyesight.rect.centerx + 0.03 * self.center[0]), int(0.97 * self.game.eyesight.rect.centery + 0.03 * self.center[1]))
    
    def deco_update(self):
        self.deco_center = vec(int(0.5 * self.game.eyesight.rect.centerx + 0.5 * self.center[0]), int(0.5 * self.game.eyesight.rect.centery + 0.5 * self.center[1]))
    
    def block(self, image, location, size = (50, 50)):
        self.ground.append(Obstacles(self.game, {'통상' : Animation([Scene(image, size)], None)}, location=self.start_point + location))
    
    def end_block(self, image, location, size = (50, 50)):
        self.end_point = (decoration(self.game, Scene(image, size), rp=location, follow=False))
    
    def deco(self, image, location, ratio = 1, follow = True):
        if follow:
            a = location - vec(self.deco_center) + vec(self.start_point)
        else:
            a = location
        self.ground.append(decoration(self.game, Scene(image, ratio, t = '비율'), rp = a, follow = follow))
    
    def move_block(self, image, speed, startpoint, endpoint, size = (100, 100)):
        self.ground.append(Obstaclase_Move(self.game, {'통상' : Animation([Scene(image, size)], None)}, speed, self.start_point + startpoint, self.start_point + endpoint))
    
    def move_block_repeat(self, image, speed, startpoint, endpoint, size = (100, 100)):
        self.ground.append(Obstaclase_Move_repeat(self.game, {'통상' : Animation([Scene(image, size)], None)}, speed, self.start_point + startpoint, self.start_point + endpoint))

    def spawn_block(self, spawn_block):
        self.ground.append(spawn_block)

    def Kill_block(self, image, location, size = (50, 50)):
        self.ground.append(Kill_block(self.game, {'통상' : Animation([Scene(image, size)], None)}, location=self.start_point + location))
    
    def Kill_block_move(self, image, speed, startpoint, endpoint, size = (100, 100)):
        self.ground.append(Kill_block_Move(self.game, {'통상' : Animation([Scene(image, size)], None)}, speed, self.start_point + startpoint, self.start_point + endpoint))

    def Kill_block_move_repeat(self, image, speed, startpoint, endpoint, size = (100, 100)):
        self.ground.append(Kill_block_Move_repeat(self.game, {'통상' : Animation([Scene(image, size)], None)}, speed, self.start_point + startpoint, self.start_point + endpoint))

    def black_hole(self, image, location, white_hole, size = (50, 50)):
        self.ground.append(Black_hole(self.game, {'통상' : Animation([Scene(image, size)], None)}, self.start_point+white_hole, location=self.start_point + location))

