import pygame, random

pygame.init()
WIDTH = 640
HEIGHT = 480
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Wandlight")
clock = pygame.time.Clock()

# ---------- THE ENCHANTMENT PANEL (your customizations live here) ----------
SPARK_COLORS = [(240, 180, 41), (250, 245, 235), (196, 120, 255)]
SPARK_COUNT = 40
RISE_SPEED = 2

WAND_TIP_X = WIDTH // 2
WAND_TIP_Y = 400
SKY = (45, 27, 78)
# ---------------------------------------------------------------------------

# Parallel lists: spark number i is xs[i], ys[i], speeds[i], sizes[i], colors[i]
xs = []
ys = []
speeds = []
sizes = []
colors = []

for i in range(SPARK_COUNT):
    xs.append(WAND_TIP_X + random.randint(-6, 6))
    ys.append(WAND_TIP_Y + random.randint(0, 30))
    speeds.append(RISE_SPEED + random.randint(0, 2))
    sizes.append(random.randint(2, 5))
    colors.append(random.choice(SPARK_COLORS))

def draw_wand(surface):
    pygame.draw.line(surface, (240, 180, 41),
                     (WAND_TIP_X + 60, HEIGHT - 20),
                     (WAND_TIP_X, WAND_TIP_Y), 6)
    pygame.draw.circle(surface, (250, 245, 235),
                       (WAND_TIP_X, WAND_TIP_Y), 5)

frame = 0
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(SKY)
    draw_wand(screen)

    for i in range(SPARK_COUNT):
        ys[i] = ys[i] - speeds[i]              # rising: y gets SMALLER
        xs[i] = xs[i] + random.randint(-1, 1)  # the wobble
        if ys[i] < 0:                          # past the top: respawn at the tip
            xs[i] = WAND_TIP_X + random.randint(-6, 6)
            ys[i] = WAND_TIP_Y
        pygame.draw.circle(screen, colors[i], (xs[i], ys[i]), sizes[i])

    pygame.display.flip()
    frame = frame + 1            # counts the casting; timed gates read it
    clock.tick(60)

pygame.quit()
