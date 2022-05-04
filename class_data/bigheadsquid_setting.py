from .classes.animation import *

bigheadsquid_xsize = 50

bigheadsquid_scenes_normal_ = [Scene('images\대두오징어 (1)\_monster3.png', bigheadsquid_xsize, t = 'x대입')]
ratio = bigheadsquid_scenes_normal_[0].ratio
bigheadsquid_scenes_walk_ = [Scene('images\대두오징어 (1)\_monster3_walk_' + str(i) + '.png', ratio, t = '비율') for i in range(1, 3)]
bigheadsquid_scenes_fall_ = [Scene('images\대두오징어 (1)\_monster3.png', ratio, t = '비율')]
bigheadsquid_scenes_knockback_ = [Scene('images\대두오징어 (1)\_monster3_attacked.png', ratio, t = '비율')]
bigheadsquid_scenes_attack_ = [Scene('images\대두오징어 (1)\_monster3_bow_' + str(i) + '.png', ratio, t = '비율') for i in range(1, 8)]
bigheadsquid_scenes_fly_ = [Scene('images\대두오징어 (1)\_monster3_attacked.png', ratio, t = '비율')]
bigheadsquid_scenes_die_ = [Scene('images\대두오징어 (1)\_monster3_die_'+ str(i) + '.png', ratio, t = '비율') for i in range(1, 5)]
bigheadsquid_scenes_floor_c_ = [Scene('images\대두오징어 (1)\_monster3_fall_' + str(i) + '.png', ratio, t = '비율') for i in range(1, 4)]
bigheadsquid_animations = {'통상' : Animation(bigheadsquid_scenes_normal_, None), 
                    '걷기' : Animation(bigheadsquid_scenes_walk_, None),
                    '추락' : Animation(bigheadsquid_scenes_fall_, None),
                    '넉백' : Animation(bigheadsquid_scenes_knockback_, game_Sound('sound\대두오징어\오징어-피격.wav')),
                    '공격' : Animation(bigheadsquid_scenes_attack_, game_Sound('sound\대두오징어\오징어-공격.wav')),
                    '부유' : Animation(bigheadsquid_scenes_fly_, None),
                    '죽음' : Animation(bigheadsquid_scenes_die_, None),
                    '바닥충돌' : Animation(bigheadsquid_scenes_floor_c_, None),
                    }
bigheadsquid_hp_0 = 250
bigheadsquid_attackpoint_0 = 2
bigheadsquid_speed = 90
bigheadsquid_area = 30
bigheadsquid_aggro_area = 225
bigheadsquid_attack_timming = 1
bigheadsquid_attack_cooltime = 4
bigheadsquid_attack_end = 6