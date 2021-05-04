from uuid import uuid4
from json import load, decoder, dump
from time import sleep

registro_alumnos = {
    'alumnos_registrados' : []
}

class Alumno:
    
    #CONSTRUCTOR
    def __init__(self, nombres, notas = []):
        self.nombres = nombres
        self.notas = notas

    #INTERFAZ CON EL USUARIO
    def interazEstudiante(self):
        try:
            print('''
            =============================
            =MODULO GESTOR PARA ESTUDIANTES=
            =============================
            INDICAR QUE ACCION DESEA REALIZAR:
            1 -> REGISTAR A UN NUEVO ESTUDIANTE
            2 -> LISTAR ESTUDIANTES REGISTRADOS
            3 -> RETORNAR AL MENU PRINCIPAL
            4 -> SALIR DEL SISTEMA
            ''')

            respuesta = input(">>>")

            if respuesta == "1":
                self.registar_alumno()
            elif respuesta == "2":
                self.listEstudiante()
            elif respuesta == "3":
                print("regresar al menu principal")
            elif respuesta == "4":
                print("SALIENDO DEL SISTEMA ......")
                sleep(2)
                exit()
        except Exception as ex:
            print(str(ex))

    def registar_alumno(self, nombres, notas = []):
        print('''REGISTRO DE DOCENTES
            POR FAVOR INGRESE LOS NOMBRES, EDAD Y DNI DEL DOCENTE
        ''')
        nombre = input(">>Ingresar los nombres del Docente: >>> ")
        print("Ingrese el numero de notas del estudiante")
        cant_notas = int(input(">>"))
        notas = []
        for item in range(cant_notas):
            nota = int(input(f"Ingrese Nota {item + 1}: "))
            if nota < 0 or nota >= 20:
                print("Ingrese una nota validad (Mayor igual a 0 o menor igual a 20")
            else:
                notas.append(nota)
        
        alumno = Alumno(nombre,notas)
        promedio = sum(notas)/len(notas)
        notaMaxima = max(notas)
        notaMinima = min(notas)

        registro = {
            "id" : str(uuid4()),
            "nombres" : alumno.nombres,
            "notas" : alumno.notas,
            "promedio" : float(promedio),
            "nota_maxima" : float(notaMaxima),
            "nota_minima" : float(notaMinima)
        }

        self.save_alumno(registro)

    def save_alumno(self,data):
        registro_alumnos['alumnos_registrados'].append(data)        
        alumnos = registro_alumnos['alumnos_registrados']
        archivo = open("registro_alumnos.json", "w")
        dump(alumnos, archivo, indent=4)
        archivo.close()
        print("¡ EL ESTUDIANTE SE REGISTRO CORRECTAMENTE !")
        print("Retornando al Menu de Estudiantes en 3 segundos")
        print("3")
        sleep(1)
        print("2")
        sleep(1)
        print("1")
        sleep(1)
        self.interazEstudiante()
        

    def cargar_alumnos(self):
        try:
            archivo = open("registro_alumnos.json", "r")
            registro_alumnos["alumnos_registrados"] = load(archivo)
            archivo.close()
        except FileNotFoundError:
            print("\n Creando registro de alumnos...")
            archivo = open("registro_alumnos.json", "w")
            archivo.close()
        except decoder.JSONDecodeError:
            print("\n No hay alumnos registrados, se puede crear desde ahora")

    def listEstudiante(self):
        try:
            file = open("registro_alumnos.json", "r")
            print(file.read())
            #print(">>>Digite R para retornar al menu de Gestion de Docente o Q para salir del sistema")
            #while True:
            #    opcion = input(">>>")
            #    if opcion.lower() == "r":
            #        self.interazDocente()
            #    elif opcion.lower() == "q":
            #        print("Eligio salir del sistema.... Vuelva pronto")
            #        sleep(2)
            #        exit()
            #    elif opcion != "r" or opcion != "q":
            #        print("Digite una opcion valida : (R o Q)")
        except Exception as ex:
            print(f'Ocurrio un inconveniente al leer el archivo {str(ex)}')
        else:
            file.close()

