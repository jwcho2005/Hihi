from .classes.mouse import *
from .classes.animation import *
from .gun_set import *
from .sword_set import *
from .lance_set import *
from .lobby_setting import *
import random

class Upgrade_Icon(Icon):
    def __init__(self, game, image, location, weapon, face):
        super().__init__(game, image, location, face)
        self.set_weapon = weapon
        self.upgrade_sound = game_Sound('sound\아이콘\망치.wav')
        self.message = Game_Message(self.game, self.set_weapon.name, self.face, location=vec(self.rect.center) + vec(0, -20))
        self.game.lobby.ground.append(self.message)
    
    def trigger(self):
        if self.game.player.gold >= 200:
            if self.set_weapon.upgrade < self.set_weapon.max_upgrade:
                self.upgrade_sound.sound.play()
                self.game.player.gold -= 200
                if self.set_weapon.weapon_upgrade():
                    self.game.message = message(self.game, 'Success', 3, color=BLUE)
                    self.message.delete()
                    self.message = Game_Message(self.game, self.set_weapon.name, self.face, location=vec(self.rect.center) + vec(0, -20))
                    self.game.lobby.ground.append(self.message)
                else:
                    self.game.message = message(self.game, 'Fail', 3, color = RED)
            else:
                self.game.message = message(self.game, 'Max_upgrade', 3, color=BLACK)
        else:
            self.game.message = message(self.game, 'No Money', 3, color=BLACK)

class Change_Icon(Icon):
    def __init__(self, game, image, location, weapon, face):
        super().__init__(game, image, location, face)
        self.set_weapon = weapon
    
    def trigger(self):
        self.game.player.change_weapon(self.set_weapon, self.set_weapon.w_type)
        self.game.message = message(self.game, 'Weapon Changed', 3, color=BLACK)


class Weapon_Icon(Icon):
    def __init__(self, game, image, location, weapon, face):
        super().__init__(game, image, location, face)
        self.set_weapon = weapon
    
    def trigger(self):
        self.game.mouse.face += 1
        self.game.lobby.ground.append(Upgrade_Icon(self.game, Scene('images\아이콘 (1)\_hammericon (1).png', (50, 50)), vec(self.rect.center) + vec(0, -25), self.set_weapon, self.face + 1))
        self.game.lobby.ground.append(Change_Icon(self.game, Scene('images\아이콘 (1)\_changeicon.png', (50, 50)), vec(self.rect.center) + vec(0, 25), self.set_weapon, self.face + 1))



class Inventory_slot(Icon):
    def __init__(self, game, location, face):
        super().__init__(game, Scene('images\아이콘 (1)\_inventory.png', 500, t = 'x대입'), location, face)
    
    def trigger(self):
        self.game.mouse.face = self.face

