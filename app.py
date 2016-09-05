from test import Mago, Magos

magos = Magos()
eloy = Mago('Eloy', 1, 100, magos)
franco = Mago('Franco', 1, 50, magos)

eloy.poder('fuego', 20, franco, magos)