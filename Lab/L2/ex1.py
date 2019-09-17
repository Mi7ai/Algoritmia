from typing import *

class Estudiante:

    def __init__(self, name):
        self.name = name
        self.dic = {}

    def califica(self, asig: str, calif: int):

        #if asig not in self.dic:
        self.dic[asig] = calif


    def nota(self, asig: str):
        return self.dic.get(asig)

    def media(self):
        n = len(self.dic)
        l = sum(self.dic.values())
        s = l/n
        return sum(self.dic.values()) / n if n != 0 else None


    def muestra_expediente(self):
        for key, item in self.dic.items():
            #print("Asignatura: {}:{}").format(key, item)
            print(key, '->', item)


if __name__ == '__main__':
    e = Estudiante('Paco')
    e.califica("EI1022", 6)
    print("Nota:",  e.nota("EI1022"))
    print("Media:", e.media())
    print("Expediente", e.muestra_expediente())
