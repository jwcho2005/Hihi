
import pygame as pg
from .variable import *

class Scene:
    def __init__(self, image, size_or_x, t = 'xy대입'):
        self.image_tag = image
        image = pg.image.load(image).convert_alpha()
        self.size = size_or_x
        self.ratio = None
        if t == 'xy대입':
            self.size = size_or_x
        else:
            rect = image.get_rect()
            if t == 'x대입':
                self.size = (size_or_x, int(rect.height / rect.width * size_or_x))
                self.ratio = size_or_x / rect.width
            elif t == 'y대입':
                self.size = (int(rect.width / rect.height * size_or_x), size_or_x)
                self.ratio = size_or_x / rect.height
            elif t == '비율':
                self.ratio = size_or_x
                self.size = (int(rect.width * self.ratio), int(rect.height * self.ratio))
        self.image_r = pg.transform.scale(image, self.size)
        self.image_l = pg.transform.flip(self.image_r, True, False)
        self.rect = self.image_l.get_rect()
        self.mask_r = pg.mask.from_surface(self.image_r)
        self.mask_l = pg.mask.from_surface(self.image_l)

class Animation(list):
    def __init__(self, l, s, sound_start = 0, loopstart = 0):
        super().__init__(self)
        for i in l:
            self.append(i)
        self.l_frame = len(self)
        self.p_frame = 0
        if s:
            self.sound = s.sound
            self.sound.set_volume(s.volume)
        else:
            self.sound = None
        self.sound_start = sound_start
        self.loopstart = loopstart
    
    def update(self):
        self.p_frame += 1
        if self.p_frame == self.l_frame:
            self.p_frame = self.loopstart
    
    def init(self):
        self.p_frame = 0

    def p_scene(self, direction):
        if direction == -1:
            return self[self.p_frame].image_l.copy(), self[self.p_frame].rect.copy(), self[self.p_frame].mask_l.copy()
        else:
            return self[self.p_frame].image_r.copy(), self[self.p_frame].rect.copy(), self[self.p_frame].mask_r.copy()
    
    def end_check(self):
        if self.p_frame == self.l_frame - 1:
            return True
        return False

class game_Sound:
    def __init__(self, name, volume = 1):
        self.sound = pg.mixer.Sound(name)
        self.volume = volume
        
class game_Animation(Animation):
    def __init__(self, l, s, rp = vec(0, 0), loopstart = 0):
        super().__init__(l, s, loopstart=loopstart)
        self.rp = rp
    def p_scene(self):
        return self[self.p_frame]