import mysql.connector
from flask import Blueprint
from flask import render_template,request,jsonify
from flask_login import login_required


ruta1_bp = Blueprint('ruta1', __name__)

@ruta1_bp.route("/ficha")
def index():
    return render_template("ficha.html")

@ruta1_bp.route('/ficha', methods=['GET', 'POST'])
@login_required
def fichas():
    mydb = mysql.connector.connect(
    host="186.158.11.37",
    user="mysql_user",
    password="Aedr15150302",
    database="database"
    )
    busqueda = request.form.get('valor_seacrh')
    valor_ficha = request.form.get('valor_select')
    mycursor = mydb.cursor()
    if valor_ficha == None or valor_ficha == 'todos':
        if busqueda:
            query = "SELECT dni, apellido, nombre, domicilio, telefono, fechanac, caracter,fechaingreso, fechaegreso, observacion, tipo, categoriaJug, dniJug, apellidoJug, nombreJug, fechanaciJug, tipoJug2, categoriaJug2, dniJug2, apellidoJug2, nombreJug2, fechanaciJug2 FROM socios WHERE nombre LIKE %s"
            mycursor.execute(query, ("%" + busqueda + "%",))
        else: 
            query = "SELECT dni, apellido, nombre, domicilio, telefono, fechanac, caracter, fechaingreso, fechaegreso, observacion, tipo, categoriaJug, dniJug, apellidoJug, nombreJug, fechanaciJug, tipoJug2, categoriaJug2, dniJug2, apellidoJug2, nombreJug2, fechanaciJug2 FROM socios"
            mycursor.execute(query)
    else:     
        if busqueda:
            query = "SELECT dni, apellido, nombre, domicilio, telefono, fechanac, caracter,fechaingreso, fechaegreso, observacion, tipo, categoriaJug, dniJug, apellidoJug, nombreJug, fechanaciJug, tipoJug2, categoriaJug2, dniJug2, apellidoJug2, nombreJug2, fechanaciJug2 FROM socios WHERE nombre LIKE %s and tipo LIKE %s"
            mycursor.execute(query, ("%" + busqueda + "%", "%" + valor_ficha + "%"))
        else:
            query = "SELECT dni, apellido, nombre, domicilio, telefono, fechanac, caracter,fechaingreso, fechaegreso, observacion, tipo, categoriaJug, dniJug, apellidoJug, nombreJug, fechanaciJug, tipoJug2, categoriaJug2, dniJug2, apellidoJug2, nombreJug2, fechanaciJug2 FROM socios WHERE tipo LIKE %s"
            mycursor.execute(query,("%" + valor_ficha + "%",))

    resultados = mycursor.fetchall()
    
    datos = []
    for fila in resultados:
        diccionario = {
            "campo1": fila[0],
            "campo2": fila[1],
            "campo3": fila[2],
            "campo4": fila[3],
            "campo5": fila[4],
            "campo6": fila[5],
            "campo7": fila[6],
            "campo8": fila[7],
            "campo9": fila[8],
            "campo10": fila[9],
            "campo11": fila[10],
            "campo12": fila[11],
            "campo13": fila[12],
            "campo14": fila[13],
            "campo15": fila[14],
            "campo16": fila[15],
            "campo17": fila[16],
            "campo18": fila[17],
            "campo19": fila[18],
            "campo20": fila[19],
            "campo21": fila[20],
            "campo22": fila[21],
        }
        datos.append(diccionario)
        datos=datos
    return jsonify(datos)
