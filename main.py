import math
import random
import turtle
import playsound

wn = turtle.Screen()
wn.bgcolor('black')
wn.title('Space Invaders')
wn.bgpic('space_invaders_background.gif')

# Register shapes
wn.register_shape('spaceship.gif')
wn.register_shape('invader.gif')
wn.register_shape('bullet.gif')

# Border Turtle
border_pen = turtle.Turtle()
border_pen.speed(0)
border_pen.color('white')
border_pen.penup()
border_pen.setposition(-300, -300)
border_pen.pendown()
border_pen.pensize(3)
# Draw border
for side in range(4):
    border_pen.fd(600)
    border_pen.lt(90)
border_pen.hideturtle()

# Set score
score = 0

score_pen = turtle.Turtle()
score_pen.speed(0)
score_pen.color('white')
score_pen.penup()
score_pen.setposition(-290, 280)
score_string = 'Score: {}'.format(score)
score_pen.write(score_string, False, align='left', font=('Arial', 10, 'normal'))
score_pen.hideturtle()


# Player Turtle
player = turtle.Turtle()
player.shape('spaceship.gif')
player.penup()
player.speed(0)
player.setposition(0, -250)
player.setheading(90)
player.speed = 0

# Number of enemies
num_of_enemies = 5
# List of enemies
enemies = []

# Add enemies to list
for i in range(num_of_enemies):
    enemies.append(turtle.Turtle())

# Make multiple enemies
for enemy in enemies:
    enemy.shape('invader.gif')
    enemy.penup()
    enemy.speed(0)
    x = random.randint(-200, 200)
    y = random.randint(100, 250)
    enemy.setposition(x, y)

enemy_speed = 2


# Create player's bullet
bullet = turtle.Turtle()
bullet.shape('bullet.gif')
bullet.penup()
bullet.speed(0)
bullet.setheading(90)
bullet.shapesize(.5, .5)
bullet.hideturtle()

bullet_speed = 40

# Define state of bullet
# ready - ready to fire
# fire - bullet is firing
bullet_state = 'ready'

# Move left and right
def move_left():
    player.speed = -15

def move_right():
    player.speed = 15

def move_player():
    x = player.xcor()
    x += player.speed
    if x < -280:
        x = -280
    if x > 280:
        x = 280
    player.setx(x)

def fire_bullet():
    global bullet_state
    if bullet_state == 'ready':
        bullet_state = 'fire'
        # Move bullet above player
        y = player.ycor() + 10
        x = player.xcor()
        bullet .setposition(x, y)
        bullet.showturtle()

def is_collision(obj1, obj2):
    distance = math.sqrt(math.pow(obj1.xcor() - obj2.xcor(), 2) + math.pow(obj1.ycor() - obj2.ycor(), 2))
    if distance < 25:
        return True
    else:
        return False


# Keyboard bindings
wn.listen()
wn.onkeypress(move_left, "Left")
wn.onkeypress(move_right, "Right")
wn.onkeypress(fire_bullet, "space")

# Main Game Loop
while True:

    move_player()

    for enemy in enemies:
        # Move enemy
        x = enemy.xcor()
        x += enemy_speed
        enemy.setx(x)

        # Move enemy back and down
        if enemy.xcor() > 280:
            for e in enemies:
                y = e.ycor()
                y -= 20
                e.sety(y)
            enemy_speed *= -1

        if enemy.xcor() < -280:
            for e in enemies:
                y = e.ycor()
                y -= 20
                e.sety(y)
            enemy_speed *= -1


        # Check for collision between bullet and enemy
        if is_collision(bullet, enemy):
            # Reset bullet
            bullet.hideturtle()
            bullet_state = 'ready'
            bullet.setposition(0, -400)
            # Reset enemy
            x = random.randint(-200, 200)
            y = random.randint(100, 250)
            enemy.setposition(x, y)
            # Update score
            score += 10
            score_string = 'Score: {}'.format(score)
            score_pen.clear()
            score_pen.write(score_string, False, align='left', font=('Arial', 10, 'normal'))

        # Check for collision between player and enemy
        if is_collision(player, enemy):
            player.hideturtle()
            enemy.hideturtle()
            print('Game Over')
            break


    # Move bullet
    if bullet_state == 'fire':
        y = bullet.ycor()
        y += bullet_speed
        bullet.sety(y)

    # Check to see if bullet has gone to the top
    if bullet.ycor() > 275:
        bullet.hideturtle()
        bullet_state = 'ready'

