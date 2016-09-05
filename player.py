class Player(object):
    names = []

    def __init__(self):
        self.add(self)
        pass

    def add(self, player):
        self.names.append(player)

    def search(self, player):
        if player in self.names:
            return self.names.index(player)
        else:
            return -1

    def hit(self, damage, victim):
        player = self.names[victim]
        if damage < player.life:
            life = player.life - damage
            player.set_life(life)
            player.get_life()
        else:
            print(player.name + ' die, con un hit de ' + str(damage))

    @classmethod
    def count(cls):
        return print(cls.names.__len__())
