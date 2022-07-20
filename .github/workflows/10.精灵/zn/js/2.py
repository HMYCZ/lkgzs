import pygame
import sys
import RGB

pygame.init()

pygame.mixer.music.load('../../yy/hzw.mp3')
pygame.mixer.music.play()

pm = pygame.display.set_mode((1000, 600))
pygame.display.set_caption('lkgzs')
pm.fill(RGB.Gainsboro)

js = pygame.image.load('../../img/1.png')
wz = js.get_rect()
wz.center = [500, 300]

zs = pygame.time.Clock()

while True:
    pm.blit(js, wz)
    zs.tick(30)
    event = pygame.event.wait()
    if event.type == pygame.QUIT:
        sys.exit()
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_ESCAPE:
            sys.exit()
        if event.key == pygame.K_a or event.key == pygame.K_LEFT:
            wz[0] -= 5
        if event.key == pygame.K_d or event.key == pygame.K_RIGHT:
            wz[0] += 5
        if event.key == pygame.K_s or event.key == pygame.K_DOWN:
            wz[1] += 5
        if event.key == pygame.K_w or event.key == pygame.K_UP:
            wz[1] -= 5
        if event.key == pygame.K_n:
            print('\n')
            print(zs)
            print('x:', wz[0], '  ', 'y:', wz[1])
            print(js)
        pm1 = pygame.display.set_mode((1000, 600))

    pygame.display.update()
