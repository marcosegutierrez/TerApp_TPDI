from flask import flash, render_template

def Patient_List(mysql):
    cur = mysql.connection.cursor()
    query = 'SELECT p.*, os.nombre FROM paciente p join obra_social os '
    query += 'on os.id_obra_social = p.id_obra_social;' 
    cur.execute(query)
    data = cur.fetchall()
    return data

def add_patient(mysql, request):
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
        cur.execute('INSERT INTO paciente (nombre, apellido, edad, tutor, id_obra_social, n_afiliado, dni, email, telefono, domicilio, diagnostico, fecha_de_nacimiento, fecha_de_ingreso, observaciones) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)',
                    (nombre, apellido, edad, tutor, obra_social, n_afiliado, dni, email, telefono, domicilio, diagnostico, fecha_de_nacimiento, fecha_de_ingreso, observaciones))
        mysql.connection.commit()
        flash('Paciente agregado con éxito')

def get_patient(mysql, id):
    cur = mysql.connection.cursor()
    # cambie (id) por [id] (agarra lista executable)
    cur.execute('SELECT * FROM paciente WHERE id = %s', [id])
    data = cur.fetchall()
    return data

def update_patient(mysql, id, request):
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
                id_obra_social = %s,
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
            """, (nombre, apellido, edad, tutor, obra_social, n_afiliado, dni, email, telefono, domicilio, 
            diagnostico, fecha_de_nacimiento, fecha_de_ingreso, observaciones, id))
        mysql.connection.commit()
        flash('Paciente editado con éxito')

def delete_patient(mysql, id):
    cur = mysql.connection.cursor()
    cur.execute('DELETE FROM paciente WHERE id = {0}'.format(id))
    mysql.connection.commit()
    flash('Paciente removido con éxito')

# ------------------------BUSCADOR de Paciente------------------------------

def Patient_List_Filtered(mysql, request):
    busqueda = request.form['input-search']

    if busqueda == "":
        return Patient_List()

    currentvalue = busqueda

    query = "SELECT p.*, os.nombre FROM paciente as p join obra_social as os"
    query += " on os.id_obra_social = p.id_obra_social WHERE "
    query += "p.nombre LIKE '%" + busqueda + "%' OR "
    query += "p.apellido LIKE '%" + busqueda + "%' OR "
    query += "p.edad LIKE '%" + busqueda + "%' OR "
    query += "p.tutor LIKE '%" + busqueda + "%' OR "
    query += "p.id_obra_social LIKE '%" + busqueda + "%' OR "
    query += "p.n_afiliado LIKE '%" + busqueda + "%' OR "
    query += "p.dni LIKE '%" + busqueda + "%' OR "
    query += "p.email LIKE '%" + busqueda + "%' OR "
    query += "p.telefono LIKE '%" + busqueda + "%' OR "
    query += "p.domicilio LIKE '%" + busqueda + "%' OR "
    query += "p.diagnostico LIKE '%" + busqueda + "%' OR "
    query += "p.observaciones LIKE '%" + busqueda + "%'"

    cur = mysql.connection.cursor()
    cur.execute(query)
    data = cur.fetchall()

    return [data, currentvalue]
