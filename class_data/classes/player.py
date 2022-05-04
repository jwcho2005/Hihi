from .life import *
import time

class Player(Life):
    def __init__(self, game, animations, location = vec(0, 0), speed = 0, jump_speed = 0, gold = 0):
        self.groups = game.all_sprites, game.visibles, game.lifes
        Life.__init__(self, game, self.groups, animations, location = location, speed = speed, jump_speed = jump_speed, attack_point=0, hp = 6)

        self.skills = []
        self.using_skills = {}

        self.max_sh = 6
        self.sh = 6
        self.sh_time = 6
        self.sh_destruction_time = 0
        self.max_mp = 120
        self.mp = 120
        self.gold = gold
        self.weapons = []
        self.using_weapons = {'검' :None, '창' : None, '총' : None}
        self.weapon = None

        self.jump_stack = 1

    def heal_mp(self, n):
        if self.mp + n < self.max_mp:
            self.mp += n
        else:
            self.mp = self.max_mp
    
    def damaged(self, attacker, damage):
        damage = int(damage)
        if not self.none_damage:
            if self.sh == self.max_sh:
                self.sh_destruction_time = time.time()
            if self.sh - damage < 0:
                self.hp -= (damage - self.sh)
                self.sh = 0
            else:
                self.sh -= damage

            if self.die_check():
                self.state_set('죽음')
                self.weapon.state_set('투명')

            if self.rect.center != attacker.rect.center:
                v = 2 * vec(self.rect.centerx - attacker.rect.centerx, self.rect.centery - attacker.rect.centery).normalize()
                self.knockbacked(v)
    
    def attack(self):
        if self.weapon and self.operation:
            self.weapon.attack()
    
    def add_weapon(self, weapon):
        self.weapons.append(weapon)
        weapon.master_set(self)
    
    def change_weapon(self, weapon, t):
        self.using_weapons[t] = weapon
        
    def set_weapon(self, weapon):
        if self.weapon:
            self.weapon.use = False
        self.weapon = weapon
        self.weapon.use = True
        self.attack_point = self.weapon.damage
    
    def using_change_weapon(self, t):
        self.weapon.state_set('투명')
        self.weapon.make_unvisible()
        self.set_weapon(self.using_weapons[t])

    def add_skill(self, skill):
        self.skills.append(skill)
        skill.master_set(self)

    def set_skill(self, key, skill):
        if skill in self.skills:
            self.using_skills[key] = skill
    
    def update(self):
        self.buff_update()

        if self.animation.end_check():
            if self.state == '점프시작':
                self.state_set('점프')
                if self.floor_contact():
                    self.velocity.y = -self.jump_speed
                else:
                    self.velocity.y = -int(self.jump_speed * 0.9)
            elif self.state == '죽음':
                self.game.visibles.remove(self)
            elif self.state == '대쉬':
                self.operation = True
                self.state_set('통상')
                if self.walk_control_l:
                    self.walk_l()
                if self.walk_control_r:
                    self.walk_r()
                if not (self.walk_control_l or self.walk_control_r):
                    self.state_set('통상')


        self.animation_update()

        self.end_damaged()

        if self.sh < self.max_sh and time.time() - self.sh_destruction_time>= self.sh_time:
            self.sh += 1
            self.sh_destruction_time = time.time()
        
        if self.die_check():
            self.state_set('죽음')
            self.weapon.state_set('투명')
            self.none_damage = True
            self.hp = 0

        if self.state != '죽음':
            if self.floor_contact():
                if not self.jump_stack:
                    self.jump_stack += 1
                if not self.operation and (self.state != '낙하공격'):
                    if self.velocity.x == 0:
                        self.operation = True
                        if self.walk_control_l:
                            self.walk_l()
                        if self.walk_control_r:
                            self.walk_r()
                        if not (self.walk_control_l or self.walk_control_r):
                            self.state_set('통상')
                        self.friction_switch = False
                    else:
                        if self.friction_switch:
                            self.velocity.x -= ((self.velocity.x > 0) * 2 - 1) * friction * TIME
                            if -10 < (self.velocity.x) < 10:
                                self.velocity.x = 0
                else:
                    self.friction_switch = False
                    if not (self.state == '점프시작' or self.state == '점프'):
                        if self.walk_control_l or self.walk_control_r:
                            self.state_set('걷기')
                        else:
                            self.state_set('통상')
                if self.velocity.y > 0 and self.state != '점프시작' and self.state != '점프':
                    self.velocity.y = 0

            else:
                if self.state != '낙하공격' and self.state != '대쉬' and self.state != '점프시작':
                    self.velocity += self.acceleration * TIME
                    if self.velocity.y > 0 and self.state != '추락':
                        self.state_set('추락')
                if self.weapon.state == '낙하공격_끝':
                    self.velocity.y = 0 

            for i in self.using_skills.values():
                i.update()

            if self.ceiling_contact() and self.velocity.y < 0 and not self.state == '점프시작':
                self.velocity.y = 0
                self.state_set('추락')
            
            self.rect.center += self.velocity * TIME

            self.physics_update()
        self.weapon.update()

    def jump(self):
        if (self.jump_stack) and self.operation:
            self.state_set('점프시작')
            if not self.floor_contact():
                self.jump_stack -= 1
            return True
        return False