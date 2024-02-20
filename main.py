from flask import Flask, render_template, request
import forms                # Importar archivo forms
from archivoTexto import agregar_palabras, buscar_palabras
app = Flask(__name__)
import math

@app.route("/idiomas", methods = ['GET', 'POST'])
def idiomas():
  wordEng = ""
  wordSpa = ""
  palabra = ""
  wordEq = ""
  selectLang = ""
  idiomas_clase = forms.UserFormLanguagesWords(request.form)
  
  if request.method == 'POST': 
    if "btn1" in request.form: 
        wordEng = request.form.get('wordEng')
        wordSpa = request.form.get('wordSpa')
        agregar_palabras(wordEng, wordSpa)
    elif "btn2" in request.form:
        palabra = idiomas_clase.palabra.data
        selectLang = idiomas_clase.selectLang.data
        wordEq = buscar_palabras(palabra, selectLang)
        if wordEq:
          print("Respuesta: {}".format(wordEq))
        else: 
          print("Respuesta: {}".format(wordEq))
     
  return render_template("buscador-palabras.html", form = idiomas_clase, wordEng=wordEng, wordSpa=wordSpa, palabra=palabra, wordEq=wordEq, selectLang=selectLang)


@app.route("/calcular", methods=["GET", "POST"])
def calcular():
  if request.method == "POST":
    num1 = request.form.get("n1")
    num2 = request.form.get("n2")
    return"La multiplicacion de {} x {} = {}".format(num1, num2, str(int(num1) * int(num2)))
  else:
    return '''
    <form action="/calcular" method="POST">
      <label>N1:</label>
      <input type="text" name="n1"><br>
      <label>N2:</label>
      <input type="text" name="n2"><br>
      <input type="submit"/>
    </form>
    '''

@app.route("/OperasBas")
def operas():
  return render_template("OperasBas.html")

