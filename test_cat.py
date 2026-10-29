import sys
import random
import pygame

pygame.init()

width, height = 2560, 1600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("FLY_IN 🐈")

clock = pygame.time.Clock()

background = pygame.image.load("assets/img/background.jpg").convert()
background = pygame.transform.scale(background, (width, height))

mouse = pygame.image.load("assets/img/mouse.jpg").convert_alpha()
mouse = pygame.transform.scale(mouse, (200, 200))
mouse_rect = mouse.get_rect(topleft=(0, 0))

image_files = [
    "assets/img/noodle.jpg",
    "assets/img/ramen.jpg",
    "assets/img/catM.png",
]

cats = []

for filename in image_files:
    image = pygame.image.load(filename).convert()
    image = pygame.transform.scale(image, (300, 300))

    rect = image.get_rect()
    rect.x = random.randint(0, width - rect.width)
    rect.y = random.randint(0, height - rect.height)

    speed = [
        random.choice([-15, 15]),
        random.choice([-15, 15]),
    ]

    cats.append({
        "image": image,
        "rect": rect,
        "speed": speed,
        "last_mouse_collision": False,
    })


running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.blit(background, (0, 0))

    # 1. Déplacer tous les chats
    for cat in cats:
        rect = cat["rect"]
        speed = cat["speed"]

        rect.x += speed[0]
        rect.y += speed[1]

        # Rebonds sur les bords
        if rect.left <= 0:
            rect.left = 0
            speed[0] = abs(speed[0])
        elif rect.right >= width:
            rect.right = width
            speed[0] = -abs(speed[0])

        if rect.top <= 0:
            rect.top = 0
            speed[1] = abs(speed[1])
        elif rect.bottom >= height:
            rect.bottom = height
            speed[1] = -abs(speed[1])

    # 2. Collisions entre les chats
    for i in range(len(cats)):
        for j in range(i + 1, len(cats)):
            cat1 = cats[i]
            cat2 = cats[j]

            rect1 = cat1["rect"]
            rect2 = cat2["rect"]

            if rect1.colliderect(rect2):
                # Déterminer l'axe du contact
                overlap_x = min(rect1.right, rect2.right) - max(
                    rect1.left, rect2.left
                )
                overlap_y = min(rect1.bottom, rect2.bottom) - max(
                    rect1.top, rect2.top
                )

                if overlap_x < overlap_y:
                    cat1["speed"][0] *= -1
                    cat2["speed"][0] *= -1

                    # Écarter légèrement les chats
                    if rect1.centerx < rect2.centerx:
                        rect1.right = rect2.left
                    else:
                        rect1.left = rect2.right
                else:
                    cat1["speed"][1] *= -1
                    cat2["speed"][1] *= -1

                    if rect1.centery < rect2.centery:
                        rect1.bottom = rect2.top
                    else:
                        rect1.top = rect2.bottom

    # 3. Collision avec la souris
    for cat in cats:
        touching = cat["rect"].colliderect(mouse_rect)

        if touching and not cat["last_mouse_collision"]:
            print("MIAM !")

        cat["last_mouse_collision"] = touching

    # 4. Dessiner les chats et la souris
    for cat in cats:
        screen.blit(cat["image"], cat["rect"])

    mouse_rect.center = pygame.mouse.get_pos()
    screen.blit(mouse, mouse_rect)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()

