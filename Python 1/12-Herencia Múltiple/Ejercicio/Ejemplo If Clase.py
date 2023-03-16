class FiguraGeometrica:
    def __init__(self, alto, ancho):
        if 0 < alto < 10:
            self.alto = alto
        else:
            print('Introduce un valor válido')
        if 0 < ancho < 10:
            self.ancho = ancho
        else:
            print('Introduce un valor válido')