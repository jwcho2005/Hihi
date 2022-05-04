from .obj import *

class Impact(obj):
    def __init__(self, game, animations, direction, master = None, location = vec(0, 0), relative_position = vec(0, 0), damage = 0, loop = False, tag = ['enemy']):
        self.groups = game.all_sprites, game.impacts, game.visibles
        if master:
            obj.__init__(self, game, self.groups, animations, direction=direction, location=relative_position + vec(master.rect.center))
        else:
            obj.__init__(self, game, self.groups, animations, direction=direction, location=location)
        self.tag = tag
        self.loop = loop
        self.damage = damage

        self.rp = relative_position

        self.hit_list = []
        self.master = master
        self.player_hit_check = False
    
    def get_new_hit_list(self, a):
        hit_list = pg.sprite.spritecollide(self,a,False,pg.sprite.collide_mask)
        hit_list = list(set(hit_list) - set(self.hit_list))
        self.hit_list += hit_list
        self.hit_list = list(set(self.hit_list))

        return hit_list
    
    def player_hit(self):
        return pg.sprite.collide_mask(self, self.game.player)
    
    def new_player_hit(self):
        if not self.player_hit_check and self.player_hit():
            self.player_hit_check = True
            return True
        return False

    def update(self):
        if self.animation.end_check():
            if self.loop > 1:
                self.loop -= 1
            else:
                self.delete()

        self.animation.update()
        if self.master != None:
            self.image, self.rect, self.mask = self.animation.p_scene(self.master.direction)
            self.rect.center = vec(self.master.rect.center) + vec(self.master.direction * self.rp.x, self.rp.y)
        else:
            c = self.rect.center
            self.image, self.rect, self.mask = self.animation.p_scene(self.direction)
            self.rect.center = c

        if self.damage > 0:
            if 'enemy' in self.tag:
                for i in self.get_new_hit_list(self.game.enemies):
                    i.damaged(self, self.damage)
                
            if 'player' in self.tag:
                if self.new_player_hit():
                    self.game.player.damaged(self, self.damage)
            
            for i in self.get_new_hit_list(self.game.bullets):
                i.delete()