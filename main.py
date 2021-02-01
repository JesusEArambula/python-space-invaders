import turtle, os, math, random, platform

wn = turtle.Screen()
wn.bgcolor('black')
wn.title("Space Invaders")

# Border Turtle
border_pen = turtle.Turtle()
border_pen.speed(0)
border_pen.color('white')
border_pen.penup()
border_pen.setposition(-300, -300)
border_pen.pendown()
border_pen.pensize(3)
for side in range(4):
    border_pen.fd(600)
    border_pen.lt(90)
border_pen.hideturtle()

# Player Turtle
player = turtle.Turtle()
player.color('blue')
player.shape('triangle')
player.penup()
player.speed(0)
player.setposition(0, -250)
player.setheading(90)

# Player speed
player_speed = 15

enemy = turtle.Turtle()
enemy.color('red')
enemy.shape('circle')
enemy.penup()
enemy.speed(0)
enemy.setposition(-200, -250)

enemy_speed = 2

# Create player's bullet
bullet = turtle.Turtle()
bullet.color('yellow')
bullet.shape('triangle')
bullet.penup()
bullet.speed(0)
bullet.setheading(90)
bullet.shapesize(.5, .5)
bullet.hideturtle()

bullet_speed = 20

# Define state of bullet
# ready - ready to fire
# fire - bullet is firing
bullet_state = "ready"

# Move left and right
def move_left():
    x = player.xcor()
    x -= player_speed
    if x < -280:
        x = -280
    player.setx(x)
def move_right():
    x = player.xcor()
    x += player_speed
    if x > 280:
        x = 280
    player.setx(x)
def fire_bullet():
    global bullet_state
    if bullet_state == "ready":
        bullet_state = "fire"
        # Move bullet above player
        y = player.ycor() + 10
        x = player.xcor()
        bullet .setposition(x, y)
        bullet.showturtle()
def is_collision(obj1, obj2):
    distance = math.sqrt(math.pow(obj1.xcor() - obj2.xcor(), 2) + math.pow(obj1.ycor() - obj2.ycor(), 2))
    if distance < 15:
        return True
    else:
        return False



# Keyboard bindings
turtle.listen()
turtle.onkey(move_left, "Left")
turtle.onkey(move_right, "Right")
turtle.onkey(fire_bullet, "space")

# Main Game Loop
while True:
    # Move enemy
    x = enemy.xcor()
    x += enemy_speed
    enemy.setx(x)

    # Move enemy back and down
    if enemy.xcor() > 280:
        enemy_speed *= -1
        y = enemy.ycor()
        y -= 20
        enemy.sety(y)
    if enemy.xcor() < -280:
        enemy_speed *= -1
        y = enemy.ycor()
        y -= 20
        enemy.sety(y)

    # Move bullet
    if bullet_state == "fire":
        y = bullet.ycor()
        y += bullet_speed
        bullet.sety(y)

    # Check to see if bullet has gone to the top
    if bullet.ycor() > 275:
        bullet.hideturtle()
        bullet_state = "ready"

    # Check for collision between bullet and enemy
    if is_collision(bullet, enemy):
        # Reset bullet
        bullet.hideturtle()
        bullet_state = "ready"
        bullet.setposition(0, -400)
        # Reset enemy
        enemy.setposition(-200, 250)

    if is_collision(player, enemy):
        player.hideturtle()
        enemy.hideturtle()
        print("Game Over")
        break
