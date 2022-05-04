from .variable import *
from .obj import *
import time

class Life(obj):
    def __init__(self, game, groups, animations, direction = 1, location = vec(0, 0), speed = 0, jump_speed = 0, attack_point = 0, hp = 0):
        obj.__init__(self, game, groups, animations, direction = direction, location=location)
        self.acceleration = g
        self.speed = speed
        self.speed_0 = speed
        self.jump_speed = jump_speed
        self.jump_speed_0 = jump_speed
        self.operation = True
        self.friction_switch = False

        self.max_hp = hp
        self.hp = self.max_hp
        self.attack_point = attack_point
        self.attack_point_0 = attack_point

        self.walk_control_r = False
        self.walk_control_l = False

        self.none_damage = False
        self.none_bullet = False

        self.buffs = []
    
    def buff_update(self):
        if self.buffs:
            if self.walk_control_r:
                self.velocity.x -= self.speed
            if self.walk_control_l:
                self.velocity.x += self.speed
            self.jump_speed = self.jump_speed_0
            self.speed = self.speed_0
            self.attack_point = self.attack_point_0
            b = self.buffs.copy()
            for i in b:
                if (time.time() - i.starttime) > i.duration:
                    self.buffs.remove(i)
                else:
                    i.apply(self)

            if self.walk_control_r:
                self.velocity.x += self.speed
            if self.walk_control_l:
                self.velocity.x -= self.speed
    
    def get_buff(self, buff):
        self.buffs.append(buff)

    def kill(self):
        if not self.none_damage:
            self.hp = 0

    
    def die_check(self):
        if self.hp <= 0:
            return True
        return False

    def knockbacked(self, v):
        self.operation_cancel()
        self.velocity += v
        if self.state != '죽음':
            self.state_set('넉백')
        self.friction_switch = True
    
    def damaged(self, attacker, damage):
        damage = int(damage)
        if not self.none_damage and self.state != '죽음':
            self.hp -= damage
            if self.rect.center != attacker.rect.center:
                v = 20 * vec(self.rect.centerx - attacker.rect.centerx, self.rect.centery - attacker.rect.centery).normalize()
                self.knockbacked(v)
            if self.die_check():
                self.state_set('죽음')
            self.none_damage = False
    
    def end_damaged(self):
        if self.state == '넉백' and self.animation.end_check():
            self.none_damage = False
    
    def physics_update(self):
        for i in self.game.obstacles:
            a = []
            if pg.sprite.collide_rect(self, i):
                if self.wall_r_contact() and self.velocity.x - i.velocity.x > 0:
                    if self.rect.left < i.rect.left and i.rect.left < self.rect.right and self.rect.right < i.rect.right:
                        a.append(vec(-(self.rect.right - i.rect.left), 0))
                        # v = vec(-1, 0)
                        # while(pg.sprite.collide_mask(i, self)):
                        #     self.rect.center += vec(-1, 0)
                        #     v += vec(-1, 0)
                        # a.append(v)
                if self.wall_l_contact() and self.velocity.x - i.velocity.x < 0:
                    if i.rect.left < self.rect.left and self.rect.left < i.rect.right and i.rect.right < self.rect.right:
                        a.append(vec(i.rect.right - self.rect.left, 0))
                        # v = vec(1, 0)
                        # while(pg.sprite.collide_mask(i, self)):
                        #     self.rect.center += vec(1, 0)
                        #     v += vec(1, 0)
                        # a.append(v)
            # if self.state != '낙하공격':
                if not self.ceiling_contact() and self.velocity.y - i.velocity.y >= 0:
                    if i.rect.bottom > self.rect.bottom and self.rect.bottom > i.rect.top and i.rect.top > self.rect.top: 
                        a.append(vec(0, -(self.rect.bottom-i.rect.top)))
                        # v = vec(0, -1)
                        # while(pg.sprite.collide_mask(i, self)):
                        #     self.rect.center += vec(0, -1)
                        #     v += vec(0, -1)
                        # a.append(v)
                if not self.floor_contact() and self.velocity.y - i.velocity.y < 0:
                    if self.rect.bottom > i.rect.bottom and i.rect.bottom > self.rect.top and self.rect.top > i.rect.top:
                        a.append(vec(0, i.rect.bottom - self.rect.top))
                        # v = vec(0, 1)
                        # while(pg.sprite.collide_mask(i, self)):
                        #     self.rect.center += vec(0, 1)
                        #     v += vec(0, 1)
                        # a.append(v)
            
            if a:
                self.rect.center += min(a, key = lambda x : abs(x.x) + abs(x.y))

    def operation_cancel(self):
        if self.walk_control_r:
            self.walk_r_cancel()
            self.walk_control_r = True
        if self.walk_control_l:
            self.walk_l_cancel()
            self.walk_control_l = True
        self.operation = False

    def walk_r(self):
        if self.operation:
            self.velocity.x += self.speed
            if self.state == '통상':
                self.state_set('걷기')
            self.direction = 1
        self.walk_control_r = True

    def walk_l(self):
        if self.operation:
            self.velocity.x -= self.speed
            if self.state == '통상':
                self.state_set('걷기')
            self.direction = -1
        self.walk_control_l = True

    def walk_r_cancel(self):
        if self.operation and self.walk_control_r:
            self.velocity.x -= self.speed
            if self.state == '걷기':
                self.state_set('통상')
        self.walk_control_r = False


    def walk_l_cancel(self):
        if self.operation and self.walk_control_l:
            self.velocity.x += self.speed
            if self.state == '걷기':
                self.state_set('통상')
        self.walk_control_l = False