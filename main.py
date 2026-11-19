# This is a sample Python script.
from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
def inicio():
    return render_template("inicio.html")
@app.route("/ejercicio1", methods=["GET", "POST"])
def ejercicio1():
    if request.method == "POST":
        nota1 = int(request.form["nota1"])
        nota2 = int(request.form["nota2"])
        nota3 = int(request.form["nota3"])
        promedio=(nota1+nota2+nota3)/3
        print("promedio:",promedio)


        asistencia=int(request.form["asistencia"])
        if promedio>=40 and asistencia>=75:
            estado="APROBADO"
        else:
            estado="REPROBADO"
        print("estado:",estado)
        return render_template("ejercicio1.html", promedio=promedio, estado=estado)
    return render_template("ejercicio1.html")

@app.route("/ejercicio2", methods=["GET", "POST"])
def ejercicio2():
    if request.method == "POST":
        nombre1=request.form["nombre1"].strip()
        nombre2=request.form["nombre2"].strip()
        nombre3=request.form["nombre3"].strip()
        nombres = [nombre1, nombre2, nombre3]
        if len({nombre1.lower(), nombre2.lower(), nombre3.lower()}) < 3:
            return render_template("ejercicio2.html", error="Ingresa tres nombres diferentes.")
        nombre_mas_largo = max(nombres, key=len)
        cantidad=len(nombre_mas_largo)
        print(nombre_mas_largo,cantidad)
        return render_template("ejercicio2.html", nombre=nombre_mas_largo, cantidad=cantidad)


    return render_template("ejercicio2.html")
