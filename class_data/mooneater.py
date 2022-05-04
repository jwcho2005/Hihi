from .classes.enemy import *
from .classes.impact import *
from .grimer import *
from .minion import *
from .bigheadsquid import *
from .mooneater_setting import *
import time

class Firepillar(Impact):
    def __init__(self, game, direction, stack, location=vec(0, 0), damage = 0):
        super().__init__(game, firepillar_animations, direction, location=location, damage = damage, loop = 1, tag = ['player'])
        self.stack = stack

    def update(self):
        if self.animation.end_check():
            if self.stack:
                Firepillar(self.game, self.direction, self.stack - 1, location=self.rect.center + vec(self.direction * firepillar_xl, 0), damage=self.damage)

        super().update()

class mooneater(Enemy):
    def __init__(self, game, direction = -1, location=vec(0, 0)):
        super().__init__(game, mooneater_animations,mooneater_attack_timming, mooneater_attack_end, mooneater_attack_cooltime, direction = direction, location=location, speed = mooneater_speed, attack_point=mooneater_attackpoint_0 * (1 + 0.05 * game.stage.level), hp = mooneater_hp_0, area = mooneater_area, aggro_area=mooneater_aggro_area)
        self.minion_cooltime = minion_cooltime
        self.grimer_cooltime = grimer_cooltime
        self.bigheadsquid_cooltime = bigheadsquid_cooltime
        self.minion_starttime = 0
        self.grimer_starttime = 0
        self.bigheadsquid_starttime = 0
        self.enemies = []
        self.max_enemy = max_enemy
    
    def update(self):
        super().animation_end()
        if self.die_check():
            self.game.stage.clear()

        super().animation_update()
        super().end_damaged()

        if self.state != '죽음':
            if abs(self.game.player.rect.centerx - self.rect.centerx) < self.area:
                if (time.time() - self.minion_starttime) > self.minion_cooltime and len(self.enemies) < self.max_enemy:
                    self.enemies.append(minion(self.game, direction = self.direction, location = vec(self.game.player.rect.centerx, self.rect.centery)))
                    self.enemies[-1].area = self.aggro_area
                    self.minion_starttime = time.time()

                if (time.time() - self.bigheadsquid_starttime) > self.bigheadsquid_cooltime and len(self.enemies) < self.max_enemy:
                    self.enemies.append(bigheadsquid(self.game, direction = self.direction, location =vec(self.game.player.rect.centerx, self.rect.centery)))
                    self.enemies[-1].aggro_area = self.aggro_area
                    self.bigheadsquid_starttime = time.time()
                
                if (time.time() - self.grimer_starttime) > self.grimer_cooltime and len(self.enemies) < self.max_enemy:
                    self.enemies.append(grimer(self.game,  direction = self.direction, location = vec(self.game.player.rect.centerx, self.rect.centery)))
                    self.enemies[-1].area = self.aggro_area
                    self.grimer_starttime = time.time()
        
        b = self.enemies.copy()
        for i in b:
            if not pg.sprite.collide_mask(i, self.game.eyesight):
                self.enemies.remove(i)
                i.delete()

            if i.die_check():
                self.enemies.remove(i)

        super().movestate_update()
    
    def make_attack(self):
        Firepillar(self.game, self.direction, 5, location= vec(self.rect.center) + vec(self.direction * firepillar_xl, -98), damage=self.attack_point)

    def delete(self):
        b = self.enemies.copy()
        for i in b:
            i.delete()
            self.enemies.remove(i)
        super().delete()