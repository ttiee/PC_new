import sys
import time
import pygame

print("wave正在启动...")
print("10%")
time.sleep(1)
print("80%")
time.sleep(1)
print("100%......完成")

time.sleep(3)
pygame.init()
size = width,height = 660,480
screen = pygame.display.set_mode(size)
color = (0,0,0)

wave = pygame.image.load("wave.gif")
waverect = wave.get_rect()

while True:
    for event in pygame.event.get():
         if event.type == pygame.QUIT:
              pygame.quit()
              sys.exit()

    screen.fill(color)
    screen.blit(wave, waverect)
    pygame.display.flip()