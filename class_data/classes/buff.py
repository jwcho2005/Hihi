import time

class Buff:
    def __init__(self, effect, duration):
        self.effect = effect
        self.duration = duration
        self.starttime = time.time()

    def apply(self, target):
        for i in self.effect:
            if i == '공격력':
                target.attack_point *= (1 + self.effect[i])
            elif i == '속도':
                target.speed *= (1 + self.effect[i]) 
                target.jump_speed *= (1 + self.effect[i])