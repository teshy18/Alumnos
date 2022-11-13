


# Ejercicio 2 del Modulo Clases y Objetos en Python

class Alumno():
    Nombre: str
    Nota: float

    def __init__(self, Nombre, Nota):
        self.Nombre = Nombre
        self.Nota = Nota

    def getNombre(self):
        print(self.Nombre)

    def getNota(self):
        print(self.Nota)

    def getAprobado(self):
        if self.Nota > 6:
            print('El alumno "' + self.Nombre +'" esta aprobado')
        else:
            print('El alumno "' + self.Nombre +'" esta desaprobado')


Pedro = Alumno("Pedro", 10)

Jose = Alumno("Jose", 4)

print('')
Pedro.getNombre()
Pedro.getNota()
Pedro.getAprobado()

print('')
Jose.getNombre()
Jose.getNota()
Jose.getAprobado()
