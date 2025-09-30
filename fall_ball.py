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


