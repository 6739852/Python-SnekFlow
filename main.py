from tkinter import *
import random

# ----------------------------------const_varibales
GAME_WIDTH = 700
GAME_HIGHT = 700
SPEED = 50
SPACE_SIZE = 50
BODY_PARTS = 3
SNAKE_COLOR = "#00FF00"
FOOD_COLOR = "#FF0000"
BACKGROUND_COLOR = "#000000"


# -----------------------------------------classes
class Snake:

    """
    class of the snake
    """

    def __init__(self):

        self.body_size = BODY_PARTS
        self.coordinates = []
        self.squares = []

        for i in range(0, BODY_PARTS):
            self.coordinates.append([0, 0])

        for x, y in self.coordinates:
            square = canvas.create_rectangle(x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill=SNAKE_COLOR, tag="snake")
            self.squares.append(square)


class Food:

    """
    class of the food
    """

    def __init__(self):
        x = random.randint(0, (GAME_WIDTH / SPACE_SIZE) - 1) * SPACE_SIZE
        y = random.randint(0, (GAME_HIGHT / SPACE_SIZE) - 1) * SPACE_SIZE

        self.coordonates = [x, y]

        canvas.create_oval(x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill=FOOD_COLOR, tag="food")


# -----------------------------------------functions
def next_turn(snake, food):

    """
    The function moves to the next stage in the game

    :param snake: Accepting the current snake
    :param food: Accepting the current food
    :return: none
    """

    x, y = snake.coordinates[0]

    if direction == "up":
        y -= SPACE_SIZE

    elif direction == "down":
        y += SPACE_SIZE

    elif direction == "left":
        x -= SPACE_SIZE

    elif direction == "right":
        x += SPACE_SIZE

    snake.coordinates.insert(0, (x, y))

    square = canvas.create_rectangle(x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill=SNAKE_COLOR)

    snake.squares.insert(0, square)

    if x==food.coordonates[0] and y==food.coordonates[1]:

        global score
        score += 1
        label.config(text="Score: {}".format(score))
        canvas.delete("food")
        food=Food()

    else:

        del snake.coordinates[-1]
        canvas.delete(snake.squares[-1])
        del snake.squares[-1]

    if check_collisions(snake):
        game_over()
    else:
        window.after(SPEED, next_turn, snake, food)


def change_direction(new_direction):

    """
    The function moves the snake to a new direction that accepted

    :param new_direction: Accepting the new direction to move the snake
    :return: none
    """

    global direction

    if new_direction == 'left':
        if direction != 'right':
            direction = new_direction
    elif new_direction == 'right':
        if direction != 'left':
            direction = new_direction
    elif new_direction == 'up':
        if direction != 'down':
            direction = new_direction
    elif new_direction == 'down':
        if direction != 'up':
            direction = new_direction



def check_collisions(snake):

    """
    The function checking if there are collisions

    :param snake: Accepting the snake in its status
    :return: If there is a collision the function return true and false otherwise
    """

    x,y= snake.coordinates[0]

    if x<0 or x>= GAME_WIDTH:
        return  True

    elif y < 0 or y >= GAME_HIGHT:
        return True

    for body_part in snake.coordinates[1:]:
        if x== body_part[0] and y== body_part[1]:
            return  True

    return  False


def game_over():

    """
    The function is responsible for ending the game and disappearing the board

    :return: none
    """
    canvas.delete(ALL)
    canvas.create_text(canvas.winfo_width()/2, canvas.winfo_height()/2,font=('consolas',70)
                       ,text="GAME OVER", fill="red",tag="gameover" )


# ----------------------------------------------code
window = Tk()
window.title("Snake game")
window.resizable(False, False)

score = 0
direction = 'down'

label = Label(window, text="Score:{}".format(score), font=('consolas', 40))
label.pack()

canvas = Canvas(window, bg=BACKGROUND_COLOR, height=GAME_HIGHT, width=GAME_WIDTH)
canvas.pack()

window.update()

window_width = window.winfo_width()
window_height = window.winfo_height()
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

x = int((screen_width / 2) - (window_width / 2))
y = int((screen_height / 2) - (window_height / 2))

window.geometry(f"{window_width}x{window_height}+{x}+{y}")

window.bind('<Left>', lambda event: change_direction('left'))
window.bind('<Right>', lambda event: change_direction('right'))
window.bind('<Up>', lambda event: change_direction('up'))
window.bind('<Down>', lambda event: change_direction('down'))

snake = Snake()
food = Food()

next_turn(snake, food)

window.mainloop()
