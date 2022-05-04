from .stage_set import *


a = Scene('images\아이콘 (1)\_pillar2.png', 710, t = 'y대입')
pillar1_ratio = a.ratio
pillar1_x = a.size[0]
pillar1_y = a.size[1]

a = Scene('images\타일\단색\맵 타일들\벽돌1.png', 50, t = 'y대입')
block1_ratio = a.ratio
block1_x = a.size[0]
block1_y = a.size[1]

class Stage_1(Setted_Stage):
    def __init__(self, game):
        Stage.__init__(self, game, 'Stage 1', 1, vec(200, 0), vec(3000, 0), Scene('images\_background\stage1.jpg', (1700, 1000)), game_Sound('sound\배경음악\Before Dawn.mp3', volume=0.3))
    
    def start(self):
        for i in range(0, 120, 3):
            self.deco('images\아이콘 (1)\_pillar2.png', vec(i * pillar1_x - 60 * pillar1_x, 0), pillar1_ratio)
        for i in range(0, 360):
            self.deco('images\타일\단색\맵 타일들\벽돌1.png', vec(i * 50 - 9000, -380), ratio=block1_ratio)
            self.deco('images\타일\단색\맵 타일들\벽돌1.png', vec(i * 50 - 9000, 380), ratio=block1_ratio)
        self.deco('images\문구\Move.png',vec(0,-200),ratio=2,follow=False)
        self.deco('images\문구\Move.png',vec(0,-200),ratio=2,follow=False)
        self.deco('images\문구\Jump.png',vec(50*8,-200),ratio=2,follow=False)
        self.deco('images\문구\Double Jump.png',vec(50*18+25,-200),ratio=2,follow=False)
        self.deco('images\문구\Attack.png',vec(50*29+25,-200),ratio=2,follow=False)
        self.deco('images\문구\Dash.png',vec(50*40,-200),ratio=2,follow=False)
        self.deco('images\문구\cooltime.png',vec(50*49,-200),ratio=2,follow=False)
        self.deco('images\문구\change_wea.png',vec(50*60,-200),ratio=2,follow=False)
        self.deco('images\문구\downarrow.png',vec(50*99,75),ratio=2,follow=False)
        self.deco('images\문구\Clear.png',vec(50*100,-225),ratio=2,follow=False)
        self.deco('images\문구\gun_squid.png',vec(50*75,-225),ratio=2,follow=False)
        self.deco('images\문구\디버프.png',vec(50*86,-225),ratio=2,follow=False)
        for i in range(-3,15):
            for j in range(6):
                self.block('images\타일\단색\맵 타일들\벽돌1.png', vec(50*i, 150+50*j+150))
        for i in range(7,9):
            for j in range(2):
                self.block('images\타일\단색\맵 타일들\벽돌1.png',vec(50*i,50+50*j+150))
        for i in range(15,18):
            for j in range(4):
                self.block('images\타일\단색\맵 타일들\벽돌1.png',vec(50*i,150+50*j+150))
        for i in range(17,21):
            for j in range(3):
                self.block('images\타일\단색\맵 타일들\벽돌1.png',vec(50*i,50*j+150))
        for i in range(18,35):
            for j in range(4):
                self.block('images\타일\단색\맵 타일들\벽돌1.png',vec(50*i,150+50*j+150))
        
        for i in range(35,45):
            for j in range(4):
                self.block('images\타일\단색\맵 타일들\벽돌1.png',vec(50*i,150+50*j+150))
        self.Kill_block('images\타일\가시\가시.png',vec(50*40,100+150))
        self.Kill_block('images\타일\가시\가시.png',vec(50*40,50+150))
        self.Kill_block('images\타일\가시\가시.png',vec(50*40,0+150))
        self.Kill_block('images\타일\가시\가시.png',vec(50*40,-50+150))
        self.Kill_block('images\타일\가시\가시.png',vec(50*46.5+50*2,100+150))
        self.Kill_block('images\타일\가시\가시.png',vec(50*46.5+50*2,50+150))
        self.Kill_block('images\타일\가시\가시.png',vec(50*46.5+50*2,0+150))
        self.Kill_block('images\타일\가시\가시.png',vec(50*46.5+50*2,-50+150))

        for i in range(45,101):
            for j in range(4):
                self.block('images\타일\단색\맵 타일들\벽돌1.png',vec(50*i,150+50*j+150))
        
        self.grimer_spawn_block('images\타일\단색\맵 타일들\벽돌1.png', 1, location=(50*32,150+150), size = (50, 50))
        self.bigheadsquid_spawn_block('images\타일\단색\맵 타일들\벽돌1.png', 1, location=(50*57,150+150), size = (50, 50))
        self.minion_spawn_block('images\타일\단색\맵 타일들\벽돌1.png', 1, location=(50*64,150+150), size = (50, 50))
        self.grimer_spawn_block('images\타일\단색\맵 타일들\벽돌1.png', 1, location=(50*60,150+150), size = (50, 50))
        self.bigheadsquid_spawn_block('images\타일\단색\맵 타일들\벽돌1.png', 1, location=(50*62,150+150), size = (50, 50))
        self.bigheadsquid_spawn_block('images\타일\단색\맵 타일들\벽돌1.png', 1, location=(50*75,150+150), size = (50, 50))
        self.grimer_spawn_block('images\타일\단색\맵 타일들\벽돌1.png', 1, location=(50*89,150+150), size = (50, 50))
        self.end_block('images\타일\문\문.png',location=vec(50*99,75+150),size=(100,100))

        for i in range(-15,120):
            self.Kill_block('images\타일\가시\가시.png', vec(50*i, 800+150))
        Stage.start(self)
        self.game.player.rect.center += vec(0, 150)
