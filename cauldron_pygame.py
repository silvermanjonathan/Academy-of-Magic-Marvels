import pygame, random

pygame.init()
WIDTH = 640
HEIGHT = 480
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("The Cauldron Game")
clock = pygame.time.Clock()

# ---------- THE BREWMASTER'S PANEL (your customizations live here) ----------
INGREDIENTS = [(240, 180, 41), (196, 120, 255), (120, 200, 255),
               (4, 120, 87), (250, 245, 235), (194, 65, 12)]
NAMES = ["gold", "lilac", "sky", "green", "parchment", "ember"]
POTIONS = ["Moonlight Draught", "Emberheart Tonic", "Gloamlight Elixir"]
NEED_A = [2, 5, 1]        # each potion needs flask NEED_A[p]...
NEED_B = [0, 3, 4]        # ...and flask NEED_B[p], in either order
GAME_FRAMES = 1800        # 1800 frames at 60 per second = a 30-second shift bell
SKY = (45, 27, 78)
# ----------------------------------------------------------------------------

def draw_shelf(surface):
    for i in range(6):
        pygame.draw.circle(surface, INGREDIENTS[i], (70 + i * 100, 440), 24)

def draw_cauldron(surface):
    pygame.draw.rect(surface, (20, 12, 40), (250, 300, 140, 60))
    pygame.draw.circle(surface, (20, 12, 40), (320, 300), 72, 8)

score = 0
target = random.randint(0, 2)
thrown = []
flash = 0
flash_color = SKY
time_bar = 600
frame = 0
running = True

print("=== THE CAULDRON GAME ===")
print("Orders arrive at the top of the window: two colors, one potion.")
print("Keys 1 to 6 throw the shelf flasks, left to right.")
print("Wrong flask? The brew spoils and the order starts over.")
print(f"First order: {POTIONS[target]}, {NAMES[NEED_A[target]]} + {NAMES[NEED_B[target]]}!")

while running:
    choice = -1
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN and event.key == pygame.K_1:
            choice = 0
        if event.type == pygame.KEYDOWN and event.key == pygame.K_2:
            choice = 1
        if event.type == pygame.KEYDOWN and event.key == pygame.K_3:
            choice = 2
        if event.type == pygame.KEYDOWN and event.key == pygame.K_4:
            choice = 3
        if event.type == pygame.KEYDOWN and event.key == pygame.K_5:
            choice = 4
        if event.type == pygame.KEYDOWN and event.key == pygame.K_6:
            choice = 5

    if frame < GAME_FRAMES and choice > -1 and choice != NEED_A[target] and choice != NEED_B[target]:
        print(f"The {NAMES[choice]} flask doesn't belong! The brew spoils...")
        thrown = []
        flash = 20
        flash_color = (90, 90, 100)
    if frame < GAME_FRAMES and choice > -1 and (choice == NEED_A[target] or choice == NEED_B[target]) and choice not in thrown:
        thrown.append(choice)

    if NEED_A[target] in thrown and NEED_B[target] in thrown:
        score = score + 1
        flash = 30
        flash_color = INGREDIENTS[NEED_A[target]]
        print(f"{POTIONS[target]} brewed! Score: {score}")
        thrown = []
        target = random.randint(0, 2)
        print(f"New order: {POTIONS[target]}, {NAMES[NEED_A[target]]} + {NAMES[NEED_B[target]]}!")

    if flash > 0:
        screen.fill(flash_color)
    else:
        screen.fill(SKY)
    if flash > 0:
        flash = flash - 1

    draw_cauldron(screen)
    draw_shelf(screen)
    pygame.draw.circle(screen, INGREDIENTS[NEED_A[target]], (280, 60), 22)
    pygame.draw.circle(screen, INGREDIENTS[NEED_B[target]], (360, 60), 22)
    for i in range(len(thrown)):
        pygame.draw.circle(screen, INGREDIENTS[thrown[i]], (300 + i * 40, 300), 14)
    for s in range(score):
        pygame.draw.circle(screen, (240, 180, 41), (20 + s * 24, 20), 8)
    if frame % 3 == 0 and time_bar > 0:
        time_bar = time_bar - 1
    pygame.draw.rect(screen, (240, 180, 41), (20, 468, time_bar, 6))

    pygame.display.flip()
    frame = frame + 1
    if frame == GAME_FRAMES:
        print(f"The bell rings! Final score: {score} potions. Close the window when you're ready.")
    clock.tick(60)

pygame.quit()
print(f"Kitchen closed. {score} potions this shift.")
