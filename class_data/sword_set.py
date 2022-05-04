from .classes.animation import *
from .classes.weapon import *
from .classes.impact import *

sword_cooltime = 0.5
sword_data = {
            'ironsword' : (70, 1),
            'goldsword' : (80, 3),
            'diamondsword' : (100, 5),
}

sword_locations = {'통상' : (20, -18),
            '무소유' : (20, -18),
            '투명' : (20, -18),
            '일반공격' : (30, -18),
            '걷기공격' : (20, 10),
            '낙하공격' : (0, 40),
            '낙하공격_끝' : (0, 40)
            }



class Sword(Weapon):
    def __init__(self, name, game, upgrade = 0, location = vec(0, 0)):


        sword_xsize = 24
        sword_scenes_normal_ = [Scene('images\무기\검\_' + name + '\_' + name + '.png', sword_xsize, t = 'x대입')]
        ratio = sword_scenes_normal_[0].ratio
        sword_scenes_attack1_ =  [Scene('images\무기\검\_' + name + '\_' + name + '.png', ratio, t = '비율')] + [Scene('images\무기\검\_' + name + '\_' + name + '_attack1_' + str(i) +'.png', ratio, t = '비율') for i in range(1, 5)]
        sword_scenes_attack2_ = [Scene('images\무기\검\_' + name + '\_' + name + '.png', ratio, t = '비율')] + [Scene('images\무기\검\_' + name + '\_' + name + '_attack3_' + str(i) +'.png', ratio * 1.2, t = '비율') for i in range(1, 5)]
        sword_scenes_attack3_ = [Scene('images\무기\검\_' + name + '\_' + name + '_down.png', ratio, t = '비율')]
        sword_scenes_attack3_end = [Scene('images\무기\검\_' + name + '\_' + name + '_down.png', ratio, t = '비율') for i in range(1, 7)]
        sword_scenes_unvisible_ = [Scene('images\무기\검\_' + name + '\_' + name + '.png', ratio, t = '비율')]
        sword_animations = {'통상' : Animation(sword_scenes_normal_, None),
                            '투명': Animation(sword_scenes_unvisible_, None),
                            '일반공격' : Animation(sword_scenes_attack1_, game_Sound('sound\칼\칼-세로긋기(짧게).wav')),
                            '걷기공격' : Animation(sword_scenes_attack2_, game_Sound('sound\칼\칼-가로 긋기.wav')),
                            '낙하공격' : Animation(sword_scenes_attack3_, None),
                            '낙하공격_끝' : Animation(sword_scenes_attack3_end, game_Sound('sound\칼\칼 내려찍기(뒷부분).wav'))
                            }

        sword_scenes_attack3_end_impact = [Scene('images\무기\검\_' + name + '\_' + name + '_attack2_' + str(i) +'.png', ratio, t = '비율') for i in range(1, 7)]
        self.sword_end_impact_animations = {'통상' : Animation(sword_scenes_attack3_end_impact, None)}
        self.sword_end_impact_rp = vec(0, -40)
        Weapon.__init__(self, name + '+' + str(upgrade), '검', game, sword_animations, sword_data[name][0], sword_locations, sword_cooltime, sword_data[name][1], upgrade = upgrade, location = location)
        self.name_0 = name
    def attack_end_check(self):
        if self.animation.end_check() and self.state != '낙하공격' and self.state != '낙하공격_끝':
            self.state_set('통상')
        
        if self.state == '낙하공격_끝' and self.animation.end_check():
            self.state_set('통상')
            self.master.state_set('통상')
    
    def down_attack(self):
        self.state_set('낙하공격')
        self.master.state_set('낙하공격')
        self.master.operation_cancel()
        self.master.velocity.y = 300
    
    def location_update(self):
        Weapon.location_update(self)
        if self.state == '낙하공격' and (self.floor_contact() or self.master.floor_contact()):
        #     self.rect.centery += 1
        #     for i in self.game.obstacles:
        #         if (pg.sprite.collide_rect(self, i)):
        #             self.rect.centery -= 1
        #             self.rect.bottom = i.rect.top
        #             break
        #     self.master.rect.center = self.rect.center - vec(self.master.direction * self.locations[self.state][0], self.locations[self.state][1])
            a = []
            for i in self.game.obstacles:
                if (pg.sprite.collide_mask(self, i)):
                    a.append(i.rect.top - self.rect.bottom)
            if a:
                self.rect.bottom += max(a)
            self.rect.centery -= 1
            self.state_set('낙하공격_끝')
            Impact(self.game, self.sword_end_impact_animations, self.master.direction, master = self, relative_position=self.sword_end_impact_rp, damage=self.master.attack_point, loop = 1)
            self.master.velocity.y = 0

