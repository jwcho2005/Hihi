from .classes.enemy import *
from .classes.bullet import *
from .minion_setting import *
import time

class Fireball(Enemy_Bullet):
    def __init__(self, game, animations, v, length, direction, damage, startpoint = vec(0, 0)):
        super().__init__(game, animations, v, length, direction, damage, startpoint = startpoint)
        self.state_set('소환 중')

    def animation_end(self):
        if self.animation.end_check():
            if self.state in ('적 충돌', '벽 충돌'):
                self.delete()
            elif self.state == '소환 중':
                self.state_set('통상')

class minion(Enemy):
    def __init__(self, game, direction=1, location = vec(0, 0)):
        super().__init__(game, minion_animations, minion_attack_timming, minion_attack_timming, minion_fireball_cooltime, direction=direction, location=location, speed=minion_speed, attack_point=minion_attackpoint_0 * (1 + 0.05 * game.stage.level), hp = minion_hp_0 * (1 + 0.05 * game.stage.level), area = minion_area, aggro_area = minion_aggro_area)
        self.fireball_speed = minion_fireball_speed
        self.fireball_rp = minion_fireball_rp
        self.fireball_length = minion_fireball_length
        self.warp_starttime = 0
        self.warp_cooltime = minion_warp_cooltime
        self.hid_time = minion_hid_time
        self.hid = False
        self.hid_starttime = 0
        self.none_operate.append('워프시작')
        self.none_operate.append('워프종료')
        self.fly_states.append('워프시작')
        self.fly_states.append('워프종료')

    def knockbacked(self, v):
        if self.acceleration == 0:
            self.acceleration = g
        self.operation_cancel()
        self.velocity += v
        self.state_set('넉백')
        self.friction_switch = True
    
    def animation_end(self):
        if self.animation.end_check():
            if self.state == '워프시작':
                self.rect.centerx = 2 * self.game.player.rect.centerx - self.rect.centerx
                self.state_set('워프종료')
        
            elif self.state == '워프종료':
                self.acceleration = g
                self.hid = True
                self.hid_starttime = time.time()
                self.operation = True
                self.state_set('통상')
                if self.walk_control_l:
                    self.walk_l()
                if self.walk_control_r:
                    self.walk_r()
                if not (self.walk_control_l or self.walk_control_r):
                    self.state_set('통상')

            super().animation_end()

    def state_set(self, state):
        if self.hid and self.state == state:
            self.image.set_alpha(255)
        super().state_set(state)
        if self.hid and self.state == state:
            self.image.set_alpha(128)
    
    def animation_update(self):
        if self.hid:
            self.image.set_alpha(255)
        super().animation_update()
        if self.hid:
            self.image.set_alpha(128)
        
    def knockbacked(self, v):
        super().knockbacked(v)
        self.acceleration = g
    
    def damaged(self, attacker, damage):
        if self.hid:
            self.hid_cancel()

        super().damaged(attacker, damage)

    def movestate_update(self):
        if self.state != '죽음':
            if (time.time() - self.warp_starttime) > self.warp_cooltime and abs(self.game.player.rect.centerx - self.rect.centerx) < self.area:

                self.rect.centerx = 2 * self.game.player.rect.centerx - self.rect.centerx
                c = True
                for i in self.game.obstacles:
                    if pg.sprite.collide_mask(self, i):
                        c = False
                        break
                if self.floor_contact() and c:
                    self.operation_cancel()
                    self.state_set('워프시작')
                    self.acceleration = vec(0, 0)
                    self.velocity.y = 0
                    self.warp_starttime = time.time()
                self.rect.centerx = 2 * self.game.player.rect.centerx - self.rect.centerx
            
            if self.hid and time.time() - self.hid_starttime > self.hid_time:
                self.hid_cancel()

        super().movestate_update()
    
    def hid_cancel(self):
        self.image.set_alpha(255)
        self.hid = False
        a = self.animation.p_frame
        self.animation.p_frame = a - 1
        self.animation_update()

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
                if self.game.player.rect.centerx > self.rect.centerx:
                    self.direction = 1
                else:
                    self.direction = -1
    
    def make_attack(self):
        Fireball(self.game, fireball_animations, vec(self.direction * self.fireball_speed, 0), self.fireball_length, self.direction, self.attack_point, startpoint = vec(self.rect.center) + vec(self.fireball_rp.x * self.direction, self.fireball_rp.y))