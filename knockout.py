from pygame import *

C1_GREEN = (204, 255, 204)
C1_BLUE = (153, 204, 255)
bgColor = C1_GREEN

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