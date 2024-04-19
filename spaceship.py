import pgzrun
import random

WIDTH = 800
HEIGHT = 602

ship = Actor("player/spaceships/playership1_blue")
ship.x = 370
ship.y = 550

ship2 = Actor("player/spaceships/playership1_green")
ship2.x = 370
ship2.y = 550

gem = Actor("items/gemgreen")
gem.x = random.randint(20, 780)
gem.y = 0

score = 0
score2 = 0
game_over = False


def on_mouse_move(pos, rel, buttons):
    ship.x = pos[0]


def update():
    global score, score2, game_over

    if keyboard.left:
        ship.x = ship.x - 10
    if keyboard.right:
        ship.x = ship.x + 10

    if keyboard.a:
        ship2.x = ship2.x - 10
    if keyboard.d:
        ship2.x = ship2.x + 10

    gem.y = gem.y + 4 + score / 5
    if gem.y > 600:
        game_over = True

    if gem.colliderect(ship2) and gem.colliderect(ship):
        gem.x = random.randint(20, 780)
        gem.y = 0
        score2 = score2 + 1
        score = score + 1

    if gem.colliderect(ship):
        gem.x = random.randint(20, 780)
        gem.y = 0
        score = score + 1

    if gem.colliderect(ship2):
        gem.x = random.randint(20, 780)
        gem.y = 0
        score2 = score2 + 1




def draw():
    global game_over, score, score2
    screen.fill((80, 0, 70))
    if game_over:
        screen.draw.text("Game Over", (360, 300), color=(255, 255, 255), fontsize=60)
        screen.draw.text(
            "Score: " + str(score + score2), (360, 350), color=(255, 255, 255), fontsize=60
        )
        if keyboard.r:
            score = 0
            score2 = 0
            gem.y = 0
            game_over = False
    else:
        gem.draw()
        ship.draw()
        ship2.draw()
        screen.draw.text(
            "Score Blue: " + str(score) + "\n" + "Score Green: " + str(score2), (15, 10), color=(150, 150, 255), fontsize=30
        )


pgzrun.go()  # Must be last line
