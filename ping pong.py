import pygame, sys, random
from pygame.locals import *

#FUNCTIONS

def terminate():
    pygame.quit()
    sys.exit()

def drawText(text, font, surface, x, y):
    textobj = font.render(text, 1, TEXTCOLOR)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)

pygame.init()

#SCREEN
WINDOWHEIGHT = 400
WINDOWWIDTH = 700
windowSurface = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
pygame.display.set_caption('PING PONG GAME')
FPS = 60
mainClock = pygame.time.Clock()

#COLORS
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

#PLAYERS
PLAYERWIDTH = 20
PLAYERHEIGHT = 100
PLAYER1 = {'rect': pygame.Rect(PLAYERWIDTH, (WINDOWHEIGHT / 2.5), PLAYERWIDTH, PLAYERHEIGHT),
           'color': WHITE}
PLAYER2 = {'rect': pygame.Rect(WINDOWWIDTH - PLAYERWIDTH  * 2, (WINDOWHEIGHT / 2.5), PLAYERWIDTH, PLAYERHEIGHT),
           'color': WHITE}


PLAYERSPEED = 10
moveDownPLAYER1 = moveUpPLAYER1 = False
moveDownPLAYER2 = moveUpPLAYER2 = False


#BALL
DOWNLEFT = 'downleft'
DOWNRIGHT = 'downright'
UPLEFT = 'upleft'
UPRIGHT = 'upright'

DIRECTIONS = [DOWNLEFT, DOWNRIGHT, UPLEFT, UPRIGHT]

BALLSIZE = 10

#SHOW THE START SCREEN
font = pygame.font.SysFont(None, 100)
scorePlayer1 = 0
scorePlayer2 = 0
TEXTCOLOR = (255, 255, 255)

MOVESPEED = 5



while True:
    RANDOMDIRECT = random.randint(0, len(DIRECTIONS) - 1)

    BALL = {'rect': pygame.Rect((WINDOWWIDTH / 2), (WINDOWHEIGHT / 2), BALLSIZE, BALLSIZE),
        'color': WHITE,
        'dir': DIRECTIONS[RANDOMDIRECT]}
    
    while True:
        
        for event in pygame.event.get():

            if event.type == QUIT:
                terminate()

            if event.type == KEYDOWN:
                if event.key == K_w:
                    moveUpPLAYER1 = True
                    moveDownPLAYER1 = False
                if event.key == K_s:
                    moveDownPLAYER1 = True
                    moveUpPLAYER1 = False
                if event.key == K_UP:
                    moveUpPLAYER2 = True
                    moveDownPLAYER2 = False
                if event.key == K_DOWN:
                    moveDownPLAYER2 = True
                    moveUpPLAYER2 = False                
            
            if event.type == KEYUP:
                if event.key == K_ESCAPE:
                    terminate()
                if event.key == K_w:
                    moveUpPLAYER1 = False
                if event.key == K_s:
                    moveDownPLAYER1 = False
                if event.key == K_UP:
                    moveUpPLAYER2 = False
                if event.key == K_DOWN:
                    moveDownPLAYER2 = False 
                if event.key == K_x:
                    MOVESPEED += 1
                if event.key == K_z:
                    MOVESPEED -= 1
            
        #MOVE BALL

        if BALL['dir'] == DOWNLEFT:    
            BALL['rect'].left -= MOVESPEED
            BALL['rect'].top += MOVESPEED
            
        if BALL['dir'] == DOWNRIGHT:
            BALL['rect'].left += MOVESPEED
            BALL['rect'].top += MOVESPEED
            
        if BALL['dir'] == UPLEFT:
            BALL['rect'].left -= MOVESPEED
            BALL['rect'].top -= MOVESPEED
            
        if BALL['dir'] == UPRIGHT:
            BALL['rect'].left += MOVESPEED
            BALL['rect'].top -= MOVESPEED

        if BALL['rect'].top < 0:
            if BALL['dir'] == UPLEFT:
                BALL['dir'] = DOWNLEFT
            if BALL['dir'] == UPRIGHT:
                BALL['dir'] = DOWNRIGHT
        
        if BALL['rect'].bottom > WINDOWHEIGHT:
            if BALL['dir'] == DOWNLEFT:
                BALL['dir'] = UPLEFT
            if BALL['dir'] == DOWNRIGHT:
                BALL['dir'] = UPRIGHT
        
        if BALL['rect'].left < 0:
            scorePlayer2 += 1
            break
        
        if BALL['rect'].right > WINDOWWIDTH:
            scorePlayer1 += 1
            break
        
        #MOVE PLAYERS

        if moveUpPLAYER1 and PLAYER1['rect'].top > 0:
            PLAYER1['rect'].move_ip(0, -1 * PLAYERSPEED)
        if moveDownPLAYER1 and PLAYER1['rect'].bottom < WINDOWHEIGHT:
            PLAYER1['rect'].move_ip(0, PLAYERSPEED)             

        if moveUpPLAYER2 and PLAYER2['rect'].top > 0:
            PLAYER2['rect'].move_ip(0, -1 * PLAYERSPEED)
        if moveDownPLAYER2 and PLAYER2['rect'].bottom < WINDOWHEIGHT:
            PLAYER2['rect'].move_ip(0, PLAYERSPEED)  

        windowSurface.fill(BLACK)    
        
        if BALL['rect'].colliderect(PLAYER1['rect']) or BALL['rect'].colliderect(PLAYER2['rect']):
            if BALL['rect'].left < PLAYER1['rect'].right:
                if BALL['dir'] == DOWNLEFT:
                    BALL['dir'] = DOWNRIGHT
                if BALL['dir'] == UPLEFT:
                    BALL['dir'] = UPRIGHT

            if BALL['rect'].right > PLAYER2['rect'].left:
                if BALL['dir'] == DOWNRIGHT:
                    BALL['dir'] = DOWNLEFT
                if BALL['dir'] == UPRIGHT:
                    BALL['dir'] = UPLEFT

        pygame.draw.rect(windowSurface, PLAYER1['color'], PLAYER1['rect'])
        pygame.draw.rect(windowSurface, PLAYER2['color'], PLAYER2['rect'])
        
        pygame.draw.rect(windowSurface, BALL['color'], BALL['rect'])
        
        pygame.draw.rect(windowSurface, WHITE,  (WINDOWWIDTH / 2, 0, 5, WINDOWHEIGHT))

        drawText('%s' % (scorePlayer1), font, windowSurface, 100, 10)
        drawText('%s' % (scorePlayer2), font, windowSurface, WINDOWWIDTH - 100, 10)
        
        pygame.display.update()

        mainClock.tick(FPS)
