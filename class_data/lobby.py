from .classes.stage import *
from .classes.mouse import *
from .lobby_setting import *
from .Icons import *
from .stage_placement import *

class Lobby(Stage):
    def __init__(self, game):
        super().__init__(game, 'lobby', 0, lobby_start_point, lobby_center, lobby_background, lobby_sound, background_follow=False)
    
    def end(self):
        self.sound.stop()
        self.game.player.none_damage = True
        self.game.player.sh = self.game.player.max_sh
        self.game.player.acceleration = g
        self.game.operation = True
        self.game.eyesight.mode = 'x추적'
        self.game.visibles.add(self.game.player)
        b = self.ground.copy()
        for i in b:
            self.ground.remove(i)
            i.delete()
    
    def update(self):
        pass

    def start(self):
        self.sound.play(-1)
        self.game.mouse = Mouse(self.game, 'images\타일\단색\단색1.png')
        self.ground.append(Store_Icon(self.game,  vec(self.start_point) + vec(-265, 545), 0))
        self.ground.append(Inventory_Icon(self.game, vec(lobby_start_point) + vec(-265, 545 - 1 * floor_ysize), 0))
        self.ground.append(Stage_Icon(self.game, floor3_image, vec(self.start_point) + vec(-265, 545 - 2 * floor_ysize), Stage_1(self.game), 0))
        self.ground.append(Stage_Icon(self.game, floor4_image, vec(self.start_point) + vec(-265, 545 - 3 * floor_ysize), Stage_2(self.game), 0))
        self.ground.append(Stage_Icon(self.game, floor5_image, vec(self.start_point) + vec(-265, 545 - 4 * floor_ysize), Stage_3(self.game), 0))
        self.ground.append(Stage_Icon(self.game, floor6_image, vec(self.start_point) + vec(-265, 545 - 5 * floor_ysize), Stage_4(self.game), 0))
        self.ground.append(Stage_Icon(self.game, floor7_image, vec(self.start_point) + vec(-265, 545 - 6 * floor_ysize), Stage_Boss(self.game), 0))
        # self.ground.append(Stage_Icon(self.game, floor8_image, vec(self.start_point) + vec(-300, 545 - 7 * floor_ysize), test_Stage(self.game), 0))
        self.ground.append(Icon(self.game, floor8_image, vec(self.start_point) + vec(-265, 545 - 7 * floor_ysize), 0))

        super().start()
        self.game.player.none_damage = True
        if self.game.player.hp == 0:
            self.game.player.hp = 1
        self.game.player.sh = self.game.player.max_sh
        self.game.player.operation_cancel()
        self.game.player.state_set('통상')
        self.game.visibles.add(self.game.player)
        self.game.player.weapon.state_set('투명')
        self.game.visibles.remove(self.game.player)

        self.game.player.velocity = vec(0, 0)
        self.game.player.acceleration = vec(0, 0)
        self.game.eyesight.mode = '중앙'
        self.game.eyesight.rect.center = self.center + vec(0, 315)
        self.game.mouse = Mouse(self.game, 'images\타일\단색\단색1.png')