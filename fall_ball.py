from pico2d import *
import random

KPU_WIDTH, KPU_HEIGHT = 1000, 600

class grass:
    def __init__(self):
        self.image = load_image('grass.png')

    def draw(self):
        self.image.draw(KPU_WIDTH // 2, 30)

    def update(self):
        pass


class MinBall:
    def __init__(self):
        self.image = load_image('ball21x21.png')
        self.x, self.y = random.randint(0, 1000), 599
        self.speed = random.randint(1, 10)

    def draw(self):
        self.image.draw(self.x, self.y)

    def update(self):
        self.x -= self.speed
        pass

class MaxBall:
    def __init__(self):
        self.image = load_image('ball41x41.png')
        self.x, self.y = random.randint(0, 1000), 599
        self.speed = random.randint(1, 10)

    def draw(self):
        self.image.draw(self.x, self.y)

    def update(self):
        self.x -= self.speed
        pass


def handle_events():
    global running
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False

    pass


def reset_world():
    global running, world
    running = True
    minnum = random.randint(0, 20)
    world = []

    maxballs = [MaxBall() for _ in range(20 - minnum)]
    world += maxballs
    minballs = [MinBall() for _ in range(minnum)]
    world += minballs


def update_world():
    pass


def render_world():
    clear_canvas()

    update_canvas()


open_canvas()

reset_world()

while running:
    handle_events()
    update_world()
    render_world()
    delay(0.05)

close_canvas()
