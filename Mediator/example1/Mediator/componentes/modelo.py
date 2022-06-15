from ..baseComponent import BaseComponent


class Modelo(BaseComponent):
    def __init__(self, nCentroides: int, distancia: str):
        super().__init__()
        self.nCentroides = nCentroides
        self.distancia = distancia

    def ejecutarModelo(self):
        print("Ejecutando modelo")
        self.mediator.notify(self, "Mensaje Exito")
