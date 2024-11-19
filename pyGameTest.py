# Example file showing a circle moving on screen
import pygame

#Test Push To Github

# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
dt = 0

player_pos = pygame.Vector2((screen.get_width() / 2) - 200, screen.get_height() / 2)

# Set font
font = pygame.font.Font(None, 36)

# Render text
text = font.render("", True, (255, 255, 255))
mousePointText = font.render("",True, (255, 255, 255))

# Get text rectangle
text_rect = text.get_rect()
mousePointText_rect = mousePointText.get_rect()

# Center text on screen
text_rect.center = (screen.get_width() / 2.5, (screen.get_height() / 2) - 300)
mousePointText_rect.center = (screen.get_width() / 2.5, (screen.get_height() / 2) - 250)

collide = True

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("purple")

    rect = pygame.Rect(*screen.get_rect().center, 0, 0).inflate(100, 100)
    print(rect)
    pygame.draw.rect(screen, "blue", rect)

    circ = pygame.Rect(*screen.get_rect().center, 0, 0).inflate(100, 100)
    if collide:
        color = "green"
    else:
        color = "red"
    pygame.draw.circle(screen, color, player_pos, circ.w / 2)

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        player_pos.y -= 300 * dt
    if keys[pygame.K_s]:
        player_pos.y += 300 * dt
    if keys[pygame.K_a]:
        player_pos.x -= 300 * dt
    if keys[pygame.K_d]:
        player_pos.x += 300 * dt
    circ.update(player_pos.x, player_pos.y, circ.w, circ.h)
    print(circ.x, circ.y)

    collide = rect.colliderect(circ)
    print(collide)

    point = pygame.mouse.get_pos()

    text = font.render("(" + str(int(player_pos.x)) + ", " + str(int(player_pos.y)) + ")", True, (255, 255, 255))
    mousePointText = font.render(str(point), True, (255, 255, 255))

    # Blit the text onto the screen
    screen.blit(text, text_rect)
    screen.blit(mousePointText, mousePointText_rect)

    # flip() the display to put your work on screen
    pygame.display.flip()

    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    dt = clock.tick(60) / 1000

pygame.quit()