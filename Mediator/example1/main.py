from Mediator.concreteMediator import ConcreteMediator
from Mediator.componentes.modelo import Modelo
from Mediator.componentes.preprocesado import Preprocesado
from Mediator.componentes.dashboard import Dashboard
from Mediator.componentes.mensaje import Mensaje
from Mediator.componentes.display import Display

"""
    Author: Juan Pablo Nahuelpán
    Esta implementación, es una modificación de la implementacion hecha en la web:
    https://refactoring.guru/es/design-patterns/mediator/python/example,
    Sin animo de plagiar, sino más bien entregar algo standar de la implementación,
    adaptando el código a la necesidad del ejercicio.
"""

if __name__ == "__main__":
    c1 = Modelo(4, "Euclidea")
    c2 = Preprocesado("archivo.csv")
    c3 = Dashboard()
    c4 = Mensaje()
    c5 = Display()
    mediator = ConcreteMediator(c1, c2, c3, c4, c5)

    print("preprocesado")
    c2.preprocesado()
