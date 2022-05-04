from .classes.animation import *

mooneater_scenes_normal_ = [Scene('images\보스 (1)\_boss.png', 200, t = 'x대입')]
ratio = mooneater_scenes_normal_[0].ratio
mooneater_scenes_walk_ = [Scene('images\보스 (1)\_boss_walk_' + str(i) + '.png',  ratio, t = '비율') for i in range(1, 5)]
mooneater_scenes_fall_ = [Scene('images\보스 (1)\_boss.png',  ratio, t = '비율')]
mooneater_scenes_floor_c = [Scene('images\보스 (1)\_boss.png',  ratio, t = '비율')]
mooneater_scenes_knockback_ = [Scene('images\보스 (1)\_boss_attacked_' + str(i) + '.png',  ratio, t = '비율') for i in range(1, 3)]
mooneater_scenes_fly_ = [Scene('images\보스 (1)\_boss.png',  ratio, t = '비율')]
mooneater_scenes_attack_ = [Scene('images\보스 (1)\_boss_attack_' + str(i) + '.png',  ratio, t = '비율') for i in range(1, 7) for _ in range(6)]
mooneater_scenes_die_ = [Scene('images\보스 (1)\_boss_die_'+str(i)+'.png',  ratio, t = '비율') for i in range(1, 14)]
mooneater_animations = {'통상' : Animation(mooneater_scenes_normal_, None), 
                    '걷기' : Animation(mooneater_scenes_walk_, None),
                    '추락' : Animation(mooneater_scenes_fall_, None),
                    '바닥충돌' : Animation(mooneater_scenes_floor_c, None),
                    '넉백' : Animation(mooneater_scenes_knockback_, game_Sound('sound\보스\y2mate (mp3cut.net).mp3')),
                    '부유' : Animation(mooneater_scenes_fly_, None),
                    '공격' : Animation(mooneater_scenes_attack_, None),
                    '죽음' : Animation(mooneater_scenes_die_, None),
                        }

mooneater_first_animation = game_Animation([Scene('images\보스,animation1\_animation1_' + str(i) +'.png', (1440, 810)) for i in range(1, 31) for j in range(5)], None)
mooneater_second_animation = game_Animation([Scene('images\보스,animation1\_animation2_' + str(i) +'.png', (1440, 810)) for i in range(1, 31) for j in range(5)], None)
mooneater_third_animation = game_Animation([Scene('images\보스,animation1\_animation3_' + str(i) +'.png', (1440, 810)) for i in range(1, 49) for j in range(5)] + [Scene('images\보스,animation1\_animation3_48.png', (1440, 810))] * 240, None)

mooneater_hp_0 = 2300
mooneater_attackpoint_0 = 1
mooneater_speed = 100
mooneater_area = 300
mooneater_aggro_area = 1050

mooneater_attack_timming = 30
mooneater_attack_end = 30
mooneater_attack_cooltime = 6

minion_cooltime = 11
grimer_cooltime = 7
bigheadsquid_cooltime = 12
max_enemy = 2

firepillar_xsize = 150
firepillar_xl = 70
firepillar_scenes = [Scene('images\보스 (1)\_firepillar_' + str(i) + '.png',  firepillar_xsize, t = 'x대입') for i in range(1, 5) for j in range(3)]
firepillar_animations = {'통상' : Animation(firepillar_scenes, None)}
