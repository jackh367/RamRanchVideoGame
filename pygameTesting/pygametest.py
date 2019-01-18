import pygame
pygame.init()


win = pygame.display.set_mode((500, 500))

pygame.display.set_caption("Ram Ranch: The Video Game ULTRA PRE ALPHA")

x = 50
y = 425
width = 40
height = 60
vel = 5


screen = pygame.display.set_mode((1600,800))
pygame.init()

file = 'Ram Ranch.mp3'
pygame.init()
pygame.mixer.init()
pygame.mixer.music.load(file)
pygame.mixer.music.play()
pygame.event.wait()

run = True
while run:
    pygame.time.delay(10)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT] and x > vel:
        x -= vel
    if keys[pygame.K_RIGHT] and x < 1600 - width - vel:
        x += vel
    if keys[pygame.K_UP] and y > vel:
        y -= vel
    if keys[pygame.K_DOWN] and y < 800 - height - vel:
        y += vel

    win.fill((0, 0, 0))
    pygame.draw.rect(win, (255, 0, 0), (x, y, width, height))
    pygame.display.update()

pygame.quit()