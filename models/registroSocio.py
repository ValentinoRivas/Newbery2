from flask import Flask,flash
from flask import Blueprint
from flask import render_template,request
from flask_login import login_required
import mysql.connector
import datetime
from bs4 import BeautifulSoup


ruta3_bp = Blueprint('ruta3', __name__)

@ruta3_bp.route("/registroSocio")
@login_required
def index():
    mydb = mysql.connector.connect(
    host="186.158.11.37",
    user="mysql_user",
    password="Aedr15150302",
    database="database"
    )
    ##obtengo la fecha actual
    fecha_actual = datetime.datetime.now().date()
    anio = str(fecha_actual.year)
    mes = str(fecha_actual.month)
    fecha_unificada = anio + mes
    ## obtengo la fecha qu esta por defecto en el configurador DB
    cursor = mydb.cursor()
    query = "SELECT fechaAct FROM configurador"
    cursor.execute(query)
    result3 = cursor.fetchall()
    valor = result3[0][0]
    ## Pregunt si la fecha que esta por defecto en la db es igual a la fecha actual
    if valor != fecha_unificada:
        cursor2 = mydb.cursor()
        query = "UPDATE configurador SET fechaAct = %s"
        query2 = "SELECT dni from socios"
        valores2 = (fecha_unificada,)
        cursor.execute(query, valores2)
        mydb.commit()
        cursor2.execute(query2)
        result4 = cursor2.fetchall()

        query = "INSERT INTO cuotas (dni, cuota, estado) VALUES (%s, %s, %s)"
        for row in result4:
            valor3 = (row[0], fecha_unificada, 'NO')
            cursor.execute(query, valor3)

        mydb.commit()
        cursor.close()
    return render_template("registroSocio.html")

@ruta3_bp.route('/registroSocio', methods=['GET', 'POST'])
def registro():
    mydb = mysql.connector.connect(
    host="186.158.11.37",
    user="mysql_user",
    password="Aedr15150302",
    database="database"
    )
    valor = request.form.get('valor_input')
    cursor = mydb.cursor()
    query = "SELECT * FROM socios WHERE dni = %s"
    cursor.execute(query, (valor,))
    result2 = cursor.fetchall()
    if len(result2) > 0: 
        cursor = mydb.cursor()
        query = "SELECT * FROM cuotas WHERE dni = %s AND estado = %s ORDER BY cuota ASC"
        cursor.execute(query, (valor,'NO',))
        result = cursor.fetchall()  # Obtiene todos los resultados como una lista de tuplas
        num_results = len(result)  # Cuenta la cantidad de resultados

        if num_results > 2:
            flash('<div class="alert alert-danger" role="alert">Tenes ' + str(num_results) + ' Cuotas Edeudadas</div>')
        elif num_results == 2 or num_results == 1:
            flash('<div class="alert alert-warning" role="alert">' + str(num_results) + ' cuotas adeudadas</div>')
        else:
            flash('<div class="alert alert-success" role="alert">Acceso</div>')         
        
    return ""
    cursor.close()
    mydb.close()