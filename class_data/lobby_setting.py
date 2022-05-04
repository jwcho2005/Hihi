from .classes.variable import *
from .classes.animation import *

lobby_start_point = (-200, 250)
lobby_center = (-200, 250)
lobby_background = Scene('images\_background\_mainlobby.png', SCREEN_SIZE[0], t = 'x대입')
lobby_sound = game_Sound('sound\배경음악\y2mate.com - 로스트아크 08빙하섬의 눈물Tears on the Glacier Island  LOST ARK Soundtrack Vol2 InGame Track.mp3', volume=0.1)
floor_xsize = 350
floor1_image = Scene('images\아이콘 (1)\_floor_1.png', floor_xsize, t = 'x대입')
floor_ysize = floor1_image.size[1]
floor2_image = Scene('images\아이콘 (1)\_floor_2.png', floor_xsize, t = 'x대입')
floor3_image = [Scene('images\아이콘 (1)\_floor_3.png', floor_xsize, t = 'x대입'), Scene('images\아이콘 (1)\_locked_1.png', floor_xsize, t = 'x대입')]
floor4_image = [Scene('images\아이콘 (1)\_floor_4.png', floor_xsize, t = 'x대입'), Scene('images\아이콘 (1)\_locked_2.png', floor_xsize, t = 'x대입')]
floor5_image = [Scene('images\아이콘 (1)\_floor_5.png', floor_xsize, t = 'x대입'), Scene('images\아이콘 (1)\_locked_3.png', floor_xsize, t = 'x대입')]
floor6_image = [Scene('images\아이콘 (1)\_floor_6.png', floor_xsize, t = 'x대입'), Scene('images\아이콘 (1)\_locked_4.png', floor_xsize, t = 'x대입')]
floor7_image = [Scene('images\아이콘 (1)\_floor_7.png', floor_xsize, t = 'x대입'), Scene('images\아이콘 (1)\_locked_5.png', floor_xsize, t = 'x대입')]
floor8_image = Scene('images\아이콘 (1)\_floor_8.png', floor_xsize, t = 'x대입')