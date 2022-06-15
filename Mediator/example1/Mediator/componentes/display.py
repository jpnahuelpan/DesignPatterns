from ..baseComponent import BaseComponent
from .mensaje import Mensaje


class Display(BaseComponent):
    def mostrar(self, msg: str):
        print(f"{msg} (GUI)")
