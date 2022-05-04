from .classes.animation import *
from .classes.variable import *

grimer_xsize = 50

grimer_scenes_normal_ = [Scene('images\질뻐기\_monster1_usual' + str(i) + '.png', grimer_xsize, t = 'x대입') for i in range(1, 3) for j in range(4)]
ratio = grimer_scenes_normal_[0].ratio

grimer_scenes_walk_ = [Scene('images\질뻐기\_monster1_usual' + str(i) + '.png', ratio, t = '비율') for i in range(1, 3) for j in range(4)]
grimer_scenes_fall_ = [Scene('images\질뻐기\_monster1_usual' + str(i) + '.png', ratio, t = '비율') for i in range(1, 3) for j in range(4)]
grimer_scenes_knockback_ = [Scene('images\질뻐기\_monster1_attacked.png', ratio, t = '비율')]
grimer_scenes_fly_ = [Scene('images\질뻐기\_monster1_usual' + str(i) + '.png', ratio, t = '비율') for i in range(1, 3) for j in range(4)]
grimer_scenes_attack_ = [Scene('images\질뻐기\_monster1_attack_' + str(i) + '.png', ratio, t = '비율') for i in range(1, 8)]
grimer_scenes_die_ = [Scene('images\질뻐기\_monster1_die_' +str(i)+ '.png', ratio, t = '비율') for i in range(1, 7)]
grimer_scenes_heal_ = [Scene('images\질뻐기\_monster1_heal_' +str(i)+ '.png', ratio, t = '비율') for i in range(1, 3) for j in range(10)]
grimer_scenes_floor_c_ = [Scene('images\질뻐기\_monster1_usual1.png', ratio, t = '비율')] +  [Scene('images\질뻐기\_monster1_falling_' +str(i)+ '.png', ratio, t = '비율') for i in range(1, 3) for j in range(3)]


grimer_animations = {'통상' : Animation(grimer_scenes_normal_, None), 
                    '걷기' : Animation(grimer_scenes_walk_, None),
                    '추락' : Animation(grimer_scenes_fall_, None),
                    '넉백' : Animation(grimer_scenes_knockback_, game_Sound('sound\질퍽이\피격음.wav')),
                    '부유' : Animation(grimer_scenes_fly_, None),
                    '공격' : Animation(grimer_scenes_attack_, None),
                    '죽음' : Animation(grimer_scenes_die_, None),
                    '회복' : Animation(grimer_scenes_heal_, game_Sound('sound\질퍽이\트림소리(1).wav')),
                    '바닥충돌' : Animation(grimer_scenes_floor_c_, game_Sound('sound\질퍽이\질퍽이 철푸덕.wav')),
                    }

grimer_hp_0 = 150
grimer_attackpoint_0 = 2
grimer_speed = 50
grimer_area = 350
grimer_aggro_area = 300

grimer_soil_speed = 275
grimer_attack_timming = 0
grimer_attack_cooltime = 6
grimer_soil_rp = vec(0, 0)
grimer_soil_down_attackpoint = -0.4
grimer_soil_down_speed = -0.4
grimer_soil_duration = 3

grimer_heal_point = 1/3
grimer_heal_cooltime = 8

soil1_size = 30
soil2_size = 30
soil3_size = 30

soil1_scenes_normal_ = [Scene('images\질뻐기\_fivewater1_flying.png', soil1_size, t = 'x대입')]
ratio = soil1_scenes_normal_[0].ratio
soil1_scenes_wall_ = [Scene('images\질뻐기\_fivewater1_ground_' + str(i) + '.png', ratio, t = '비율') for i in range(1, 5)]
soil1_scenes_enemy_ = [Scene('images\질뻐기\_fivewater1_explode_' + str(i) + '.png', ratio, t = '비율') for i in range(1, 4)]
soil1_animations = {'통상' : Animation(soil1_scenes_normal_, None),
                        '벽 충돌' : Animation(soil1_scenes_wall_, game_Sound('sound\질퍽이\오물 폭발 소리.wav', volume = 0.5)),
                        '적 충돌' : Animation(soil1_scenes_enemy_, game_Sound('sound\질퍽이\오물 폭발 소리.wav', volume = 0.5)),
                        }

soil2_scenes_normal_ = [Scene('images\질뻐기\_fivewater2_flying.png', soil2_size, t = 'x대입')]
ratio = soil1_scenes_normal_[0].ratio
soil2_scenes_wall_ = [Scene('images\질뻐기\_fivewater2_ground_' + str(i) + '.png', ratio, t = '비율') for i in range(1, 5)]
soil2_scenes_enemy_ = [Scene('images\질뻐기\_fivewater2_explode_' + str(i) + '.png', ratio, t = '비율') for i in range(1, 4)]
soil2_animations = {'통상' : Animation(soil2_scenes_normal_, None),
                        '벽 충돌' : Animation(soil2_scenes_wall_, game_Sound('sound\질퍽이\오물 폭발 소리.wav', volume = 0.5)),
                        '적 충돌' : Animation(soil2_scenes_enemy_, game_Sound('sound\질퍽이\오물 폭발 소리.wav', volume = 0.5)),
                        }

soil3_scenes_normal_ = [Scene('images\질뻐기\_fivewater3_flying.png', soil3_size, t = 'x대입')]
ratio = soil1_scenes_normal_[0].ratio
soil3_scenes_wall_ = [Scene('images\질뻐기\_fivewater3_ground_' + str(i) + '.png', ratio, t = '비율') for i in range(1, 5)]
soil3_scenes_enemy_ = [Scene('images\질뻐기\_fivewater3_explode_' + str(i) + '.png', ratio, t = '비율') for i in range(1, 4)]
soil3_animations = {'통상' : Animation(soil3_scenes_normal_, None),
                        '벽 충돌' : Animation(soil3_scenes_wall_, game_Sound('sound\질퍽이\오물 폭발 소리.wav', volume = 0.5)),
                        '적 충돌' : Animation(soil3_scenes_enemy_, game_Sound('sound\질퍽이\오물 폭발 소리.wav', volume = 0.5)),
                        }
