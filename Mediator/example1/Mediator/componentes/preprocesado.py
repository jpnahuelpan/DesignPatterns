from ..baseComponent import BaseComponent


class Preprocesado(BaseComponent):
    def __init__(self, filePath: str):
        super().__init__()
        self.filePath = filePath

    def preprocesado(self):
        print("Se procesa el archivo: " + self.filePath)
        self.filePath = "archivo_pre.csv"
        self.datoProcesado()

    def datoProcesado(self):
        self.mediator.notify(self, self.filePath)
