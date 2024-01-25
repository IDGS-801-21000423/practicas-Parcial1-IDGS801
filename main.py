from flask import Flask, render_template, request

app = Flask(__name__)


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
    
    
  


if __name__ =="__main__":
  app.run(debug=True)   # Cambios en tiempo real