@app.route("/resultado", methods=["GET", "POST"])
def result():
  if request.method == "POST":
    if request.form.get("op") == "suma":
      num1 = request.form.get("n1")     
      num2 = request.form.get("n2") 
      return "La suma de {} + {} = {}".format(num1,num2, str(int(num1) + int(num2)))
    elif request.form.get("op") == "resta":
      num1 = request.form.get("n1")     
      num2 = request.form.get("n2") 
      return "La resta de {} - {} = {}".format(num1,num2, str(int(num1) - int(num2)))    
    elif request.form.get("op") == "division":
      num1 = request.form.get("n1")     
      num2 = request.form.get("n2") 
      return "La division de {} / {} = {}".format(num1,num2, str(int(num1) / int(num2)))
    elif request.form.get("op") == "multiplicacion":
      num1 =request.form.get("n1")
      num2 =request.form.get("n2")
      return"La multiplicacion de {} x {} = {}".format(num1, num2, str(int(num1) * int(num2)))
    elif request.form.get("op") == "exponente":
      num1 =request.form.get("n1")
      num2 =request.form.get("n2")
      return"El resultado de elevar {} al {} = {}".format(num1, num2, str(int(num1) ** int(num2)))
    elif request.form.get("op") == "div_exacta":
      num1 =request.form.get("n1")
      num2 =request.form.get("n2")
      return"La division exacta de {} // {} = {}".format(num1, num2, str(int(num1) // int(num2)))
    

@app.route("/distancias", methods = ['GET', 'POST'])
def distancias():
  distancias_clase = forms.UserFormDistance(request.form)
  distanciaX = ""
  distanciaX2 = ""
  distanciaY = ""
  distanciaY2 = ""
  distancia_calculada = "" 
  if request.method == 'POST':
    distanciaX = distancias_clase.distanciaX.data
    distanciaX2 = distancias_clase.distanciaX2.data
    distanciaY = distancias_clase.distanciaY.data
    distanciaY2 = distancias_clase.distanciaY2.data
    distancia_calculada = math.sqrt((pow((distanciaX2 - distanciaX), 2) + pow((distanciaY2 - distanciaY), 2)))
    print("DistanciaX: {}".format(distanciaX))
    print("DistanciaX2: {}".format(distanciaX2))
    print("DistanciaY: {}".format(distanciaY))
    print("DistanciaY2: {}".format(distanciaY2))
    print("Distancia Calculada: {}".format(distancia_calculada))
  

  return render_template("distancias.html", form = distancias_clase, distanciaX=distanciaX, distanciaX2=distanciaX2, distanciaY=distanciaY, distanciaY2=distanciaY2, distancia_calculada=distancia_calculada)
  

@app.route("/colores", methods = ['GET', 'POST'])
def colores():
  colores_clase = forms.UserFormColors(request.form)
  banda1 = ""
  banda2 = ""
  banda3 = ""
  tol = ""
  primerB = ""
  valor = ""
  valorMinimoIng = ""
  valorMaximoIng = ""
  colortd = ""
  colortd2 = ""
  colortd3 = ""
  colortol = ""
  textBanda1 = ""
  textBanda2 = ""
  textBanda3 = ""
  textTol = ""
  if request.method == 'POST':
    banda1 = colores_clase.banda1.data
    banda2 = colores_clase.banda2.data
    banda3 = colores_clase.banda3.data
    tol = colores_clase.tol.data  
    primerB = banda1 + banda2
    
    if banda1 == '0':
      colortd = '#000000'
      textBanda1 = 'Negro'
    elif banda1 == '1':
      colortd = '#A52A2A'
      textBanda1 = 'Cafe'
    elif banda1 == '2':
      colortd = '#FF0000'
      textBanda1 = 'Rojo'
    elif banda1 == '3':
      colortd = '#FFA500'
      textBanda1 = 'Naranja'
    elif banda1 == '4':
      colortd = '#FFFF00'
      textBanda1 = 'Amarillo'
    elif banda1 == '5':
      colortd = '#008000'
      textBanda1 = 'Verde'
    elif banda1 == '6':
      colortd = '#0000FF'
      textBanda1 = 'Azul'
    elif banda1 == '7':
      colortd = '#800080'
      textBanda1 = 'Violeta'
    elif banda1 == '8':
      colortd = '#808080'
      textBanda1 = 'Gris'
    elif banda1 == '9':
      colortd = '#FFFFFF'
      textBanda1 = 'Blanco'
    else:
      colortd = ''
      textBanda1 = ''
    
    if banda2 == '0':
      colortd2 = '#000000'
      textBanda2 = 'Negro'
    elif banda2 == '1':
      colortd2 = '#A52A2A'
      textBanda2 = 'Cafe'
    elif banda2 == '2':
      colortd2 = '#FF0000'
      textBanda2 = 'Rojo'
    elif banda2 == '3':
      colortd2 = '#FFA500'
      textBanda2 = 'Naranja'
    elif banda2 == '4':
      colortd2 = '#FFFF00'
      textBanda2 = 'Amarillo'
    elif banda2 == '5':
      colortd2 = '#008000'
      textBanda2 = 'Verde'
    elif banda2 == '6':
      colortd2 = '#0000FF'
      textBanda2 = 'Azul'
    elif banda2 == '7':
      colortd2 = '#800080'
      textBanda2 = 'Violeta'
    elif banda2 == '8':
      colortd2 = '#808080'
      textBanda2 = 'Gris'
    elif banda2 == '9':
      colortd2 = '#FFFFFF'
      textBanda2 = 'Blanco'
    else:
      colortd2 = ''
      textBanda2 = ''
    
    
    if banda3 == '1':
      colortd3 = '#000000'
      textBanda3 = 'Negro'
    elif banda3 == '10':
      colortd3 = '#A52A2A'
      textBanda3 = 'Cafe'
    elif banda3 == '100':
      colortd3 = '#FF0000'
      textBanda3 = 'Rojo'
    elif banda3 == '1000':
      colortd3 = '#FFA500'
      textBanda3 = 'Naranja'
    elif banda3 == '10000':
      colortd3 = '#FFFF00'
      textBanda3 = 'Amarillo'
    elif banda3 == '100000':
      colortd3 = '#008000'
      textBanda3 = 'Verde'
    elif banda3 == '1000000':
      colortd3 = '#0000FF'
      textBanda3 = 'Azul'
    elif banda3 == '10000000':
      colortd3 = '#800080'
      textBanda3 = 'Violeta'
    elif banda3 == '100000000':
      colortd3 = '#808080'
      textBanda3 = 'Gris'
    elif banda3 == '1000000000':
      colortd3 = '#FFFFFF'
      textBanda3 = 'Blanco'
    else:
      colortd3 = ''
      textBanda3 = ''
    
    valor = int(primerB) * int(banda3)
    if request.form.get("tol") == "oro":
      colortol = '#FFD700'
      textTol = "Oro"
      porcentaje = int(valor) * 5 / 100
      valorMaximoIng = valor + porcentaje
      valorMinimoIng = valor - porcentaje
    elif request.form.get("tol") == "plata":
      colortol = '#C0C0C0'
      textTol = "Plata"
      porcentaje = int(valor) * 10 / 100
      valorMaximoIng = valor + porcentaje
      valorMinimoIng = valor - porcentaje
    
  return render_template("colores-resistencias.html", form = colores_clase, banda1=banda1, banda2=banda2, banda3=banda3, tol=tol, primerB=primerB, valor=valor, valorMaximoIng=valorMaximoIng, valorMinimoIng=valorMinimoIng, colortd=colortd,colortd2=colortd2,colortd3=colortd3,colortol=colortol, textBanda1=textBanda1, textBanda2=textBanda2, textBanda3=textBanda3, textTol=textTol)

if __name__ =="__main__":
  app.run(debug=True)   # Cambios en tiempo real