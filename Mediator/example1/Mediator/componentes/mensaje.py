from ..baseComponent import BaseComponent


class Mensaje(BaseComponent):
    def mensajeError(self):
        self.mediator.notify(self, "Mensaje Error")

    def mensajeExito(self):
        self.mediator.notify(self, "Mensaje Exito")