class Stage_2(Setted_Stage):
    def __init__(self, game):
        Stage.__init__(self, game, 'Stage 2',  2, vec(200, 0), vec(1600, 0), Scene('images\_background\stage2.jpg', 900, t= 'y대입'), game_Sound('sound\배경음악\듸뷔시의 달빛.mp3', volume=0.3))
    
    def start(self):
        for i in range(0, 120, 3):
            self.deco('images\아이콘 (1)\_pillar2.png', vec(i * pillar1_x - 60 * pillar1_x, 0), pillar1_ratio)
        for i in range(0, 360):
            self.deco('images\타일\단색\맵 타일들\벽돌2.png', vec(i * 50 - 9000, -380), ratio=block1_ratio)
            self.deco('images\타일\단색\맵 타일들\벽돌2.png', vec(i * 50 - 9000, 380), ratio=block1_ratio)

        for i in range(-10,62):
            for j in range(6):
                self.block('images\타일\단색\맵 타일들\벽돌2.png',vec(200+50*i,200+50*j+100))
        for i in range(6,10):
            for j in range(2):
                self.block('images\타일\단색\맵 타일들\벽돌2.png',vec(200+50*i,150-50*j+100))
        self.block('images\타일\단색\맵 타일들\벽돌2.png',vec(200+50*9,50+100))
        for i in range(12,17):
            for j in range(4):
                self.block('images\타일\단색\맵 타일들\벽돌2.png',vec(200+50*i,150-50*j+100))
        for i in range(18,20):
            for j in range(5):
                self.block('images\타일\단색\맵 타일들\벽돌2.png',vec(200+50*i,150-50*j+100))
        for j in range(10):
            self.block('images\타일\단색\맵 타일들\벽돌2.png',vec(200+50*23,150-50*j+100))
        self.move_block('images\타일\단색\맵 타일들\벽돌2.png',100,vec(200+50*20.5,150-50*4-25+100),vec(200+50*20.5,150-50*14-25+100),size=(100,100))
        for i in range(23,27):
            for j in range(14,16):
                self.block('images\타일\단색\맵 타일들\벽돌2.png',vec(200+50*i,150-50*j+100))
        self.Kill_block('images\타일\가시\가시.png',location=vec(200+50*23,100-50*9+100))
        # self.Kill_block('images\타일\가시\가시.png',location=vec(50*24,100-50*3))
        self.Kill_block('images\타일\가시\가시.png',location=vec(200+50*24,250-50*7-25+100))
        self.Kill_block('images\타일\가시\가시.png',location=vec(200+50*25,250-50*7-25+100))
        self.Kill_block('images\타일\가시\가시.png',location=vec(200+50*26,250-50*7-25+100))
        self.Kill_block('images\타일\가시\가시.png',location=vec(200+50*26,250-50*6+100))
        for i in range(10,12):
            self.Kill_block('images\타일\가시\가시.png',location=vec(200+50*i,200-50+100))
        self.Kill_block('images\타일\가시\가시.png',location=vec(200+50*15,200-50*5+100))
        self.Kill_block('images\타일\가시\가시.png',location=vec(200+50*16,200-50*5+100))
        self.Kill_block('images\타일\가시\가시.png',location=vec(200+50*17,200-50+100))
        for i in range(20,23):
            self.Kill_block('images\타일\가시\가시.png',location=vec(200+50*i,200-50+100))
        for i in range(24,27):
            self.Kill_block('images\타일\가시\가시.png',location=vec(200+50*i,200-50*4+100))
        for j in range(4,11):
            self.Kill_block('images\타일\가시\가시.png',location=vec(200+50*22,200-50*j-20+100))
        for j in range(4,14):
            self.Kill_block('images\타일\가시\가시.png',location=vec(200+50*29,200-50*j-25+100))
        for j in range(4,14):
            self.Kill_block('images\타일\가시\가시.png',location=vec(200+50*30,200-50*j-25+100))
        for i in range(31,50):
            self.block('images\타일\단색\맵 타일들\벽돌2.png',vec(200+50*i,200-50*4))
        
        self.bigheadsquid_spawn_block('images\타일\단색\맵 타일들\벽돌2.png',1,location=vec(200+50*4,200+100),size=(50,50))
        self.grimer_spawn_block('images\타일\단색\맵 타일들\벽돌2.png',1,location=vec(200+50*7,200-50*2+100),size=(50,50))

        self.bigheadsquid_spawn_block('images\타일\단색\맵 타일들\벽돌2.png',1,location = vec(200+50*40,200-50*4))
        self.bigheadsquid_spawn_block('images\타일\단색\맵 타일들\벽돌2.png',1, location = vec(200+50*38,200-50*4))
        self.grimer_spawn_block('images\타일\단색\맵 타일들\벽돌2.png',1, location = vec(200+50*38,200-50*4))
   

        self.bigheadsquid_spawn_block('images\타일\단색\맵 타일들\벽돌2.png',1,location = vec(200+50*33,200+100))
        self.bigheadsquid_spawn_block('images\타일\단색\맵 타일들\벽돌2.png',1, location = vec(200+50*38,200+100))
        self.grimer_spawn_block('images\타일\단색\맵 타일들\벽돌2.png',2, location = vec(200+50*42,200+100))
        self.minion_spawn_block('images\타일\단색\맵 타일들\벽돌2.png',2, location = vec(200+50*43,200+100)) 
        self.bigheadsquid_spawn_block('images\타일\단색\맵 타일들\벽돌2.png',2, location = vec(200+50*46,200+100))
        self.minion_spawn_block('images\타일\단색\맵 타일들\벽돌2.png',1, location = vec(200+50*47,200+100))
        self.bigheadsquid_spawn_block('images\타일\단색\맵 타일들\벽돌2.png',2, location = vec(200+50*50,200+100))
        for i in range(54,62):
            for j in range(3):
                self.block('images\타일\단색\맵 타일들\벽돌2.png',vec(200+50*i,150-50*j+100))
        self.Kill_block('images\타일\가시\가시.png',location=vec(200+50*53,150+100))
        self.block('images\타일\단색\맵 타일들\벽돌2.png',vec(200+50*64,50+100))
        self.block('images\타일\단색\맵 타일들\벽돌2.png',vec(200+50*66,-50+100))
        self.block('images\타일\단색\맵 타일들\벽돌2.png',vec(200+50*70,0+100))
        self.block('images\타일\단색\맵 타일들\벽돌2.png',vec(200+50*74,0+100))
        self.block('images\타일\단색\맵 타일들\벽돌2.png',vec(200+50*79,0+100))
        self.block('images\타일\단색\맵 타일들\벽돌2.png',vec(200+50*80,0+100))
        self.block('images\타일\단색\맵 타일들\벽돌2.png',vec(200+50*81,0+100))
        self.block('images\타일\단색\맵 타일들\벽돌2.png',vec(200+50*81,-50+100))
        self.block('images\타일\단색\맵 타일들\벽돌2.png',vec(200+50*84,50+100))
        self.block('images\타일\단색\맵 타일들\벽돌2.png',vec(200+50*88,100+100))
        self.block('images\타일\단색\맵 타일들\벽돌2.png',vec(200+50*92,50+100))
        self.block('images\타일\단색\맵 타일들\벽돌2.png',vec(200+50*95,-50+100))
        self.block('images\타일\단색\맵 타일들\벽돌2.png',vec(200+50*96,-50+100))
        self.block('images\타일\단색\맵 타일들\벽돌2.png',vec(200+50*97,-50+100))
        self.block('images\타일\단색\맵 타일들\벽돌2.png',vec(200+50*98,-50+100))
        self.block('images\타일\단색\맵 타일들\벽돌2.png',vec(200+50*98,-100+100))
        for i in range(106,114):
            self.block('images\타일\단색\맵 타일들\벽돌2.png',vec(200+50*i,0+100))
        self.block('images\타일\단색\맵 타일들\벽돌2.png',vec(200+50*110,-50+100))
        self.Kill_block('images\타일\가시\가시.png',vec(200+50*67,-50+100))
        self.Kill_block('images\타일\가시\가시.png',vec(200+50*69,-50+100))
        self.Kill_block('images\타일\가시\가시.png',vec(200+50*74,-50+100))
        self.Kill_block('images\타일\가시\가시.png',vec(200+50*106,-50+100))
        self.Kill_block('images\타일\가시\가시.png',vec(200+50*110,-100+100))
        self.grimer_spawn_block('images\타일\단색\맵 타일들\벽돌2.png',1,vec(200+50*80,0+100))
        self.grimer_spawn_block('images\타일\단색\맵 타일들\벽돌2.png',1,vec(200+50*96,-50+100))
        self.block('images\타일\단색\맵 타일들\벽돌2.png',vec(200+50*102,-50+100))
        self.end_block('images\타일\문\문.png',vec(200+50*112,-75+100),size=(100,100))
        self.black_hole('images\타일\이동\_blackhole_3.png',vec(200+50*24,200-50*5-40+100),vec(200+50*59,-50+100),size=(100,100))
        self.deco('images\타일\이동\_whitehole_3.png',location = vec(200+50*59,-25+100),ratio = 4, follow = False)
        for i in range(-15,120):
            self.Kill_block('images\타일\가시\가시.png', vec(200+50*i, 800+100))
        super().start()
        self.game.player.rect.center += vec(0, 100)


