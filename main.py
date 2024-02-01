from flask import Flask, render_template, request
import forms                # Importar archivo forms
app = Flask(__name__)
import math

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
  


if __name__ =="__main__":
  app.run(debug=True)   # Cambios en tiempo real