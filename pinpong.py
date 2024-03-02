from pygame import *
from random import randint
from time import time as timer

font.init()
font = font.Font(None, 35)
lose1 = font.render('100 луз братишка', True, (180, 150, 0))
lose2 = font.render('100 луз, сорян', True, (180, 150, 0))







#шрифты и надписи





#нам нужны такие картинки:
img_back = "iasha.jpg" #фон игры
img_hero = "pin.png" #герой
img_ball = "meach1.png" #пуля









rel_time = False




#класс-родитель для других спрайтов
class GameSprite(sprite.Sprite):
 #конструктор класса
    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):
      
        sprite.Sprite.__init__(self)


        self.image = transform.scale(image.load(player_image), (size_x, size_y))
        self.speed = player_speed

        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
 
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))




#класс главного игрока
class Player(GameSprite):
   #метод для управления спрайтом стрелками клавиатуры
    def update_1(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < 450:
            self.rect.y += self.speed
    
    def update_2(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < 450:
            self.rect.y += self.speed




win_width = 700
win_height = 500
display.set_caption("tennis")
window = display.set_mode((win_width, win_height))
background = transform.scale(image.load(img_back), (win_width, win_height))







speed_x = 3
speed_y = 3



ship = Player(img_hero, 30, 200, 50, 200, 10)
ship1 = Player(img_hero, 600, 200, 50, 200, 10)
ball = GameSprite(img_ball, 250, 250, 50, 50, 10)


clock = time.Clock()
game = True
finish = False


while game:
  
    for e in event.get():
        if e.type == QUIT:
            game = False
       #событие нажатия на пробел - спрайт стреляет
      

    if not finish:
        #обновляем фон
        window.blit(background,(0,0))


       #производим движения спрайтов
        ship.update_1()
        ship1.update_2()
        ball.rect.x += speed_x
        ball.rect.y += speed_y    

        if sprite.collide_rect(ship, ball) or sprite.collide_rect(ship1, ball):
            speed_x *= -1
        if ball.rect.y > 450 or ball.rect.y < 10: 
            speed_y *= -1
        ship.reset()
        ship1.reset()
        ball.reset()

        if ball.rect.x < 0:
            finish = True
            window.blit(lose1, (200, 200))
        if ball.rect.x > 700:
            finish = True
            window.blit(lose2, (200, 200))
      
    display.update()
   #цикл срабатывает каждую 0.05 секунд
    clock.tick(60)
   #цикл срабатывает каждую 0.05 секунд
