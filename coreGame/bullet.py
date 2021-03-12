import pygame
import threading
from coreGame.objectBase import SpaceObject
from coreGame.directionBase import Direction as Dr
from coreGame.gameStatus import Status, ObS
from coreGame.GameInstance import Gi
from coreGame.alien import Alien
class Bullet(SpaceObject):
    def __init__(self, game, img, size, obj_fired, direction=Dr.UP):
        """

        :param game(GameBase): environment of the game (all game attribute shared by all instance)
        :param img(str): path of the image
        :param size(int): bites of the image
        :param obj_fired(SpaceObject): obj that fire the bullet
        :param direction(Direction): direction of the bullet, related to the rotation of img
        """
        super().__init__(game, img, size, direction=direction)
        self.obj_fired = obj_fired
        self.class_name = Gi.BULLET
        self.shooter = obj_fired.class_name

        if self.shooter == Gi.PLAYER:
            # self.x = obj_fired.x + obj_fired.width / 2
            # self.y = obj_fired.y - obj_fired.height - 1
            self.x = obj_fired.x + 16
            self.y = obj_fired.y + 20
        elif self.shooter == Gi.ALIEN:
            # self.x = obj_fired.x + obj_fired.width / 2
            # self.y = obj_fired.y + obj_fired.height + 1
            self.x = obj_fired.x + 16
            self.y = obj_fired.y + obj_fired.height + 1
        self.speed = 2
        self.game_env.list_object.append(self)

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        self.__x = value

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        self.__y = value

    @staticmethod
    def check_coordinate(value, edge):
        if type(value) is not int and type(value) is not float:
            raise TypeError("X and Y must be positive integers")
        if value < 0 or value > edge:
            pass

    def move(self):
        class_name = self.get_class_name(self.obj_fired)
        if class_name == Gi.PLAYER:
            self.y -= self.speed
        if class_name == Gi.ALIEN:
            self.y += self.speed
        """
        if self.obj_fired.__class__.__name__ == "Player":
            self.y -= self.speed
            print("player")
        elif self.obj_fired.__class__.__name__ == "Alien":
            print("alien")
            self.y += self.speed
        """
        # if the bullet reaches the top bord it kills it self
        if self.y < 0 or self.y > self.limit_y:
            self.kill_self()

    def update(self):
        self.move()

    def on_collision(self, obj_hit):
        if obj_hit.class_name == Gi.ALIEN and self.shooter == Gi.PLAYER:
            self.game_env.player_score += 1
            old_speed = obj_hit.speed
            # to stop the while loop of the thread (quit the thread)
            obj_hit.status = ObS.DEAD
            obj_hit.kill_self()
            new_Alien = Alien(self.game_env, "alien.png", 64)
            new_Alien.speed = old_speed + 0.2
            self.kill_self()
            # last thing to do is kill bullet instance
        if obj_hit.class_name == Gi.PLAYER and self.shooter == Gi.ALIEN:
            obj_hit.kill_self()
            from coreGame.player import Player
            Player(self.game_env, "UFO.png", 64)  # append self in list_object
            self.game_env.player_score = 0
            self.kill_self()
