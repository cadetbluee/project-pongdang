<<<<<<< HEAD
from pygame import *
=======
import pygame, sys
from button import Button
import random
>>>>>>> edf3d6c1f081373bfc48181b37ec5ac7feb8ea05

C1_GREEN = (204, 255, 204)
C1_BLUE = (153, 204, 255)
bgColor = C1_GREEN

<<<<<<< HEAD
size = width, height = 800,600
screen = display.set_mode(size)
screen.fill(bgColor)
display.update()
init()

start = (0,0)
end = (0,0)
dSize = (0,0)
drawing = False
rectList = []

run =True
while (run):
    for pyEvent in event.get():
        if pyEvent.type == QUIT:
            run = False
        elif pyEvent.type == MOUSEBUTTONDOWN:
            start = pyEvent.pos
            dSize = 0,0
            drawing = True
            print(pyEvent)
        elif pyEvent.type == MOUSEBUTTONUP:
            end = pyEvent.pos
            dSize = end[0]-start[0], end[1]-start[1]
            drawing = False
            rect = Rect(start,dSize)
            rectList.append(rect)
            print(pyEvent)
        elif pyEvent.type == MOUSEMOTION and drawing:
            end = pyEvent.pos
            dSize = end[0]-start[0], end[1]-start[1]
            screen.fill(bgColor)
            for r in rectList:
                draw.rect(screen,(0,0,0),r,4)
            draw.rect(screen,(255,0,0),(start,dSize),2)
            display.update()

print("END HERE")
quit()
=======
display_width = 650 # 가로 사이즈
display_height = 977
SCREEN=pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption("Menu")

BG=pygame.image.load('assets/main_background.jpg').convert()
BG=pygame.transform.smoothscale(BG, SCREEN.get_size())

def get_font(size): 
    return pygame.font.SysFont("comicsans", size)
def play():
    while True:
        PLAY_MOUSE_POS = pygame.mouse.get_pos()

        SCREEN.fill("black")

        PLAY_TEXT = get_font(45).render("This is the PLAY screen.", True, "White")
        PLAY_RECT = PLAY_TEXT.get_rect(center=(640, 260))
        SCREEN.blit(PLAY_TEXT, PLAY_RECT)

        PLAY_BACK = Button(image=None, pos=(640, 460), 
                            text_input="BACK", font=get_font(75), base_color="White", hovering_color="Green")

        PLAY_BACK.changeColor(PLAY_MOUSE_POS)
        PLAY_BACK.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BACK.checkForInput(PLAY_MOUSE_POS):
                    main_menu()

        pygame.display.update()

def main_menu():
    while True:
        SCREEN.blit(BG, (0, 0))

        MENU_MOUSE_POS = pygame.mouse.get_pos()

     
        buttom_img=pygame.image.load("assets/play.png")
        buttom_img = pygame.transform.scale(buttom_img, (200,100))
        PLAY_BUTTON = Button(buttom_img, pos=(200, 800), 
                            text_input="PLAY", font=get_font(50), base_color="#d7fcd4", hovering_color="White")

        QUIT_BUTTON = Button(buttom_img, pos=(500, 800), 
                            text_input="QUIT", font=get_font(50), base_color="#d7fcd4", hovering_color="White")



        for button in [PLAY_BUTTON,QUIT_BUTTON]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(SCREEN)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
                    play()

                if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    pygame.quit()
                    sys.exit()

        pygame.display.update()
        
main_menu()
>>>>>>> edf3d6c1f081373bfc48181b37ec5ac7feb8ea05
