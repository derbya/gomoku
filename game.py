from viz import Viz
import pygame

done = False
size = 19
visualizer = Viz(size, 32 * (size - 1), 32 * (size - 1))
visualizer.initializeTextureBoard(size)

for y in range(size - 1):
    for x in range(size - 1):
        if x == 0:
            if y == 0:
                visualizer.insertTexture(x, y, 'TLCorner')
            elif y == size - 2:
                visualizer.insertTexture(x, y, 'TRCorner')
            else:
                visualizer.insertTexture(x, y, 'Top')
        elif x == size - 2:
            if y == 0:
                visualizer.insertTexture(x, y, 'BLCorner')
            elif y == size - 2:
                visualizer.insertTexture(x, y, 'BRCorner')
            else:
                visualizer.insertTexture(x, y, 'Bottom')
        else:
            if y == 0:
                visualizer.insertTexture(x, y, 'Left')
            elif y == size - 2:
                visualizer.insertTexture(x, y, 'Right')
            else:
                visualizer.insertTexture(x, y, 'Center')

visualizer.expose(size)
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
#        if event.type == pygame.MOUSEBUTTON:
    pygame.display.flip()
#visualizer.expose(size)
#visualizer.mainLoop()
