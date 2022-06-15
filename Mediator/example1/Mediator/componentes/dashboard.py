from ..baseComponent import BaseComponent


class Dashboard(BaseComponent):
    def mostrarResultados(self):
        print("Se esta generando el dashboard")
        self.mediator.notify(self, "dashboard listo")
