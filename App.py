from flask import Flask, render_template, request, redirect, url_for, flash
from flask.globals import request
from flask_mysqldb import MySQL

app = Flask(__name__)

# Mysql Connection
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'terapp'
mysql = MySQL(app)

# settings
app.secret_key = 'mysecretkey'


# ------------------------------PROFESIONAL--------------------------------------
@app.route('/professional')
def My_Profile():
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM profesional')
    data = cur.fetchall()
    return render_template('My_Profile.html', profesional=data)


@app.route('/professional/add_professional', methods=['POST'])
def add_professional():
    if request.method == 'POST':
        nombre = request.form['nombre']
        apellido = request.form['apellido']
        dni = request.form['dni']
        telefono = request.form['telefono']
        direccion = request.form['direccion']
        email = request.form['email']
        titulo = request.form['titulo']
        es_prestador = request.form['es_prestador']
        obra_social = request.form['obra_social']
        institucion_educativa = request.form['institucion_educativa']
        esta_matriculado = request.form['esta_matriculado']
        matricula = request.form['matricula']
        contraseña = request.form['contraseña']
        repetir_contraseña = request.form['repetir_contraseña']

        cur = mysql.connection.cursor()
        cur.execute('INSERT INTO profesional (nombre, apellido, dni, telefono, direccion, email, titulo, es_prestador, obra_social, institucion_educativa, esta_matriculado, matricula, contraseña, repetir_contraseña) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)',
                    (nombre, apellido, dni, telefono, direccion, email, titulo, es_prestador, obra_social, institucion_educativa, esta_matriculado, matricula, contraseña, repetir_contraseña))
        mysql.connection.commit()
        return redirect(url_for('Personalized_Welcomed'))


@app.route('/professional/edit_professional')
def edit_professional():
    return 'edit professional'


@app.route('/professional/delete_professional')
def delete_professional():
    return 'delete professional'


# ------------------------------PACIENTE------------------------------
@app.route('/patient')
def Patient_List():
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM paciente')
    data = cur.fetchall()
    return render_template('Patient_List.html', paciente=data)


@app.route('/patient/add_patient', methods=['POST'])  # el botón guardar
def add_patient():
    if request.method == 'POST':
        nombre = request.form['nombre']
        apellido = request.form['apellido']
        edad = request.form['edad']
        tutor = request.form['tutor']
        obra_social = request.form['obra_social']
        n_afiliado = request.form['n_afiliado']
        dni = request.form['dni']
        email = request.form['email']
        telefono = request.form['telefono']
        domicilio = request.form['domicilio']
        diagnostico = request.form['diagnostico']
        fecha_de_nacimiento = request.form['fecha_de_nacimiento']
        fecha_de_ingreso = request.form['fecha_de_ingreso']
        observaciones = request.form['observaciones']

        cur = mysql.connection.cursor()
        cur.execute('INSERT INTO paciente (nombre, apellido, edad, tutor, obra_social, n_afiliado, dni, email, telefono, domicilio, diagnostico, fecha_de_nacimiento, fecha_de_ingreso, observaciones) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)',
                    (nombre, apellido, edad, tutor, obra_social, n_afiliado, dni, email, telefono, domicilio, diagnostico, fecha_de_nacimiento, fecha_de_ingreso, observaciones))
        mysql.connection.commit()
        flash('Contacto agregado satisfactoriamente')
        return redirect(url_for('Patient_List'))


@app.route('/patient/edit_patient/<id>')
def get_patient(id):
    cur = mysql.connection.cursor()
    # cambie (id) por [id] (agarra lista executable)
    cur.execute('SELECT * FROM paciente WHERE id = %s', [id])
    data = cur.fetchall()
    return render_template('Edit_Patient.html', patient=data[0])


@app.route('/update/<id>', methods=['POST'])
def update_patient(id):
    if request.method == 'POST':
        nombre = request.form['nombre']
        apellido = request.form['apellido']
        edad = request.form['edad']
        tutor = request.form['tutor']
        obra_social = request.form['obra_social']
        n_afiliado = request.form['n_afiliado']
        dni = request.form['dni']
        email = request.form['email']
        telefono = request.form['telefono']
        domicilio = request.form['domicilio']
        diagnostico = request.form['diagnostico']
        fecha_de_nacimiento = request.form['fecha_de_nacimiento']
        fecha_de_ingreso = request.form['fecha_de_ingreso']
        observaciones = request.form['observaciones']
        cur = mysql.connection.cursor()
        cur.execute("""
            UPDATE paciente
            SET nombre = %s,
                apellido = %s,
                edad = %s,
                tutor = %s,
                obra_social = %s,
                n_afiliado = %s,
                dni = %s,
                email = %s,
                telefono = %s,
                domicilio = %s,
                diagnostico = %s,
                fecha_de_nacimiento = %s,
                fecha_de_ingreso = %s,
                observaciones = %s
            WHERE id = %s  
            """, (nombre, apellido, edad, tutor, obra_social, n_afiliado, dni, email, telefono, domicilio, diagnostico, fecha_de_nacimiento, fecha_de_ingreso, observaciones, id))
        mysql.connection.commit()
        return redirect(url_for('Patient_List'))


@app.route('/patient/delete_patient/<string:id>')
def delete_patient(id):
    cur = mysql.connection.cursor()
    cur.execute('DELETE FROM paciente WHERE id = {0}'.format(id))
    mysql.connection.commit()
    flash('Paciente removido satisfactoriamente')
    return redirect(url_for('Patient_List'))


# ----------------------BIENVENIDA PERSONALIZADA--------------
@app.route('/personalized_welcome')
def Personalized_Welcomed():
    return render_template('Personalized_Welcome.html')

events = [
    {
        'todo' : 'Xiaomi',
        'date' : '2022-06-07',
    },
    {
        'todo' : 'Nora',
        'date' : '2022-06-07',
    },
    {
        'todo' : 'Marcos',
        'date' : '2022-06-07',
    },
    {
        'todo' : 'Gonzalo',
        'date' : '2022-06-09',
    },

]

@app.route('/calendar')
def calendar():
   return render_template('calendar.html',
   events = events)

# ------------------------INICIO------------------------------


@app.route('/beginning')
def Beginning():
    return render_template('Beginning.html')

# -En caso de querer comenzar con localhost:3000 
@app.route('/')
def New_Patient():
    return render_template('Beginning.html')

# ------------------------LOGIN------------------------------


@app.route('/login')
def Login():
    return render_template('Login.html')

# ------------------------DEBUG---------------------------------


if __name__ == '__main__':
    app.run(port=3000, debug=True)
