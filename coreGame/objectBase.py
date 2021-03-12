import pygame
from random import randint
from math import sqrt, pow
from coreGame.GameInstance import Gi
from coreGame.gameStatus import ObS
from coreGame.directionBase import Direction as Dr


class SpaceObject:
    def __init__(self, game, img, size, x=0, y=0, direction=Dr.UP):
        self.direction = direction
        self.game_env = game
        self.image_size = size
        self.x = x
        self.y = y
        self.img = img
        self.speed = 1
        self.limit_x = self.game_env.sc_width - self.image_size
        self.limit_y = self.game_env.sc_height - self.image_size
        self.width = size
        self.height = size
        self.health = 1
        self.class_name = ""
        self.status = ObS.ALIVE

    @staticmethod
    def check_coordinate(value, edge):
        if type(value) is not int and type(value) is not float:
            raise TypeError("X and Y must be positive integers")
        if value < 0 or value > edge:
            raise ValueError("out of limit pls check Value")

    @staticmethod
    def get_class_name(obj):
        return obj.class_name

    def update_xy(self, x, y):
        self.x = x
        self.y = y

    @staticmethod
    def check_screen(width, height):
        if type(width) is not int or type(height) is not int:
            raise TypeError("width and height must be positive integers")
        if width < 200 or width > 1800:
            raise ValueError("out of limit: MIN width = 200, MAX = 1800")
        if height < 200 or height > 900:
            raise ValueError("out of limit: MIN height = 200, MAX = 900")

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        self.__height = value

    @property
    def image_size(self):
        return self.__image_size

    @image_size.setter
    def image_size(self, value):
        self.__image_size = value

    @property
    def game_env(self):
        return self.__game_env

    @game_env.setter
    def game_env(self, value):
        self.__game_env = value

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        limit = self.game_env.sc_width - self.image_size
        self.check_coordinate(value, limit)
        self.__x = value

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        limit = self.game_env.sc_height - self.image_size
        self.check_coordinate(value, limit)
        self.__y = value

    @property
    def speed(self):
        return self.__speed

    @speed.setter
    def speed(self, value):
        self.check_coordinate(value, 5)
        self.__speed = value

    @property
    def img(self):
        return self.__img

    @img.setter
    def img(self, value):
        if type(value) is not str:
            raise TypeError("pls give me the path of the img")
        # scale the image to 64*64
        picture = pygame.image.load(value)
        picture = pygame.transform.scale(picture, (self.image_size, self.image_size))
        if self.direction == Dr.DOWN:
            picture = pygame.transform.rotate(picture, 180)
        self.__img = picture

    @classmethod
    def update(cls):
        pass

    def kill_self(self):
        # search for the obj in game_env and remove it
        try:
            self.game_env.list_object.remove(self)
            # delete instance bullet
        except Exception:
            print(f"[ERROR, {self.__class__.__name__}]: "
                  f"instance \"{self.class_name}\" not found ")
        del self

    def check_if_tow_objs_hits(self, second_obj):
        """
        check if self and second_obj hits
        :param second_obj: any obj from the list_obj
        :return: True or False
        """
        self_shape = {"x": self.x, "y": self.y, "width": self.width, "height": self.height}
        obj_shape = {"x": second_obj.x, "y": second_obj.y,
                     "width": second_obj.width, "height": second_obj.height}

        if self_shape["x"] < obj_shape["x"] + obj_shape["width"] and \
                self_shape["x"] + self_shape["width"] > obj_shape["x"] and \
                self_shape["y"] < obj_shape["y"] + obj_shape["height"] and \
                self_shape["height"] + self_shape["y"] > obj_shape["y"]:
            return True

        return False
        # distance = sqrt(pow(self.x - second_obj.x , 2) + pow(second_obj.y -self.y, 2))

    def check_collision(self):
        """
        loop throw list_objects and check if the self hit some one
        :return:
        """
        for obj in self.game_env.list_object:
            # any one except self
            if obj is not self:
                if self.check_if_tow_objs_hits(obj) is True:
                    # we call on_collision of every self
                    self.on_collision(obj)

    def on_collision(self, other_object):
        pass
