from .classes.enemy import *
from .classes.bullet import *
from .classes.buff import *
from .classes.variable import *
from .grimer_setting import *
import time
import random

class Soil(Enemy_Bullet):
    def __init__(self, game, direction, v, damage, startpoint = vec(0, 0)):
        super().__init__(game, random.choice([soil1_animations, soil2_animations, soil3_animations]), v, grimer_area + 2000, direction, damage, startpoint=startpoint)

    def move(self):
        if self.state != '벽 충돌' and self.state != '적 충돌':
            self.velocity += g * TIME
            self.rect.center += self.velocity * TIME

    def enemy_c(self):
        if not self.hit and not self.game.player.none_damage:
            if pg.sprite.collide_mask(self, self.game.player):
                self.state_set('적 충돌')
                if not self.game.player.none_bullet:
                    self.game.player.damaged(self, self.damage)
                    self.game.player.buffs.append(Buff({'공격력' : grimer_soil_down_attackpoint, '속도' : grimer_soil_down_speed}, grimer_soil_duration))
                self.hit = True
    
    def physics_update(self):
        for i in self.game.obstacles:
            a = []
            if pg.sprite.collide_mask(self, i):
                if i.rect.bottom > self.rect.bottom and self.rect.bottom > i.rect.top and i.rect.top > self.rect.top: 
                    a.append(vec(0, -(self.rect.bottom-i.rect.top)))
                if self.rect.bottom > i.rect.bottom and i.rect.bottom > self.rect.top and self.rect.top > i.rect.top:
                    a.append(vec(0, i.rect.bottom - self.rect.top))
            if a:
                self.rect.center += min(a, key = lambda x : abs(x.x) + abs(x.y))

class grimer(Enemy):
    def __init__(self, game, direction = 1, location = vec(0, 0)):
        grimer_attackpoint = int((grimer_attackpoint_0) * (1 + 0.05 * (game.stage.level)))
        grimer_hp = int((grimer_hp_0) * (1 + 0.05 * game.stage.level))
        super().__init__(game, grimer_animations, grimer_attack_timming, grimer_attack_timming, grimer_attack_cooltime, direction=direction, location=location, speed = grimer_speed, attack_point=grimer_attackpoint, hp = grimer_hp, area = grimer_area, aggro_area=grimer_aggro_area)
        self.heal_point = int(self.max_hp * grimer_heal_point)
        self.heal_cooltime = grimer_heal_cooltime
        self.heal_starttime = 0

        self.soil_speed = grimer_soil_speed
        self.soil_rp = grimer_soil_rp
        self.none_operate.append('회복')

    def movestate_update(self):
        if self.state != '죽음':
            if (time.time() - self.heal_starttime) > self.heal_cooltime and self.hp != self.max_hp:
                self.state_set('회복')
                self.heal_starttime = time.time()
                self.operation_cancel()


        super().movestate_update()
    
    def animation_end(self):
        if self.animation.end_check():
            if self.state == '회복':
                self.state_set('통상')

            elif self.state == '회복':
                if self.hp + self.heal_point <= self.max_hp:
                    self.hp += self.heal_point
                else:
                    self.hp = self.max_hp

            super().animation_end()
            
    
    def move(self):
        if self.operation:
            if abs(self.game.player.rect.centerx - self.rect.centerx) < self.aggro_area:
                if self.game.player.rect.centerx > self.rect.centerx:
                    if not self.walk_control_l:
                        self.walk_r_cancel()
                        self.walk_l()
                else:
                    if not self.walk_control_r:
                        self.walk_l_cancel()
                        self.walk_r()
            else: 
                self.walk_r_cancel()
                self.walk_l_cancel()

            if abs(self.game.player.rect.centerx - self.rect.centerx) < self.area:
                self.attack()
    
    def make_attack(self):
        x = -self.game.player.rect.centerx + self.rect.centerx
        y = self.game.player.rect.centery - self.rect.centery
        pm = -abs(self.game.player.rect.centerx)/self.game.player.rect.centerx
        k = self.soil_speed**2+2*g.y*y
        if k>=0:
            t = (self.soil_speed+k**0.5)/g.y
            v_x = pm*x/t
        else:
            v_x = 0
        a = vec(self.rect.center) + vec(self.soil_rp * self.direction, self.soil_rp.y)
        v = vec(v_x , -self.soil_speed)
        Soil(self.game, self.direction, v, self.attack_point, startpoint = a)