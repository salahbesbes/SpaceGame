from coreGame.GameInstance import Gi


class SHC:
    shooter = None
    victim = None

    def __init__(self, shooter, victim):
        SHC.shooter = shooter
        SHC.victim = victim

    @classmethod
    def take_care_of_health(cls):
        pass

    @classmethod
    def calcul_damage(cls):
        cls.victim.health -= 0.5
        print("victim has health decreased to ", cls.victim.health)

    @classmethod
    def check_health(cls):
        if cls.victim.health < 0:
            print("victim has health lower than 0 ")
