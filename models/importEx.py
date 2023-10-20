import pandas as pd
import numpy as np
import mysql.connector

def importEx():

    # Leer los datos del archivo Excel
    df = pd.read_excel('./src/static/others/datos.xlsx')
    df.replace('', np.nan, inplace=True)
    # Conectarse a la base de datos MySQL
    cnx = mysql.connector.connect(user='root', password='15021503Valegamer151',
                                host='localhost',
                                database='database')

    # Crear un cursor y ejecutar una consulta
    cursor = cnx.cursor()
    consulta = "INSERT INTO socios (dni, apellido, nombre, domicilio, telefono, fechanac, caracter, ene, feb, mar, abril, may, jun, jul, ago, sep, oct, nov, dic, fechaingreso, fechaegreso, observacion, tipo, categoriaJug, dniJug, apellidoJug, nombreJug, fechanaciJug, tipoJug2, categoriaJug2, dniJug2, apellidoJug2, nombreJug2, fechanaciJug2) VALUES (%s,%s,%s,%s, %s, %s,%s, %s, %s,%s, %s, %s,%s, %s, %s,%s, %s, %s,%s, %s, %s,%s, %s, %s,%s, %s, %s,%s, %s, %s,%s, %s, %s, %s)"
    for i, fila in df.iterrows():
        datos = (fila['A'], fila['B'], fila['C'], fila['D'], fila['E'], fila['F'], fila['G'], fila['H'], fila['I'], fila['J'], fila['K'], fila['L'], fila['M'], fila['N'], fila['Ñ'], fila['O'], fila['P'], fila['Q'], fila['R'], fila['S'], fila['T'], fila['U'], fila['V'], fila['W'], fila['X'], fila['Y'], fila['Z'], fila['AA'], fila['BB'], fila['CC'], fila['DD'], fila['EE'], fila['FF'], fila['GG'])
        datos = [None if pd.isna(value) else value for value in fila]
        cursor.execute(consulta, datos)

    # Confirmar los cambios y cerrar la conexión
    cnx.commit()
    cursor.close()
    cnx.close()