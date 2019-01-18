#find a way to make the ram img flip in the direction he's moving
#i have left an image of the ram facing in the right direction in the github repository

# Import and initialize pygame module.
import pygame
pygame.init()

# Set up game window.
screen = pygame.display.set_mode((1600,700))
pygame.display.set_caption("Ram Ranch: The Video Game alpha")

# Setting up sounds.
file = 'Ram Ranch.mp3'
pygame.mixer.init()
pygame.mixer.music.load(file)
pygame.mixer.music.play()
pygame.event.wait()

# Setting up ram.
ramimg = pygame.image.load("ram.png")
ramx = 50
ramy = 425
ramwidth = 40
ramheight = 60
ramvel = 5

# Setting up the ranch.
ranchimg = pygame.image.load("ranch.jpg")
ranchx = 0
ranchy = 0
ranchwidth = 1920
ranchheight = 734

# Start game loop.
run = True
while run:

    # pygame.time.delay(10)

    # Process events.
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    # Get user input and move the ram.
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and ramx > ramvel:
        ramx -= ramvel
    if keys[pygame.K_RIGHT] and ramx < 1600 - ramwidth - ramvel:
        ramx += ramvel
    if keys[pygame.K_UP] and ramy > ramvel:
        ramy -= ramvel
    if keys[pygame.K_DOWN] and ramy < 800 - ramheight - ramvel:
        ramy += ramvel

    # Render the scene.
    screen.fill((0, 0, 0))
    screen.blit(ranchimg, (ranchx, ranchy))
    screen.blit(ramimg, (ramx, ramy))

    pygame.display.update()

pygame.quit()