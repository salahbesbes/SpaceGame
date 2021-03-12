import pygame
from coreGame.objectBase import SpaceObject
from coreGame.directionBase import Direction as Dr
from coreGame.gameStatus import Status, ObS
from coreGame.bullet import Bullet
from coreGame.GameInstance import Gi


class Player(SpaceObject):
    def __init__(self, game, img, size):
        super().__init__(game, img, size)
        self.class_name = Gi.PLAYER
        x, y = self.initial_position()
        self.update_xy(x, y)
        self.game_env.list_object.append(self)

    def initial_position(self):
        x = self.game_env.sc_width / 2 - self.image_size
        y = self.game_env.sc_height - self.game_env.sc_height / 7
        return x, y

    def render_on_screen(self, screen: pygame.Surface):
        screen.blit(self.img, (self.x, self.y))

    def fire_bullet(self):
        Bullet(self.game_env, "bullet.png", 32, self)

    def move(self, direction):
        limitX = self.limit_x
        limitY = self.limit_y
        if direction == Dr.LEFT:
            if self.x - self.speed > 0:
                self.x -= self.speed
        elif direction == Dr.RIGHT:
            if self.x + self.speed < limitX:
                self.x += self.speed
        elif direction == Dr.UP:
            if self.y - self.speed > 0:
                self.y -= self.speed
        elif direction == Dr.DOWN:
            if self.y + self.speed < limitY:
                self.y += self.speed

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.move(Dr.LEFT)
        if keys[pygame.K_RIGHT]:
            self.move(Dr.RIGHT)
        if keys[pygame.K_UP]:
            self.move(Dr.UP)
        if keys[pygame.K_DOWN]:
            self.move(Dr.DOWN)