class Inventory_Icon(Icon):
    def __init__(self, game, location, face):
        super().__init__(game, floor1_image, location, face)
    
    def trigger(self):
        self.game.mouse.face = self.face + 1
        self.game.lobby.ground.append(Inventory_slot(self.game, self.rect.center + vec(425, -75), self.face + 1))
        for j, i in enumerate(self.game.player.weapons):
            a = i.animations['통상'][0].image_tag
            self.game.lobby.ground.append(Weapon_Icon(self.game, Scene(a, 1.3, t = '비율'), self.rect.center + vec(229+98 * (j % 5), 21-98 * (j // 5)), i, self.face + 1))
    

class Stage_Icon(Icon):
    def __init__(self, game, images, location, stage, face):
        self.set_stage = stage
        if game.level + 1 >= self.set_stage.level: 
            super().__init__(game, images[0], location, face)
        else:
            super().__init__(game, images[1], location, face)
    
    def trigger(self):
        if self.game.level + 1 >= self.set_stage.level: 
            self.game.mouse.face += 1
            self.game.lobby.ground.append(Stage_start_Icon(self.game, vec(self.rect.center) + vec(0, 0), self.set_stage, self.face + 1))


class Stage_start_Icon(Icon):
    def __init__(self, game, location, stage, face):
        super().__init__(game, Scene('images\아이콘 (1)\_startbutton.png', 350, t = 'x대입'), location, face)
        self.set_stage = stage

    def trigger(self):
        self.game.lobby.end()
        self.game.stage = self.set_stage
        self.game.stage.start()
    
    
class Store_Icon(Icon):
    def __init__(self, game, location, face):
        super().__init__(game, floor2_image, location, face)

    def trigger(self):
        self.game.mouse.face += 1
        self.game.lobby.ground.append(Icon(self.game, Scene('images\타일\단색\단색1.png', (120, 170)), vec(self.rect.center) + vec(235, 0), self.face + 1))
        self.game.lobby.ground.append(Draw_Icon(self.game, vec(self.rect.center) + vec(235, -53), self.face + 1))
        self.game.lobby.ground.append(Mp_Cure_Icon(self.game, vec(self.rect.center) + vec(235, 0), self.face + 1))
        self.game.lobby.ground.append(Cure_Icon(self.game, vec(self.rect.center) + vec(235, 53), self.face + 1))

class Draw_Icon(Icon):
    def __init__(self, game, location, face):
        super().__init__(game, Scene('images\아이콘 (1)\_gatcha.png', (100, 50)), location, face)
    
    def trigger(self):
        if self.game.player.gold >= 500:
            self.game.player.gold -= 500
            a = random.random()
            b = False
            if a < 0.1:
                b = Sword('ironsword', self.game)
            elif 0.1 <= a < 0.2:
                b = Lance('ironlance', self.game)
            elif 0.2 <= a < 0.25:
                b = Pistol('iron', self.game)
            elif 0.25 <= a < 0.3:
                b = Sniper('iron', self.game)
            elif 0.3 <= a < 0.35:
                b = Shotgun('iron', self.game)
            elif 0.35 <= a < 0.4:
                b = Sword('goldsword', self.game)
            elif 0.4 <= a < 0.45:
                b = Lance('goldlance', self.game)
            elif 0.45 <= a < 0.425:
                b = Pistol('gold', self.game)
            elif 0.425 <= a < 0.45:
                b = Sniper('gold', self.game)
            elif 0.45 <= a < 0.475:
                b = Shotgun('gold', self.game)
            elif 0.475 <= a < 0.5:
                b = Sword('diamondsword', self.game)
            elif 0.5 <= a < 0.525:
                b = Lance('diamondlance', self.game)
            elif 0.525 <= a < 0.5375:
                b = Pistol('diamond', self.game)
            elif 0.5375 <= a < 0.55:
                b = Sniper('diamond', self.game)
            elif 0.55 <= a < 0.5625:
                b = Shotgun('diamond', self.game)
            else:
                self.game.player.gold += 200
                self.game.message = message(self.game, 'GOLD', 3, color=BLACK)
            if b:
                a = False
                for i in self.game.player.weapons:
                    if b.name_0 == i.name_0:
                        a = True
                if a:
                    self.game.message = message(self.game, 'You have same weapon', 3, color=BLACK)
                    b.delete()
                else:
                    self.game.player.add_weapon(b)
                    self.game.message = message(self.game, 'You get new weapon', 3, color=BLACK)
        else:
            self.game.message = message(self.game, 'No Money', 3, color=BLACK)


class Cure_Icon(Icon):
    def __init__(self, game, location, face):
        super().__init__(game, Scene('images\아이콘 (1)\_hphealbutton.png', 100, t = 'x대입'), location, face)
        
    
    def trigger(self):
        if self.game.player.gold >= 200:
            self.game.player.gold -= 200
            if self.game.player.hp + 2 < self.game.player.max_hp:
                self.game.player.hp += 2
            else:
                self.game.player.hp = self.game.player.max_hp
            self.game.message = message(self.game, 'Cured', 3, color=RED)
        else:
            self.game.message = message(self.game, 'No Money', 3, color=BLACK)

class Mp_Cure_Icon(Icon):
    def __init__(self, game, location, face):
        super().__init__(game, Scene('images\아이콘 (1)\_mphealbutton.png', 100, t = 'x대입'), location, face)
        
    
    def trigger(self):
        if self.game.player.gold >= 200:
            self.game.player.heal_mp(100)
            self.game.message = message(self.game, 'Cured', 3, color=BLUE)
        else:
            self.game.message = message(self.game, 'No Money', 3, color=BLACK)

Hp_Icon_animations = {'통상' : Animation([Scene('images\아이콘 (1)\heart_full.png', 40, t = 'x대입')], None), '빈' : Animation([Scene('images\아이콘 (1)\heart_empty.png', 40, t = 'x대입')], None)}

class Hp_Icon(obj):
    def __init__(self, game, rp, hl):
        self.groups = game.all_sprites, game.icons, game.visibles
        super().__init__(game, self.groups, Hp_Icon_animations, location=vec(game.eyesight.rect.center) + rp)
        self.rp = rp
        self.hl = hl
        self.face = 0
    
    def update(self):
        self.rect.center = vec(self.game.eyesight.rect.center) + self.rp
        if self.game.player.hp >= self.hl:
            self.state_set('통상')
        else:
            self.state_set('빈')
    
    def trigger(self):
        pass

Sh_Icon_animations = {'통상' : Animation([Scene('images\아이콘 (1)\shield.png', 40, t = 'x대입')], None), '빈' : Animation([Scene('images\아이콘 (1)\shield_empty.png', 40, t = 'x대입')], None)}

class Sh_Icon(obj):
    def __init__(self, game, rp, hl):
        self.groups = game.all_sprites, game.icons, game.visibles
        super().__init__(game, self.groups, Sh_Icon_animations, location=vec(game.eyesight.rect.center) + rp)
        self.rp = rp
        self.hl = hl
        self.face = 0
    
    def update(self):
        self.rect.center = vec(self.game.eyesight.rect.center) + self.rp
        if self.game.player.sh >= self.hl:
            self.state_set('통상')
        else:
            self.state_set('빈')
    
    def trigger(self):
        pass

class Follow_Icon(Icon):
    def __init__(self, game, image, rp):
        self.rp = rp
        super().__init__(game, image, vec(game.eyesight.rect.center) + self.rp, 0)
    
    def update(self):
        self.rect.center = vec(self.game.eyesight.rect.center) + self.rp

class Mp_bar(Follow_Icon):
    def __init__(self, game, image, rp):
        super().__init__(game, image, rp)
    
    def update(self):
        super().update()
        self.image = pg.transform.scale(self.image, (int(self.game.player.mp * 2), self.rect.height))