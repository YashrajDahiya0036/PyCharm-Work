import turtle
import random

WIDTH, HEIGHT = 500, 500
COLORS = ["Red", "Green", "Blue", "Yellow", "Orange", "Purple", "Pink", "Cyan", "Magenta", "Brown"]
# SPEEDS = [i for i in range(1, 11)]


def get_number_of_racers():
    while True:
        racers = input("Enter the numbers of racers(2 - 10): ")
        if racers.isdigit():
            racers = int(racers)
        else:
            print("Please enter a integer.")
            continue
        if 10 >= racers >= 2:
            return racers
        else:
            print("Enter between 2 and 10.")


def create_racers():
    racers = get_number_of_racers()
    list_of_racers = []
    list_of_colors = []
    # screen_dime = start_screen()
    # list_of_speeds = []
    # width = screen_dime[0]
    # global height
    # height = screen_dime[1]
    # start_pos = int((width//racers+1)-width)
    # remainder = width//racers+1
    spacing_x = WIDTH//(racers+1)

    """
    random.shuffle(COLORS)
    list_of_colors = COLORS[:racers]
    random.shuffle(SPEEDS)
    list_of_speeds = SPEEDS[:racers]
    """
    for i in range(0, racers):
        random_color = random.choice(COLORS)
        list_of_colors.append(random_color)
        COLORS.remove(random_color)
    # for i in range(0, racers):
    #     random_speed = random.choice(SPEEDS)
    #     list_of_speeds.append(random_speed)
    #     SPEEDS.remove(random_speed)
    for y, color in enumerate(list_of_colors):
        i = turtle.Turtle()
        i.shape("turtle")
        i.color(color)
        i.left(90)
        i.penup()
        i.setpos(-WIDTH//2 + (y + 1) * spacing_x, -(HEIGHT//2)+30)
        i.pendown()
        list_of_racers.append(i)
        # start_pos += remainder
    return list_of_racers


def race():
    racers = create_racers()

    while True:
        for i in racers:
            distance = random.randrange(1, 10)
            i.forward(distance)
            x, y = i.pos()
            # print(x, y)
            # print(int(HEIGHT - 10))
            # print(int(y))
            if int(y) >= HEIGHT//2 - 30:
                return i.color()[0]

# trial = turtle.Turtle()
# trial.forward(400)
# trial.left(90)
# trial.forward(250)
# trial.left(90)
# trial.forward(500)
# trial.left(90)
# trial.forward(500)
# trial.left(90)
# trial.forward(500)
# trial.left(90)
# trial.forward(250)


def start_screen():
    screen = turtle.Screen()
    screen.setup(WIDTH, HEIGHT)
    screen.screensize(WIDTH, HEIGHT, "black")
    screen.title("Racing!")
    return screen.screensize()


start_screen()
winner = race()

print("The winner of the race is", winner, ".")

# screen.mainloop()
# winner = race()
# print("The winner of the race is "+ winner)

# time.sleep(5)

turtle.mainloop()
