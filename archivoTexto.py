# archivoTexto.py

from io import open 

def agregar_palabras(wordEng, wordSpa):
  mi_archivo = open('mi_archivo.txt', 'a')
  mi_archivo.write('\n {} {}'.format(wordEng, wordSpa))
  mi_archivo.close()
  return wordEng, wordSpa
  
def buscar_palabras(word, selectLang):
  mi_archivo = open('mi_archivo.txt', 'r')
  lineas = mi_archivo.readlines()
  
  for linea in lineas:
    palabras = linea.split()
    if len(palabras) == 2:
      palabra_ing, palabra_esp = palabras 
      if word == palabra_esp and selectLang == 'ingles':
        return palabra_ing
      elif word == palabra_ing and selectLang == 'espanol':
        return palabra_esp
  return 'Palabra no encontrada'