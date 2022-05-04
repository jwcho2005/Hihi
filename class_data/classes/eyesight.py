from .variable import *
from .message import *

class Eyesight(pg.sprite.Sprite):
    def __init__(self, game, image, size = (100, 100), location = vec(0, 0)):
        self.groups = game.all_sprites
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = pg.image.load(image).convert_alpha()
        self.image = pg.transform.scale(self.image, size)
        self.rect = self.image.get_rect()
        self.rect.center = location
        self.mask = pg.mask.from_surface(self.image)
        self.mode = 'x추적'
        # '추적', 'x추적', 'y추적', '중앙'

    def get_hit_list(self, a):
        hit_list = []
        for i in pg.sprite.spritecollide(self,a,False,pg.sprite.collide_mask):
            if i in self.game.visibles:
                hit_list.append(i)
        return hit_list
    
    def location_update(self):
        if self.mode == '추적':
            self.rect.center = vec(self.game.player.rect.centerx, self.game.player.rect.centery)
        elif self.mode == 'x추적':
            self.rect.centerx = self.game.player.rect.centerx
        elif self.mode == 'y추적':
            self.rect.centery = self.game.player.rect.centery
        elif self.mode == '중앙':
            pass

    def update(self):
        self.location_update()