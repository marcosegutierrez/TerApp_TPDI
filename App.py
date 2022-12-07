from flask import Flask, render_template, request, session, redirect, url_for, flash
from flask.globals import request
from flask_mysqldb import MySQL
import modules.beginning as beginning, modules.login as login
import modules.wait as wait, modules.patient as patient, modules.professional as professional, modules.professional1 as professional1
import modules.contact as contact, modules.diary as diary

app = Flask(__name__)

# Mysql Connection
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'terapp'
mysql = MySQL(app)

# settings
app.secret_key = 'mysecretkey'

# global
global profesional_global

# ------------------------INICIO------------------------------

@app.route('/beginning')
def Beginning():
    data = beginning.Beginning(mysql)
    return render_template('Beginning.html', en_espera=data)

# -En caso de querer comenzar con localhost:3000

@app.route('/')
def New_Patient():
    data = beginning.Beginning(mysql)
    return render_template('Beginning.html', en_espera=data)


# ------------------------LOGIN------------------------------

@app.route('/login')
def Login():
    template = login.Login(session)
    return render_template(template)

    # ------------------------------LOGIN Verificación de datos--------------------------------------

@app.route('/login', methods=['POST'])
def do_admin_login():
    state = login.do_admin_login(request, mysql, session)
    if state == 1: return Login()


@app.route('/logout')
def logout():
    login.logout(session)
    return(Login())

# ------------------------------PROFESIONAL--------------------------------------

@app.route('/professional')
def My_Profile():
    data = professional.My_Profile(mysql)
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM obra_social')
    obras_sociales = cur.fetchall()
    return render_template('My_Profile.html', profesional=data, obras_sociales=obras_sociales)


@app.route('/professional/add_professional', methods=['POST'])
def add_professional():
    professional.add_professional(request, mysql)
    flash('Registro exitoso! Ingresa con tus credenciales')
    return redirect(url_for('Login'))

     # ---------- Editar perfil profesional----------------

@app.route('/edit_professional')
def get_profesional():
    data = professional.get_profesional(session, mysql)
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM obra_social')
    obras_sociales = cur.fetchall()
    return render_template('Edit_Professional.html', professional=data[0], obras_sociales=obras_sociales)

@app.route('/update_professional/<id>', methods=['POST'])
def update_professional(id):
    professional.update_professional(id, request, mysql)
    flash('Perfil editado con éxito')
    return redirect(url_for('Personalized_Welcome'))

 # ---- Solo disponible para un perfil administrador ----


@app.route('/professional/delete_professional')
def delete_professional():
    return 'delete professional'


# ------------------------------PACIENTE------------------------------

@app.route('/patient')
def Patient_List():
    data = patient.Patient_List(mysql)
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM obra_social')
    obras_sociales = cur.fetchall()
    return render_template('Patient_List.html', paciente=data, obras_sociales=obras_sociales)

@app.route('/patient/add_patient', methods=['POST'])  # el botón guardar
def add_patient():
    patient.add_patient(mysql, request)
    return redirect(url_for('Patient_List'))

@app.route('/patient/edit_patient/<id>')
def get_patient(id):
    data = patient.get_patient(mysql, id)
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM obra_social')
    obras_sociales = cur.fetchall()
    return render_template('Edit_Patient.html', patient=data[0],obras_sociales=obras_sociales)

@app.route('/update/<id>', methods=['POST'])
def update_patient(id):
    patient.update_patient(mysql, id, request)
    return redirect(url_for('Patient_List'))

@app.route('/patient/delete_patient/<string:id>')
def delete_patient(id):
    patient.delete_patient(mysql, id)
    return redirect(url_for('Patient_List'))

    # ------------------------BUSCADOR de Paciente------------------------------

@app.route('/patient', methods=['POST'])
def Patient_List_Filtered():
    if request.form['input-search'] == "" :
        return Patient_List()
    [data, currentvalue] = patient.Patient_List_Filtered(mysql, request)
    return render_template('Patient_List.html', paciente=data, currentvalue=currentvalue)

# ----------------------Agenda--------------

@app.route('/agenda')
def agenda():
    data = diary.agenda(mysql)
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM agenda')
    data = cur.fetchall()
    return render_template('agenda.html', agenda=data)

@app.route('/agenda/add_turno', methods=['POST'])
def add_turno():
    diary.add_turno(mysql, request)
    return redirect(url_for('agenda'))

@app.route('/agenda/edit_turno/<id>')
def get_turno(id):
    data = diary.get_turno(mysql, id)
    return render_template('Edit_Turno.html', agenda=data[0])

@app.route('/update_turno/<id>', methods=['POST'])
def update_turno(id):
    diary.update_turno(mysql, id, request)
    return redirect(url_for('agenda'))

@app.route('/agenda/delete_turno/<string:id>')
def delete_turno(id):
    diary.delete_turno(mysql, id)
    return redirect(url_for('agenda'))

    # ------------------------BUSCADOR de Agenda------------------------------


@app.route('/agenda', methods=['POST'])
def agenda_Filtered():
    busqueda = request.form['input-search']

    if busqueda == "":
        return agenda()

    currentvalue = busqueda

    query = "SELECT * FROM agenda WHERE "
    query += "nombre_apellido LIKE '%" + busqueda + "%' OR "
    query += "fecha LIKE '%" + busqueda + "%' OR "
    query += "hora LIKE '%" + busqueda + "%' OR "
    query += "observaciones LIKE '%" + busqueda + "%'"

    cur = mysql.connection.cursor()
    cur.execute(query)
    data = cur.fetchall()

    return render_template('agenda.html', agenda=data, currentvalue=currentvalue)

    # --- Ruta que da funcionalidad al botón Volver en cada vista ---


@app.route('/personalized_welcome')
def Personalized_Welcome():
    return render_template('Personalized_Welcome.html')


# ------------------------CONTACTENOS: Soporte técnico---------------------------------

@app.route('/contact')
def contact_form():
    return render_template('contact.html')

@app.route('/contact/add_message', methods=['POST'])  #boton "ENVIAR"
def add_message():
    contact.add_message(mysql, request)
    return redirect(url_for('Personalized_Welcome'))
    #return redirect(url_for('contact'))    


# -------------------PACIENTES EN ESPERA--------------------

@app.route('/waiting')
def waiting():
    data = wait.waiting(mysql)
    return render_template('Wait.html', en_espera=data)


@app.route('/waitingUpdate')
def waiting_update():
    wait.waiting_update(mysql)
    return redirect(url_for('waiting'))


@app.route('/waitingUpdate2')
def waiting_update2():
    wait.waiting_update(mysql)
    return redirect(url_for('Beginning'))


@app.route('/waitingDelete')
def waiting_delete():
    wait.waiting_delete(mysql)
    return redirect(url_for('Beginning'))


@app.route('/waitingReset')
def waiting_reset():
    wait.waiting_reset(mysql)
    return redirect(url_for('Beginning'))


# ------------------------DEBUG---------------------------------

if __name__ == '__main__':
    app.run(port=3000, debug=True)
