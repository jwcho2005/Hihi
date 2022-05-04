from .classes.animation import *
from .classes.variable import *

minion_scenes_normal_ = [Scene('images\롤미니언\_monster2.png', 50, t = 'x대입')]
ratio = minion_scenes_normal_[0].ratio
minion_scenes_walk_ = [Scene('images\롤미니언\_monster2_walk_'+str(i)+'.png', ratio, t = '비율') for i in range(1, 5)]
minion_scenes_fall_ = [Scene('images\롤미니언\_monster2.png', ratio, t = '비율')]
minion_scenes_floor_c = [Scene('images\롤미니언\_monster2.png', ratio, t = '비율')]
minion_scenes_knockback_ = [Scene('images\롤미니언\_monster2_attacked.png', ratio, t = '비율')]
minion_scenes_fly_ = [Scene('images\롤미니언\_monster2.png', ratio, t = '비율')]
minion_scenes_attack_ = [Scene('images\롤미니언\_monster2.png', ratio, t = '비율')] * 8
minion_scenes_warp_start_ = [Scene('images\롤미니언\_monster2_teleport_'+str(i)+'.png', ratio, t = '비율') for i in range(1, 19)]
minion_scenes_warp_end_ = [Scene('images\롤미니언\_monster2_teleport_'+str(i)+'.png', ratio, t = '비율') for i in range(18, 0, -1)]
minion_scenes_die_ = [Scene('images\롤미니언\_monster2_die_'+str(i)+'.png', ratio, t = '비율') for i in range(1, 5)]
minion_animations = {'통상' : Animation(minion_scenes_normal_, None), 
                    '걷기' : Animation(minion_scenes_walk_, None),
                    '추락' : Animation(minion_scenes_fall_, None),
                    '바닥충돌' : Animation(minion_scenes_floor_c, None),
                    '넉백' : Animation(minion_scenes_knockback_, game_Sound('sound\롤 미니언\다치는 소리.wav')),
                    '부유' : Animation(minion_scenes_fly_, None),
                    '공격' : Animation(minion_scenes_attack_, None),
                    '워프시작' : Animation(minion_scenes_warp_start_, None),
                    '죽음' : Animation(minion_scenes_die_, None),
                    '워프종료' : Animation(minion_scenes_warp_end_, None),
                    }
minion_hp_0 = 200
minion_attackpoint_0 = 3
minion_speed = 75
minion_area = 250
minion_aggro_area = 200

minion_fireball_speed = 200
minion_attack_timming = 0
minion_fireball_rp = vec(20, 0)
minion_fireball_cooltime = 10
minion_fireball_length = 1000

minion_warp_cooltime = 12
minion_hid_time = 2

fireball_scenes_normal_ = [Scene('images\롤미니언\_fireball1_attack_'+ str(i) + 'a.png', 70, t = 'x대입') for i in range(1, 4)]
fireball_ratio = fireball_scenes_normal_[0].ratio
fireball_scenes_wall_ = [Scene('images\롤미니언\_fireball_wall_'+ str(i) + 'a.png', fireball_ratio, t = '비율') for i in range(1, 7)]
fireball_scenes_enemy_ = [Scene('images\롤미니언\_fireball_player_'+ str(i) + 'a.png', fireball_ratio, t = '비율') for i in range(1, 6)]
fireball_scenes_making_ = [Scene('images\롤미니언\_fireball_made_'+ str(i) + '.png', fireball_ratio, t = '비율') for i in range(1, 9)]
fireball_animations = {'통상' : Animation(fireball_scenes_normal_, None),
                        '벽 충돌' : Animation(fireball_scenes_wall_, None),
                        '적 충돌' : Animation(fireball_scenes_enemy_, game_Sound('sound\롤 미니언\파이어볼 플레이어가 맞음.wav')),
                        '소환 중' : Animation(fireball_scenes_making_, game_Sound('sound\롤 미니언\파이어볼 던짐.wav')),
                        }