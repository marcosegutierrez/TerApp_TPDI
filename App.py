from flask import Flask, render_template, request, session, redirect, url_for, flash
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

# global
global profesional_global

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
    if session.get('logueado'):
       return render_template('Personalized_Welcome.html')
    else:
        
        return render_template('Login.html')
        
    # ------------------------------LOGIN Verificación de datos--------------------------------------


@app.route('/login', methods=['POST'])
def do_admin_login():
  login = request.form
  
  email = login['email']
  password = login['password']

  if email is '' or password is '':
        flash("Completar campos! vuelve a intentarlo")
        return Login();

  cur = mysql.connection.cursor()
  cur.execute('SELECT * FROM profesional WHERE email = %s or contraseña = %s', [email,password])

  profesional = cur.fetchone()

  if profesional is None :
        flash("Ups! vuelve a intentarlo")
        return Login();

  password_db = profesional[13] #indice de la contraseña
  session['profesional_actual'] = profesional;
  session['logueado'] = (password == password_db)
  
  return Login()

@app.route('/logout')
def logout():
  session['logueado'] = False
  session['profesional_actual'] = None
  return Login()


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
        flash('Registro exitoso! Ingresa con tus credenciales')
        return redirect(url_for('Login'))
        

     #---Editar perfil profesional--
@app.route('/edit_professional')
def get_profesional():
    profesional_actual = session['profesional_actual']
    id_profesional_actual = session['profesional_actual'][0]
    
    cur = mysql.connection.cursor()
    # cambie (id) por [id] (agarra lista executable)
    cur.execute('SELECT * FROM profesional WHERE id_profesional = %s', [id_profesional_actual])
    data = cur.fetchall()
    
    return render_template('Edit_Professional.html', professional=data[0])


@app.route('/update_professional/<id>', methods=['POST'])
def update_professional(id):
    if request.method == 'POST':
        nombre = request.form['nombre']
        apellido = request.form['apellido']
        dni = request.form['dni']
        telefono = request.form['telefono']
        direccion = request.form['direccion']
        email = request.form['email']
        titulo = request.form['titulo']
        es_prestador = request.form.get('es_prestador')
        obra_social = request.form['obra_social']
        institucion_educativa = request.form['institucion_educativa']
        esta_matriculado = request.form.get('esta_matriculado')
        matricula = request.form['matricula']
        contraseña = request.form['contraseña']
        repetir_contraseña = request.form['repetir_contraseña']
        cur = mysql.connection.cursor()
        cur.execute("""
            UPDATE profesional
            SET nombre = %s,
                apellido = %s,
                dni = %s,
                telefono = %s,
                direccion = %s,
                email = %s,
                titulo = %s,
                es_prestador = %s,
                obra_social = %s,
                institucion_educativa = %s,
                esta_matriculado = %s,
                matricula = %s,
                contraseña = %s,
                repetir_contraseña = %s
            WHERE id_profesional = %s  
            """, (nombre, apellido, dni, telefono, direccion, email, titulo, es_prestador, 
            obra_social, institucion_educativa, esta_matriculado, 
            matricula, contraseña, repetir_contraseña, id))
        mysql.connection.commit()
        return redirect(url_for('Personalized_Welcome'))

 # ---- Solo disponible para un perfil administrador ---- 
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
        flash('Paciente agregado satisfactoriamente')
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
        flash('Paciente editado satisfactoriamente')
        return redirect(url_for('Patient_List'))


@app.route('/patient/delete_patient/<string:id>')
def delete_patient(id):
    cur = mysql.connection.cursor()
    cur.execute('DELETE FROM paciente WHERE id = {0}'.format(id))
    mysql.connection.commit()
    flash('Paciente removido satisfactoriamente')
    return redirect(url_for('Patient_List'))

    # ------------------------BUSCADOR de Paciente------------------------------

@app.route('/patient', methods=['POST'])
def Patient_List_Filtered():
    busqueda = request.form['input-search']

    if busqueda == "":
        return Patient_List()

    currentvalue = busqueda

    query = "SELECT * FROM paciente WHERE "
    query += "nombre LIKE '%" + busqueda + "%' OR "
    query += "apellido LIKE '%" + busqueda + "%' OR "
    query += "edad LIKE '%" + busqueda + "%' OR "
    query += "tutor LIKE '%" + busqueda + "%' OR "
    query += "obra_social LIKE '%" + busqueda + "%' OR "
    query += "n_afiliado LIKE '%" + busqueda + "%' OR "
    query += "dni LIKE '%" + busqueda + "%' OR "
    query += "email LIKE '%" + busqueda + "%' OR "  
    query += "telefono LIKE '%" + busqueda + "%' OR "
    query += "domicilio LIKE '%" + busqueda + "%' OR "
    query += "diagnostico LIKE '%" + busqueda + "%' OR "
    query += "observaciones LIKE '%" + busqueda + "%'"

    cur = mysql.connection.cursor()
    cur.execute(query)
    data = cur.fetchall()
    
    return render_template('Patient_List.html', paciente=data, currentvalue = currentvalue)

# ----------------------BIENVENIDA PERSONALIZADA: Calendario--------------

@app.route('/personalized_welcome')
def Personalized_Welcome():
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



# ------------------------DEBUG---------------------------------


if __name__ == '__main__':
    app.run(port=3000, debug=True)
