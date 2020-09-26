import flask
from flask import render_template
import requests
import flask_login
from app import app
from .user import User


@app.route('/')
@app.route('/index')
def index():
        return render_template('index.html', title='Home')
@app.route('/BusquedaArtesanos')
def BusquedaArtesanos():
    return render_template('BusquedaArtesanos.html', title='Buscar Artesanos')
@app.route('/RegistrarArtesano')
def RegistrarArtesano():
    return render_template('RegistrarArtesano.html', title='Registrar Artesanos')
@app.route('/InscripcionCurso')
def InscripcionCurso():
    return render_template('InscripcionCurso.html', title='Inscripcion a Curso')
@app.route('/RegistrarAcuerdo')
def RegistrarAcuerdo():
    return render_template('RegistrarAcuerdo.html', title='Registrar Acuerdo')
@app.route('/CrearCurso')
def CrearCurso():
    return render_template('CrearCurso.html', title='Crear Curso')
@app.route('/InfoCurso')
def InfoCurso():
    return render_template('InfoCurso.html', title='Informacion de Curso')
@app.route('/Login', methods=['GET', 'POST'])
def Login():
        if flask.request.method == 'GET':
                return render_template('login.html', title='Login')
        email = flask.request.form.get('email')
        password = flask.request.form['password']
        res = requests.post('http://127.0.0.1:5000/sessions/', json={"email": email,
                                                                 "password": password})
        if res.status_code == 200:
                usrid = res.json()['_id']
                user = User()
                user.id = usrid
                flask_login.login_user(user)
                return flask.redirect(flask.url_for('protected'))

        return 'Bad login'
@app.route('/NuevoInstructor')
def NuevoInstructor():
    return render_template('NuevoInstructor.html', title='Nuevo Instructor de Curso')
@app.route('/Registrate')
def Registrate():
    return render_template('registrate.html', title='Registrarse al Sistema')
#@app.route('/RegistrarArtesano/<string:id>')
#def getID(id):
 #       idpagina = {'pagina': id}
  #      return render_template('RegistrarArtesano.html', title='Registrar Artesanos', idpagina=idpagina)

    
