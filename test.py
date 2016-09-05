class Mago(object):
    def __init__(self, nombre, nivel, vida, clase):
        self.id = clase.cantidad
        self.nombre = nombre
        self.nivel = nivel
        self.vida = vida
        clase.agrega(self)

    def poder(self, tipo, danio, victima, mago):
        victima = mago.busca(victima)
        if victima > 0:
            return mago.golpea(danio, victima)
        else:
            print('no se encontro el player')

    def getVida(self):
        if self.vida > 0:
            print('el player ' + self.nombre + ' tiene ' + str(self.vida) + 'hp.')
        else:
            print('el player ' + self.nombre + ' esta muerto')

        return self.vida

    def setVida(self, vida):
        self.vida = vida


class Magos(object):
    nombres = []

    def __init__(self):
        pass

    def agrega(self, mago):
        Magos.nombres.append(mago)
        pass

    def busca(self, mago):
        if mago in self.nombres:
            return self.nombres.index(mago)
        else:
            return -1

    def golpea(self, danio, victima):
        player = self.nombres[victima]
        if danio < player.vida:
            vida = player.vida - danio
            player.setVida(vida)
            player.getVida()
        else:
            print(player.nombre + ' murio, con un golpe de ' + str(danio))

    def cantidad(self):
        return print(Magos.nombres.__len__())
