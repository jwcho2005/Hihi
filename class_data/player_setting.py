from .classes.animation import *

player_scenes_normal_ = [Scene('images\플레이어\walk_1.png', 50, t = 'x대입')]
ratio = player_scenes_normal_[0].ratio

player_scenes_jump_ = [Scene('images\플레이어\jump_3.png', ratio, t = '비율')]
player_scenes_walk_ = [Scene('images\플레이어\walk_' + str(i) + '.png', ratio, t = '비율') for i in range(1, 7)]
player_scenes_fall_ = [Scene('images\플레이어\walk_1.png', ratio, t = '비율')]
player_scenes_dash_ = [Scene('images\플레이어\jump_1.png', ratio, t = '비율')] * 5
player_scenes_knockback_ = [Scene('images\플레이어\_attacked.png', ratio, t = '비율')]
player_scenes_jump_start_ = [Scene('images\플레이어\jump_' + str(i) + '.png', ratio, t = '비율') for i in range(1, 4)]
player_scenes_attack3_ = [Scene('images\플레이어\_attack2.png', ratio, t = '비율')]
player_scenes_die_ = [Scene('images\플레이어\jump_3.png', ratio, t = '비율')] + [Scene('images\플레이어\die_' + str(i) + '.png', ratio, t = '비율') for i in range(1, 5)]
player_animations = {'통상' : Animation(player_scenes_normal_, None), 
                    '점프' : Animation(player_scenes_jump_, None),
                    '점프시작' :  Animation(player_scenes_jump_start_ , game_Sound('sound\플레이어\플레이어-점프.wav')),
                    '걷기' : Animation(player_scenes_walk_, None),
                    '대쉬' : Animation(player_scenes_dash_, game_Sound('sound\플레이어\대쉬소리.wav')),
                    '추락' : Animation(player_scenes_fall_, None),
                    '넉백' : Animation(player_scenes_knockback_, game_Sound('sound\플레이어\몬스터한테 맞는 소리.wav')),
                    '낙하공격' : Animation(player_scenes_attack3_, None),
                    '죽음' : Animation(player_scenes_die_, None)
                    }
player_speed = 200
player_jump_speed = 250