from flask import Blueprint
from flask import render_template,request
from flask_login import login_required
import mysql.connector


ruta2_bp = Blueprint('ruta2', __name__)

@ruta2_bp.route("/abm_ficha")
@login_required
def index():
    return render_template("ABM_ficha.html")

@ruta2_bp.route('/abm_ficha', methods=['GET', 'POST'])
def ABM():
    mydb = mysql.connector.connect(
    host="186.158.11.37",
    user="mysql_user",
    password="Aedr15150302",
    database="database"
    )
    mycursor = mydb.cursor()
    #manejador de solicitud
    if 'guardar' in request.form:
        query = "INSERT INTO socios (dni, apellido, nombre, domicilio, telefono, fechanac, caracter,fechaingreso, fechaegreso, observacion, tipo, categoriaJug, dniJug, apellidoJug, nombreJug, fechanaciJug, tipoJug2, categoriaJug2, dniJug2, apellidoJug2, nombreJug2, fechanaciJug2) VALUES (%s, %s, %s,%s, %s, %s,%s, %s, %s,%s, %s, %s,%s, %s, %s,%s, %s, %s,%s, %s, %s, %s)"
        valores = (request.form.get('dni'),request.form.get('apellido'),request.form.get('nombre'),request.form.get('domicilio'),request.form.get('telefono'),request.form.get('fechaNa'),request.form.get('caracter'),'as', 'Prueba','as' ,request.form.get('tipo_jug1'),request.form.get('categoria_jug1'),request.form.get('dni_jug1'),request.form.get('apellido_jug1'),request.form.get('nombre_jug1'),request.form.get('fechaNa_jug1'),request.form.get('tipo_jug2'),request.form.get('categoria_jug2'),request.form.get('dni_jug2'),request.form.get('apellido_jug2'),request.form.get('nombre_jug2'),request.form.get('fechaNa_jug2'))
        mycursor.execute(query, valores)
        mydb.commit()
    elif 'eliminar' in request.form:
        query = "DELETE FROM socios WHERE dni = %s AND apellido = %s"
        valores2 = (request.form.get('dni'),request.form.get('apellido'))
        mycursor.execute(query, valores2)
        mydb.commit()
    elif 'modificar' in request.form:
        query = "UPDATE socios SET dni = %s, apellido= %s, nombre= %s, domicilio= %s, telefono= %s, fechanac= %s, caracter= %s,fechaingreso= %s, fechaegreso= %s, observacion= %s, tipo= %s, categoriaJug= %s, dniJug= %s, apellidoJug= %s, nombreJug= %s, fechanaciJug= %s, tipoJug2= %s, categoriaJug2= %s, dniJug2= %s, apellidoJug2= %s, nombreJug2= %s, fechanaciJug2= %s"
        valores3 = (request.form.get('dni'),request.form.get('apellido'),request.form.get('nombre'),request.form.get('domicilio'),request.form.get('telefono'),request.form.get('fechaNa'),request.form.get('caracter'),'as', 'Prueba','as' ,request.form.get('tipo_jug1'),request.form.get('categoria_jug1'),request.form.get('dni_jug1'),request.form.get('apellido_jug1'),request.form.get('nombre_jug1'),request.form.get('fechaNa_jug1'),request.form.get('tipo_jug2'),request.form.get('categoria_jug2'),request.form.get('dni_jug2'),request.form.get('apellido_jug2'),request.form.get('nombre_jug2'),request.form.get('fechaNa_jug2'))
        mycursor.execute(query, (valores3))
        mydb.commit()
    else:
        # Acción por defecto si no se envía ningún botón válido
        return 'Acción no válida'

    return render_template("ficha.html")

