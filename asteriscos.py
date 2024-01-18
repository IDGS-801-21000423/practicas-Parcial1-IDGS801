'''
1.- Pedir Numero: 5
'''
class MostrarAsteriscos:
  # Declaracion del constructor de la clase
    def __init__(self):
        self.numero = int(input("Ingrese un número: "))
        
  # Declaracion de los metodos de la clase
    def crearAsteriscos(self):
        for i in range(1, self.numero + 1):
            print("*" * i)

def main():
  obj = MostrarAsteriscos()
  obj.crearAsteriscos()


if __name__=="__main__":
    main()      
    

