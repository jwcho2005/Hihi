from .variable import *
from .message import *
import random

class Mouse(pg.sprite.Sprite):
    def __init__(self, game, image):
        self.groups = game.all_sprites
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = pg.image.load(image).convert_alpha()
        self.image = pg.transform.scale(self.image, (1, 1))
        self.mask = pg.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.center = pg.mouse.get_pos()
        self.face = 0
    
    def update(self):
        a = True
        self.rect.center = vec(pg.mouse.get_pos()) - vec( - self.game.eyesight.rect.center[0] + SCREEN_SIZE[0]/2, - self.game.eyesight.rect.center[1] + SCREEN_SIZE[1]/2)
        for i in pg.sprite.spritecollide(self, self.game.icons, False, pg.sprite.collide_mask):
            if i.face == self.face:
                i.trigger()
                a = False
        
        if a and self.face > 0:
            b = self.game.icons.copy()
            for i in b:
                if i.face == self.face:
                    i.delete()
            self.face -= 1
        

class Icon(pg.sprite.Sprite):
    def __init__(self, game, image, location, face):
        self.groups = game.all_sprites, game.icons, game.visibles
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = image.image_r
        self.mask = image.mask_r
        self.rect = image.rect
        self.rect.center = location
        self.face = face

    def delete(self):
        for i in self.groups:
            i.remove(self)
        del self
    
    def trigger(self):
        pass
    
    def update(self):
        pass

class Game_Message(pg.sprite.Sprite):
    def __init__(self, game, message, face, font = 'calibri', size = 30, location = vec(0, 0), color = WHITE):
        self.groups = game.all_sprites, game.icons, game.visibles
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.font = font
        self.size = size
        message_font = pg.font.SysFont(font, size)
        self.image = message_font.render(message, True, color)
        self.rect = self.image.get_rect()
        self.rect.center = location
        self.face = face
        
    def delete(self):
        for i in self.groups:
            i.remove(self)
        del self

class Follow_Game_Message(Game_Message):
    def __init__(self, game, message, rp,  font = 'calibri', size = 30, color = WHITE):
        self.rp = rp
        super().__init__(game, message, 0, location=self.rp + vec(game.eyesight.rect.center), font = font, size = size, color = color)
    
    def update(self):
        self.rect.center = self.rp + vec(self.game.eyesight.rect.center)

class Mp_num(Follow_Game_Message):
    def update(self):
        message_font = pg.font.SysFont(self.font, self.size)
        self.image = message_font.render(str(self.game.player.mp), True, BLACK)
        self.rect = self.image.get_rect()
        super().update()

class Gold_num(Follow_Game_Message):
    def update(self):
        message_font = pg.font.SysFont(self.font, self.size)
        self.image = message_font.render(str(self.game.player.gold), True, WHITE)
        self.rect = self.image.get_rect()
        super().update()