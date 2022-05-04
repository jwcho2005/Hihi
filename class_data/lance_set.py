from .classes.weapon import *
from .classes.animation import *

lance_cooltime = 0.8

lance_data = {'ironlance' : (50, 1),
            'goldlance' : (70, 3),
            'diamondlance' : (80, 5)}

lance_locations = {'통상' : (20, -35),
            '무소유' : (20, -35),
            '투명' : (20, -35),
            '일반공격' : (50, -70),
            '걷기공격' : (50, -25),
            '낙하공격' : (50, -25),
            }

class Lance(Weapon):
    def __init__(self, name, game, upgrade = 0, location = vec(0, 0)):
        lance_scenes_normal_ = [Scene('images\무기\창\_' + name + '\_' + name + '.png', 21, t = 'x대입')]
        ratio = lance_scenes_normal_[0].ratio
        lance_scenes_attack1_ =  [Scene('images\무기\창\_' + name + '\_' + name + '.png', ratio, t = '비율')] + [Scene('images\무기\창\_' + name + '\_' + name + '_attack1_' + str(i) +'a.png', ratio, t = '비율') for i in range(1, 5)]
        lance_scenes_attack2_ = [Scene('images\무기\창\_' + name + '\_' + name + '.png', ratio, t = '비율')] + [Scene('images\무기\창\_' + name + '\_' + name + '_attack2_' + str(i) +'.png', ratio, t = '비율') for i in range(1, 5)]
        lance_scenes_unvisible_ = [Scene('images\무기\창\_' + name + '\_' + name + '.png', ratio, t = '비율')]
        lance_animations = {'통상' : Animation(lance_scenes_normal_, None),
                            '투명': Animation(lance_scenes_unvisible_, None),
                            '일반공격' : Animation(lance_scenes_attack1_, game_Sound('sound\창\창 찌르기(1).wav')),
                            '걷기공격' : Animation(lance_scenes_attack2_, game_Sound('sound\창\창 가로베기.wav')),
                            '낙하공격' : Animation(lance_scenes_attack2_, game_Sound('sound\창\창 가로베기.wav'))
                            }
        Weapon.__init__(self, name + '+' + str(upgrade), '창', game, lance_animations, lance_data[name][0], lance_locations, lance_cooltime, lance_data[name][1], upgrade = upgrade, location = location)
        self.name_0 = name