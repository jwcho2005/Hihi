from .classes.obstacles import *
from .minion import *
from .grimer import *
from .bigheadsquid import *

class spawn_minion(Obstaclase_spawn):
    def __init__(self, game, animations, num, location=vec(0, 0)):
        super().__init__(game, animations, num, location=location)
        self.rps = [vec(-(num - 1) * 50 + 100 * i, -100) for i in range(num)]

    def spawn(self):
        for i in self.rps:
            self.enemies.append(minion(self.game, location = vec(self.rect.center) + i))


class spawn_bigheadsquid(Obstaclase_spawn):
    def __init__(self, game, animations, num, location=vec(0, 0)):
        super().__init__(game, animations, num, location=location)
        self.rps = [vec(-(num - 1) * 50 + 100 * i, -100) for i in range(num)]

    def spawn(self):
        for i in self.rps:
            self.enemies.append(bigheadsquid(self.game, location = vec(self.rect.center) + i))

class spawn_grimer(Obstaclase_spawn):
    def __init__(self, game, animations, num, location=vec(0, 0)):
        super().__init__(game, animations, num, location=location)
        self.rps = [vec(-(num - 1) * 50 + 100 * i, -100) for i in range(num)]

    def spawn(self):
        for i in self.rps:
            self.enemies.append(grimer(self.game, location = vec(self.rect.center) + i))

    