class Stage_4(Setted_Stage):
    def __init__(self, game):
        Stage.__init__(self, game, 'Stage 4', 4, vec(200, 0), vec(4500, 0), Scene('images\_background\stage4.jpg',  900, t= 'y대입'), game_Sound('sound\배경음악\Wrath of Monoceros.mp3', volume=0.3))
    
    def start(self):
        for i in range(0, 120, 3):
            self.deco('images\아이콘 (1)\_pillar_4.png', vec(i * pillar1_x - 60 * pillar1_x, 0), pillar1_ratio)
        for i in range(0, 720):
            self.deco('images\타일\단색\맵 타일들\벽돌4.png', vec(i * 50 - 12000, -380), ratio=block1_ratio)
            self.deco('images\타일\단색\맵 타일들\벽돌4.png', vec(i * 50 - 12000, 380), ratio=block1_ratio)

        self.block('images\타일\단색\맵 타일들\벽돌4.png',vec(0,100))
        self.move_block_repeat('images\타일\단색\맵 타일들\맵 타일들 (1)\_3x1_green.png',100,vec(200+0,100),vec(200+300,100),size=(150,50))
        self.Kill_block_move_repeat('images\타일\가시\가시.png',200,vec(200+400,100),vec(200+400,-200),size=(50,50))
        self.block('images\타일\단색\맵 타일들\벽돌4.png',vec(200+400,-250))
        self.Kill_block_move_repeat('images\타일\가시\가시.png',225,vec(200+450,100),vec(200+450,-200),size=(50,50))
        self.block('images\타일\단색\맵 타일들\벽돌4.png',vec(200+450,-250))
        self.move_block_repeat('images\타일\단색\맵 타일들\맵 타일들 (1)\_3x1_green.png',75,vec(200+650,150),vec(200+900,150),size=(150,50))
        self.Kill_block_move_repeat('images\타일\가시\가시.png',150,vec(200+1050,100),vec(200+1050,-200),size=(50,50))
        self.block('images\타일\단색\맵 타일들\벽돌4.png',vec(200+1050,-250))
        self.Kill_block_move_repeat('images\타일\가시\가시.png',200,vec(200+1100,100),vec(200+1100,-200),size=(50,50))
        self.block('images\타일\단색\맵 타일들\벽돌4.png',vec(200+1100,-250))
        self.Kill_block_move_repeat('images\타일\가시\가시.png',250,vec(200+1150,100),vec(200+1150,-200),size=(50,50))
        self.block('images\타일\단색\맵 타일들\벽돌4.png',vec(200+1150,-250))
        self.move_block_repeat('images\타일\단색\맵 타일들\운석\Big.png',125,vec(200+1250,75),vec(200+1700,75),size=(150,150))
        self.grimer_spawn_block('images\타일\단색\맵 타일들\벽돌4.png',1,vec(200+600,-100))
        self.block('images\타일\단색\맵 타일들\벽돌4.png',vec(200+550,-150+12.5),size=(20,20))
        self.block('images\타일\단색\맵 타일들\벽돌4.png',vec(200+650,-150+12.5),size=(20,20))
        self.grimer_spawn_block('images\타일\단색\맵 타일들\벽돌4.png',1,vec(200+1450,-150))
        self.block('images\타일\단색\맵 타일들\벽돌4.png',vec(200+1400,-200+12.5),size=(20,20))
        self.block('images\타일\단색\맵 타일들\벽돌4.png',vec(200+1500,-200+12.5),size=(20,20))
        for i in range(42,44):
            self.block('images\타일\단색\맵 타일들\벽돌4.png',vec(200+50*i,-100))
        self.block('images\타일\단색\맵 타일들\벽돌4.png',vec(200+50*48,0))
        self.Kill_block_move_repeat('images\타일\가시\가시.png',250,vec(200+2350,50),vec(200+2350,-100),size=(50,50))
        self.move_block_repeat('images\타일\단색\맵 타일들\맵 타일들 (1)\_4x1_green.png',75,vec(200+2800,-50),vec(200+4300,-50),size=(50*13,150))
        self.Kill_block_move_repeat('images\타일\가시\가시.png',250,vec(200+2550,-150),vec(200+2550,-400),size=(50,50))
        self.Kill_block_move_repeat('images\타일\가시\가시.png',150,vec(200+3000,-150-12.5),vec(200+3000,-400),size=(75,75))
        self.Kill_block_move_repeat('images\타일\가시\가시.png',200,vec(200+3700,-150),vec(200+3700,-400),size=(50,50))
        self.Kill_block_move_repeat('images\타일\가시\가시.png',175,vec(200+4150,-150),vec(200+4150,-400),size=(50,50))
        self.bigheadsquid_spawn_block('images\타일\단색\맵 타일들\벽돌4.png',1,vec(200+3600,-500),size=(50,50))
        self.bigheadsquid_spawn_block('images\타일\단색\맵 타일들\벽돌4.png',1,vec(200+4100,-500),size=(50,50))
        self.bigheadsquid_spawn_block('images\타일\단색\맵 타일들\벽돌4.png',1,vec(200+3000,-500),size=(50,50))
        self.grimer_spawn_block('images\타일\단색\맵 타일들\벽돌4.png',1,vec(200+2700,-300))
        self.block('images\타일\단색\맵 타일들\벽돌2.png',vec(200+2650,-350+12.5),size=(40,20))
        self.block('images\타일\단색\맵 타일들\벽돌2.png',vec(200+2750,-350+12.5),size=(40,20))
        self.grimer_spawn_block('images\타일\단색\맵 타일들\벽돌4.png',1,vec(200+3200,-300))
        self.block('images\타일\단색\맵 타일들\벽돌2.png',vec(200+3150,-350+12.5),size=(20,20))
        self.block('images\타일\단색\맵 타일들\벽돌2.png',vec(200+3250,-350+12.5),size=(20,20))
        self.grimer_spawn_block('images\타일\단색\맵 타일들\벽돌4.png',1,vec(200+3800,-300))
        self.block('images\타일\단색\맵 타일들\벽돌2.png',vec(200+3750,-350+25),size=(20,20))
        self.block('images\타일\단색\맵 타일들\벽돌2.png',vec(200+3850,-350+25),size=(20,20))
        self.grimer_spawn_block('images\타일\단색\맵 타일들\벽돌4.png',1,vec(4250,-300))
        self.block('images\타일\단색\맵 타일들\벽돌2.png',vec(200+4200,-350+25),size=(20,20))
        self.block('images\타일\단색\맵 타일들\벽돌2.png',vec(200+4300,-350+25),size=(20,20))
        for i in range(10):
            self.block('images\타일\단색\맵 타일들\벽돌4.png',vec(50*3+200+5300+50*i,300),size=(50,50))
        self.end_block('images\타일\문\문.png',vec(200+5300+50*8,300-75),size=(100,100))
        for i in range(-15,200):
            self.Kill_block('images\타일\가시\가시.png', vec(200+50*i, 800))
        super().start()

