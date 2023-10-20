from flask import Flask, render_template, request, redirect, url_for, flash
from flask_mysqldb import MySQL
from flask_login import LoginManager, login_user, logout_user, login_required

#Modelos
from models.ModelUser import ModelUser
from models.rellenarTB import *
from models.importEx import importEx
from models.rellenarTB import ruta1_bp
from models.ABM_ficha import ruta2_bp
from models.registroSocio import ruta3_bp
from models.pagarCuota import ruta4_bp



# Entities: 
from models.entities.User import User

class Config:
    SECRET_KEY = 'B!1w8NAt1T^%kvhUI*S^'
    DEBUG = False
    MYSQL_HOST = '186.158.11.37'
    MYSQL_USER = 'mysql_user'
    MYSQL_PASSWORD = 'Aedr15150302'
    MYSQL_DB = 'database'

class DevelopmentConfig(Config):
    DEBUG = True

# Configura la aplicación
app = Flask(__name__)
app.config.from_object(DevelopmentConfig)

# Configura el sistema de registro

db = MySQL(app)

login_manager_app = LoginManager(app)

@login_manager_app.user_loader
def load_user(id):
    return ModelUser.get_by_id(db, id)

@app.route('/')
def index():
    return redirect(url_for('home'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        user = User(0, request.form['email'], request.form['password'])
        logged_user = ModelUser.login(db, user)
        if logged_user != None:
            if logged_user.password:
                login_user(logged_user)
                return redirect(url_for('home'))
            else:
                flash('Invalid password')
                return render_template('login.html')
        else:
            flash('User not found')
            return render_template('login.html')
    else:
        return render_template('login.html')

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('login'))

@app.route('/home')
@login_required
def home():
    return render_template('home.html')

def status_401(error):
    return redirect(url_for('login'))

def status_404(error):
    return "<h1>la Url que esta intentando acceder no existe!</h1>", 404

app.register_error_handler(401, status_401)
app.register_error_handler(404, status_404)

app.register_blueprint(ruta1_bp)
app.register_blueprint(ruta2_bp)
app.register_blueprint(ruta3_bp)
app.register_blueprint(ruta4_bp)

if __name__ == '__main__':
    app.run()