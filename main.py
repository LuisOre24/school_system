from alumno import *
from docente import *
from time import sleep

class Start(Alumno, Docente):

    def __init__(self):
        try:
            print('''
            BIENVENIDO AL SISTEMA DE GESTION ESCOLAR
            ¿QUE ES LO QUE DESEA GESTIONAR?
            1 -> GESTION PARA DOCENTES
            2 -> GESTION PARA ESTUDIANTES
            3 -> SALIR DEL SISTEMA
            ''')
            opcion = input(">>")
            if opcion == "1":
                self.loadTeacher()
                self.interazDocente()
                #Docente.interazDocente()
            if opcion == "2":
                self.cargar_alumnos()
                self.interazEstudiante()
            if opcion == "3":
                print("Saliendo del Sistema ....")
                sleep(2)
                exit()
        except KeyboardInterrupt:
            print("Forzando salida del sistema")
    
Start()
    
    
    