from .classes.enemy import *
from .bigheadsquid_setting import *

class bigheadsquid(Enemy):
    def __init__(self, game, direction=1, location = vec(0, 0)):
        super().__init__(game, bigheadsquid_animations, bigheadsquid_attack_timming, bigheadsquid_attack_end, bigheadsquid_attack_cooltime, direction = direction, location = location, speed = bigheadsquid_speed, attack_point=bigheadsquid_attackpoint_0 * (1 + 0.05 * game.stage.level), hp = bigheadsquid_hp_0 * (1 + 0.05 * game.stage.level), area = bigheadsquid_area, aggro_area = bigheadsquid_aggro_area)
        self.none_bullet = True
        self.attacked = False

    def attack(self):
        if self.operation and self.allow:
            self.operation_cancel()
            self.state_set('공격')
            self.attacked = False
            self.allow = False
            self.start_time = time.time()

    def die_check(self):
        if self.hp <= 0:
            self.attacked = False
            return True
        return False
    
    def make_attack(self):
        if pg.sprite.collide_mask(self, self.game.player) and not self.attacked:
            self.game.player.damaged(self, self.attack_point)
            self.attacked = True
    
    def movestate_update(self):
        if self.state == '죽음':
            if pg.sprite.collide_mask(self, self.game.player) and not self.attacked:
                self.game.player.damaged(self, self.attack_point)
                self.attacked = True
        
        super().movestate_update()