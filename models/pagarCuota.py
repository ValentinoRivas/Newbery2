from flask import Blueprint
from flask import render_template,request
from flask_login import login_required
import mysql.connector
from datetime import datetime
from flask import session

ruta4_bp = Blueprint('ruta4', __name__)


@ruta4_bp.route("/pagarCuota")
@login_required
def index():
    return render_template("pagarCuota.html")

@ruta4_bp.route('/buscarDT', methods=['GET', 'POST'])
def buscarDT():
    mydb = mysql.connector.connect(
    host="186.158.11.37",
    user="mysql_user",
    password="Aedr15150302",
    database="database"
    )   
    valor2 = request.form.get('dni')
    session['valor2'] = valor2
    cursor = mydb.cursor()
    query = "SELECT dni,cuota,estado FROM cuotas WHERE dni = %s AND estado = %s ORDER BY cuota ASC"
    cursor.execute(query, (valor2,'NO',))
    datos = cursor.fetchall()
    primer_dato = datos[0] if datos else None
    mydb.close()
    return render_template('pagarCuota.html', primer_dato=primer_dato)


@ruta4_bp.route("/pago",methods=['GET', 'POST'] )
@login_required
def pago():
    mydb = mysql.connector.connect(
    host="186.158.11.37",
    user="mysql_user",
    password="Aedr15150302",
    database="database"
    )
    valor2 = session.get('valor2')
    session.pop('valor2', None) 
    cursor = mydb.cursor()
    query = "SELECT * FROM cuotas WHERE dni = %s AND estado = %s ORDER BY cuota ASC"
    cursor.execute(query, (valor2,'NO',))
    result = cursor.fetchone()
    cursor.fetchall()  

    if result:
        valor1, valor2, valor3, valor4 = result
        query = "UPDATE cuotas SET estado = %s WHERE cuota = %s AND dni = %s"
        valores = ('SI', valor3, valor2)
        cursor.execute(query, valores)
        mydb.commit()
    mydb.close()
    cursor.close()
    return render_template("pagarCuota.html")    