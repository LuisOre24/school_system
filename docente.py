from uuid import uuid4
from json import dump,load, decoder
from time import sleep

registro_docente = {
    'registro_docentes' : []
}

class Docente:
    def __init__(self, nombres, edad, dni):
        self.nombres = nombres
        self.edad = edad
        self.dni = dni


    def interazDocente(self):
        try:
            print('''
            =============================
            =MODULO GESTOR PARA DOCENTES=
            =============================
            INDICAR QUE ACCION DESEA REALIZAR:
            1 -> REGISTAR A UN NUEVO DOCENTE
            2 -> LISTAR DOCENTES REGISTRADOS
            3 -> RETORNAR AL MENU PRINCIPAL
            4 -> SALIR DEL SISTEMA
            ''')

            respuesta = input(">>>")
            if respuesta == "0":
                self.deleteTeacher()
            if respuesta == "1":
                self.registerTeacher()
            elif respuesta == "2":
                self.listTeacher()
            elif respuesta == "3":
                print("regresar al menu principal")
            elif respuesta == "4":
                print("SALIENDO DEL SISTEMA ......")
                sleep(2)
                exit()
        except Exception as ex:
            print(str(ex))

    def registerTeacher(self):
        print('''REGISTRO DE DOCENTES
            POR FAVOR INGRESE LOS NOMBRES, EDAD Y DNI DEL DOCENTE
        ''')
        nombre = input(">>Ingresar los nombres del Docente: >>> ")
        edad = input(">>Ingresar la edad del Docente: >>> ")
        dni = input(">>Ingresar el DNI del Docente: >>> ")

        docente = Docente(nombre, edad, dni)

        registro = {
            "id" : str(uuid4()),
            "nombres_docente" : docente.nombres,
            "edad_docente" : docente.edad,
            "dni_docente" : docente.dni
        }

        self.saveTeacher(registro)

    def saveTeacher(self, data):
        registro_docente['registro_docentes'].append(data)
        docentes = registro_docente['registro_docentes']
        file = open("registro_docentes.json", "w")
        dump(docentes, file, indent = 4)
        file.close()
        print("¡ EL DOCENTE SE REGISTRO CORRECTAMENTE !")
        print("Retornando al Menu de Docentes en 3 segundos")
        print("3")
        sleep(1)
        print("2")
        sleep(1)
        print("1")
        sleep(1)
        self.interazDocente()

    def loadTeacher(self):
        try:
            file = open("registro_docentes.json", "r")
            registro_docente['registro_docentes'] = load(file)            
            file.close()
        except FileNotFoundError:
            print("No existe registro de docentes creado, se procedera a crear registro")
            file = open("registro_docentes.json", "w")
            file.close()
        except decoder.JSONDecodeError:
            print("No existe docentes registrados")
            #print("Redireccionando al menu de Gestion de Docentes")
            #sleep(1)
            #print("........")
            #
            #self.interazDocente()
    
    def listTeacher(self):
        try:
            file = open("registro_docentes.json", "r")
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
            

################################### PENDIENTE POR RESOLVER ########################################
    def deleteTeacher(self):
        #file = len(registro_docente['registro_docentes'])
        ##for item in range(file):
        #print(registro_docente['registro_docentes']())
        #print(f'{file}')

        try:
            file = open("registro_docentes.json", "r")
            registro_docente['registro_docentes'] = load(file)            
            
            x = 0
            #for key , value in registro_docente.items():
            #    print(f'{key, value}\n')
            #    x += 1
            #    print(str(x))
            print(registro_docente['registro_docentes'])

            registro = registro_docente['registro_docentes']
            data = dict(registro)

            print(type(data))

            file.close()
        except FileNotFoundError:
            print("No existe registro de docentes creado, se procedera a crear registro")
            file = open("registro_docentes.json", "w")
            file.close()
        except decoder.JSONDecodeError:
            print("No existe docentes registrados")
