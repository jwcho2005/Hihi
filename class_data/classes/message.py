from .variable import *
import time

class message(pg.sprite.Sprite):
    def __init__(self, game, message, show_time, font = 'calibri', size =50, location = vec(0, 0), color = WHITE):
        self.groups = game.all_sprites
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        message_font = pg.font.SysFont(font, size)
        self.message = message_font.render(message, True, color)
        self.rect = self.message.get_rect()
        self.rect.center = location
        self.show_time = show_time
        if self.show_time:
            self.starttime = time.time()
    
    def update(self):
        if self.show_time and time.time() - self.starttime > self.show_time:
            self.game.message = None