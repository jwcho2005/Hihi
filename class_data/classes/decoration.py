from .variable import *
from .obj import *
from .animation import *

class decoration(obj):
    def __init__(self, game, scene, rp = vec(0, 0), follow = True):
        self.groups = game.all_sprites, game.visibles, game.decos
        obj.__init__(self, game, self.groups, {'통상' : Animation([scene], None)})
        self.follow = follow
        self.rp = rp
        if self.follow:
            self.rect.center = self.game.stage.deco_center + self.rp
        else:
            self.rect.center = self.game.stage.start_point + self.rp
    
    def update(self):
        if self.follow:
            self.rect.center = self.game.stage.deco_center + self.rp
        else:
            self.rect.center = self.game.stage.start_point + self.rp

    
