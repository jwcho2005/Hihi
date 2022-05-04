from .obj import *

class Bullet(obj):
    def __init__(self, game, animations, v, length, direction, damage, startpoint = vec(0, 0)):
        self.groups = game.all_sprites, game.bullets, game.visibles
        obj.__init__(self, game, self.groups, animations, direction=direction, location=startpoint)

        self.velocity = v
        self.length = length
        self.startpoint = startpoint
        self.damage = damage
        self.penetrate = False
        self.hit = False
        if self.animation.sound:
            self.animation.sound.play()
        self.tag = 'enemy'
    
    def animation_end(self):
        if self.animation.end_check():
            if self.state in ('적 충돌', '벽 충돌'):
                self.delete()


    def update(self):
        self.animation_end()
        if abs(self.rect.centerx - self.startpoint.x) > self.length:
            self.delete()

        self.enemy_c()
        self.wall_c()

        self.animation_update()
        self.move()

        if self.state == '적 충돌' or self.state == '벽 충돌':
            self.physics_update()

    def player_c(self):
        if not self.hit and pg.sprite.collide_mask(self, self.game.player) and not self.game.player.none_damage:
            self.state_set('적 충돌')
            if not self.game.player.none_bullet:
                self.game.player.damaged(self, self.damage)
            self.hit = True

    def enemy_c(self):
        if self.state =='통상':
            for i in pg.sprite.spritecollide(self, self.game.enemies, False, pg.sprite.collide_mask):
                self.state_set('적 충돌')
                if not i.none_bullet:
                    i.damaged(self, self.damage)
                self.hit = True

    def wall_c(self):
        for i in pg.sprite.spritecollide(self, self.game.obstacles, False, pg.sprite.collide_mask):
            if not (self.penetrate and i.penetrated):
                self.state_set('벽 충돌')
                self.hit = True
                break
            

    def physics_update(self):
        for i in self.game.obstacles:
            a = []
            if pg.sprite.collide_mask(self, i):
                if self.rect.left < i.rect.left and i.rect.left < self.rect.right and self.rect.right < i.rect.right:
                    a.append(vec(-(self.rect.right - i.rect.left), 0))
                if i.rect.left < self.rect.left and self.rect.left < i.rect.right and i.rect.right < self.rect.right:
                    a.append(vec(i.rect.right - self.rect.left, 0))
            
            if a:
                self.rect.center += min(a, key = lambda x : abs(x.x) + abs(x.y))
    
    def move(self):
        if self.state == '통상':
            self.rect.center += self.velocity * TIME

class Enemy_Bullet(Bullet):
    def __init__(self, game, animations, v, length, direction, damage, startpoint = 0):
        super().__init__(game, animations, v, length, direction, damage, startpoint = startpoint)
        self.tag = 'player'
    
    def enemy_c(self):
        super().player_c()