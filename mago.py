from player import Player


class Mages(Player):
    names = []

    def agrega(self, mage):
        self.names.append(mage)

    @classmethod
    def count(cls):
        return print(cls.names.__len__())


class Mage(object):
    def __init__(self, name, level, life, clase):
        self.id = clase.count
        self.name = name
        self.level = level
        self.life = life
        clase.agrega(self)

    def hit(self, type, damage, victim, mage):
        damage = self.level * damage
        victim = mage.search(victim)
        if victim > 0:
            return mage.hit(damage, victim)
        else:
            print('no se encontro el player')

    def get_life(self):
        if self.life > 0:
            print('el player ' + self.name + ' tiene ' + str(self.life) + 'hp.')
        else:
            print('el player ' + self.name + ' esta muerto')

        return self.life

    def set_life(self, life):
        self.life = life
