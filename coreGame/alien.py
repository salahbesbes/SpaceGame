import pygame
from random import randint
from time import sleep, time
import threading
import asyncio
from coreGame.objectBase import SpaceObject
from coreGame.directionBase import Direction as Dr
from coreGame.gameStatus import Status, ObS
from coreGame.GameInstance import Gi

class Alien(SpaceObject):
    def __init__(self, game, img, size):
        super().__init__(game, img, size)
        self.class_name = Gi.ALIEN
        #  generate the player position from the size of the image
        x, y = self.generate_new_position()
        self.update_xy(x, y)
        self.direction = Dr.RIGHT
        self.speed = 0.1
        # creating a thread => target is autoFire and flag daemon is set to True
        # because we want the thread to die just after the frame closes
        self.thread = threading.Thread(target=self.auto_fire_bullet, daemon=True)
        if self.thread:
            self.thread.start()
        self.game_env.list_object.append(self)

    def generate_new_position(self):
        x = randint(0, self.limit_x)
        y = randint(0, int(self.limit_y / 7))
        return x, y

    def move(self):
        # automatically move to the right first then if it reaches the limits change direction
        limitX = self.limit_x
        if self.direction == Dr.RIGHT:
            if self.x + self.speed < limitX:
                self.x += self.speed
            else:
                # self.8y += 64
                self.direction = Dr.LEFT

        elif self.direction == Dr.LEFT:
            if self.x - self.speed > 0:
                self.x -= self.speed
            else:
                # self.y += 64
                self.direction = Dr.RIGHT

        elif self.direction == Dr.UP:
            if self.y - self.speed > 0:
                self.y -= self.speed

        elif self.direction == Dr.DOWN:
            if self.y + self.speed < limitY - 64:
                self.y += self.speed

    def update(self):
        self.move()

    def auto_fire_bullet(self):
        """
        this function uses sleep() since it will execute in each frame,
        it will cause delay of each frame to slow down, so we have to run it
        separately from the main loop (frame) by creating a thread
        it will start executing immediately when the instance is created
        """
        sleep(2)
        while self.status == ObS.ALIVE:
            from coreGame.bullet import Bullet
            Bullet(self.game_env, "bullet.png", 32, self, Dr.DOWN)
            sleep(2)
