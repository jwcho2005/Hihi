from .obj import *

class Obstacles(obj):
    def __init__(self, game, animations, location = vec(0, 0), penetrated = False):
        self.groups = game.all_sprites, game.obstacles, game.visibles
        obj.__init__(self, game, self.groups, animations, location=location)
        self.penetrated = penetrated
    
    def update(self):
        pass

class Obstaclase_Move(Obstacles):
    def __init__(self, game, animations, speed, startpoint, endpoint):
        super().__init__(game, animations, location=startpoint)

        self.startpoint = startpoint
        self.endpoint = endpoint
        self.speed = speed

        self.velocity = (self.endpoint - self.startpoint).normalize() * speed
    
    def update(self):
        self.restart()
        self.rect.center += self.velocity * TIME
        self.life_check()

    def restart(self):
        if (vec(self.rect.center) - self.startpoint).length() >= (self.endpoint - self.startpoint).length():
            self.rect.center = self.startpoint
    
    def life_check(self):
        self.rect.center += vec(0, -5)
        if pg.sprite.collide_mask(self, self.game.player):
            self.game.player.rect.center += (self.endpoint - self.startpoint).normalize() * self.speed * TIME
        for i in pg.sprite.spritecollide(self, self.game.weapons, False, pg.sprite.collide_mask):
            if i.w_type == '검' and (i.state == '낙하공격' or i.state == '낙하공격_끝'):
                if self.state == '낙하공격':
                    i.state_set('낙하공격_끝')
                self.game.player.weapon.rect.center += (self.endpoint - self.startpoint).normalize() * self.speed * TIME
        
        for i in pg.sprite.spritecollide(self, self.game.enemies, False, pg.sprite.collide_mask):
            i.rect.center += (self.endpoint - self.startpoint).normalize() * self.speed * TIME

        self.rect.center -= vec(0, -5)

class Obstaclase_Move_repeat(Obstaclase_Move):
    def __init__(self, game, animations, speed, startpoint, endpoint):
        super().__init__(game, animations, speed, startpoint, endpoint)
        self.length = (self.endpoint - self.startpoint).length()
    
    def update(self):
        self.restart()
        self.rect.center += (self.endpoint - self.startpoint).normalize() * self.speed * TIME
        self.life_check()
    
    def restart(self):
        if (vec(self.rect.center) - self.startpoint).length() >= self.length:
            self.endpoint, self.startpoint = self.startpoint, self.endpoint        

class Obstaclase_spawn(Obstacles):
    def __init__(self, game, animations, num, location = vec(0, 0)):
        self.groups = game.all_sprites, game.obstacles, game.visibles
        super().__init__(game, animations, location=location)
        self.num = num
        self.spawned = False
        self.enemies = []
    
    def update(self):
        self.spawn_check()
    
    def spawn_check(self):
        if pg.sprite.collide_mask(self, self.game.eyesight) and not self.spawned:
                self.spawn()
                self.spawned = True

    def spawn(self):
        pass

    def delete(self):
        for i in self.enemies:
            i.delete()
        super().delete()