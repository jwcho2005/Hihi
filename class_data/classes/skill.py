from .impact import *
import time

class Skill:
    def __init__(self, game, skill_type, animation, cool_time, rp, mp):
        self.game = game
        self.type = skill_type
        self.cool_time = cool_time
        
        self.switch = False
        self.animation = animation
        self.rp = rp
        self.allow = True
        self.trigger_time = 0

        self.mp = mp
        
    def master_set(self, master):
        self.master = master
    
    def trigger(self):
        if self.allow and self.master.mp >= self.mp and self.master.operation:
            self.switch = True
            self.impact = Impact(self.game, self.animation, self.master.direction, master = self.master, location=self.master.rect.center, relative_position=self.master.direction * self.rp)
            self.trigger_time = time.time()
            self.allow = False
            self.master.operation_cancel()
            self.master -= self.mp
    
    def update(self):
        if self.switch:
            if self.impact.animation.end_check():
                self.master.operation = True
                self.switch = False
                self.impact.delete()

        if time.time() - self.trigger_time >= self.cool_time and not self.switch:
            self.allow = True