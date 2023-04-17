from pygame import *

mixer.init()
mixer.music.load('Kagamine Len - Banana song.mp3')
mixer.music.play()

FPS = 60
WIN_WIGHT = 700
WIN_HEIGHT = 500
RUN = True
PLAYER_IMG = "BANANA.png"
BACKGROUND_IMG = 'BANANANANNANANNANA_BG.png'
win = display.set_mode((WIN_WIGHT, WIN_HEIGHT))
display.set_caption('鏡音レンはバナナナナナナナナナナナナナナナナナナ!!!!!!!!!!!!')

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):
        sprite.Sprite.__init__(self)

        self.image = transform.scale(image.load(player_image), (size_x, size_y))
        self.speed = player_speed

        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y

    def reset(self):
        win.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 30:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < WIN_HEIGHT - 100:
            self.rect.y += self.speed

BACKGROUND = transform.scale(image.load(BACKGROUND_IMG), (WIN_WIGHT, WIN_HEIGHT))
player1 = Player(PLAYER_IMG, 10, 100, 86, 143, 10)
player2 = Player(PLAYER_IMG, 604, 100, 86, 143, 10)

while RUN:
    for e in event.get():
        if e.type == QUIT:
            RUN = False

    win.blit(BACKGROUND, (0, 0))
    player1.reset()
    player2.reset()

    player1.update()
    player2.update()

    time.delay(FPS)
    display.update()

