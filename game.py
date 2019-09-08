from viz import Viz
import pygame

class Game:
    playerDictionary = {    True : 1, False : 2   }
    currentPlayer = True
    done = False
    gameBoard = []

    def __init__(self, size):
        self.size = size
        self.visualizer = Viz(size, 32 * (size - 1), 32 * (size - 1))
        self.visualizer.initializeTextureBoard(size)
        for i in range(size - 1):
            new = []
            for j in range(size - 1):
                new.append(0)
            self.gameBoard.append(new)
        for y in range(size - 1):
            for x in range(size - 1):
                if x == 0:
                    if y == 0:
                        self.visualizer.insertTexture(x, y, 'TLCorner')
                    elif y == size - 2:
                        self.visualizer.insertTexture(x, y, 'TRCorner')
                    else:
                        self.visualizer.insertTexture(x, y, 'Top')
                elif x == size - 2:
                    if y == 0:
                        self.visualizer.insertTexture(x, y, 'BLCorner')
                    elif y == size - 2:
                        self.visualizer.insertTexture(x, y, 'BRCorner')
                    else:
                        self.visualizer.insertTexture(x, y, 'Bottom')
                else:
                    if y == 0:
                        self.visualizer.insertTexture(x, y, 'Left')
                    elif y == size - 2:
                        self.visualizer.insertTexture(x, y, 'Right')
                    else:
                        self.visualizer.insertTexture(x, y, 'Center')
        self.visualizer.expose(size)

    def checkCapture(self, x, y):
        player  = self.playerDictionary[self.currentPlayer]
        opponent = self.playerDictionary[not self.currentPlayer]
        indexList = []
        try:
            if self.gameBoard[y][x - 3] == player:
                if self.gameBoard[y][x - 1] == opponent and self.gameBoard[y][x - 2] == opponent:
                    indexList.append((x - 1, y))
                    indexList.append((x - 2, y))
        except IndexError:
            pass
        try:
            if self.gameBoard[y - 3][x] == player:
                if self.gameBoard[y - 1][x] == opponent and self.gameBoard[y - 2][x] == opponent:
                    indexList.append((x, y - 1))
                    indexList.append((x, y - 2))
        except IndexError:
            pass
        try:
            if self.gameBoard[y][x + 3] == player:
                if self.gameBoard[y][x + 1] == opponent and self.gameBoard[y][x + 2] == opponent:
                    indexList.append((x + 1, y))
                    indexList.append((x + 2, y))
        except IndexError:
            pass
        try:
            if self.gameBoard[y + 3][x] == player:
                if self.gameBoard[y + 1][x] == opponent and self.gameBoard[y + 2][x] == opponent:
                    indexList.append((x, y + 1))
                    indexList.append((x, y + 2))
        except IndexError:
            pass
        try:
            if self.gameBoard[y + 3][x + 3] == player:
                if self.gameBoard[y + 1][x + 1] == opponent and self.gameBoard[y + 2][x + 2] == opponent:
                    indexList.append((x + 1, y + 1))
                    indexList.append((x + 2, y + 2))
        except IndexError:
            pass
        try:
            if self.gameBoard[y - 3][x + 3] == player:
                if self.gameBoard[y - 1][x + 1] == opponent and self.gameBoard[y - 2][x + 2] == opponent:
                    indexList.append((x + 1, y - 1))
                    indexList.append((x + 2, y - 2))
        except IndexError:
            pass
        try:
            if self.gameBoard[y - 3][x - 3] == player:
                if self.gameBoard[y - 1][x - 1] == opponent and self.gameBoard[y - 2][x - 2] == opponent:
                    indexList.append((x - 1, y - 1))
                    indexList.append((x - 2, y - 2))
        except IndexError:
            pass
        try:
            if self.gameBoard[y + 3][x - 3] == player:
                if self.gameBoard[y + 1][x - 1] == opponent and self.gameBoard[y + 2][x - 2] == opponent:
                    indexList.append((x - 1, y + 1))
                    indexList.append((x - 2, y + 2))
        except IndexError:
            pass
        return indexList

    def isThree(self, x, y):
        return False

    def isSelfCapture(self, x, y):
        player = self.playerDictionary[self.currentPlayer]
        opponent = self.playerDictionary[not self.currentPlayer]
        try:
            if self.gameBoard[y - 1][x] == opponent:
                try:
                    if self.gameBoard[y + 1][x] == player and self.gameBoard[y + 2][x] == opponent:
                        return True
                except IndexError:
                    pass
        except IndexError:
            pass
        try:
            if self.gameBoard[y + 1][x] == opponent:
                try:
                    if self.gameBoard[y - 1][x] == player and self.gameBoard[y - 2][x] == opponent:
                        return True
                except IndexError:
                    pass
        except IndexError:
            pass
        try:
            if self.gameBoard[y][x + 1] == opponent:
                try:
                    if self.gameBoard[y][x - 1] == player and self.gameBoard[y][x - 2] == opponent:
                        return True
                except IndexError:
                    pass
        except IndexError:
            pass
        try:
            if self.gameBoard[y][x - 1] == opponent:
                try:
                    if self.gameBoard[y][x + 1] == player and self.gameBoard[y][x + 2] == opponent:
                        return True
                except IndexError:
                    pass
        except IndexError:
            pass
        try:
            if self.gameBoard[y -1][x - 1] == opponent:
                try:
                    if self.gameBoard[y + 1][x + 1] == player and self.gameBoard[y + 2][x + 2] == opponent:
                        return True
                except IndexError:
                    pass
        except IndexError:
            pass
        try:
            if self.gameBoard[y + 1][x - 1] == opponent:
                try:
                    if self.gameBoard[y - 1][x + 1] == player and self.gameBoard[y - 2][x + 2] == opponent:
                        return True
                except IndexError:
                    pass
        except IndexError:
            pass
        try:
            if self.gameBoard[y - 1][x + 1] == opponent:
                try:
                    if self.gameBoard[y + 1][x - 1] == player and self.gameBoard[y + 2][x - 2] == opponent:
                        return True
                except IndexError:
                    pass
        except IndexError:
            pass
        try:
            if self.gameBoard[y + 1][x + 1] == opponent:
                try:
                    if self.gameBoard[y - 1][x - 1] == player and self.gameBoard[y - 2][x - 2] == opponent:
                        return True
                except IndexError:
                    pass
        except IndexError:
            pass
        return False

    def checkMove(self):
        position = pygame.mouse.get_pos()
        x = ((position[0] // 10) * 10) // 32
        y = ((position[1] // 10) * 10) // 32
        if x < 0 or y < 0 or x > self.size or y > self.size:
            return
        if not self.gameBoard[y][x]:
            if self.isThree(x, y):
                return
            if self.isSelfCapture(x, y):
                return
            capture = self.checkCapture(x, y)
            for moveIndex in capture:
                self.gameBoard[moveIndex[1]][moveIndex[0]] = 0
                self.visualizer.insertTexture(moveIndex[1], moveIndex[0], 'Center')
            self.gameBoard[y][x] = self.playerDictionary[self.currentPlayer]
            self.visualizer.insertTexture(y, x, self.currentPlayer)
            self.currentPlayer = not self.currentPlayer
            self.visualizer.expose(self.size)

    def mainLoop(self):
        while not self.done:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.done = True
                if event.type == pygame.MOUSEBUTTONDOWN:
                    self.checkMove()
            pygame.display.flip()

game = Game(25)
game.mainLoop()
