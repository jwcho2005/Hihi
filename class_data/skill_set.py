from .classes.animation import *
from .classes.skill import *
from .classes.message import *
from .player_setting import *

class Dash(Skill):
    def __init__(self, game):
        super().__init__(game, '이동기',{'통상' : Animation([Scene('images\대쉬\dashcloud.png', ratio, t = '비율')] * 5, None)}, 4, vec(-10, 0), 20)
        self.length = vec(40, 0) * FPS
        self.direction = 1

    def trigger(self):
        if self.allow and self.master.operation and self.master.mp > self.mp:
            self.switch = True
            self.master.mp -= self.mp
            self.trigger_time = time.time()
            self.allow = False
            self.master.operation_cancel()
            self.direction = self.master.direction
            if self.master.walk_control_r:
                self.direction = 1
            if self.master.walk_control_l:
                self.direction = -1
            self.master.velocity = self.direction * self.length
            self.master.velocity.y = 0
            self.impact = Impact(self.game, self.animation, self.master.direction, master = self.master, location = self.master.direction * vec(-50, 0), relative_position=vec(-50, 0))
            self.master.state_set('대쉬')
            self.master.weapon.state_set('투명')
            self.master.none_damage = True
        elif not self.allow:
            self.game.message = message(self.game, "It's cooltime", 1)
        elif self.master.mp <= self.mp:
            self.game.message = message(self.game, "You have no mp", 1)
    
    def update(self):
        if self.switch:
            self.master.velocity.y = 0
            if self.impact.animation.end_check():
                self.switch = False
                self.master.velocity -= self.direction * self.length
                self.master.none_damage = False


        if time.time() - self.trigger_time >= self.cool_time and self.master.floor_contact() and not self.switch:
            self.allow = True