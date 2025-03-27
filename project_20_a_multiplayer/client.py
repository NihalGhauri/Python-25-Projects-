
import pygame
from network import Network

width = 500
height = 500

win = pygame.display.set_mode((width, height))
pygame.display.set_caption("Client")

class Player:
    def __init__(self, x, y, width, height, color):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.rect = (x, y, width, height)
        self.vel = 3

    def draw(self, win):
        pygame.draw.rect(win, self.color, self.rect)

    def move(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT]:
            self.x -= self.vel
        if keys[pygame.K_RIGHT]:
            self.x += self.vel
        if keys[pygame.K_UP]:
            self.y -= self.vel
        if keys[pygame.K_DOWN]:
            self.y += self.vel

        self.update()

    def update(self):
        self.rect = (self.x, self.y, self.width, self.height)


def read_pos(data):

    if data is None or not isinstance(data, str):
        return 0, 0  
    try:
        x, y = map(int, data.split(","))
        return x, y
    except ValueError:
        return 0, 0  


def make_pos(tup):
    #Convert position tuple to string 
    return f"{tup[0]},{tup[1]}"


def redraw_window(win, player, player2):
    win.fill((255, 255, 255))  
    player.draw(win)
    player2.draw(win)
    pygame.display.update()


def main():
    run = True
    n = Network()
    start_pos = read_pos(n.getPos())  # Read initial position from the server
    p = Player(start_pos[0], start_pos[1], 50, 50, (0, 255, 0))
    p2 = Player(0, 0, 50, 50, (255, 0, 0))
    clock = pygame.time.Clock()

    while run:
        clock.tick(60)

        try:
            # Send player position and get opponent's position
            p2_pos = read_pos(n.send(make_pos((p.x, p.y))))
            p2.x = p2_pos[0]
            p2.y = p2_pos[1]
            p2.update()
        except Exception as e:
            print(f"Error during network communication: {e}")
            run = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        p.move()
        redraw_window(win, p, p2)

    pygame.quit()


if __name__ == "__main__":
    main()












import pygame
from network import Network

width = 500
height = 500
win = pygame.display.set_mode((width, height))
pygame.display.set_caption("Client")

clientNumber = 0


class Player():
    def __init__(self, x, y, width, height, color):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.rect = (x,y,width,height)
        self.vel = 3

    def draw(self, win):
        pygame.draw.rect(win, self.color, self.rect)

    def move(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT]:
            self.x -= self.vel

        if keys[pygame.K_RIGHT]:
            self.x += self.vel

        if keys[pygame.K_UP]:
            self.y -= self.vel

        if keys[pygame.K_DOWN]:
            self.y += self.vel

        self.update()

    def update(self):
        self.rect = (self.x, self.y, self.width, self.height)


def read_pos(str):
    str = str.split(",")
    return int(str[0]), int(str[1])


def make_pos(tup):
    return str(tup[0]) + "," + str(tup[1])


def redrawWindow(win,player, player2):
    win.fill((255,255,255))
    player.draw(win)
    player2.draw(win)
    pygame.display.update()


def main():
    run = True
    n = Network()
    startPos = read_pos(n.getPos())
    p = Player(startPos[0],startPos[1],100,100,(0,255,0))
    p2 = Player(0,0,100,100,(255,0,0))
    clock = pygame.time.Clock()

    while run:
        clock.tick(60)
        p2Pos = read_pos(n.send(make_pos((p.x, p.y))))
        p2.x = p2Pos[0]
        p2.y = p2Pos[1]
        p2.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()

        p.move()
        redrawWindow(win, p, p2)

main()
