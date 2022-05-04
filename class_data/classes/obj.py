from .variable import *


class obj(pg.sprite.Sprite):
    def __init__(self, game, groups, animations, direction = 1, location = vec(0, 0)):
        self.groups = groups
        self.velocity = vec(0, 0)
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.state = '통상'
        self.animations = animations
        self.animation = self.animations[self.state]
        self.image, self.rect, self.mask = self.animation.p_scene(direction)
        self.direction = direction
        self.rect.center = location

    def state_set(self, state):
        if self.state != state:
            t = False
            if self.floor_contact():
                t = True
                y = self.rect.bottom
            else:
                y = self.rect.centery
            x = self.rect.centerx
            if self.animation.sound:
                self.animation.sound.stop()
            self.state = state
            self.animation.init()
            self.animation = self.animations[self.state]
            self.image, self.rect, self.mask = self.animation.p_scene(self.direction)
            if t:
                self.rect.bottom = y
            else:
                self.rect.centery = y
            self.rect.centerx = x
            if self.animation.sound and self.animation.sound_start == 0:    
                self.animation.sound.play()
    
    # def image_flip(self):
    #     if self.direction == -1:
    #         self.image = pg.transform.flip(self.image, True, False)
    
    def animation_update(self):
        t = False
        if self.floor_contact():
            t = True
            y = self.rect.copy().bottom
        else:
            y = self.rect.copy().centery
        x = self.rect.copy().centerx
        self.animation.update()
        self.image, self.rect, self.mask = self.animation.p_scene(self.direction)
        if self.animation.sound and self.animation.sound_start == self.animation.p_frame and self.animation.sound_start:
            self.animation.sound.play()
        if t:
            self.rect.bottom = y
        else:
            self.rect.centery = y
        self.rect.centerx = x

    def floor_contact(self):
        # self.rect.centery += 1
        # for i in self.game.obstacles:
        #     if (pg.sprite.collide_mask(self, i)):
        #         self.rect.centery -= 1
        #         return True
        # self.rect.centery -= 1
        # return False
        self.rect.centery += 1
        for i in self.game.obstacles:
            if pg.sprite.collide_mask(self, i):
                if self.rect.bottom - 1 == i.rect.top:
                    self.rect.centery -= 1
                    return True
        self.rect.centery -= 1
        return False

    
    def ceiling_contact(self):
        # self.rect.centery -= 1
        # for i in self.game.obstacles:
        #     if (pg.sprite.collide_mask(self, i)):
        #         self.rect.centery += 1
        #         return True
        # self.rect.centery += 1
        # return False
        self.rect.centery -= 1
        for i in self.game.obstacles:
            if pg.sprite.collide_mask(self, i):
                if self.rect.bottom + 1 == i.rect.top:
                    self.rect.centery += 1
                    return True
        self.rect.centery += 1
        return False

    def wall_r_contact(self):
        self.rect.centerx += 1
        for i in self.game.obstacles:
            if (pg.sprite.collide_mask(self, i)):
                self.rect.centerx -= 1
                return True
        self.rect.centerx -= 1
        return False
    
    def wall_l_contact(self):
        self.rect.centerx -= 1
        for i in self.game.obstacles:
            if (pg.sprite.collide_mask(self, i)):
                self.rect.centerx += 1
                return True
        self.rect.centerx += 1
        return False

    def delete(self):
        for i in self.groups:
            i.remove(self)
        del self