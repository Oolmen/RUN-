from pygame import *
from sys import *
from time import sleep

font.init()
font1 = font.Font(None, 40)
font2 = font.Font(None, 80)
win = font1.render('YOU PROFESSIONAL RUNNER!', True, (50, 200, 100))
lose = font2.render('ПРИВЕТ, ПУПСИК', True, (200, 20, 30))




#главный класс спрайтов
class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed):
        super().__init__()

        self.image = transform.scale(image.load(player_image), (50, 50))
        self.speed = player_speed

        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y

        def update_dist(self, target):
            dist_x = target.rect.x - self.rect.x
            dist_y = target.rect.y - self.rect.y

            distance = ((dist_x**2) + (dist_y**2))**0.5
            if distance > 0:
                norm_x = dist_x / distance
                norm_y = dist_y / distance
                self.rect.x += norm_x * self.speed
                self.rect.y += norm_y * self.speed

        def reset(self):
            window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_a] and self.rect.x > 5:
            self.rect.x -= self.speed
        if keys[K_d] and self.rect.x < win_shirina - 80:
            self.rect.x += self.speed
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < win_visota - 80:
            self.rect.y += self.speed
            
class Pups(GameSprite):
    def update(self, target):
        if target.rect.x > self.rect.x:
            self.rect.x += 2
        elif target.rect.x < self.rect.x:
            self.rect.x -= 2

        if target.rect.y > self.rect.y:
            self.rect.y += 2
        elif target.rect.y < self.rect.y:
            self.rect.y -= 2

win_shirina = 700
win_visota = 500
window = display.set_mode((win_shirina, win_visota))
display.set_caption("RUN!")
background = transform.scale(image.load("background.jpg"), (win_shirina, win_visota))

target = Player('kachok.jpeg', 5, win_visota - 80, 4)
pupsik = Pups("pupsik.jpeg", win_shirina - 80, 280, 2)

sprites = sprite.Group()
sprites.add(target, pupsik)

FPS = 60
mixer.init()
mixer.music.load('sigmaphonk.ogg')
mixer.music.play()
getout = mixer.Sound('tuco-get-out.ogg')
pupsich = mixer.Sound('privet-pupsik.ogg')
game = True
finish = False
vremay = 0

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False

    if finish != True:
        
        window.blit(background, (0, 0))
        pupsik.update(target)
        target.update()

        if sprite.collide_rect(pupsik, target):
            finish = True
            window.blit(lose, (100, 190))
            pupsich.play()

    sprites.draw(window)
    display.update()

        


    
        
    

