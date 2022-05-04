from .classes.animation import *
from .classes.weapon import *
from .classes.bullet import *

gun_data = {
            'ironpistol' : (40, 1, 3, 1, 30, 10),
            'goldpistol' : (60, 3, 3, 1, 30, 10),
            'diamondpistol' : (80, 5, 3, 1, 30, 10),
            'ironshotgun' : (60, 1, 4, 15, 70, 10),
            'goldshotgun' : (80, 3, 4, 15, 70, 10),
            'diamondshotgun' : (110, 5, 4, 15, 70, 10),
            'ironsniper' : (120, 1, 7, 5, 70, 10),
            'goldsniper' : (160, 3, 7, 5, 70, 10),
            'diamondsniper' : (200, 5, 7, 5, 70, 10),
}

pistol_locations = {'통상' : (30, 0),
            '투명' : (30, 0),
            '일반공격' : (30, 0),
            }

shotgun_locations = {'통상' : (10, 5),
            '투명' : (10, 5),
            '일반공격' : (37, -4),
            }

sniper_locations = {'통상' : (20, 5),
            '투명' : (20, 5),
            '일반공격' : (20, 5),
            }

gun_locations = {
                'pistol' : pistol_locations,
                'shotgun' : shotgun_locations,  
                'sniper' : sniper_locations,
                }

pistol_bullet_length = 300
pistol_bullet_speed = 250
pistol_bullet_rp = vec(10, -5)

sniper_bullet_length = 700
sniper_bullet_speed = 400
sniper_bullet_rp = 70

shotgun_bullet_length = 150
shotgun_bullet_speed = 300
shotgun_bullet_rp = 30


gun_animations = {}

bullet_animations = {}

sniper_bullet_animations = {}

for name in ['pistol', 'shotgun', 'sniper']:
    for series in ['diamond', 'gold', 'iron']:
        series_name = series + name
        gun_xsize = gun_data[series_name][4]
        gun_scenes_normal_ = [Scene('images\무기\총\_' + series_name + '.png', gun_xsize, t = 'x대입')]
        ratio = gun_scenes_normal_[0].ratio
        if name == 'pistol'or name == 'sniper':
            gun_scenes_attack1_ =  [Scene('images\무기\총\_' + series_name + '.png', ratio, t = '비율')]
            if name == 'pistol':
                sound = game_Sound('sound\총\권총.wav')
            else:
                sound = game_Sound('sound\총\저격총.wav')
        elif name == 'shotgun':
            gun_scenes_attack1_ =  [Scene('images\무기\총\_' + series_name + '_attack_' + str(i) + '.png', ratio, t = '비율') for i in range(1, 9)]
            sound = game_Sound('sound\총\샷건.wav')
        gun_animations[series_name] = {'통상' : Animation(gun_scenes_normal_, None),
                            '투명': Animation(gun_scenes_normal_, None),
                            '일반공격' : Animation(gun_scenes_attack1_, sound),
                            }

for series in ['diamond', 'gold', 'iron']:
    bullet_size = gun_data[series_name][5]
    bullet_scenes_normal_ = [Scene('images\무기\총\_' + series + 'bullet.png', bullet_size, t = 'x대입')]
    bullet_ratio = bullet_scenes_normal_[0].ratio
    bullet_scenes_wall_ = [Scene('images\무기\총\_' + series + 'bullet.png', bullet_ratio, t = '비율')]
    bullet_scenes_enemy_ = [Scene('images\무기\총\_' + series + 'bullet.png', bullet_ratio, t = '비율')]
    sniper_bullet_animations[series] = {'통상' : Animation(bullet_scenes_normal_, None),
                            '벽 충돌' : Animation(bullet_scenes_wall_, None),
                            '적 충돌' : Animation(bullet_scenes_enemy_, None),
                            }

for series in ['diamond', 'gold', 'iron']:
    bullet_size = gun_data[series_name][5]
    bullet_scenes_normal_ = [Scene('images\무기\총\_' + series + 'sniper_bullet.png', bullet_size, t = 'x대입')]
    bullet_ratio = bullet_scenes_normal_[0].ratio
    bullet_scenes_wall_ = [Scene('images\무기\총\_' + series + 'sniper_bullet.png', bullet_ratio, t = '비율')]
    bullet_scenes_enemy_ = [Scene('images\무기\총\_' + series + 'sniper_bullet.png', bullet_ratio, t = '비율')]
    bullet_animations[series] = {'통상' : Animation(bullet_scenes_normal_, None),
                            '벽 충돌' : Animation(bullet_scenes_wall_, None),
                            '적 충돌' : Animation(bullet_scenes_enemy_, None),
                            }

class Gun(Weapon):
    def __init__(self, name, series, game, upgrade, location = vec(0, 0)):
        series_name = series + name
        self.name_0 = series_name
        gun_xsize = gun_data[series_name][4]
        self.bullet_animations = bullet_animations[series]
        self.use_mp = gun_data[series_name][3]
        Weapon.__init__(self, series_name, '총', game, gun_animations[series_name], gun_data[series_name][0], gun_locations[name], gun_data[series_name][2], gun_data[series_name][1], upgrade=upgrade, location=location)
    
    def attack(self):
        if self.allow and self.master.mp >= self.use_mp:
            self.normal_attack()
        
            self.master.mp -= self.use_mp
            self.game.visibles.add(self)
            self.allow = False
            self.hit_list = []
            if not self.switch:
                self.switch = True
            self.start_time = time.time()
            self.end_time = time.time()
    
    def hit_check(self):
        pass

class Pistol(Gun):
    def __init__(self, series, game, upgrade = 0, location=vec(0, 0)):
        super().__init__('pistol', series, game, upgrade, location=location)
        self.name = self.name + '+' + str(upgrade)

    def normal_attack(self):
        self.state_set('일반공격')
        Bullet(self.game, self.bullet_animations, vec(self.master.direction, 0) * pistol_bullet_speed, pistol_bullet_length, self.master.direction, self.master.attack_point, startpoint=self.rect.center + vec(self.master.direction * pistol_bullet_rp.x, pistol_bullet_rp.y))

class Sniper(Gun):
    def __init__(self, series, game, upgrade = 0, location=vec(0, 0)):
        super().__init__('sniper', series, game, upgrade, location=location)
        self.bullet_animations = sniper_bullet_animations[series]
        self.name = self.name + '+' + str(upgrade)

    def normal_attack(self):
        self.state_set('일반공격')
        Bullet(self.game, self.bullet_animations, vec(self.master.direction, 0) * sniper_bullet_speed, sniper_bullet_length, self.master.direction, self.master.attack_point, startpoint=self.rect.center + vec(self.master.direction, 0) * sniper_bullet_rp)

class Shotgun(Gun):
    def __init__(self, series, game, upgrade = 0, location=vec(0, 0)):
        super().__init__('shotgun', series, game, upgrade, location=location)
        self.name = self.name + '+' + str(upgrade)

    def attack_end_check(self):
        if self.state == '일반공격' and self.animation.end_check():
            for i in range(-2, 3):
                a = vec(self.master.direction, 0).rotate(15 * i)
                Bullet(self.game, self.bullet_animations, a * shotgun_bullet_speed, shotgun_bullet_length, self.master.direction, self.damage, startpoint=vec(self.rect.center) + a * shotgun_bullet_rp)
        super().attack_end_check()