a = Scene('images\아이콘 (1)\_tree_1.png', 810, t = 'y대입')
tree1_ratio = a.ratio
tree1_x = a.size[0]
tree1_y = a.size[1]

a = Scene('images\아이콘 (1)\_tree_2.png', 810, t = 'y대입')
tree2_ratio = a.ratio
tree2_x = a.size[0]
tree2_y = a.size[1]

class Stage_3(Setted_Stage):
    def __init__(self, game):
        Stage.__init__(self, game, 'Stage 3', 3, vec(200, 0), vec(1600, 0), Scene('images\_background\stage3.jpg',  900, t= 'y대입'), game_Sound('sound\배경음악\Windless Star Sea.mp3', volume=0.3))
    
    def start(self):
        for i in range(0, 360, 3):
            if i % 2 == 1:
                self.deco('images\아이콘 (1)\_tree_1.png', vec(i * tree1_x - 180 * tree1_x, 0), tree1_ratio)
            else:
                self.deco('images\아이콘 (1)\_tree_2.png', vec(i * tree1_x - 180 * tree1_x, 0), tree2_ratio)

        self.block('images\타일\단색\맵 타일들\맵 타일들 (1)\_47x6ground.png',vec(200+50*19,150+50*2.5),size=(50*47,50*6))
        for i in range(0,2):
            self.block('images\타일\단색\맵 타일들\맵 타일들 (1)\ground_1 (1).png',vec(200+50*i,100),size=(50,50))
        for i in range(9,11):
            self.block('images\타일\단색\맵 타일들\맵 타일들 (1)\ground_1 (1).png',vec(200+50*i,100),size=(50,50))
        for i in range(14,16):
            for j in range(2):
                self.block('images\타일\단색\맵 타일들\맵 타일들 (1)\ground_1 (1).png',vec(200+50*i,100-50*j),size=(50,50))
        for i in range(16,19):
            for j in range(4):
                self.block('images\타일\단색\맵 타일들\맵 타일들 (1)\ground_1 (1).png',vec(200+50*i,100-50*j),size=(50,50))
        self.block('images\타일\단색\맵 타일들\맵 타일들 (1)\_aaaa.png',vec(200+50*27,100-50*2.5),size=(50*17,50*6))
        for i in range(36,38):
            for j in range(4):
                self.block('images\타일\단색\맵 타일들\맵 타일들 (1)\ground_1 (1).png',vec(200+50*i,100-50*j))
        for i in range(38,40):
            for j in range(2):
                self.block('images\타일\단색\맵 타일들\맵 타일들 (1)\ground_1 (1).png',vec(200+50*i,100-50*j))
        for i in range(43,45):
            for j in range(4):
                self.block('images\타일\단색\맵 타일들\맵 타일들 (1)\ground_1 (1).png',vec(200+50*i,250+50*j))
        for i in range(45,48):
            for j in range(2):
                self.block('images\타일\단색\맵 타일들\맵 타일들 (1)\ground_1 (1).png',vec(200+50*i,350+50*j))
        self.move_block_repeat('images\타일\단색\맵 타일들\맵 타일들 (1)\ground_1 (1).png',150,vec(200+50*50,400),vec(200+50*55,400),size=(50*5,50*3))
        for i in range(58,69):
            for j in range(5):
                self.block('images\타일\단색\맵 타일들\맵 타일들 (1)\ground_1 (1).png',vec(200+50*i,300+50*j))
        for i in range(64,69):
            for j in range(2):
                self.block('images\타일\단색\맵 타일들\맵 타일들 (1)\ground_1 (1).png',vec(200+50*i,250-50*j))
        for i in range(67,69):
            for j in range(2):
                self.block('images\타일\단색\맵 타일들\맵 타일들 (1)\ground_1 (1).png',vec(200+50*i,150-50*j))
        for i in range(69,80):
            self.block('images\타일\단색\맵 타일들\맵 타일들 (1)\ground_1 (1).png',vec(200+50*i,650))
        for i in range(82,91):
            self.block('images\타일\단색\맵 타일들\맵 타일들 (1)\ground_1 (1).png',vec(200+50*i,600))
        for i in range(98,102):
            self.block('images\타일\단색\맵 타일들\맵 타일들 (1)\ground_1 (1).png',vec(200+50*i,500))
        self.end_block('images\타일\문\문.png',vec(200+50*100,425),size=(100,100))
        self.move_block_repeat('images\타일\단색\맵 타일들\맵 타일들 (1)\_eee.png',100,vec(200+50*91.5,625),vec(200+50*96.5,625),size=(100,100))

        for i in range(69,71):
            self.block('images\타일\단색\맵 타일들\맵 타일들 (1)\ground_1 (1).png',vec(200+50*i,-150))
        for i in range(71,74):
            self.block('images\타일\단색\맵 타일들\맵 타일들 (1)\ground_1 (1).png',location = vec(200+50*i,-150))
        for i in range(74,80):
            self.block('images\타일\단색\맵 타일들\맵 타일들 (1)\ground_1 (1).png',vec(200+50*i,-150))
        for i in range(82,91):
            self.block('images\타일\단색\맵 타일들\맵 타일들 (1)\ground_1 (1).png',vec(200+50*i,-200))
        for i in range(98,102):
            self.block('images\타일\단색\맵 타일들\맵 타일들 (1)\ground_1 (1).png',vec(200+50*i,500-800))
        self.Kill_block('images\타일\가시\가시.png',vec(200+50,50))
        self.Kill_block('images\타일\가시\가시.png',vec(200+50*15,0))
        self.Kill_block('images\타일\가시\가시.png',vec(200+50*37,-100))
        self.Kill_block('images\타일\가시\가시.png',vec(200+50*38,0))
        self.Kill_block('images\타일\가시\가시.png',vec(200+50*43,200))
        self.Kill_block('images\타일\가시\가시.png',vec(200+50*44,200))
        self.Kill_block('images\타일\가시\가시.png',vec(200+50*46,300))
        self.Kill_block('images\타일\가시\가시.png',vec(200+50*65,150))
        self.Kill_block('images\타일\가시\가시.png',vec(200+50*69,600))
        self.Kill_block('images\타일\가시\가시.png',vec(200+50*70,600))
        self.Kill_block('images\타일\가시\가시.png',vec(200+50*74,600))
        self.Kill_block('images\타일\가시\가시.png',vec(200+50*75,600))
        self.Kill_block('images\타일\가시\가시.png',vec(200+50*76,600))
        self.Kill_block('images\타일\가시\가시.png',vec(200+50*77,600))
        self.Kill_block('images\타일\가시\가시.png',vec(200+50*84,550))
        self.Kill_block('images\타일\가시\가시.png',vec(200+50*84,500))
        self.Kill_block('images\타일\가시\가시.png',vec(200+50*84,450))
        self.Kill_block('images\타일\가시\가시.png',vec(200+50*87,550))
        self.Kill_block('images\타일\가시\가시.png',vec(200+50*87,500))
        self.Kill_block('images\타일\가시\가시.png',vec(200+50*88,500))
        self.Kill_block('images\타일\가시\가시.png',vec(200+50*70,-200))
        self.Kill_block('images\타일\가시\가시.png',vec(200+50*74,-200))
        self.Kill_block('images\타일\가시\가시.png',vec(200+50*75,-200))
        self.Kill_block('images\타일\가시\가시.png',vec(200+50*76,-200))
        self.Kill_block('images\타일\가시\가시.png',vec(200+50*77,-200))
        self.Kill_block('images\타일\가시\가시.png',vec(200+50*84,-250))
        self.Kill_block('images\타일\가시\가시.png',vec(200+50*84,-300))
        self.Kill_block('images\타일\가시\가시.png',vec(200+50*84,-350))
        self.Kill_block('images\타일\가시\가시.png',vec(200+50*87,-250))
        self.Kill_block('images\타일\가시\가시.png',vec(200+50*87,-300))
        self.Kill_block('images\타일\가시\가시.png',vec(200+50*88,-300))
        
        self.move_block_repeat('images\타일\단색\맵 타일들\맵 타일들 (1)\_eee.png',100,vec(200+50*91.5,-175),vec(200+50*96.5,-175),size=(100,100))
        self.block('images\타일\문\문.png',vec(200+50*100,425-800),size=(100,100))
        self.bigheadsquid_spawn_block('images\타일\단색\맵 타일들\맵 타일들 (1)\ground_1 (1).png',1,vec(200+50*5,150),size=(50,50))
        self.minion_spawn_block('images\타일\단색\맵 타일들\맵 타일들 (1)\ground_1 (1).png',1,vec(200+50*8,150),size=(50,50))
        self.minion_spawn_block('images\타일\단색\맵 타일들\맵 타일들 (1)\ground_1 (1).png',1,vec(200+50*10,100),size=(50,50))
        self.bigheadsquid_spawn_block('images\타일\단색\맵 타일들\맵 타일들 (1)\ground_1 (1).png',1,vec(200+50*17,-50),size=(50,50))
        self.bigheadsquid_spawn_block('images\타일\단색\맵 타일들\맵 타일들 (1)\ground_1 (1).png',1,vec(200+50*22,-150),size=(50,50))
        self.bigheadsquid_spawn_block('images\타일\단색\맵 타일들\맵 타일들 (1)\ground_1 (1).png',1,vec(200+50*32,-150),size=(50,50))
        self.minion_spawn_block('images\타일\단색\맵 타일들\맵 타일들 (1)\ground_1 (1).png',1,vec(200+50*29,-150),size=(50,50))
        self.grimer_spawn_block('images\타일\단색\맵 타일들\맵 타일들 (1)\ground_1 (1).png',1,vec(200+50*25,-150),size=(50,50))
        self.grimer_spawn_block('images\타일\단색\맵 타일들\맵 타일들 (1)\ground_1 (1).png',1,vec(200+50*25,-350))
        self.block('images\타일\단색\맵 타일들\벽돌3.png',vec(200+50*24,-400+12.5),size=(20,20))
        self.block('images\타일\단색\맵 타일들\벽돌3.png',vec(200+50*26,-400+12.5),size=(20,20))
        self.grimer_spawn_block('images\타일\단색\맵 타일들\맵 타일들 (1)\ground_1 (1).png',1,vec(200+50*32,-350))
        self.block('images\타일\단색\맵 타일들\벽돌3.png',vec(200+50*31,-400+12.5),size=(20,20))
        self.block('images\타일\단색\맵 타일들\벽돌3.png',vec(200+50*33,-400+12.5),size=(20,20))

        self.block('images\타일\단색\맵 타일들\맵 타일들 (1)\ground_1 (1).png',vec(200+50*35,-200),size=(50,50))

        self.bigheadsquid_spawn_block('images\타일\단색\맵 타일들\맵 타일들 (1)\ground_1 (1).png',1,vec(200+50*42,150),size=(50,50))
        self.grimer_spawn_block('images\타일\단색\맵 타일들\맵 타일들 (1)\ground_1 (1).png',1,vec(200+50*60,300))
        self.bigheadsquid_spawn_block('images\타일\단색\맵 타일들\맵 타일들 (1)\ground_1 (1).png',1,vec(200+50*61,300),size=(50,50))
        self.bigheadsquid_spawn_block('images\타일\단색\맵 타일들\맵 타일들 (1)\ground_1 (1).png',1,vec(200+50*62,300),size=(50,50))
        for i in range(-15,120):
            self.Kill_block('images\타일\가시\가시.png', vec(200+50*i, 800))
        super().start()
