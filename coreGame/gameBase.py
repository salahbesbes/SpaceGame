import pygame
from coreGame.gameStatus import Status
from coreGame.player import Player
from coreGame.alien import Alien
from coreGame.score import DisplayOnScreen
from pygame import mixer


class GameBase:
    def __init__(self, sc_width, sc_height):
        self.list_object = []
        self.sc_width = sc_width
        self.sc_height = sc_height
        self.time = 0
        self.status = Status.RUNNING
        self.screen = None
        self.background = None
        self.current_player = None
        self.text_score = None
        self.player_score = 0

    def handle_game_logic(self):
        for obj in self.list_object:
            # it update each obj
            obj.update()
            obj.check_collision()

    @property
    def sc_height(self):
        return self.__sc_height

    @sc_height.setter
    def sc_height(self, value):
        self.__sc_height = value

    @property
    def sc_width(self):
        return self.__sc_width

    @sc_width.setter
    def sc_width(self, value):
        self.__sc_width = value

    def render_all(self):
        self.text_score.render(f"score: {self.player_score}")
        for obj in self.list_object:
            # render an element
            self.screen.blit(obj.img, (obj.x, obj.y))

    def handle_screen(self):
        self.screen.fill((91, 79, 99))
        self.screen.blit(self.background, (0, 0))
        self.handle_game_logic()
        self.render_all()
        pygame.display.update()

    def get_player_instance(self):
        instance_name = "Player"
        try:
            for obj in self.list_object:
                if type(obj) is eval(instance_name):
                    return obj
        except NameError:
            print(f"[ERROR, {self.__class__.__name__}]: "
                  f"instance \"{instance_name}\" not found ")

    def play_game(self):
        while self.status == Status.RUNNING:
            events = pygame.event.get()
            for event in events:
                if event.type == pygame.QUIT:
                    self.status = Status.STOP
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        print("space pressed")
                        self.current_player.fire_bullet()
                        mixer.Sound("when_shoot.wav").play()
                    if event.key == pygame.K_p:
                        print(f"len objects = {len(self.list_object)}")
                        for ob in self.list_object:
                            print(ob)
            self.handle_screen()
            # if the player die new instance is updated
            self.current_player = self.get_player_instance()

    def init_game(self):
        pygame.init()
        # Title and Icon
        pygame.display.set_caption("Space Invaders")
        icon = pygame.image.load('ufo.png')
        pygame.display.set_icon(icon)

        # create screen
        self.screen = pygame.display.set_mode((self.sc_width, self.sc_height))
        background = pygame.image.load('backGround.png')
        self.background = pygame.transform.scale(
            background, (self.sc_width, self.sc_height))
        # each instance of the hole game must be appended in the list
        # append and save the instance to the game env
        self.current_player = Player(self, "UFO.png", 64)
        Alien(self, "alien.png", 64)  # append self in list_object
        # create an instance that display score
        self.text_score = DisplayOnScreen(self)
        # add sound in background (infinite loop)
        mixer.music.load("background.wav")
        mixer.music.play(-1)
