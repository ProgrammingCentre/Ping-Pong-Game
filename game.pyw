import pygame

HEIGHT, WIDTH = 600, 900

game = pygame.init()
gameWindow = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Ping Pong With Atul")
pygame.display.update()

x_speed = 5
y_speed = 5

ball = pygame.image.load("ball.png")


rect1 = pygame.Rect(300, 250, 50, 50)
rect2 = pygame.Rect(300, 20, 100, 40)
rect3 = pygame.Rect(300, 520, 100, 40)


def new():
    global x_speed, y_speed
    pygame.draw.rect(gameWindow, (255, 0, 0), rect1)
    pygame.draw.rect(gameWindow, (0, 0, 255), rect2)
    pygame.draw.rect(gameWindow, (0, 255, 0), rect3)
    rect1.x += x_speed
    rect1.y += y_speed
    if rect1.right >= WIDTH or rect1.left <= 0:
        x_speed *= -1
    if rect1.bottom >= HEIGHT or rect1.top <= 0:
        y_speed *= -1
    if rect2.right >= HEIGHT or rect2.left <= 0:
        x_speed *= -1
    if rect1.colliderect(rect2):
        if rect1.right >= 150 or rect1.left <= 0:
            x_speed *= -1

        if rect1.bottom >= 100 or rect1.top <= 0:
            y_speed *= -1
    if rect1.colliderect(rect3):
        if rect1.right >= 150 or rect1.left <= 0:
            x_speed *= -1

        if rect1.bottom >= 520 or rect1.top <= 0:
            y_speed *= -1


clock = pygame.time.Clock()


def draw():
    gameWindow.fill((0, 0, 0))


run = True
while run:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        keys = pygame.key.get_pressed()
        if keys[pygame.K_j]:
            rect2.x -= 40
        if keys[pygame.K_l]:
            rect2.x += 40
        if keys[pygame.K_d]:
            rect3.x += 40
        if keys[pygame.K_a]:
            rect3.x -= 40

    if rect1.bottom >= HEIGHT:
        pygame.font.init()
        myFont = pygame.font.SysFont("System", 100)
        txt = myFont.render("Blue won!", False, (0, 0, 0))
        gameWindow.fill((255, 255, 255))
        gameWindow.blit(txt, (300, 300))
    elif rect1.top == 0:
        pygame.font.init()
        myFont = pygame.font.SysFont("System", 100)
        txt = myFont.render("Green Won!", False, (0, 0, 0))
        gameWindow.fill((255, 255, 255))
        gameWindow.blit(txt, (300, 300))
    else:
        new()
    pygame.display.update()
    draw()

pygame.quit()
