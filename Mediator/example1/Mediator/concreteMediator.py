from .interfaceMediator import Mediator
from .componentes.preprocesado import Preprocesado
from .componentes.modelo import Modelo
from .componentes.dashboard import Dashboard
from .componentes.mensaje import Mensaje
from .componentes.display import Display


class ConcreteMediator(Mediator):
    def __init__(self,
                 component1: Modelo,
                 component2: Preprocesado,
                 component3: Dashboard,
                 component4: Mensaje,
                 component5: Display):
        self._component1 = component1
        self._component1.mediator = self
        self._component2 = component2
        self._component2.mediator = self
        self._component3 = component3
        self._component3.mediator = self
        self._component4 = component4
        self._component4.mediator = self
        self._component5 = component5
        self._component5.mediator = self

    def modelo(self, event: str):
        if event == "Mensaje Exito":
            self._component4.mensajeExito()
            self._component3.mostrarResultados()
        elif event == "Mensaje Error":
            print("Se murió el modelo :( ")

    def preprocesado(self, event: str):
        if event == "archivo.csv":
            print("Archivo no preprocesado")
            self._component2.preprocesado()
        elif event == "archivo_pre.csv":
            print("Archivo ya está preprocesado")
            self._component1.ejecutarModelo()

    def dashboard(self, event: str):
        if event == "dashboard listo":
            print("Ya se esta visualizando el dashboard(GUI)")

    def mensaje(self, event: str):
        if event == "Mensaje Exito":
            self._component5.mostrar("Mensaje Exito")
        elif event == "Mensaje Error":
            self._component5.mostrar("Mensaje Error")

    def display(self, event: str):
        if event == "Mensaje Exito":
            self._component5.mensajeExito()

    def notify(self, sender: object, event: str):
        if str(type(sender).__name__) == "Modelo":
            self.modelo(event)
        elif str(type(sender).__name__) == "Preprocesado":
            self.preprocesado(event)
        elif str(type(sender).__name__) == "Dashboard":
            self.dashboard(event)
        elif str(type(sender).__name__) == "Mensaje":
            self.mensaje(event)
        elif str(type(sender).__name__) == "Display":
            self.display(event)
