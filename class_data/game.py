import pygame as pg
from .classes.variable import *

pg.init()

screen= pg.display.set_mode(SCREEN_SIZE)
pg.display.set_caption("Star Light")

from .skill_set import *
from .sword_set import *
from .lance_set import *
from .gun_set import *
from .lobby import *
from .classes.player import Player
from .classes.eyesight import Eyesight
from .player_setting import *
from .eyesight_setting import *

left_key = pg.K_LEFT
right_key = pg.K_RIGHT

class Game:
  def new(self):
    # Group 객체
    self.all_sprites = pg.sprite.Group()
    self.bullets = pg.sprite.Group()
    self.impacts = pg.sprite.Group()
    self.obstacles = pg.sprite.Group()
    self.enemies = pg.sprite.Group()
    self.weapons = pg.sprite.Group()
    self.visibles = pg.sprite.Group()
    self.enemies = pg.sprite.Group()
    self.lifes = pg.sprite.Group()
    self.bullets = pg.sprite.Group()
    self.decos = pg.sprite.Group()
    self.icons = pg.sprite.Group()
    self.gimic_obstacles = pg.sprite.Group()
    
    # 단일 객체
    self.player = Player(self, player_animations, speed = player_speed, jump_speed= player_jump_speed)
    self.eyesight = Eyesight(self, eyesight_image, size = eyesight_size, location=vec(self.player.rect.centerx, self.player.rect.centery))
    self.stage = None
    self.lobby = Lobby(self)
    self.message = None
    self.mouse = None
    self.animation = None
    self.startpage = game_Animation([Scene('images\시작 애니메이션\_start_' + str(i) +'.png', (1440, 810)) for i in range(1, 34) for j in range(3)], None, loopstart=98)

    #요소
    self.level = 0

  def save(self):
      file = open('data.txt', 'w')
      file.write(str(self.level) + '\n')
      file.write(str(self.player.hp) + '\n')
      file.write(str(self.player.mp) + '\n')
      file.write(str(self.player.gold) + '\n')
      for i in self.player.weapons:
          s = i.name_0 + ' '
          s += str(i.upgrade)
          if i in self.player.using_weapons.values():
              s += ' *'
          if i.use:
              s += ' *'
          s += '\n'
          file.write(s)
  
  def setting(self):
      self.player.add_skill(Dash(self))
      self.player.set_skill(pg.K_TAB, self.player.skills[0])
      file = open('data.txt', 'r')
      a = file.readlines()
      self.level = int(a[0])
      self.player.hp = int(a[1])
      self.player.mp = int(a[2])
      self.player.gold = int(a[3])
      for i in a[4:]:
          r = i.split()
          if r[0] == 'ironsword':
              self.player.add_weapon(Sword(r[0], self, upgrade=int(r[1])))
          if r[0] == 'goldsword':
              self.player.add_weapon(Sword(r[0], self, upgrade=int(r[1])))
          if r[0] == 'diamondsword':
              self.player.add_weapon(Sword(r[0], self, upgrade=int(r[1])))
          if r[0] == 'ironlance':
              self.player.add_weapon(Lance(r[0], self, upgrade=int(r[1])))
          if r[0] == 'goldlance':
              self.player.add_weapon(Lance(r[0], self, upgrade=int(r[1])))
          if r[0] == 'diamondlance':
              self.player.add_weapon(Lance(r[0], self, upgrade=int(r[1])))
          if r[0] == 'ironpistol':
              self.player.add_weapon(Pistol('iron', self, upgrade=int(r[1])))
          if r[0] == 'goldpistol':
              self.player.add_weapon(Pistol('gold', self, upgrade=int(r[1])))
          if r[0] == 'diamondpistol':
              self.player.add_weapon(Pistol('diamond', self, upgrade=int(r[1])))
          if r[0] == 'ironshotgun':
              self.player.add_weapon(Shotgun('iron', self, upgrade=int(r[1])))
          if r[0] == 'goldshotgun':
              self.player.add_weapon(Shotgun('gold', self, upgrade=int(r[1])))
          if r[0] == 'diamondshotgun':
              self.player.add_weapon(Shotgun('diamond', self, upgrade=int(r[1])))
          if r[0] == 'ironsniper':
              self.player.add_weapon(Sniper('iron', self, upgrade=int(r[1])))
          if r[0] == 'goldsniper':
              self.player.add_weapon(Sniper('gold', self, upgrade=int(r[1])))
          if r[0] == 'diamondsniper':
              self.player.add_weapon(Sniper('diamond', self, upgrade=int(r[1])))
          if len(r) >= 3:
              self.player.change_weapon(self.player.weapons[-1], self.player.weapons[-1].w_type)
          if len(r) == 4:
              self.player.set_weapon(self.player.weapons[-1])
      file.close()
  

  
  def main(self):
    self.setting()
    for i in range(6):
        Hp_Icon(self, vec(-690 + 45 * i, -350), i + 1)

    for i in range(6):
        Sh_Icon(self, vec(-690 + 45 * i, -280), i + 1)

    Follow_Icon(self, Scene('images\아이콘 (1)\mana.png', 45, t = 'y대입'), vec(-700, -220))
    Follow_Icon(self, Scene('images\아이콘 (1)\_black.png', (240, 45)), vec(-560, -220))
    Mp_bar(self, Scene('images\아이콘 (1)\_blue.png', (240, 45)), vec(-560, -220))
    Mp_num(self, str(self.player.mp), vec(-560, -220), size = 30)
    Follow_Icon(self, Scene('images\아이콘 (1)\coin.png', 45, t = 'y대입'), vec(-700, -170))
    Gold_num(self, str(self.player.mp), vec(-560, -170), size = 30, color = WHITE)

    done = False

    while not done:
      clock.tick(FPS)
      screen.fill((0, 0, 0))
      if self.startpage:
          self.startpage.update()
          for event in pg.event.get():
              if event.type == pg.QUIT:
                  done = True
              elif event.type == pg.MOUSEBUTTONUP:
                  self.startpage = None
                  self.lobby.start()
      else:
          if self.animation:
              if self.animation:
                  self.animation.update()

          for event in pg.event.get():
              if event.type == pg.QUIT:
                  done = True
                  self.save()
              elif event.type == pg.KEYDOWN:
                  if event.key == left_key:
                      self.player.walk_l()
                  if event.key == right_key:
                      self.player.walk_r()
                  if event.key == pg.K_UP:
                      self.player.jump()
                  if event.key == pg.K_1:
                      self.player.using_change_weapon('검')
                  if event.key == pg.K_2:
                      self.player.using_change_weapon('창')
                  if event.key == pg.K_3:
                      self.player.using_change_weapon('총')
                  if event.key == pg.K_ESCAPE:
                      if self.stage:
                          self.stage.end()

              elif event.type == pg.KEYUP:
                  if event.key == left_key:
                      self.player.walk_l_cancel()
                  if event.key == right_key:
                      self.player.walk_r_cancel()
                  if event.key == pg.K_SPACE:
                      self.player.attack()
                  if event.key in self.player.using_skills:
                      self.player.using_skills[event.key].trigger()
                      
              elif event.type == pg.MOUSEBUTTONUP:
                  if event.button == 1:
                      if self.mouse:
                          self.mouse.update()
              
              elif event.type == pg.MOUSEWHEEL:
                  if not self.stage:
                      if abs(self.lobby.center[1] - (self.eyesight.rect.centery - 30 * event.y)) <= 315:
                          self.eyesight.rect.centery -= 30 * event.y

          if not self.animation:
              for i in self.obstacles:
                  i.update()
              
              for i in self.gimic_obstacles:
                  i.update()

              for i in self.enemies:
                  i.update()

              self.player.update()
          self.eyesight.update()
          if self.stage:
              self.stage.update()

          if not self.animation:

              for i in self.impacts:
                  i.update()

              for i in self.bullets:
                  i.update()

              for i in self.decos:
                  i.update()
              
              for i in self.icons:
                  i.update()
              
          if self.message:
              self.message.update()
          
      if self.stage:
          screen.blit(self.stage.background, (self.stage.rect.topleft[0] - self.eyesight.rect.center[0] + SCREEN_SIZE[0]/2, self.stage.rect.topleft[1] - self.eyesight.rect.center[1] + SCREEN_SIZE[1]/2))
      else:
          screen.blit(self.lobby.background, (self.lobby.rect.topleft[0] - self.eyesight.rect.center[0] + SCREEN_SIZE[0]/2, self.lobby.rect.topleft[1] - self.eyesight.rect.center[1] + SCREEN_SIZE[1]/2))

      for i in [self.decos, self.obstacles, self.gimic_obstacles, self.enemies, [self.player], self.weapons, self.bullets, self.impacts, self.icons]:
          for j in self.eyesight.get_hit_list(i):
              screen.blit(j.image, (j.rect.topleft[0] - self.eyesight.rect.center[0] + SCREEN_SIZE[0]/2, j.rect.topleft[1] - self.eyesight.rect.center[1] + SCREEN_SIZE[1]/2))

      if self.message:
          screen.blit(self.message.message, (self.message.rect.topleft[0]  + SCREEN_SIZE[0]/2, self.message.rect.topleft[1] + SCREEN_SIZE[1]/2))
      
      if self.animation:
          a = self.animation.p_scene()
          a.rect.center = vec(self.eyesight.rect.center)
          screen.blit(a.image_r, (a.rect.topleft[0] - self.eyesight.rect.center[0] + SCREEN_SIZE[0]/2, a.rect.topleft[1] - self.eyesight.rect.center[1] + SCREEN_SIZE[1]/2))
          if self.animation.end_check():
              self.animation = None
          
      if self.startpage:
          a = self.startpage.p_scene()
          a.rect.center = vec(self.eyesight.rect.center)
          screen.blit(a.image_r, (a.rect.topleft[0] - self.eyesight.rect.center[0] + SCREEN_SIZE[0]/2, a.rect.topleft[1] - self.eyesight.rect.center[1] + SCREEN_SIZE[1]/2))

      pg.display.flip()