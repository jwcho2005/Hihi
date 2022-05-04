from .obj import *

class Kill_block(obj):
    def __init__(self, game, animations, location=vec(0, 0)):
        self.groups = game.all_sprites, game.gimic_obstacles, game.visibles
        obj.__init__(self, game, self.groups, animations, location=location)
    
    def update(self):
        for i in pg.sprite.spritecollide(self, self.game.lifes, False, pg.sprite.collide_mask):
            i.kill()

class Kill_block_Move(obj):
    def __init__(self, game, animations, speed, startpoint, endpoint):
        self.groups = game.all_sprites, game.gimic_obstacles, game.visibles
        obj.__init__(self, game, self.groups, animations, location=startpoint)

        self.startpoint = startpoint
        self.endpoint = endpoint
        self.speed = speed

        self.length = (self.endpoint - self.startpoint).length()

        self.velocity = (self.endpoint - self.startpoint).normalize() * speed
    
    def update(self):
        for i in pg.sprite.spritecollide(self, self.game.lifes, False, pg.sprite.collide_mask):
            i.kill()

        self.restart()
        self.rect.center += self.velocity * TIME

    def restart(self):
        if (vec(self.rect.center) - self.startpoint).length() >= self.length:
            self.rect.center = self.startpoint

class Kill_block_Move_repeat( Kill_block_Move):  
    def update(self):
        self.restart()
        for i in pg.sprite.spritecollide(self, self.game.lifes, False, pg.sprite.collide_mask):
            i.kill()
        self.rect.center += (self.endpoint - self.startpoint).normalize() * self.speed * TIME
    
    def restart(self):
        if (vec(self.rect.center) - self.startpoint).length() >= self.length:
            self.endpoint, self.startpoint = self.startpoint, self.endpoint 

class Black_hole(obj):
    def __init__(self, game, animations, White_hole, location=vec(0, 0)):
        self.groups = game.all_sprites, game.gimic_obstacles, game.visibles
        obj.__init__(self, game, self.groups, animations, location=location)
        self.out = White_hole
    
    def update(self):
        if pg.sprite.collide_mask(self, self.game.player):
            self.game.player.rect.center = self.out