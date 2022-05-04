from .life import *
from .impact import *

class Enemy(Life):
    def __init__(self, game, animations, attack_timming, attack_end, attack_cooltime, direction = 1, location = vec(0, 0), speed = 0, attack_point = 0, hp = 0, area = 50, aggro_area= 50, die_mp = 15):
        self.groups = game.all_sprites, game.visibles, game.lifes, game.enemies
        Life.__init__(self, game, self.groups, animations, direction=direction, location=location, speed = speed, attack_point= attack_point, hp = hp)
        self.area = area
        self.aggro_area = aggro_area
        self.attack_timming = attack_timming
        self.attack_end = attack_end
        self.attack_cooltime = attack_cooltime
        self.start_time = 0
        self.allow = True
        self.none_operate = ['공격', '바닥충돌']
        self.die_mp = die_mp
        self.fly_states = ['부유', '추락']

    def movestate_update(self):
        if self.state != '죽음':
            if self.floor_contact():
                if not self.operation:
                    if self.velocity.x == 0:
                        if not self.state in self.none_operate:
                            self.state_set('통상')
                            self.operation = True
                            if self.walk_control_l:
                                self.walk_l()
                            if self.walk_control_r:
                                self.walk_r()
                            if not (self.walk_control_l or self.walk_control_r):
                                self.state_set('통상')
                        self.friction_switch = False
                    else:
                        if self.friction_switch:
                            self.velocity.x -= ((self.velocity.x > 0) * 2 - 1) * friction * TIME
                            if -20 < (self.velocity.x) < 20:
                                self.velocity.x = 0
                else:
                    self.friction_switch = False
                    if not self.state == '부유':
                        if self.state == '추락':
                            self.state_set('바닥충돌')
                        else:
                            if not self.state in self.none_operate:
                                if self.walk_control_l or self.walk_control_r:
                                    self.state_set('걷기')
                                else:
                                    self.state_set('통상')
                            self.move()


                if self.velocity.y > 0 and self.state != '부유':
                    self.velocity.y = 0

            else:
                self.velocity += self.acceleration * TIME
                if not self.state in self.fly_states:
                    if self.velocity.y > 0:
                        self.state_set('추락')
                    else:
                        self.state_set('부유')

            if self.ceiling_contact() and self.velocity.y < 0:
                self.velocity.y = 0
            
            self.rect.center += self.velocity * TIME

            self.physics_update()

            if self.state == '공격' or self.state == '넉백':
                if self.game.player.rect.centerx < self.rect.centerx:
                    self.walk_control_l = True
                    self.walk_control_r = False
                else:
                    self.walk_control_r = True
                    self.walk_control_l = False

            if self.state == '공격' and self.attack_end >= self.animation.p_frame >= self.attack_timming:
                self.make_attack()
            
            if not self.allow and ((time.time() - self.start_time) > self.attack_cooltime):
                self.allow = True
            
            if self.die_check():
                self.state_set('죽음')


    def move(self):
        if self.operation:
            if abs(self.game.player.rect.centerx - self.rect.centerx) < self.aggro_area:
                if self.game.player.rect.centerx < self.rect.centerx:
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

    def update(self):
        self.animation_end()
        self.animation_update()
        self.movestate_update()
        self.end_damaged()
    
    def animation_end(self):
        if self.animation.end_check():
            if self.state in self.none_operate:
                self.operation = True

            if self.state == '죽음':
                self.delete()
                self.game.player.heal_mp(self.die_mp)
            
            elif self.state == '바닥충돌':
                if self.walk_control_l or self.walk_control_r:
                    self.state_set('걷기')
                else:
                    self.state_set('통상')
            
            elif self.state == '공격':
                self.state_set('통상')
                if self.walk_control_l:
                    self.walk_l()
                if self.walk_control_r:
                    self.walk_r()
                if not (self.walk_control_l or self.walk_control_r):
                    self.state_set('통상')

    
    def attack(self):
        if self.operation and self.allow:
            self.operation_cancel()
            self.state_set('공격')
            self.allow = False
            self.start_time = time.time()
    
    def floated(self, v):
        self.state_set('부유')
        self.operation_cancel()
        self.velocity += v
    
    def make_attack(self):
        pass