import pygame

class Viz:
    imageDictionary =  {}
    boardTextures = []
    done = False
    def __init__(self, size, width, height):
        pygame.init()
        self.screen = pygame.display.set_mode((width, height))
        self.imageDictionary.update( { 'BLCorner' : pygame.image.load('images/BLCorner.png')  } )
        self.imageDictionary.update( { 'BRCorner' : pygame.image.load('images/BRCorner.png')  } )
        self.imageDictionary.update( { 'TRCorner' : pygame.image.load('images/TRCorner.png')  } )
        self.imageDictionary.update( { 'TLCorner' : pygame.image.load('images/TLCorner.png')  } )
        self.imageDictionary.update( { 'Top' : pygame.image.load('images/Top.png')  } )
        self.imageDictionary.update( { 'Bottom' : pygame.image.load('images/Bottom.png')  } )
        self.imageDictionary.update( { 'Left' : pygame.image.load('images/Left.png')  } )
        self.imageDictionary.update( { 'Right' : pygame.image.load('images/Right.png')  } )
        self.imageDictionary.update( { 'Center' : pygame.image.load('images/Center.png')  } )
        self.imageDictionary.update( { 'bg' : pygame.image.load('images/woodBG.jpg')  } )

    def drawBackground(self):
        self.screen.blit(self.imageDictionary['bg'], (0, 0))
#        self.screen.fill((255, 255, 255))

    def expose(self, size):
        self.drawBackground()
        for i in range(size - 1):
            for j in range(size - 1):
                self.screen.blit(self.boardTextures[j][i], (i * 32, j * 32))

    def insertTexture(self, x, y, image):
        self.boardTextures[x][y].blit(self.imageDictionary[image], (0, 0))

    def initializeTextureBoard(self, size):
        for y in range(0, size - 1):
            new = []
            for x in range(0, size - 1):
                new.append(pygame.Surface((32, 32), pygame.SRCALPHA))
            self.boardTextures.append(new)

#    def mainLoop(self):
#        while not self.done:
#            for event in pygame.event.get():
#                if event.type == pygame.QUIT:
#                    self.done = True
#            pygame.display.flip()
