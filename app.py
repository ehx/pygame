from player import Player
from mago import Mage, Mages

magos = Mages()
eloy = Mage('Eloy', 2, 100, magos)
franco = Mage('Franco', 1, 50, magos)
a = Player()

eloy.hit('fuego', 20, franco, magos)

Mages.count()
Player.count()
