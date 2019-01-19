# Import and initialize pygame module.
import pygame
pygame.init()

# Set up game window.
screen = pygame.display.set_mode((1280,720))
pygame.display.set_caption("Ram Ranch: The Video Game")

# Setting up sounds.
file = 'Ram Ranch.mp3'
pygame.mixer.init()
pygame.mixer.music.load(file)
#pygame.mixer.music.play()
pygame.event.wait()

# Setting up ram.
ramleft = pygame.image.load("ram.png")
ramright = pygame.image.load("ramflipped.png")
ramimg = ramright
ramx = 50
ramy = 425
ramwidth = 40
ramheight = 60
ramvel = 5.5

def collision(rect1, rect2):
    # Get the upper left coordinate of the first rectangle.
    l1 = (rect1[0], rect1[1])

    # Get the lower right coordinate of the first rectangle.
    r1 = (rect1[0] + rect1[2], rect1[1] + rect1[3])

    # Get the upper left coordinate of the second triangle.
    l2 = (rect2[0], rect2[1])

    # Get the lower right coordinate of the second triangle.
    r2 = (rect2[0] + rect2[2], rect2[1] + rect2[3])

    # If the rectangles do not overlap in the x-dimension, then return false.
    if l1[0] > r2[0] or l2[0] > r1[0]:
        return False

    # If the rectangles do not overlap in the y-dimension, then return false.
    if l1[1] > r2[1] or l2[1] > r1[1]:
        return False

    # If neither of the above if-statements are true, then the rectangles must
    # overlap in some way, therefore the function returns True.
    return True



# Setting up the ranch.
ranchimg = pygame.image.load("ranch.jpg")
ranchx = 0
ranchy = 0
ranchwidth = 1920
ranchheight = 734

# setting up enemies
cowboyleft = pygame.image.load("cowboyleft.png")
cowboyright = pygame.image.load("cowboyright.png")
cowboyimg = cowboyright
cowboyx = 0
cowboyy = 0
cowboywidth = 180
cowboyheight = 194
cowboyvel = 2.5


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
        ramimg = ramleft
        ramx -= ramvel
    if keys[pygame.K_RIGHT] and ramx < 1600 - ramwidth - ramvel:
        ramimg = ramright
        ramx += ramvel
    if keys[pygame.K_UP] and ramy > ramvel:
        ramy -= ramvel
    if keys[pygame.K_DOWN] and ramy < 800 - ramheight - ramvel:
        ramy += ramvel


    #where cowboy follows the ram
    if ramx > cowboyx:
        cowboyx = cowboyx + cowboyvel
    if ramy > cowboyy:
        cowboyy = cowboyy + cowboyvel
    if ramx < cowboyx:
            cowboyx = cowboyx - cowboyvel
    if ramy < cowboyy:
            cowboyy = cowboyy - cowboyvel



    # Render the scene.
    screen.fill((0, 0, 0))
    screen.blit(ranchimg, (ranchx, ranchy))
    screen.blit(ramimg, (ramx, ramy))
    screen.blit(cowboyimg, (cowboyx, cowboyy))
    pygame.display.update()


pygame.quit()