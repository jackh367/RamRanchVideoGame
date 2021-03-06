# Import and initialize pygame module.
import pygame
from random import choice
pygame.init()
pygame.font.init()
# Set up game window.
screen = pygame.display.set_mode((1280,720))
pygame.display.set_caption("Ram Ranch: The Video Game")
screenwidth = 1280
screenheight = 720
score = 0
pygame.font.init()
myfont = pygame.font.SysFont('Comic Sans MS', 60)
text_surface = myfont.render('{}'.format(score), False, (255, 225, 255.))
# Setting up sounds.
file = 'Ram Ranch Alternative Music.mp3'
pygame.mixer.init()
pygame.mixer.music.load(file)
pygame.mixer.music.play(loops=1)
pygame.event.wait()

# Sound effect
def munch():
    effect = pygame.mixer.Sound('munch.wav')
    effect.play()

# Setting up ram.
ramleft = pygame.image.load("ram.png")
ramright = pygame.image.load("ramflipped.png")
ramimg = ramright
ramx = 50
ramy = 425
ramwidth = 40
ramheight = 60
ramvel = 15

# Prints score to a text file, not implemented
# scores = open("scores.txt")
# scores.write("Your score that game was {}".format(score))


#simply begins playing new song, nothing else
def ramranch():
    global cowboyvel
    global ramvel
    file = 'Ram Ranch.mp3'
    pygame.mixer.init()
    pygame.mixer.music.load(file)
    pygame.mixer.music.play(loops=1)
    pygame.event.wait()


# Hard Mode: Reached once 100 points are attained
def hardmode():
    global cowboyvel
    global ramvel
    file = 'hardmodemusicAlternative.mp3'
    pygame.mixer.init()
    pygame.mixer.music.load(file)
    pygame.mixer.music.play(loops=1)
    pygame.event.wait()
    cowboyvel = 4
    ramvel = 13

#Insane Mode: Reached once 200 points are attained
def insanemode():
    global cowboyvel
    global ramvel
    file = 'hardmodemusicAlternative.mp3'
    pygame.mixer.init()
    pygame.mixer.music.load(file)
    pygame.mixer.music.play(loops=1)
    pygame.event.wait()
    cowboyvel = 8
    ramvel = 22

    # Supposed to fill the screen with an alternative background. Not working as of yet
    #screen.fill((0, 0, 0))
    #screen.blit(hellimg, (hellx, helly))
    #screen.blit(hellimg, 0, 0, 0, area=None, special_flags=0)
    #pygame.surface.blit();

    # Hitboxes

def collision(rect1, rect2,):
    # Get the upper left coordinate of the first rectangle.
    l1 = (rect1[0], rect1[1])

    # Get the lower right coordinate of the first rectangle.
    r1 = (rect1[0] + rect1[2], rect1[1] + rect1[3])

    # Get the upper left coordinate of the second rectangle.
    l2 = (rect2[0], rect2[1])

    # Get the lower right coordinate of the second rectangle.
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

# Setting up the ranch with an alternative sky (For hard mode.)
hellimg = pygame.image.load("hell.jpg")
hellx = 0
helly = 0
hellwidth = 1920
hellheight = 734

# Setting up the literal depths of hell. (For insane mode.)
hellactualimg = pygame.image.load("hell.jpg")
hellactualx = 0
hellactualy = 0
hellactualwidth = 1920
hellactualheight = 734

# Grass x,y and image.
grassx = 700
grassy = 500
grassimg = pygame.image.load("grass.png")
grasswidth = 200
grassheight = 256

# Soul X,Y and image.
soulx = 700
souly = 500
soulimg = pygame.image.load("soul.png")
soulwidth = 200
soulheight = 256

# setting up enemies
cowboyleft = pygame.image.load("cowboyleft.png")
cowboyright = pygame.image.load("cowboyright.png")
cowboyimg = cowboyright
cowboyx = 600
cowboyy = 400
cowboywidth = 180
cowboyheight = 194
cowboyvel = 2

# Setting up grass.
def spawngrass():
    global grassx, grassy
    grassx = choice(range(1000))
    grassy = choice(range(600))
    if collision(((grassx, grassy, grasswidth, grassheight)), ((grassx, grassy, 230, 200))):
        grassx = choice(range(1000))
<<<<<<< HEAD
        grassy = choice(range(690))
=======
        grassy = choice(range(600))
>>>>>>> e8f8b434aee0aaf4a8f97ec6d1f08d4d5c159630

# Setting up souls. (Replaces grass in insane mode.)
def spawnsoul():
    global soulx, souly
    soulx = choice(range(1000))
    souly = choice(range(600))
    if collision(((soulx, souly, grasswidth, grassheight)), ((soulx, souly, 230, 200))):
        soulx = choice(range(1000))
        souly = choice(range(600))


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
    if keys[pygame.K_RIGHT] and ramx < 1280 - ramwidth - ramvel:
        ramimg = ramright # Set the ram image to the right one.
        ramx += ramvel
    if keys[pygame.K_UP] and ramy > ramvel:
        ramy -= ramvel
    if keys[pygame.K_DOWN] and ramy < 700 - ramheight - ramvel:
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
    soulrect = (soulx, souly, soulwidth, soulheight)
    if collision(cowboyrect, ramrect):
        break
        scores()

    if collision(ramrect, grassrect):
        score += 1
        munch()
        grassx = choice(range(1000))
        grassy = choice(range(600))

    if score == 10:
<<<<<<< HEAD
        cowboyvel = 3
    if score == 20:
        cowboyvel = 4
    if score == 30:
        cowboyvel = 4.5
    if score == 40:
        cowboyvel = 5
    if score == 50:
        score = 0
        hardmode()
=======
        cowboyvel = 1.6
    if score == 20:
        cowboyvel = 2.7
    if score == 30:
        cowboyvel = 2.8
    if score == 40:
        cowboyvel = 2.9
    if score == 50:
        score += 1
        ramranch()
    if score == 100:
        score += 1
        hardmode()
    if score == 150:
        cowboyvel = 6
    if score == 200:
        score += 1
        insanemode()

>>>>>>> e8f8b434aee0aaf4a8f97ec6d1f08d4d5c159630
    text_surface = myfont.render('{}'.format(score), False, (255, 255, 255.))
    # Render the scene.
    screen.fill((0, 0, 0))
    screen.blit(ranchimg, (ranchx, ranchy))
    screen.blit(ramimg, (ramx, ramy))
    screen.blit(cowboyimg, (cowboyx, cowboyy))
    screen.blit(grassimg, (grassx, grassy))
    screen.blit(text_surface, (20,20))
    pygame.display.update()

    #if hardmode(): True
    #screen.Surface.blit(hellimg, (hellx, helly))
#else:
    #if insanemode(): True
    #screen.Surface.blit(hellactualimg, (hellactualx, hellactualy))
    #screen.Surface.blit(soulimg, (soulx, souly))




pygame.quit()