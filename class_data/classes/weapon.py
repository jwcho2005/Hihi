from .obj import *
import time
import random

class Weapon(obj):
    def __init__(self, name, w_type,  game, animations, damage, locations, cool_time, max_upgrade, upgrade = 0, location = vec(0, 0)):
        self.groups = game.all_sprites, game.weapons
        obj.__init__(self, game, self.groups, animations, location=location)
        self.state = '투명'
        self.use = False

        self.name = name
        self.name_0 = name

        self.w_type = w_type
        self.locations = locations
        self.master = None
        self.damage_0 = damage
        self.max_upgrade = max_upgrade
        self.upgrade = upgrade
        self.damage = self.damage_0 * (1 + self.upgrade * 0.2)

        self.time = 10
        self.start_time = 0
        self.switch = True

        self.allow = True

        self.hit_list = []

        self.end_time = 0
        self.cool_time = cool_time

    def master_set(self, master):
        self.master = master
        self.state_set('통상')
    
    def get_new_hit_list(self, tag = False):
        if not tag:
            tag = self.game.enemies
        hit_list = pg.sprite.spritecollide(self,tag,False,pg.sprite.collide_mask)
        hit_list = list(set(hit_list) - set(self.hit_list))
        self.hit_list += hit_list
        self.hit_list = list(set(self.hit_list))

        return hit_list
    
    def update(self):
        if self.state in ['일반공격', '걷기공격', '낙하공격', '낙하공격_끝']:
            if self.master.state == '넉백':
                self.switch = False
                self.state_set('투명')
            else:
                self.attack_end_check()
        
        self.make_unvisible()

        self.animation.update()
        self.image, self.rect, self.mask = self.animation.p_scene(self.master.direction)
        
        self.location_update()
        


        self.hit_check()

        if self.switch and ((time.time() - self.start_time) > self.time):
            self.switch = False
            self.state_set('투명')
        
        if not self.allow and ((time.time() - self.end_time) > self.cool_time):
            self.allow = True

    def hit_check(self):
        if self.state in ['일반공격', '걷기공격', '낙하공격', '낙하공격_끝']:
            for i in self.get_new_hit_list():
                i.damaged(self, self.damage)

            for i in self.get_new_hit_list(self.game.bullets):
                if i.tag == 'player':
                    i.state_set('적 충돌')
                    i.hit = True
    
    def make_unvisible(self):
        if self.state == '투명' and self.animation.end_check() and self in self.game.visibles:
            self.game.visibles.remove(self)
    
    def attack(self):
        if self.allow:
            if self.master.state == '통상':
                self.normal_attack()
            elif self.master.state == '걷기':
                self.walk_attack()
            elif self.master.state == '점프' or self.master.state == '추락':
                self.down_attack()
        
            self.game.visibles.add(self)
            self.allow = False
            self.hit_list = []
            if not self.switch:
                self.switch = True
            self.start_time = time.time()
            self.end_time = time.time()
    
    def state_set(self, state):
        if self.state != state:
            if self.animation.sound and state != '통상':
                self.animation.sound.stop()
            c = self.rect.center
            self.state = state
            self.animation.init()
            self.animation = self.animations[self.state]
            self.image, self.rect, self.mask = self.animation.p_scene(self.direction)
            self.rect.center = c
            if self.animation.sound != None:    
                self.animation.sound.play()
    
    def normal_attack(self):
        self.state_set('일반공격')
    
    def walk_attack(self):
        self.state_set('걷기공격')
    
    def down_attack(self):
        self.state_set('낙하공격')
    
    def attack_end_check(self):
        if self.animation.end_check():
            self.state_set('통상')

    def floor_contact(self):
        self.rect.centery += 1
        for i in self.game.obstacles:
            if (pg.sprite.collide_mask(self, i)):
                self.rect.centery -= 1
                return True
        self.rect.centery -= 1
        return False
    
    def location_update(self):
        self.rect.center = self.master.rect.center + vec(self.master.direction * self.locations[self.state][0], self.locations[self.state][1])

    def weapon_upgrade(self):
        a = random.random()
        if a > 0.5:
            self.upgrade += 1
            self.name = self.name[:-1] + str(self.upgrade)
            self.damage = self.damage_0 * (1 + self.upgrade * 0.2)
            return True
        return False