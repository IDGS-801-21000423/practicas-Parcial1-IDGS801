
class Listas:
  
  # Declaracion del constructor de la clase
    def __init__(self):
      self.listaUsuario = []
      self.listaPar = []
      self.listaImPar = []
        
  
  # Declaracion de los metodos de la clase
    def ingresarLista(self):
      self.listaUsuario = list(map(int, input("Ingrese algunos numeros: ").split()))
      
      
    def ordenarLista(self):
      self.listaUsuario.sort()
      print(f"Mi lista ordenada: ",self.listaUsuario)
    
    def agregarListaParInpar(self):
      for num in self.listaUsuario:
        if num % 2 == 0:
          self.listaPar.append(num)
        else:
          self.listaImPar.append(num)
      print(f'Impares: ', self.listaImPar)
      print(f'Pares: ',self.listaPar)
      
      repetidos = set([num for num in self.listaUsuario if self.listaUsuario.count(num) > 1])
      if repetidos:
          #print(f"{repetidos}")
          for num in repetidos:
              print(f"{num} => {self.listaUsuario.count(num)} veces.")
      else:
          print("No hay valores repetidos")
            


def main():
  obj = Listas()
  obj.ingresarLista()
  obj.ordenarLista()
  obj.agregarListaParInpar()

if __name__=="__main__":
    main()
    


  