class Stage_Boss(Setted_Stage):
    def __init__(self, game):
        Stage.__init__(self, game, 'Boss Stage', 5, vec(200, 0), vec(1000, -100), Scene('images\_background\stage_boss1.png', 900, t = 'y대입'), game_Sound('sound\배경음악\종천의 폐막곡.mp3', volume=0.3))
        self.frist_time = 100
        self.second_time = 200
        self.third_time = 300
        self.stack = 1
        mooneater_first_animation.init()
        mooneater_second_animation.init()
        mooneater_third_animation.init()
    
    def image_update(self, scene):
        self.background = scene.image_r
        a = self.rect.center
        self.rect = scene.rect
        self.rect.center = a
        self.background_update()
    
    def update(self):
        if time.time() - self.start_time > self.frist_time and self.stack == 1:
            self.game.animation = mooneater_first_animation
            self.game.visibles.remove(self.boss)
            self.stack += 1
        if time.time() - self.start_time > self.second_time and self.stack == 2:
            self.game.animation = mooneater_second_animation
            self.game.visibles.remove(self.boss)
            self.stack += 1
        if time.time() - self.start_time > self.third_time and self.stack == 3:
            self.game.animation = mooneater_third_animation
            self.game.visibles.remove(self.boss)
            self.stack += 1
        
        if self.game.animation and self.game.animation.end_check():
            self.game.visibles.add(self.boss)
            if self.stack == 3:
                self.image_update(Scene('images\_background\stage_boss3.png', 900, t = 'y대입'))
            elif self.stack == 2:
                self.image_update(Scene('images\_background\stage_boss2.png', 900, t = 'y대입'))
        
        if self.game.animation and self.game.animation.p_frame == 240 and self.stack == 4:
            self.end()
            self.game.visibles.add(self.boss)
            self.stack += 1
            
        if self.boss:
            if self.boss.state == '죽음' and self.boss.animation.end_check():
                self.clear()
                
        
        super().update()

    def start(self):
        for i in range(0, 120, 3):
            self.deco('images\아이콘 (1)\_pillar_3.png', vec(i * pillar1_x - 60 * pillar1_x, 0), pillar1_ratio)
        for i in range(0, 120):
            self.deco('images\타일\단색\맵 타일들\Bossbrick.png', vec(i * 50 - 3000, -380), ratio=block1_ratio)
            self.deco('images\타일\단색\맵 타일들\Bossbrick.png', vec(i * 50 - 3000, 380), ratio=block1_ratio)

        for i in range(-5,1):
            for j in range(16):
                self.block('images\타일\단색\맵 타일들\Bossbrick.png',vec(50*i,-250+50*j),size=(50,50))
        for i in range(11):
            for j in range(15-i):
                self.block('images\타일\단색\맵 타일들\Bossbrick.png',vec(50+100*i,-200+50*i+50*j),size=(50,50))
                self.block('images\타일\단색\맵 타일들\Bossbrick.png',vec(100+100*i,-200+50*i+50*j),size=(50,50))
        for i in range(23,61):
            for j in range(4):
                self.block('images\타일\단색\맵 타일들\Bossbrick.png',vec(50*i,300+50*j),size=(50,50))
        # self.grimer_spawn_block('images\타일\단색\맵 타일들\Bossbrick.png',1,vec(50*35,-300))
        # self.block('images\타일\단색\맵 타일들\Bossbrick.png',vec(50*34,-300-50+12.5),size=(50,25))
        # self.block('images\타일\단색\맵 타일들\Bossbrick.png',vec(50*36,-300-50+12.5),size=(50,25))
        self.mooneater_spawn(vec(2000,-500))
        super().start()
        self.game.player.rect.center += vec(0, -300)
        


