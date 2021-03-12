import pygame


class DisplayOnScreen:
    def __init__(self, game_env, content="",
                 font="freesansbold.ttf", size=32, x=10, y=10,
                 color=(255, 255, 255)):
        self.game_env = game_env
        self.font = font
        self.size = size
        self.x = x
        self.y = y
        self.content = content
        self.color = color

    @property
    def content(self):
        return self.__content

    @content.setter
    def content(self, value):
        if value == "":
            self.__content = f"score: {self.game_env.player_score}"
        else:
            self.__content = value

    def render(self, content):
        self.content = content
        font = pygame.font.Font(self.font, self.size)
        text = font.render(self.content, True, self.color)
        self.game_env.screen.blit(text, (self.x, self.y))
