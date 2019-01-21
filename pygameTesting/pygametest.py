# Import and initialize pygame module.
import pygame
from random import choice
pygame.init()

# Set up game window.
screen = pygame.display.set_mode((1280,720))
pygame.display.set_caption("Ram Ranch")

# Setting up sounds.
file = 'Ram Ranch.mp3'
pygame.mixer.init()
pygame.mixer.music.load(file)
#pygame.mixer.music.play()
pygame.event.wait()
#munch sound effect when ram eats grass
def munch():
    file = 'munch.mp3'
    pygame.mixer.init()
    pygame.mixer.music.load(file)
    pygame.mixer.music.play()
    pygame.event.wait()



# Setting up ram.
ramleft = pygame.image.load("ram.png")
ramright = pygame.image.load("ramflipped.png")
ramimg = ramright
ramx = 50
ramy = 425
ramwidth = 40
ramheight = 60
ramvel = 20

# this variable keeps track of the ram's grass eaten
score = 0
#sets up harder version of the game
def hardmode():
    global cowboyvel
    global ramvel
    #file = 'hardmodemusic.mp3'
    pygame.mixer.init()
    pygame.mixer.music.load(file)
    pygame.mixer.music.play()
    pygame.event.wait()
    cowboyvel = 45
    ramvel = 60
#sets up probably impossible version of the game if you even make it this far
def impossiblemode():
    global cowboyvel
    global ramvel
    cowboyvel = 999
    ramvel = 999


# This method detects if two rectangles are overlapping.
# Implements the algorithm found at https://www.geeksforgeeks.org/find-two-rectangles-overlap/
# INPUTS:
# rect1 -> a tuple containing the upper left x coordinate, upper left y coordinate,
#          width, and height of a rectangle.
# rect2 -> a tuple containing the upper left x coordinate, upper left y coordinate,
#          width, and height of a second rectangle.
# OUTPUTS:
# returns true if the rectangles overlap and false if they don't.
# ---------------------------------------------------------------------------------
def collision(rect1, rect2, rect3):
    # Get the upper left coordinate of the first rectangle.
    l1 = (rect1[0], rect1[1])

    # Get the lower right coordinate of the first rectangle.
    r1 = (rect1[0] + rect1[2], rect1[1] + rect1[3])

    # Get the upper left coordinate of the second rectangle.
    l2 = (rect2[0], rect2[1])

    # Get the lower right coordinate of the second rectangle.
    r2 = (rect2[0] + rect2[2], rect2[1] + rect2[3])

    # Get the upper left coordinate of the third rectangle.
    l3 = (rect3[0], rect3[1])

    # Get the lower right coordinate of the third rectangle.
    r3 = (rect3[0] + rect3[2], rect3[1] + rect3[3])

    # If the rectangles do not overlap in the x-dimension, then return false.
    if l1[0] > r2[0] or l2[0] > r1[0] or l3[0] > r3[0]:
        return False

    # If the rectangles do not overlap in the y-dimension, then return false.
    if l1[1] > r2[1] or l2[1] > r1[1] or l3[1] > r3[1]:
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

# grass x,y and img
grassx = 0
grassy = 0
grassimg = pygame.image.load("grass.png")
grasswidth = 191
grassheight = 256


# setting up enemies
cowboyleft = pygame.image.load("cowboyleft.png")
cowboyright = pygame.image.load("cowboyright.png")
cowboyimg = cowboyright
cowboyx = 0
cowboyy = 0
cowboywidth = 180
cowboyheight = 194
cowboyvel = 3.5

# setting up grass that ram runs around and eats
def spawngrass():
    global grassx, grassy
    grassx = choice(range(1000))
    grassy = choice(range(700))
    if collision(((grassx, grassy, grasswidth, grassheight)), ((grassx, grassy, 230, 200))):
        grassx = choice(range(1000))
        grassy = choice(range(700))


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
        ramimg = ramleft # Set the ram image to the left one.
        ramx -= ramvel
    if keys[pygame.K_RIGHT] and ramx < 1600 - ramwidth - ramvel:
        ramimg = ramright # Set the ram image to the right one.
        ramx += ramvel
    if keys[pygame.K_UP] and ramy > ramvel:
        ramy -= ramvel
    if keys[pygame.K_DOWN] and ramy < 800 - ramheight - ramvel:
        ramy += ramvel


    #where cowboy follows the ram
    if ramx > cowboyx:
        cowboyimg = cowboyright
        cowboyx = cowboyx + cowboyvel
    if ramy > cowboyy:
        cowboyy = cowboyy + cowboyvel
    if ramx < cowboyx:
        cowboyimg = cowboyleft
        cowboyx = cowboyx - cowboyvel
    if ramy < cowboyy:
            cowboyy = cowboyy - cowboyvel

    grassrect = (grassx, grassy, grasswidth, grassheight)
    cowboyrect = (cowboyx, cowboyy, cowboywidth, cowboyheight)
    ramrect = (ramx, ramy, ramwidth, ramheight)
    if collision(cowboyrect, ramrect):
        #webbrowser.open('https://fbcdn-sphotos-e-a.hubatka.cz/hphotos-ak-prn1/44530_491807354174208_665546187_n.jpg')
        pygame.quit()
    if collision(ramrect, grassrect):
        score += 1
        munch()



    if score == 50:
        hardmode()

    if score == 100:
        impossiblemode()

    # Render the scene.
    screen.fill((0, 0, 0))
    screen.blit(ranchimg, (ranchx, ranchy))
    screen.blit(ramimg, (ramx, ramy))
    screen.blit(cowboyimg, (cowboyx, cowboyy))
    screen.blit(grassimg, (grassx, grassy))
    pygame.display.update()


pygame.quit()